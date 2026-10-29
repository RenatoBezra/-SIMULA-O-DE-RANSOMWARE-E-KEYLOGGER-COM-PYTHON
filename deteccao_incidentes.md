# 🔍 Detecção de Incidentes — Ransomware e Keylogger

## Indicadores de Comprometimento (IoC) — Ransomware

### Sinais precoces (antes da cifragem em massa)
| Indicador | Ferramenta de Detecção |
|---|---|
| Acesso incomum a grandes volumes de arquivos em curto período | SIEM / auditoria de arquivos (Windows Event 4663) |
| Tentativas de desabilitar VSS (`vssadmin delete shadows`) | EDR / monitoramento de processos |
| Criação de processos filhos suspeitos a partir do Office/PDF | EDR com análise comportamental |
| Comunicação com IPs/domínios de C2 (Command & Control) | Firewall NGFW / DNS Sinkhole |
| Exclusão de backups locais | Auditoria de eventos / SIEM |

### Sinais durante a cifragem
| Indicador | Como detectar |
|---|---|
| CPU/disco em uso intenso sem causa aparente | Monitoramento de recursos (Zabbix, Datadog) |
| Extensões desconhecidas aparecendo em arquivos (`.locked`, `.enc`, `.crypted`) | SIEM / File Integrity Monitoring (FIM) |
| Nota de resgate (`README.txt`, `DECRYPT.txt`) criada em múltiplas pastas | FIM / EDR |

---

## Indicadores de Comprometimento (IoC) — Keylogger

| Indicador | Como detectar |
|---|---|
| Processo desconhecido com handle para dispositivos de teclado | Sysinternals Process Explorer / EDR |
| Hook de teclado registrado (`SetWindowsHookEx` com `WH_KEYBOARD_LL`) | Análise de API calls / EDR |
| Processo gravando arquivo de log em pasta suspeita | FIM / auditoria de arquivos |
| Tráfego de saída em porta não padrão (exfiltração do log) | Firewall de saída / NDR |
| Entrada no registro para persistência (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`) | Monitoramento de registro / EDR |

---

## Ferramentas de Detecção

### Nível Host (Endpoint)
- **EDR** (Endpoint Detection & Response): CrowdStrike, Microsoft Defender for Endpoint, SentinelOne
- **Antivírus tradicional**: detecta assinaturas conhecidas
- **Sysinternals Suite** (Windows): Process Monitor, Process Explorer, Autoruns — análise manual
- **Auditpol** (Windows): habilitar auditoria de acesso a objetos

### Nível Rede
- **IDS/IPS**: Snort, Suricata — detecta padrões de tráfego malicioso
- **DNS Filtering**: bloqueia e loga consultas a domínios maliciosos (Cisco Umbrella, Cloudflare Gateway)
- **SIEM**: Splunk, Elastic SIEM, Microsoft Sentinel — correlação de eventos

### Integridade de Arquivos
- **FIM** (File Integrity Monitoring): OSSEC, Wazuh, Tripwire
- Alerta quando arquivos críticos são modificados ou extensões mudam em massa

---

## Linha do Tempo Típica de um Ataque de Ransomware

```
Dia 0    → Phishing ou exploit instala o "loader" (dropper)
Dia 1–14 → Reconhecimento interno: mapear rede, AD, backups
           Movimento lateral: spread para mais máquinas
           Exfiltração: copiar dados antes de cifrar (dupla extorsão)
Dia X    → Gatilho: cifra tudo simultaneamente
           Nota de resgate aparece
Dia X+   → Investigação, contenção, recuperação
```

**Detecção precoce (dias 1–14) é a chave**: interromper o ataque antes da cifragem elimina o impacto mais grave.

---

## SIEM: Exemplos de Regras de Correlação

```
# Alerta: criação em massa de arquivos com extensão desconhecida
regra: arquivo_novo.extensão NOT IN (lista_conhecida)
       E contagem > 100 em 60 segundos
       E mesmo processo
→ ALERTA CRÍTICO: possível ransomware

# Alerta: hook de teclado registrado
regra: processo_api_call = "SetWindowsHookEx"
       E parâmetro = "WH_KEYBOARD_LL"
       E processo NOT IN (lista_aprovada)
→ ALERTA ALTO: possível keylogger
```
