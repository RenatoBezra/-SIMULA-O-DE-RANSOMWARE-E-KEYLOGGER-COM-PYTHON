# 🚨 Resposta a Incidentes — Ransomware e Keylogger

## Framework: NIST SP 800-61 (adaptado)

As fases são: **Preparação → Detecção → Contenção → Erradicação → Recuperação → Lições Aprendidas**

---

## Fase 1: Preparação (antes do incidente)

- [ ] Plano de Resposta a Incidentes (IR Plan) documentado e testado
- [ ] Equipe de resposta definida (CSIRT / SOC)
- [ ] Backups verificados e testados (restore drill mensal)
- [ ] Contatos de fornecedores, autoridades e seguradoras mapeados
- [ ] Imagens de referência (gold images) dos sistemas críticos armazenadas offline
- [ ] Segmentação de rede implementada (limita propagação lateral)

---

## Fase 2: Detecção e Análise

1. **Confirme o incidente**: não confunda erros de sistema com cifragem maliciosa.
2. **Escopo**: quantas máquinas afetadas? Quais dados? Qual variante?
3. **Colete evidências ANTES de qualquer ação**:
   - Capture memória RAM (volatility, FTK Imager) — a chave pode estar na memória
   - Registre logs de sistema, firewall e SIEM
   - Fotografe a tela da máquina afetada (nota de resgate)
4. **Identifique o vetor de entrada**: phishing? RDP exposto? Vulnerabilidade?
5. **Notifique a cadeia de comando** e ative o plano de IR.

---

## Fase 3: Contenção

### Contenção imediata (primeiros minutos)
```
1. ISOLAR as máquinas afetadas da rede (desconectar cabo de rede / desativar Wi-Fi)
   ⚠️  NÃO DESLIGUE: memória RAM pode conter chave de descriptografia
2. Desativar contas comprometidas no Active Directory
3. Bloquear IPs/domínios de C2 no firewall
4. Revogar VPNs e acessos remotos
```

### Contenção de longo prazo
- Isolar segmentos de rede afetados
- Monitorar tráfego em busca de persistência residual
- Verificar e revogar certificados comprometidos

---

## Fase 4: Erradicação

- Identificar e remover o malware de todas as máquinas (incluindo as não cifradas)
- Corrigir a vulnerabilidade explorada (patch, configuração, senha)
- Remover contas backdoor criadas pelo atacante
- Verificar scripts de persistência: registro, tarefas agendadas, serviços
- Realizar varredura completa com EDR/antivírus em toda a rede

---

## Fase 5: Recuperação

### Prioridade de restauração
```
1. Infraestrutura crítica (AD, DNS, autenticação)
2. Sistemas de negócio essenciais
3. Sistemas de suporte
4. Estações de trabalho dos usuários
```

### Checklist de recuperação
- [ ] Restaurar a partir de backup **verificado** (anterior ao ataque)
- [ ] Validar integridade dos dados restaurados
- [ ] Reinstalar SO limpo antes de restaurar dados (não confiar na imagem comprometida)
- [ ] Redefinir TODAS as senhas (especialmente se keylogger estava ativo)
- [ ] Reemitir certificados e tokens comprometidos
- [ ] Monitorar sistemas restaurados por 30 dias (attacker may lurk)

### ⚠️ Sobre pagar o resgate
| Argumento | Realidade |
|---|---|
| "Vou recuperar os dados pagando" | 40% das vítimas não recuperam mesmo após pagar (Coveware, 2023) |
| "É mais barato que a recuperação" | Custos médios de recuperação excedem o resgate (downtime, forense, reputação) |
| "Só desta vez" | Pagadores são alvos recorrentes — sinaliza disposição de pagar |
| "Autoridades entendem" | Em vários países, pagar grupos sancionados (ex: Evil Corp) pode ser ilegal |

---

## Fase 6: Lições Aprendidas (Post-mortem)

Realizar reunião pós-incidente com:
1. **Cronologia completa**: quando entrou, quando detectado, quando contido
2. **Causa raiz**: qual controle falhou? Por quê?
3. **Impacto**: dados afetados, horas de downtime, custo financeiro
4. **Melhorias**: o que implementar para evitar recorrência?
5. **Atualização do IR Plan**: incorporar aprendizados

---

## Recursos de Apoio

| Recurso | URL |
|---|---|
| No More Ransom (chaves de descriptografia gratuitas) | https://www.nomoreransom.org |
| ID Ransomware (identificar variante pela nota) | https://id-ransomware.malwarehunterteam.com |
| CISA Ransomware Guide | https://www.cisa.gov/stopransomware |
| CERT.br (BR) | https://www.cert.br |
