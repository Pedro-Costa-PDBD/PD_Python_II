from rich.console import Console
from rich.text import Text

console = Console()

def texto_colorido(texto: str, is_arquivo: bool):
    """
    Exibe o texto em cores.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    styled_text = Text(texto, style="bold green")
    console.print(styled_text)


def texto_com_fundo(texto: str, is_arquivo: bool):
    """
    Exibe o texto com um fundo colorido.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    styled_text = Text(texto, style="on yellow bold red")
    console.print(styled_text)