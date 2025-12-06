
# ⌨️ Lógica de Implementação: Keylogger Simulado

## 🎯 Objetivo
[cite_start]Demonstrar a captura de teclas e a exfiltração de dados, utilizando as bibliotecas **pynput** [cite: 33] [cite_start]e **smtplib**[cite: 34].

## 🎧 1. Captura de Teclas com pynput
* [cite_start]**Tecnologia:** `pynput.keyboard.Listener`[cite: 33].

### 1.1. Tratamento de Eventos
* **Função:** Detalhe a função `on_press(key)` ou `on_release(key)` responsável por capturar o evento.
* [cite_start]**Log:** Explique como a tecla capturada é convertida para string e registrada no arquivo `.txt`  (`logs.txt`).
* **Furtividade na Captura:** Detalhe a lógica usada para lidar com teclas especiais (ex: `space`, `enter`) para manter o arquivo de log organizado.

## 📤 2. Exfiltração de Dados com smtplib
[cite_start]O envio de e-mail é a simulação do roubo de dados furtivo.

* [cite_start]**Tecnologia:** Módulo `smtplib` [cite: 34] do Python.
* **Periodicidade:** Descreva a lógica (ex: função `send_email_log` que é chamada a cada X tempo ou X linhas de texto) para enviar o conteúdo do `logs.txt`.
* **Configuração Simulada:** Explique como o script se conecta ao servidor SMTP (necessita de servidor, porta, credenciais, etc.) para o envio.

## 👻 3. Furtividade na Execução
* [cite_start]**Técnicas Documentadas:** Detalhe as medidas implementadas (ou estudadas) para tornar o script menos visível ao usuário, como a execução em segundo plano ou a ocultação da janela de terminal.
