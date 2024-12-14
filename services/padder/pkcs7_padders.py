from cryptography.hazmat.primitives.padding import PKCS7

class PKCS7Padder:
    def __init__(self, block_size: int):
        self.padder = PKCS7(block_size).padder()
        self.unpadder = PKCS7(block_size).unpadder()

    def pad(self, plain_text: str):
        return self.padder.update(plain_text.encode("utf-8")) + self.padder.finalize()
    
    def unpad(self, cipher_text: bytes):
        return self.unpadder.update(cipher_text) + self.unpadder.finalize()
