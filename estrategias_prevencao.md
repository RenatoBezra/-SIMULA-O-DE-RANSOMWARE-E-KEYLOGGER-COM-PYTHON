# 🛡️ Estratégias de Prevenção — Ransomware e Keylogger

## 1. Backup — A Principal Defesa contra Ransomware

| Prática | Por quê funciona |
|---|---|
| **Regra 3-2-1**: 3 cópias, 2 mídias diferentes, 1 offline | Cópia offline é inacessível ao ransomware |
| Backups testados regularmente (restore drill) | Backup que nunca foi restaurado pode estar corrompido |
| Snapshots automáticos do sistema (VSS no Windows) | Permitem voltar ao estado pré-ataque |
| Armazenamento imutável em nuvem (Object Lock S3) | Ransomware não consegue deletar versões travadas |

### Por que o backup offline é decisivo
Um ransomware moderno enumera drives mapeados e backups em rede. Se o backup está em um HD externo **desconectado** ou em uma fita offline, ele não pode ser cifrado. Após o incidente, a recuperação é simples: formatar, reinstalar, restaurar backup.

---

## 2. Patches e Atualizações

- Mantenha SO, navegadores e aplicativos **sempre atualizados**.
- Ransomwares históricos como WannaCry e NotPetya exploraram vulnerabilidades já corrigidas (MS17-010 / EternalBlue) em máquinas sem patch.
- Configure o **Windows Update** (ou equivalente) para instalação automática de patches de segurança críticos.
- Priorize patches de: SO, Office, Java, Adobe Reader, navegadores.

---

## 3. Princípio do Menor Privilégio (PoLP)

- Usuários cotidianos **não devem ter conta de administrador**.
- Serviços de rede devem rodar com contas de serviço restritas.
- Limite quais usuários podem executar scripts (PowerShell, macros VBA).
- Use **Controle de Acesso Baseado em Função (RBAC)** em sistemas corporativos.

**Impacto:** Um ransomware executado por um usuário comum tem acesso limitado — não consegue cifrar arquivos do sistema, de outros usuários ou desabilitar o antivírus.

---

## 4. Filtragem de E-mail e Web (Vetor #1 de Infecção)

- Implemente **gateway de e-mail** com análise de anexos em sandbox.
- Bloqueie extensões perigosas: `.exe`, `.bat`, `.vbs`, `.js`, `.hta`, `.scr`, `.ps1`.
- Use **filtro de URL** (DNS Filtering / Proxy) para bloquear domínios maliciosos.
- Treine usuários: não abrir anexos inesperados, verificar remetente antes de clicar.

---

## 5. Proteção contra Keyloggers

| Medida | Eficácia |
|---|---|
| **Autenticação de dois fatores (2FA/MFA)** | Mesmo capturando a senha, o atacante precisa do segundo fator |
| **Gerenciador de senhas** (Bitwarden, KeePass) | Preenche campos sem digitação real — keylogger captura nada |
| **Teclado virtual** para dados bancários | Cliques em botões na tela não são interceptados por keylogger de teclado |
| **Antivírus/EDR com detecção comportamental** | Identifica hooks de teclado suspeitos |
| **Verificação de integridade do SO** (Secure Boot + TPM) | Bloqueia rootkits que interceptam drivers de teclado |

---

## 6. Controles de Rede

- **Segmentação de rede**: isolar servidores críticos de estações de trabalho.
- **Zero Trust**: autenticar e autorizar cada acesso, mesmo dentro da rede interna.
- **Firewall de saída**: bloquear conexões não autorizadas (impede exfiltração de dados do keylogger).
- **Desabilitar SMBv1**: protocolo usado pelo WannaCry/NotPetya para propagação lateral.

---

## 7. Conscientização e Cultura de Segurança

- Treinamentos periódicos sobre **phishing e engenharia social** (vetor mais comum).
- Simulações de phishing para medir e reduzir a taxa de cliques.
- Política clara de reporte de incidentes (sem punição para quem reporta rapidamente).
- Exercícios de resposta a incidentes (tabletop exercises).
