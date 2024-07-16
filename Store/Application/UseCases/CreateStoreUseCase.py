from Domain.Entity.Store import Store
from Domain.Entity.Address import Address
from Domain.Entity.InformationStore import InformationStore
from Infrastructure.Services.bucketStore import send_file
from werkzeug.utils import secure_filename
import os
from ..Exceptions.StoreValidationExists import StoreValidationExists
import tempfile
import hashlib
from Infrastructure.Services.rabbitmq.NewStoreServiceSaga import NewStoreServiceSaga


class CreateStoreUseCase:
    def __init__(self, store_repository):
        self.store_repository = store_repository

    def execute(self, store_data, image_file) -> Store:
        store_validation = StoreValidationExists(self.store_repository)
        if store_validation.validate_store_by_rfc(store_data['rfc']):
            raise Exception("RFC already exists")
        if store_validation.validate_store_by_phone_number(store_data['phone_number']):
            raise Exception("Phone number already exists")

        original_filename = secure_filename(image_file.filename)
        hash_object = hashlib.sha256(original_filename.encode())
        hex_dig = hash_object.hexdigest()
        filename = f"{hex_dig}{os.path.splitext(original_filename)[1]}"
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(
            temp_dir, filename)

        store_data_complete = Store(
            name=store_data['name'],
            rfc=store_data['rfc'],
            address=None,
            information=None
        )
        store_uuid = store_data_complete.uuid

        image_file.save(temp_path)
        bucket_name = os.getenv('S3_BUCKET_NAME')
        path = os.getenv('S3_PATH')
        object_name = f"{path}/{filename}"
        send_file(temp_path, bucket_name, store_uuid, object_name
                  )
        region = os.getenv('S3_PATH')
        space_name = bucket_name
        image_url = f"https://{space_name}.{
            region}.digitaloceanspaces.com/{object_name}"

        os.remove(temp_path)

        store_data['url_image'] = image_url
        address = Address(
            street=store_data['street'],
            number=store_data['number'],
            neighborhood=store_data['neighborhood'],
            city=store_data['city'],
            reference=store_data['reference']
        )

        information = InformationStore(
            url_image=store_data['url_image'],
            phone_number=store_data['phone_number'],
            opening_hours=store_data['opening_hours'],
            closing_hours=store_data['closing_hours']
        )

        store_data_complete = Store(
            name=store_data['name'],
            rfc=store_data['rfc'],
            address=address,
            information=information
        )

        saga = NewStoreServiceSaga()
        saga.send_store_info(store_data_complete.to_dict())

        return self.store_repository.create(store_data_complete)
