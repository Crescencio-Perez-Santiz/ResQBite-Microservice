from abc import ABC, abstractmethod
from Domain.Entity.User import User

class UserInterface(ABC):
    
    @abstractmethod
    def save_user(self, user: User):
        pass
    
    def get_user(self, user_id):
        pass
    
    def get_users(self):
        pass
    
    def update_user(self, user: User):
        pass
    
    def delete_user(self, user_id):
        pass