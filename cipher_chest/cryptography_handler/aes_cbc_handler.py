from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import logging

from .cryptography_handler import CryptographyHandler
from cipher_chest.padder.pkcs7_padder import PKCS7Padder

class AESCBCHandler(CryptographyHandler):
    def __init__(self):
        self.backend = default_backend()

    def encrypt(self, plain_text: str, key: bytes, iv: bytes):
        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), self.backend)
            encryptor = cipher.encryptor()
            
            padding_service = PKCS7Padder(algorithms.AES.block_size)
            padded_plain_text = padding_service.pad(plain_text)
            
            cipher_text = encryptor.update(padded_plain_text) + encryptor.finalize()

            cipher_text = (cipher_text)

            return {
                "success": True,
                "cipher_text": cipher_text
            }
        except (ValueError, TypeError) as e:
            logging.exception(f"Invalid arguments: {e}")
        except AttributeError as e:
            logging.exception(f"Attribute error: {e}")

    def decrypt(self, cipher_text: bytes, key: bytes, iv: bytes):
        try:
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), self.backend)
            decryptor = cipher.decryptor()

            cipher_text = decryptor.update(cipher_text) + decryptor.finalize()

            padding_service = PKCS7Padder(algorithms.AES.block_size)
            unpadded_cipher_text = padding_service.unpad(cipher_text)

            plain_text = unpadded_cipher_text.decode("utf-8")

            return {
                "success": True,
                "plain_text": plain_text
            }
        except (ValueError, TypeError) as e:
            logging.exception(f"Invalid arguments: {e}")
        except AttributeError as e:
            logging.exception(f"Attribute error: {e}")
