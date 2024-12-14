import secrets
import logging

class SaltService:
    def generate_salt(self, bytes_size: int = 32):
        try:
            salt = bytearray(bytes_size)
            for i in range(bytes_size):
                salt[i] = secrets.randbelow(256)
            return bytes(salt)
        except (ValueError, TypeError) as e :
            logging.exception(f"Invalid argument: {e}")
