from DataBase.MySQLConnection import DBConnection
from Domain.Entity.User import User as UserDomain
from Domain.Port.UserInterface import UserInterface
from .UserModel import User


class UserRepository(UserInterface):
    def __init__(self):
        self.db = DBConnection()
        self.session = self.db.Session()

    def save_user(self, user: UserDomain):
        try:
            user = User(
                uuid=user.uuid,
                email=user.email,
                password=user.password,
                location=user.location,
                user_type_suscriber=user.user_type_suscriber,
                name=user.contact.name,
                last_name=user.contact.last_name,
                address=user.contact.address,
                phone_number=user.contact.phone_number,
            )
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def get_user_by_uuid(self, user_uuid):
        try:
            user = self.session.query(User).filter_by(uuid=user_uuid).first()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def update_user(
        self,
        user_uuid: int,
        password: str,
        name: str,
        last_name: str,
        address: str,
        phone_number: str,
    ):
        try:
            user = self.get_user_by_uuid(user_uuid)
            if user is None:
                raise Exception("User not found")

            user.password = password
            user.name = name
            user.last_name = last_name
            user.address = address
            user.phone_number = phone_number
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def get_user_by_email(self, email):
        try:
            user = self.session.query(User).filter_by(email=email).first()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def get_user_by_phone_number(self, phone_number):
        try:
            user = self.session.query(User).filter_by(
                phone_number=phone_number).first()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def update_location(self, user_uuid, location):
        try:
            user = self.get_user_by_uuid(user_uuid)
            if user is None:
                raise Exception("User not found")
            if user.location == location:
                return user
            else:
                user.location = location
                self.session.commit()
                return user
        except Exception as e:
            self.session.rollback()
            raise e

    def find_by_uuid(self, user_uuid):
        try:
            user = self.session.query(User).filter_by(uuid=user_uuid).first()
            return user
        except Exception as e:
            self.session.rollback()
            raise e

    def update_uuid(self, user_uuid, store_uuid):
        try:
            user = self.get_user_by_uuid(user_uuid)
            if user is None:
                raise Exception("User not found")
            user.store_uuid = store_uuid
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e
    
    def update_user_type(self, user_uuid, user_type):
        try:
            user = self.get_user_by_uuid(user_uuid)
            if user is None:
                raise Exception("User not found")
            user.user_type_suscriber = user_type
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e
