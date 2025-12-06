
# 📤 Detalhamento: Exfiltração de Logs via E-mail (smtplib)

## 🎯 Objetivo
Documentar a lógica utilizada no Keylogger Simulado para a exfiltração (envio furtivo) dos logs capturados, utilizando o módulo nativo **`smtplib`** do Python.

## 1. ⚙️ Configuração Simulada do Servidor SMTP

Para simular o roubo de dados, o script precisa se conectar a um servidor de e-mail (simulado ou de teste, como Gmail/Outlook com App Passwords).

* **Tecnologia:** `smtplib` (protocolo SMTP).
* **Conexão:** Detalhar o uso de `smtplib.SMTP_SSL()` para garantir uma conexão segura e criptografada (porta 465, geralmente).
* **Autenticação:** O script simula o uso de credenciais (e-mail do atacante e senha/token) para realizar o login no servidor: `server.login(remetente, senha)`.

## 2. 📝 Lógica da Mensagem e Anexo

O conteúdo capturado (`logs.txt`) precisa ser transformado em um e-mail com anexo.

* **Módulos Adicionais:** Uso dos módulos `email.mime.multipart` e `email.mime.text` para estruturar a mensagem de forma profissional.
* **Corpo da Mensagem:** A mensagem de e-mail deve ser mínima para evitar suspeitas (simulando furtividade).
* **Anexo:** O arquivo de log (`logs.txt`) deve ser anexado à mensagem antes do envio.

## 3. ⏱️ Função de Envio Automático

O elemento crucial da exfiltração é a periodicidade e a automação do envio, que garante que o atacante receba os dados mesmo que o computador da vítima seja desligado.

### Lógica da Função `send_logs_via_email()`:

1.  **Condição de Disparo:** A função é chamada a cada intervalo de tempo (ex: a cada 10 minutos) ou quando o arquivo `logs.txt` atinge um certo tamanho (ex: 500 KB).
2.  **Envio:** Executa o processo de conexão, login, construção e envio da mensagem.
3.  **Limpeza:** Após o envio bem-sucedido, o arquivo `logs.txt` é **limpo/resetado** para iniciar uma nova captura, minimizando o volume de dados e o risco de detecção.

## ⚠️ Nota de Segurança
Esta documentação é para fins estritamente educacionais e foi desenvolvida em um ambiente isolado. [cite_start]O envio de e-mails via `smtplib` em um cenário real exige credenciais de aplicativos ou tokens específicos e pode ser bloqueado por firewalls de rede[cite: 10].
