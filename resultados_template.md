# 📊 Resultados da Simulação — Template

> **Instruções:** Preencha este documento com os resultados **reais** obtidos ao executar os scripts no seu computador. Não invente saídas — registre o que realmente aconteceu, mesmo que diferente do esperado.

---

## 1. Ambiente de Laboratório

| Item | Detalhe |
|---|---|
| Sistema Operacional | _(ex.: Windows 11, Ubuntu 22.04)_ |
| Versão do Python | _(saída de `python3 --version`)_ |
| Versão da biblioteca `cryptography` | _(saída de `pip show cryptography`)_ |
| Versão da biblioteca `pynput` | _(saída de `pip show pynput`)_ |
| Data de execução | _(DD/MM/AAAA)_ |

---

## 2. Módulo Ransomware — Resultados

### 2.1 Criação dos Arquivos de Teste

```
# Cole aqui a saída real de:
# python3 ransomware_simulado/criador_arquivos_teste.py

[cole a saída aqui]
```

**Arquivos criados:** _liste os nomes_

### 2.2 Cifragem (Encriptador)

```
# Cole aqui a saída real de:
# python3 ransomware_simulado/encriptador.py

[cole a saída aqui]
```

**Observações:**
- [ ] Os arquivos `.txt` foram substituídos por `.txt.enc`
- [ ] O arquivo `chave_laboratorio.key` foi gerado
- [ ] A nota de resgate `LEIA-ME-RANSOMWARE.txt` foi criada
- [ ] O conteúdo dos `.enc` é ilegível (texto cifrado)

**Captura de tela sugerida:** `evidencias/encriptacao.png`

### 2.3 Descriptografia (Decriptador)

```
# Cole aqui a saída real de:
# python3 ransomware_simulado/decriptador.py

[cole a saída aqui]
```

**Observações:**
- [ ] Os arquivos originais `.txt` foram recuperados
- [ ] Os arquivos `.enc` foram removidos
- [ ] A nota de resgate foi removida
- [ ] O conteúdo recuperado é idêntico ao original

---

## 3. Módulo Keylogger — Resultados

### 3.1 Execução do Keylogger Simulado

```
# Cole aqui a saída parcial (primeiras linhas) de:
# python3 keylogger_simulado/keylogger.py

[cole a saída aqui — oculte senhas reais se digitou alguma]
```

**Observações:**
- [ ] Consentimento foi solicitado antes do início
- [ ] As teclas apareceram em tempo real na tela
- [ ] O log foi salvo em `keylogger_simulado/capturas/`
- [ ] O programa encerrou ao pressionar ESC (ou atingir limite)

**Trecho do arquivo de log gerado** (oculte dados sensíveis):
```
[cole as primeiras linhas do arquivo .log aqui]
```

---

## 4. Análise Comparativa: Simulação × Ataque Real

| Aspecto | Esta Simulação | Ataque Real |
|---|---|---|
| Cifragem | Fernet/AES-128, chave local | AES-256 + RSA-2048, chave remota |
| Escopo | Só arquivos fictícios em `arquivos_teste/` | Todos os drives mapeados, rede |
| Persistência | Nenhuma | Registro, serviços, WMI |
| Exfiltração | Não ocorre | Dados enviados antes da cifragem |
| Propagação | Não ocorre | Movimento lateral, worm (WannaCry) |
| Keylogger | Visível, consentido, terminal apenas | Oculto, qualquer janela, rede |

---

## 5. Reflexões e Aprendizados

**O que este laboratório demonstrou:**

_(Escreva em suas próprias palavras o que você aprendeu com a simulação)_

**A principal diferença entre a simulação e um ataque real que mais me impressionou:**

_(Descreva)_

**Qual medida de defesa você implementaria PRIMEIRO em uma empresa real:**

_(Justifique)_
