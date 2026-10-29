# 📚 Conceitos Fundamentais — Ransomware e Keylogger

## O Que É Ransomware?

Ransomware é um tipo de malware que **cifra os arquivos da vítima** e exige pagamento (resgate) para fornecer a chave de descriptografia. O nome vem do inglês *ransom* (resgate) + *software*.

### Ciclo de Vida de um Ataque de Ransomware

```
1. INFECÇÃO
   └─ Phishing com anexo malicioso
   └─ Exploit de vulnerabilidade (ex: RDP exposto)
   └─ Drive-by download (site comprometido)

2. ESTABELECIMENTO (Persistence)
   └─ Cria entrada no registro ou tarefa agendada
   └─ Pode ficar dormindo dias/semanas

3. RECONHECIMENTO INTERNO
   └─ Mapeia drives de rede, backups, AD
   └─ Identifica os dados mais valiosos

4. EXFILTRAÇÃO (Dupla Extorsão)
   └─ Copia dados para servidor do atacante
   └─ "Pague ou publicamos os dados"

5. CIFRAGEM
   └─ Gera par de chaves RSA local
   └─ Cifra arquivos com AES (rápido)
   └─ Cifra a chave AES com RSA pública do atacante
   └─ Apaga cópias de sombra (VSS)

6. EXTORSÃO
   └─ Nota de resgate com prazo e valor
   └─ Site onion para negociação
   └─ Pagamento em criptomoeda
```

### Evolução das Gerações

| Geração | Característica | Exemplo |
|---|---|---|
| 1ª (2005–2012) | Bloqueio de tela, sem cifragem real | Police Ransomware |
| 2ª (2013–2016) | Cifragem assimétrica real | CryptoLocker, CTB-Locker |
| 3ª (2017–2019) | Worm + ransomware (auto-propagação) | WannaCry, NotPetya |
| 4ª (2020+) | Dupla extorsão + RaaS (Ransomware as a Service) | REvil, Conti, LockBit |

---

## O Que É Keylogger?

Keylogger é um software (ou hardware) que **registra as teclas digitadas** pelo usuário sem seu conhecimento. Pode ser:

- **Software**: hook de teclado no SO, driver interceptador, malware
- **Hardware**: dispositivo físico entre teclado e computador

### O Que um Keylogger Real Captura

- Senhas digitadas em qualquer aplicativo
- Mensagens de chat e e-mail
- Dados de cartão de crédito
- Consultas de busca
- Qualquer texto digitado

### Como é Distribuído

- Bundling com software pirata
- Phishing (download de "atualizações" falsas)
- Exploits de browser (drive-by download)
- Acesso físico ao computador (keylogger de hardware)
- RAT (Remote Access Trojan) com componente keylogger

---

## Criptografia Aplicada ao Ransomware

### Por que AES + RSA (criptografia híbrida)?

| Algoritmo | Velocidade | Segurança | Uso no ransomware |
|---|---|---|---|
| AES-256 (simétrico) | Muito rápido | Alta | Cifra os arquivos |
| RSA-2048 (assimétrico) | Lento | Alta | Protege a chave AES |

**Fluxo:**
```
Para cada arquivo:
  1. Gera chave AES aleatória (256 bits)
  2. Cifra o arquivo com AES ← muito rápido
  3. Cifra a chave AES com RSA pública do atacante
  4. Armazena a chave AES cifrada junto ao arquivo

Para descriptografar:
  1. Atacante usa RSA privada (que só ele tem) para decifrar a chave AES
  2. A chave AES decifra o arquivo
```

**Por que isso importa:** sem a chave RSA privada do atacante, a recuperação é **computacionalmente inviável** com hardware moderno.

---

## Fernet: Algoritmo Usado nesta Simulação

Esta simulação usa `cryptography.Fernet` (biblioteca Python), que implementa:
- **AES-128 no modo CBC** para cifragem
- **HMAC-SHA256** para integridade (detecta alteração do arquivo cifrado)
- **Chave simétrica** (mesma chave para cifrar e decifrar)

Difere do ransomware real: aqui a chave fica local (fins didáticos). Em ataques reais, a chave fica exclusivamente com o atacante.

---

## Legislação Brasileira

| Lei | Relevância |
|---|---|
| **Lei 12.737/2012** (Lei Carolina Dieckmann) | Criminaliza invasão de dispositivo informático |
| **Lei 14.155/2021** | Aumenta penas para crimes de invasão com obtenção de dados e fraudes eletrônicas |
| **LGPD (Lei 13.709/2018)** | Obriga notificação à ANPD em caso de vazamento de dados pessoais |

Criar ou distribuir ransomware/keylogger fora de contexto autorizado configura crime com penas de reclusão de 2 a 5 anos (agravadas se há dano a infraestrutura crítica ou vítima em condição especial).
