import os
import pyaes
from pathlib import Path


def decrypt_file(encrypted_file_path, key_string, output_path=None):
    try:
        # Validar entrada
        if len(key_string) not in [16, 24, 32]:
            raise ValueError("Tamanho da chave inválido")

        key = key_string.encode('utf-8')
        file_path = Path(encrypted_file_path)

        if not file_path.exists():
            raise FileNotFoundError("Arquivo criptografado não encontrado")

        # Criar backup
        backup_path = file_path.with_suffix(file_path.suffix + '.backup')
        os.replace(str(file_path), str(backup_path))

        # Ler arquivo
        with open(backup_path, "rb") as file:
            file_data = file.read()

        # Descriptografar
        try:
            aes = pyaes.AESModeOfOperationCTR(key)
            decrypt_data = aes.decrypt(file_data)
        except Exception as e:
            os.replace(str(backup_path), str(file_path))  # Restaurar original
            raise Exception(f"Erro na descriptografia: {e}")

        # Definir caminho de saída
        if output_path is None:
            output_path = file_path.with_suffix('')

        # Verificar permissões
        if os.path.exists(output_path):
            if not os.access(output_path, os.W_OK):
                raise PermissionError(
                    "Sem permissão para sobrescrever arquivo")

        # Salvar arquivo descriptografado
        with open(output_path, "wb") as new_file:
            new_file.write(decrypt_data)

        return True

    except Exception as e:
        print(f"Erro: {e}")
        return False


# Uso
if __name__ == "__main__":
    success = decrypt_file(
        "teste.txt.ransomwaretroll",
        "testeransomwares"
    )
    if success:
        print("Arquivo descriptografado com sucesso")
