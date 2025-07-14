

class UserHelper:
    
    @classmethod
    def is_admin(cls, user):
        if not user:
            return False
        try:
            user.admin
            return True
        except:
            return False
        
    @classmethod
    def is_client(cls, user):
        if not user:
            return False
        try:
            user.client
            return True
        except:
            return False