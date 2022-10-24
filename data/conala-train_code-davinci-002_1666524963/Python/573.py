import base64
import hashlib
import hmac
import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt_urlsafe_base64(urlsafe_base64_string, key):
    """
    Decrypts a urlsafe base64 string with a key.
    """
    # Decode the base64 string
    base64_string = base64.urlsafe_b64decode(urlsafe_base64_string)

    # Decrypt the base64 string
    decrypted_string = decrypt(base64_string, key)

    # Return the decrypted string
    return decrypted_string

def decrypt(encrypted_string, key):
    """
    Decrypts an encrypted string with a key.
    """
    # Decode the encrypted string
    encrypted_bytes = encrypted_string.decode('utf-8')

    # Decrypt the encrypted bytes
    decrypted_bytes = decrypt_bytes(encrypted_bytes, key)

    # Decode the decrypted bytes
    decrypted_string = decrypted_bytes.decode('utf-8')

    # Return the decrypted string
    return decrypted_string

def decrypt_bytes(encrypted_bytes, key):
    """
    Decrypts encrypted bytes with a key.
    """
    # Decode the key
    key_bytes = key.encode('utf-8')

    # Get the initialization vector
    iv = encrypted_bytes[:16]

    # Get the encrypted data
    encrypted_data = encrypted_bytes[16:]

    # Create the cipher
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)

    # Decrypt the encrypted data
    decrypted_bytes = cipher.decrypt(encrypted_data)

    # Unpad the decrypted bytes
    decrypted_bytes = unpad(decrypted_bytes, AES.block_size)

    # Return the decrypted bytes
    return decrypted_bytes

def decrypt_json(encrypted_json, key):
    """
    Decrypts an encrypted json string with a key.
    """