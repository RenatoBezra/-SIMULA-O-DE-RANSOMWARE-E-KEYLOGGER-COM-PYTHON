#!/usr/bin/env python3
"""
decriptador.py
Simula a fase de DESCRIPTOGRAFIA de um ransomware — RECUPERAÇÃO dos arquivos.

Escopo : APENAS a pasta arquivos_teste/ dentro deste projeto.
Chave  : lida do arquivo chave_laboratorio.key gerado pelo encriptador.

Uso:
    python3 ransomware_simulado/decriptador.py

O que acontece:
  1. Carrega a chave Fernet do arquivo local.
  2. Descriptografa cada arquivo .txt.enc → <nome>.txt original.
  3. Remove o arquivo cifrado.
  4. Remove a nota de resgate fictícia.

⚠️ USO RESTRITO AO LABORATÓRIO. Fins exclusivamente educacionais.
"""
import sys
from pathlib import Path

try:
    from cryptography.fernet import Fernet, InvalidToken
except ImportError:
    sys.exit("Instale a dependência:  pip install cryptography")

RAIZ = Path(__file__).resolve().parent.parent
PASTA_TESTE = RAIZ / "arquivos_teste"
ARQUIVO_CHAVE = RAIZ / "chave_laboratorio.key"
NOTA_RESGATE = PASTA_TESTE / "LEIA-ME-RANSOMWARE.txt"


def carregar_chave() -> bytes:
    if not ARQUIVO_CHAVE.exists():
        sys.exit(
            f"[ABORTADO] Arquivo de chave não encontrado: {ARQUIVO_CHAVE.name}\n"
            "Em um ransomware real, esta chave estaria com o atacante.\n"
            "No laboratório: execute o encriptador.py antes do decriptador."
        )
    return ARQUIVO_CHAVE.read_bytes()


def validar_escopo() -> None:
    if not PASTA_TESTE.exists():
        sys.exit(f"[ABORTADO] Pasta de teste não encontrada: {PASTA_TESTE}")
    try:
        PASTA_TESTE.resolve().relative_to(RAIZ.resolve())
    except ValueError:
        sys.exit("[ABORTADO] Pasta de teste fora do diretório do projeto.")


def descriptografar_arquivos(fernet: Fernet) -> int:
    alvos = list(PASTA_TESTE.glob("*.enc"))
    if not alvos:
        print("[AVISO] Nenhum arquivo .enc encontrado. Execute o encriptador primeiro.")
        return 0

    print(f"[*] Descriptografando {len(alvos)} arquivo(s) em {PASTA_TESTE.name}/\n")
    recuperados = 0
    for alvo in alvos:
        try:
            cifrado = alvo.read_bytes()
            original = fernet.decrypt(cifrado)
            # Recupera o nome original removendo a extensão .enc
            destino = alvo.with_suffix("")  # remove .enc, mantém .txt
            destino.write_bytes(original)
            alvo.unlink()
            print(f"    [+] {alvo.name}  →  {destino.name}")
            recuperados += 1
        except InvalidToken:
            print(f"    [ERRO] {alvo.name}: chave incorreta ou arquivo corrompido.")

    return recuperados


def remover_nota() -> None:
    if NOTA_RESGATE.exists():
        NOTA_RESGATE.unlink()
        print(f"[*] Nota de resgate removida: {NOTA_RESGATE.name}")


def main() -> None:
    print("=" * 60)
    print("  SIMULAÇÃO EDUCACIONAL — FASE DE DESCRIPTOGRAFIA")
    print("=" * 60)
    print(f"  Escopo: {PASTA_TESTE}")
    print("=" * 60 + "\n")

    validar_escopo()
    chave = carregar_chave()
    fernet = Fernet(chave)
    total = descriptografar_arquivos(fernet)

    if total:
        remover_nota()
        print(f"\n[OK] {total} arquivo(s) recuperado(s).")
        print("     OBSERVAÇÃO DIDÁTICA: a recuperação só foi possível porque")
        print("     a chave estava disponível localmente.")
        print("     Em ataques reais, a chave fica com o atacante.")
