#!/usr/bin/env python3
"""
keylogger.py
Simulação EDUCACIONAL, INTERATIVA e TOTALMENTE VISÍVEL de keylogger.

DIFERENÇAS CRÍTICAS em relação a um keylogger real (malicioso):
  ✅ Opera SOMENTE com consentimento explícito do usuário (confirmação no início).
  ✅ Atividade é exibida EM TEMPO REAL na tela (zero ocultação).
  ✅ Encerramento a qualquer momento com ESC ou Ctrl+C.
  ✅ Log salvo LOCALMENTE — nenhum dado enviado pela rede.
  ✅ Pasta e arquivo de log são exibidos claramente ao usuário.
  ✅ Sem persistência: não se registra como serviço, tarefa agendada ou chave de registro.
  ✅ Sem ofuscação de código.

Onde rodar: em seu próprio computador, janela de terminal visível.
Uso:
    python3 keylogger_simulado/keylogger.py

⚠️ USO RESTRITO AO LABORATÓRIO PRÓPRIO — NUNCA em equipamento de terceiros.
"""
import sys
import datetime
from pathlib import Path

try:
    from pynput import keyboard
except ImportError:
    sys.exit("Instale a dependência:  pip install pynput")

RAIZ = Path(__file__).resolve().parent.parent
PASTA_LOG = RAIZ / "keylogger_simulado" / "capturas"
LIMITE_TECLAS = 200          # teto didático — encerra automaticamente
TECLA_SAIDA = keyboard.Key.esc


# ---------------------------------------------------------------------------
# Utilitários de exibição
# ---------------------------------------------------------------------------

def cabecalho() -> None:
    print("\n" + "=" * 65)
    print("   SIMULAÇÃO EDUCACIONAL DE KEYLOGGER — DIO Cybersecurity Lab")
    print("=" * 65)
    print("""
  O QUE ESTE SCRIPT FAZ:
    • Registra as teclas digitadas NESTA janela de terminal.
    • Exibe cada tecla na tela em tempo real (sem ocultação).
    • Salva um log local na pasta keylogger_simulado/capturas/.
    • Para automaticamente após {} teclas ou ao pressionar ESC.

  O QUE ELE NÃO FAZ (diferença de um keylogger malicioso):
    • Não monitora outras janelas ou aplicativos do sistema.
    • Não envia dados pela internet.
    • Não se instala como serviço ou processo oculto.
    • Não persiste após o encerramento do terminal.
""".format(LIMITE_TECLAS))


def solicitar_consentimento() -> bool:
    print("-" * 65)
    print("  ⚠️  CONSENTIMENTO NECESSÁRIO")
    print("-" * 65)
    resp = input(
        "  Você confirma que está executando esta simulação\n"
        "  em seu PRÓPRIO computador, com fins EDUCACIONAIS? [s/N]: "
    ).strip().lower()
    return resp == "s"


# ---------------------------------------------------------------------------
# Núcleo do keylogger simulado
# ---------------------------------------------------------------------------

class KeyloggerEducacional:
    def __init__(self, arquivo_log: Path) -> None:
        self.arquivo_log = arquivo_log
        self.contador = 0
        self.buffer: list[str] = []
        self.listener: keyboard.Listener | None = None

        arquivo_log.parent.mkdir(parents=True, exist_ok=True)
        self._escrever_cabecalho_log()

    def _escrever_cabecalho_log(self) -> None:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.arquivo_log.open("w", encoding="utf-8") as f:
            f.write(f"=== LOG DE SIMULAÇÃO EDUCACIONAL ===\n")
            f.write(f"Início   : {ts}\n")
            f.write(f"Arquivo  : {self.arquivo_log}\n")
            f.write(f"Limite   : {LIMITE_TECLAS} teclas\n")
            f.write("=" * 40 + "\n\n")

    def _registrar(self, entrada: str) -> None:
        ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        linha = f"[{ts}] {entrada}"
        self.buffer.append(linha)
        print(f"  {linha}")
        with self.arquivo_log.open("a", encoding="utf-8") as f:
            f.write(linha + "\n")

    def ao_pressionar(self, tecla: keyboard.Key | keyboard.KeyCode) -> bool | None:
        self.contador += 1

        # Converte a tecla para representação legível
        if hasattr(tecla, "char") and tecla.char is not None:
            representacao = f"CHAR  : '{tecla.char}'"
        elif tecla == keyboard.Key.space:
            representacao = "ESPAÇO"
        elif tecla == keyboard.Key.enter:
            representacao = "ENTER"
        elif tecla == keyboard.Key.backspace:
            representacao = "BACKSPACE"
        elif tecla == keyboard.Key.tab:
            representacao = "TAB"
        elif tecla == TECLA_SAIDA:
            representacao = "ESC — encerrando…"
            self._registrar(representacao)
            return False   # Para o listener
        else:
            representacao = f"ESPECIAL: {tecla}"

        self._registrar(representacao)

        if self.contador >= LIMITE_TECLAS:
            self._registrar(f"LIMITE DE {LIMITE_TECLAS} TECLAS ATINGIDO — encerrando…")
            return False

        return None  # Continua ouvindo

    def iniciar(self) -> None:
        print("\n" + "-" * 65)
        print(f"  Monitorando teclas… (ESC ou {LIMITE_TECLAS} teclas para parar)")
        print(f"  Log em tempo real abaixo  |  Arquivo: {self.arquivo_log.name}")
        print("-" * 65 + "\n")
        with keyboard.Listener(on_press=self.ao_pressionar) as listener:
            self.listener = listener
            listener.join()
        self._finalizar()

    def _finalizar(self) -> None:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.arquivo_log.open("a", encoding="utf-8") as f:
            f.write(f"\n=== FIM DA SESSÃO — {ts} ===\n")
            f.write(f"Total de teclas capturadas: {self.contador}\n")

        print("\n" + "=" * 65)
        print(f"  [OK] Sessão encerrada. Total de teclas: {self.contador}")
        print(f"       Log salvo em: {self.arquivo_log}")
        print("=" * 65)
        print("""
  REFLEXÃO DIDÁTICA:
    Em um keylogger MALICIOSO real:
      • Este log seria enviado silenciosamente para o atacante.
      • O processo estaria oculto no gerenciador de tarefas.
      • Ele re-iniciaria automaticamente a cada boot.
      • Poderia capturar qualquer janela, não só o terminal.

  DEFESAS CONTRA KEYLOGGERS REAIS:
      • Antivírus/EDR atualizado com detecção comportamental.
      • Autenticação de dois fatores (mesmo que a senha seja capturada,
        o segundo fator protege a conta).
      • Teclado virtual para dados sensíveis (ex.: internet banking).
      • Gerenciadores de senha que preenchem campos automaticamente
        (sem digitação real que possa ser interceptada).
""")


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------

def main() -> None:
    cabecalho()

    if not solicitar_consentimento():
        print("\n[Encerrado] Execução cancelada pelo usuário — correto!")
        sys.exit(0)

    ts_arquivo = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo_log = PASTA_LOG / f"sessao_{ts_arquivo}.log"

    kl = KeyloggerEducacional(arquivo_log)
    try:
        kl.iniciar()
    except KeyboardInterrupt:
        print("\n[Encerrado] Ctrl+C detectado.")


if __name__ == "__main__":
    main()
