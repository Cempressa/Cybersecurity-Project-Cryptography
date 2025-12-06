
# 🛡️ Reflexão e Estratégias de Defesa

## 🎯 Objetivo
[cite_start]Documentar as medidas essenciais de prevenção e defesa  contra ameaças digitais, com foco em Ransomware e Keyloggers, conforme o desafio.

---

## 1. Defesas Técnicas

### 1.1. Antivírus e EDR (Endpoint Detection and Response)
* **Eficácia contra Ransomware:** Como a análise comportamental (EDR) detecta tentativas de criptografia em massa de arquivos e como ela pode interromper o processo antes do dano ser concluído.
* **Eficácia contra Keylogger:** Como o AV/EDR pode identificar processos que tentam interceptar eventos do teclado ou abrir conexões de rede suspeitas (exfiltração).

### 1.2. Firewall de Rede e Pessoal
* **Mitigação de Exfiltração:** Como um firewall bem configurado pode bloquear o tráfego de saída do `smtplib` do Keylogger para o servidor do atacante.
* **Segmentação:** A importância da segmentação de rede para conter a propagação de um Ransomware.

### 1.3. Sandboxing e Isolamento
* [cite_start]**Conceito:** O uso de Ambientes Virtuais (como a MV Kali utilizada no projeto) para executar e analisar códigos suspeitos sem risco ao sistema operacional principal.
* **Uso:** Como o sandboxing pode ser aplicado na abertura de anexos de e-mail ou links desconhecidos.

## 2. Defesas Comportamentais

### 2.1. Conscientização do Usuário
* [cite_start]**O Elo Mais Fraco:** Por que a educação do usuário é a defesa mais crítica contra phishing e engenharia social, que são vetores comuns para Keyloggers e Ransomware[cite: 17].
* **Boas Práticas:** Detalhe o uso de senhas fortes, MFA e a prática de desconfiar de links e anexos.

### 2.2. Política de Backup (Mitigação do Ransomware)
* **Estratégia 3-2-1:** Documente a importância de manter backups regulares, testados e **isolados** (offline ou air-gapped) como a última linha de defesa contra o sequestro de dados.
