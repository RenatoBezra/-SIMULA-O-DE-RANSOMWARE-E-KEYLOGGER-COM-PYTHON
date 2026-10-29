#!/usr/bin/env python3
"""
criador_arquivos_teste.py
Cria arquivos FICTÍCIOS para uso como "vítimas" da simulação de ransomware.

Onde rodar: qualquer SO, dentro da pasta do projeto (rede local, sem internet).
Uso:
    python3 ransomware_simulado/criador_arquivos_teste.py

Saída: pasta arquivos_teste/ com 5 arquivos .txt fictícios prontos para cifrar.

⚠️ FINS EXCLUSIVAMENTE EDUCACIONAIS.
   Todos os dados são inventados. Nenhum arquivo real é tocado.
"""
import sys
from pathlib import Path

DESTINO = Path(__file__).resolve().parent.parent / "arquivos_teste"

ARQUIVOS_FICTICIOS = {
    "relatorio_financeiro_q1.txt": """\
=== RELATÓRIO FINANCEIRO — 1º TRIMESTRE (FICTÍCIO) ===
Empresa : Acme Corp Ltda (CNPJ 00.000.000/0001-00) — dados inventados
Receita : R$ 1.234.567,89
Despesas: R$ 987.654,32
Lucro   : R$ 246.913,57
---
Este arquivo é FICTÍCIO e foi criado apenas para demonstração educacional.
""",
    "lista_clientes.txt": """\
=== LISTA DE CLIENTES (FICTÍCIA) ===
ID   | Nome            | E-mail (fictício)
-----|-----------------|----------------------------
001  | João da Silva   | joao@exemplo-ficticio.com
002  | Maria Oliveira  | maria@exemplo-ficticio.com
003  | Carlos Pereira  | carlos@exemplo-ficticio.com
---
Dados INVENTADOS — nenhuma pessoa real identificada.
""",
    "senhas_sistema.txt": """\
=== CREDENCIAIS DE SISTEMA (FICTÍCIAS) ===
Sistema : Portal Interno Acme (fictício)
Usuário : admin_ficticio
Senha   : SenhaSuperFicticia@2024
---
⚠️ NUNCA armazene senhas reais em arquivos de texto.
   Este arquivo é 100% inventado para fins didáticos.
""",
    "contrato_fornecedor.txt": """\
=== CONTRATO DE FORNECIMENTO N.º 001/2024 (FICTÍCIO) ===
Contratante: Acme Corp Ltda (inventada)
Fornecedor : Beta Supplies S/A (inventada)
Objeto     : Fornecimento de materiais de escritório
Valor      : R$ 50.000,00 / mês
Vigência   : 12 meses a partir de 01/01/2024
---
Documento FICTÍCIO criado para simulação educacional de ransomware.
""",
    "dados_pessoais_rh.txt": """\
=== CADASTRO DE COLABORADORES — RH (FICTÍCIO) ===
Matrícula | Nome             | Cargo         | Salário (R$)
----------|------------------|---------------|-------------
1001      | Ana Fictícia     | Analista       | 5.000,00
1002      | Bruno Fictício   | Desenvolvedor  | 7.500,00
1003      | Carla Fictícia   | Gerente        | 12.000,00
---
ATENÇÃO: estes dados são COMPLETAMENTE INVENTADOS.
Jamais armazene dados pessoais reais sem proteção adequada (LGPD).
""",
}


def criar_arquivos() -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    print(f"[*] Criando arquivos fictícios em: {DESTINO}\n")
    for nome, conteudo in ARQUIVOS_FICTICIOS.items():
        caminho = DESTINO / nome
        caminho.write_text(conteudo, encoding="utf-8")
        print(f"    [+] {nome}  ({caminho.stat().st_size} bytes)")
    print(f"\n[OK] {len(ARQUIVOS_FICTICIOS)} arquivos fictícios criados.")
    print("     Execute encriptador.py para cifrar estes arquivos.")


if __name__ == "__main__":
    criar_arquivos()
