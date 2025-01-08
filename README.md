# Projeto Educacional de Ransomware - DIO Cibersegurança

## 📋 Descrição
Este projeto faz parte do Módulo 2 da Trilha de Santander Bootcamp Cibersegurança #2! e Digital Innovation One (DIO). Consiste em uma implementação educacional de um ransomware e sua respectiva ferramenta de criptografia e descriptografia, desenvolvidos em Python para fins de estudo e compreensão dos mecanismos de segurança.

## 🎯 Objetivos do Projeto
- Demonstrar conceitos práticos de criptografia
- Implementar manipulação segura de arquivos em Python
- Aplicar algoritmos de segurança em cenários reais
- Desenvolver boas práticas de programação
- Promover consciência sobre segurança cibernética

## 🔐 Funcionalidades
### Módulo de Criptografia
- Encriptação de arquivos utilizando AES (Advanced Encryption Standard)
- Modo de operação CTR (Counter)
- Sistema de backup automático dos arquivos originais
- Gestão segura de arquivos
- Tratamento robusto de erros e exceções

### Módulo de Descriptografia
- Descriptografia de arquivos usando a mesma implementação AES-CTR
- Validação da chave de descriptografia
- Verificação de integridade dos arquivos
- Sistema de recuperação em caso de falhas
- Backup automático dos arquivos criptografados

## 🛠️ Tecnologias Utilizadas
- Kali Linux
- Python 3.x
- Biblioteca pyaes para criptografia
- Bibliotecas nativas:
  - os: Manipulação de sistema de arquivos
  - pathlib: Gestão segura de caminhos
  - typing: Tipagem estática

## 📦 Pré-requisitos
```bash
pip install pyaes
```

## 🚀 Como Executar

### Criptografia
```bash
python ransomware.py
```

### Descriptografia
```bash
python decrypt_ransomware.py
```

## 📁 Estrutura do Projeto
```
.
├── ransomware.py          # Script de criptografia
├── decrypter.py           # Script de descriptografia
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

## 🔒 Aspectos de Segurança
- Verificação de permissões e existência de arquivos
- Backup automático antes de qualquer operação
- Uso de context managers para manipulação segura
- Tratamento abrangente de exceções
- Validação robusta de entrada de dados
- Sistema de recuperação para falhas
- Logging para auditoria (opcional)

## 📚 Melhorias Implementadas
1. Código modularizado e reutilizável
2. Tratamento de erros abrangente
3. Sistema de backup automático
4. Validação robusta de entrada
5. Verificação de permissões do sistema
6. Manipulação segura de caminhos de arquivo
7. Documentação clara e detalhada
8. Tipagem estática para maior segurança

## 🔗 Links Úteis
- [Digital Innovation One](https://www.dio.me/)
- [Documentação Python](https://docs.python.org/3/)
- [Documentação pyaes](https://pypi.org/project/pyaes/)

## 🎁 Agradecimentos
- Santander Bootcamp Cibersegurança #2!
- Digital Innovation One
- Instrutor do curso
- Comunidade DIO

---
⌨️ Desenvolvido com 💙 como parte do curso de Santander Bootcamp Cibersegurança #2! e DIO