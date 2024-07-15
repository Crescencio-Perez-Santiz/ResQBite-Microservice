import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Obtener la clave AES desde el entorno
AES_KEY_HEX = os.getenv('AES_KEY_HEX')
AES_KEY = bytes.fromhex(AES_KEY_HEX)  # Convertir la clave hexadecimal a bytes

def encrypt_data(data: str) -> bytes:
    # Padding (relleno) para asegurar que el mensaje sea múltiplo de 16 bytes (tamaño del bloque AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    # Generar un vector de inicialización (IV) seguro
    iv = os.urandom(algorithms.AES.block_size // 8)

    # Crear el cifrador AES en modo CBC con la clave y IV
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encriptar los datos
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # El IV debe ser almacenado y pasado junto al texto cifrado
    encrypted_data = iv + ciphertext
    return encrypted_data

def decrypt_data(encrypted_data: bytes) -> str:
    # Extraer IV y texto cifrado
    iv = encrypted_data[:algorithms.AES.block_size // 8]
    ciphertext = encrypted_data[algorithms.AES.block_size // 8:]

    # Crear el descifrador AES en modo CBC con la clave y IV
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Desencriptar los datos
    decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Quitar el relleno
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_data.decode()
