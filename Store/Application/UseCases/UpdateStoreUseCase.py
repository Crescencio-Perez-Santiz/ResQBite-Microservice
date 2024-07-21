from flask_jwt_extended import get_jwt_identity
from werkzeug.utils import secure_filename
import os
import tempfile
import hashlib
import time
from Infrastructure.Services.bucketStore import send_file, delete_file


class UpdateStoreUseCase:
    def __init__(self, store_repository):
        self.store_repository = store_repository

    def execute(self, store_data, image_file):
        user_uuid = get_jwt_identity()
        print(user_uuid)

        current_store = self.store_repository.get_store_by_user_uuid(user_uuid)

        if not current_store:
            raise ValueError("Store not found")

        if 'phone_number' in store_data and store_data['phone_number'] != current_store.phone_number:
            if self.store_repository.phone_exists(store_data['phone_number']):
                raise ValueError("El número de teléfono ya está en uso.")
        else:
            store_data['phone_number'] = current_store.phone_number

        if image_file:
            original_filename = secure_filename(image_file.filename)
            timestamp = int(time.time())
            unique_filename = f"{timestamp}_{original_filename}"

            hash_object = hashlib.sha256(unique_filename.encode())
            hex_dig = hash_object.hexdigest()
            filename = f"{hex_dig}{os.path.splitext(original_filename)[1]}"
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, filename)

            image_file.save(temp_path)
            bucket_name = os.getenv('S3_BUCKET_NAME')
            path = os.getenv('S3_PATH')
            object_name = f"{path}/{filename}"
            send_file(temp_path, bucket_name, current_store.uuid, object_name)

            region = os.getenv('S3_REGION')
            space_name = bucket_name
            image_url = f"https://{space_name}.{
                region}.digitaloceanspaces.com/{bucket_name}/{object_name}"

            os.remove(temp_path)

            if current_store.image:
                old_object_name = current_store.image.split('/')[-1]
                delete_file(
                    f"https://{bucket_name}.nyc3.digitaloceanspaces.com/{path}/{old_object_name}", bucket_name)

            store_data['image'] = image_url
        else:
            store_data['image'] = current_store.image

        fields_to_update = [
            'street', 'number', 'neighborhood', 'city', 'reference',
            'image', 'phone_number', 'opening_hours', 'closing_hours',
            'name',
        ]
        for field in fields_to_update:
            if field in store_data and store_data[field] != getattr(current_store, field):
                setattr(current_store, field, store_data[field])

        updated_store = self.store_repository.update(current_store, user_uuid)
        return updated_store
