from rich.console import Console
from rich.layout import Layout

console = Console()

def exibir_layout(texto: str, is_arquivo: bool):
    """
    Exibe o texto formatado usando rich.Layout.
    """
    layout = Layout()
    layout.split_column(
        Layout(name="topo", size=3),
        Layout(name="corpo"),
        Layout(name="rodape", size=3),
    )
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()

    layout["topo"].update("TOPO")
    layout["corpo"].update(texto)
    layout["rodape"].update("RODAPÉ")
    console.print(layout)


def exibir_centralizado(texto: str, is_arquivo: bool):
    """
    Exibe o texto centralizado no layout.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(f"[bold cyan]{texto.center(50)}[/bold cyan]")