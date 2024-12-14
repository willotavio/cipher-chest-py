from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from .cryptography_handler import CryptographyHandler
from services.padder.pkcs7_padders import PKCS7Padder

class AESCBCHandler(CryptographyHandler):
    def __init__(self):
        self.backend = default_backend()
        self.padding_service = PKCS7Padder(algorithms.AES.block_size)

    def encrypt(self, plain_text: str, key: bytes, iv: bytes):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), self.backend)
        encryptor = cipher.encryptor()

        padded_plain_text = self.padding_service.pad(plain_text)
        
        cipher_text = encryptor.update(padded_plain_text) + encryptor.finalize()

        cipher_text = (cipher_text)

        return {
            "success": True,
            "cipher_text": cipher_text
        }

    def decrypt(self, cipher_text: bytes, key: bytes, iv: bytes):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), self.backend)
        decryptor = cipher.decryptor()

        cipher_text = decryptor.update(cipher_text) + decryptor.finalize()

        unpadded_cipher_text = self.padding_service.unpad(cipher_text)

        plain_text = unpadded_cipher_text.decode("utf-8")

        return {
            "success": True,
            "plain_text": plain_text
        }
