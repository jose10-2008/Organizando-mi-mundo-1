from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table


class TaskView:
    """Vista que muestra información de las tareas en la consola."""

    console = Console()

    @staticmethod
    def display_menu():
        """Muestra el menú principal al usuario."""
        panel = Panel(
            "[bold cyan]1[/bold cyan]. Crear tarea\n"
            "[bold cyan]2[/bold cyan]. Listar tareas\n"
            "[bold cyan]3[/bold cyan]. Marcar tarea como completada\n"
            "[bold cyan]4[/bold cyan]. Exportar tareas a CSV\n"
            "[bold cyan]5[/bold cyan]. Salir",
            title="[bold green]Organizando Mi Mundo[/bold green]",
            border_style="green",
        )
        TaskView.console.print(panel)

    @staticmethod
    def display_tasks(tasks):
        """Muestra todas las tareas en una lista ordenada."""
        if not tasks:
            TaskView.console.print(Panel("No hay tareas aún.", title="[bold yellow]Tareas[/bold yellow]", border_style="yellow"))
            return

        table = Table(title="Tareas", show_lines=True)
        table.add_column("#", justify="right")
        table.add_column("Título", style="cyan")
        table.add_column("Descripción", style="magenta")
        table.add_column("Estado", style="green")

        for index, task in enumerate(tasks, start=1):
            estado = "✅ Completada" if task.completed else "❌ Pendiente"
            table.add_row(str(index), task.title, task.description, estado)

        TaskView.console.print(table)

    @staticmethod
    def display_message(message):
        """Muestra un mensaje simple en pantalla."""
        TaskView.console.print(Panel(message, border_style="blue"))

    @staticmethod
    def ask_for_task_data():
        """Pide título y descripción al usuario para crear una tarea."""
        title = Prompt.ask("Título de la tarea").strip()
        description = Prompt.ask("Descripción de la tarea").strip()
        return title, description

    @staticmethod
    def ask_for_task_index():
        """Pide al usuario el número de tarea para marcarla completada."""
        return Prompt.ask("Número de tarea a marcar como completada").strip()

    @staticmethod
    def ask_for_export_filename():
        """Pide al usuario el nombre del archivo CSV donde se exportarán las tareas."""
        return Prompt.ask("Nombre del archivo CSV", default="tareas.csv").strip()
