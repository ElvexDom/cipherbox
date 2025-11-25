from cryptography.fernet import Fernet

class crypto_tools:
    
    @staticmethod
    def generate_key():
        key = Fernet.generate_key()
        return key
    
    @staticmethod
    def encrypt(message, key):
        f = Fernet(key)
        ciphertext = f.encrypt(message.encode('utf-8'))
        return ciphertext
    
    @staticmethod
    def decrypt(crypt_message, key):
        f = Fernet(key)
        plaintext = f.decrypt(crypt_message).decode('utf-8')
        return plaintext
