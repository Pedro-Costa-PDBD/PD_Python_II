import argparse
from personalizador import Biblioteca_Rich_layout, Biblioteca_Rich_display, Biblioteca_Rich_estilo, Biblioteca_Rich_painel

# Mapeamento de módulos e funções
modulos = {
    "layout": Biblioteca_Rich_layout,
    "painel": Biblioteca_Rich_display,
    "progresso": Biblioteca_Rich_estilo,
    "estilo": Biblioteca_Rich_painel
}

funcoes = {
    "layout": ["exibir_layout", "exibir_centralizado"],
    "painel": ["exibir_painel", "exibir_painel_alerta"],
    "progresso": ["barra_progresso", "progresso_simples"],
    "estilo": ["texto_colorido", "texto_com_fundo"]
}

# Configuração do argparse
parser = argparse.ArgumentParser(description="Personalizador de Texto com Rich")
parser.add_argument("texto", help="Texto ou caminho para o arquivo")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica se o texto é um arquivo")
parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(), help="Módulo para usar")
parser.add_argument("-f", "--funcao", required=True, help="Função do módulo para executar")

args = parser.parse_args()

# Executa a função escolhida
modulo = modulos[args.modulo]
if args.funcao in funcoes[args.modulo]:
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)
else:
    print(f"Função inválida para o módulo {args.modulo}. Opções: {funcoes[args.modulo]}")