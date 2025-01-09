from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def barra_progresso(texto: str, is_arquivo: bool):
    """
    Exibe uma barra de progresso simulada.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        task = progress.add_task(f"{texto}", total=100)
        for _ in range(100):
            progress.update(task, advance=1)


def progresso_simples(texto: str, is_arquivo: bool):
    """
    Exibe uma barra de progresso simples.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    with Progress() as progress:
        task = progress.add_task("[cyan]Carregando...", total=100)
        for _ in range(100):
            progress.update(task, advance=1)