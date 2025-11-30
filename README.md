# 🛡️ Cybersecurity-Project-Cryptography: Simulação de Malware para Defesa

## 🎯 Visão Geral do Projeto

[cite_start]Este projeto é a implementação prática e documentada dos conceitos de segurança cibernética, simulando o comportamento de malwares em um **ambiente 100% controlado e seguro** (Máquina Virtual)[cite: 3]. [cite_start]O objetivo é demonstrar o funcionamento prático de ameaças como **Ransomware** e **Keylogger** [cite: 4][cite_start], para então **refletir sobre as estratégias eficazes de detecção, mitigação e proteção**[cite: 5].

---

## ✅ Objetivos de Aprendizagem e Entrega

[cite_start]A conclusão deste desafio demonstra a capacidade de[cite: 15]:

* [cite_start]Compreender o funcionamento prático de **Ransomware** e **Keylogger**[cite: 16].
* [cite_start]Programar scripts simples em **Python** simulando ataques reais em ambiente controlado[cite: 18].
* [cite_start]Refletir sobre estratégias de **defesa e prevenção** contra malwares[cite: 19].
* [cite_start]Documentar os experimentos e utilizar o **GitHub** como portfólio técnico[cite: 20].

---

## 1. 🔒 Módulo Ransomware Simulado

Esta seção documenta a simulação de um sequestro de dados e o processo de recuperação (descriptografia).

### 1.1. Lógica de Implementação

* [cite_start]**Tecnologia:** Python com a biblioteca `Cryptography` (módulo **Fernet**) para criptografia simétrica robusta[cite: 32].
* **Alvo:** A simulação foi executada apenas em um diretório isolado (`TARGET_FILES`) dentro de uma Máquina Virtual (VM) para garantir o controle total do ambiente.
* **Processo de Ataque (`ransomware.py`):**
    1.  [cite_start]**Geração da Chave:** Uma chave **Fernet** é gerada [cite: 32] e salva de forma simulada (`key.txt`), representando a chave que seria enviada para o atacante.
    2.  **Criptografia:** O script itera sobre os arquivos alvo, lê o conteúdo, criptografa-o com a chave gerada, e sobrescreve o arquivo original, adicionando a extensão `.encrypted`.
    3.  **Mensagem de Resgate:** Um arquivo (`LEIA_ME_RESGATE.txt`) é criado no diretório, simulando a notificação e a demanda de resgate.

### 1.2. Processo de Descriptografia (`decrypt.py`)

* O script de descriptografia simula a etapa de recuperação de dados. Ele carrega a chave (`key.txt`), identifica os arquivos com a extensão `.encrypted` e inverte o processo, restaurando o conteúdo original dos arquivos.

---

## 2. ⌨️ Módulo Keylogger Simulado

Esta seção documenta a simulação de um ataque de captura de teclas e a exfiltração de dados (envio de logs).

### 2.1. Lógica de Implementação

* [cite_start]**Captura de Teclas:** Utilização da biblioteca `pynput` para criar um listener (ouvinte) que monitora e registra eventos do teclado[cite: 33].
* **Registro de Logs:** As teclas capturadas são salvas periodicamente em um arquivo de log temporário (`logs.txt`).
* [cite_start]**Exfiltração (Envio de E-mail):** O script utiliza o módulo `smtplib` do Python para configurar um envio automático dos logs por e-mail, simulando o roubo e a transmissão dos dados capturados para o atacante[cite: 34].

### 2.2. Estratégias de Furtividade (Documentadas)

A simulação focou em aspectos de furtividade, como:
* Execução em background (sem interface de terminal visível).
* Tratamento de teclas especiais (ex: `[enter]`, `[space]`) para manter a clareza do arquivo de logs.

---

## 3. 🛡️ Reflexão sobre Defesa e Mitigação

A compreensão de como os malwares funcionam permite desenvolver defesas mais robustas. [cite_start]As principais medidas de prevenção e defesa contra Ransomware e Keyloggers incluem[cite: 10]:

* **Antivírus e EDR:** Utilização de soluções de Endpoint Detection and Response (EDR) que monitoram comportamentos anômalos (ex: um programa criptografando em massa arquivos de usuário) em vez de apenas assinaturas de arquivos.
* **Firewall:** Configuração para bloquear comunicações de saída suspeitas, impedindo que o Keylogger envie logs pela rede (`smtplib`).
* **Sandboxing e Isolamento:** Execução de aplicativos suspeitos em ambientes isolados (Máquinas Virtuais) para conter qualquer potencial dano.
* [cite_start]**Conscientização do Usuário:** A principal defesa[cite: 17]. Treinamento para identificar phishing, não abrir anexos suspeitos e usar autenticação de múltiplos fatores (MFA).
* **Backups:** Manter backups regulares e isolados (offline) é a mitigação mais eficaz contra o Ransomware.

---

## 💻 Estrutura do Repositório
Cybersecurity-Project-Cryptography/ ├── README.md (Este arquivo detalhado) ├── requirements.txt (Dependências Python: cryptography, pynput) ├── /ransomware-sim/ │ └── ransomware_logic.md (Documentação da lógica de criptografia/descriptografia) ├── /keylogger-sim/ │ └── keylogger_logic.md (Documentação da lógica de captura e exfiltração de logs) └── /defesa-e-analise/ └── defesas.md (Documentação detalhada das estratégias de prevenção)

## ⚠️ Aviso e Boas Práticas em Segurança

Este projeto foi desenvolvido estritamente para **fins educacionais e de auditoria de segurança**, conforme proposto no Desafio DIO. A aplicação dos conhecimentos aqui documentados deve seguir rigorosamente a **ética profissional**.

**Regras Essenciais:**

* **1. Conhecimento e Responsabilidade:** **Nunca** execute comandos sem o devido conhecimento de seus efeitos e implicações legais. A compreensão é a primeira linha de defesa.
* **2. Ambiente Controlado:** **Somente** realize testes em ambientes controlados e de sua propriedade (como as VMs Metasploitable 2 ou DVWA). Atacar sistemas sem permissão é ilegal.
* **3. Profissionalismo:** Utilize ferramentas adequadas para o trabalho, sem improvisação. O uso correto e ético das ferramentas é um sinal de profissionalismo.
* **4. Organização do Laboratório:** Mantenha seu laboratório virtual e seus arquivos de projeto organizados. A clareza no ambiente de testes leva à clareza na análise de resultados.
* **5. Conhecimento é Ferramenta:** Lembre-se que o **conhecimento** também é uma ferramenta poderosa. Mantenha sua mente focada e "limpa", dedicando-se ao estudo contínuo e à aplicação ética dos conceitos de segurança.
