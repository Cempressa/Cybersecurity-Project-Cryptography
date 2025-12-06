# 🔒 Lógica de Implementação: Ransomware Simulado

## 🎯 Objetivo
[cite_start]Detalhar o funcionamento do script de criptografia (`encrypt.py`) e descriptografia (`decrypt.py`) em Python, utilizando a biblioteca **Cryptography (Fernet)**[cite: 32], em um ambiente de teste isolado.

## ⚙️ 1. Geração da Chave Simétrica (Fernet)
A criptografia Fernet é um tipo de criptografia simétrica.

* **Ação:** O script `encrypt.py` gera uma chave única e a armazena (simulando o envio para o atacante).
* **Código/Função Principal:** `Fernet.generate_key()`
* **Detalhamento:** Explique como essa chave é salva de forma isolada (`key.txt`) para uso posterior no script de recuperação.

## 🔐 2. Processo de Criptografia (Ataque)
Esta seção foca na funcionalidade do script `encrypt.py`.

### 2.1. Definição do Alvo
* [cite_start]**Lógica:** O script utiliza `import os` [cite: 29] para iterar sobre os arquivos na pasta `TARGET_FILES/`.
* **Filtro:** Detalhe como o código verifica se o item é um arquivo e ignora arquivos de sistema ou a própria chave de recuperação.

### 2.2. Ação de Criptografia
* **Passos:**
    1.  Abrir o arquivo alvo em modo binário (`"rb"`).
    2.  Ler o conteúdo.
    3.  Criptografar o conteúdo: `Fernet(key).encrypt(data)`.
    4.  Sobrescrever o arquivo original com os dados criptografados.
    5.  **Renomeação:** Adicionar a extensão `.encrypted` ao arquivo.

## 🔓 3. Processo de Descriptografia (Recuperação)
Esta seção documenta o script `decrypt.py` para a recuperação dos dados.

* **Recuperação da Chave:** O script lê a chave salva em `key.txt`.
* **Descriptografia:** O script itera sobre os arquivos com a extensão `.encrypted` e utiliza: `Fernet(key).decrypt(encrypted_data)`.
* **Resultado:** Os arquivos são restaurados ao seu estado original e renomeados.

## 🚨 4. Mensagem de Resgate
* [cite_start]**Funcionamento:** Detalhe o conteúdo e o nome do arquivo (ex: `LEIA_ME_RESGATE.txt`) gerado pelo script. Inclua um exemplo simulado do texto de "resgate".
