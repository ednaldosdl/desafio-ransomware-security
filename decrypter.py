import os
import pyaes
from pathlib import Path


def encrypt_file(file_path: str, key: bytes) -> bool:
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo {file_path} não encontrado")

        # Abre e lê o arquivo de forma segura usando context manager
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Inicializa o encriptador AES
        aes = pyaes.AESModeOfOperationCTR(key)

        # Encripta os dados
        crypto_data = aes.encrypt(file_data)

        # Cria backup antes de modificar
        backup_path = file_path + ".backup"
        with open(backup_path, "wb") as backup:
            backup.write(file_data)

        # Salva arquivo encriptado
        encrypted_path = file_path + ".encrypted"
        with open(encrypted_path, "wb") as new_file:
            new_file.write(crypto_data)

        # Remove original apenas se tudo deu certo
        os.remove(file_path)
        return True

    except Exception as e:
        print(f"Erro durante encriptação: {str(e)}")
        return False


def main():
    # Configurações em variáveis separadas
    KEY = os.environ.get("ENCRYPTION_KEY", b"testeransomwares")
    TARGET_FILE = "teste.txt"

    # Executa encriptação
    success = encrypt_file(TARGET_FILE, KEY)
    if success:
        print(f"Arquivo {TARGET_FILE} encriptado com sucesso")
    else:
        print("Falha na encriptação")


if __name__ == "__main__":
    main()
