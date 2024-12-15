from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import logging

from .derivator import Derivator

class PBKDF2Derivator(Derivator):
    def __init__(self):
        self.backend = default_backend()

    def derive(self, password: str, salt: bytes, key_length: int, iv_length: int = 16):
        try:
            iterations = 10000
            
            pbkdf2 = PBKDF2HMAC(
                algorithm=SHA256(),
                salt=salt,
                length=key_length + iv_length,
                iterations=iterations,
                backend=self.backend
            )

            password_bytes = password.encode("utf-8")
            key_and_iv = pbkdf2.derive(password_bytes)

            return {
                "key": key_and_iv[:key_length],
                "iv": key_and_iv[key_length:]
            }
        except (ValueError, TypeError) as e:
            logging.exception(f"Invalid arguments: {e}")
        except AttributeError as e:
            logging.exception(f"Attribute error: {e}")
