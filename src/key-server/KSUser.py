import rsa

class KSUser:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        (self.public_key, self.private_key) = rsa.newkeys(512)
    
    def get_private_key(self,password) -> rsa.PrivateKey:
        if(self.password==password):
            return self.private_key
        else:
            return None

    def get_public_key(self) -> rsa.PublicKey:
        return self.public_key