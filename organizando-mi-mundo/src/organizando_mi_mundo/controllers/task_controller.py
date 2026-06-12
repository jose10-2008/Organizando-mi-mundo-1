"""Controlador principal del proyecto.

Contiene `TaskController`, que orquesta el flujo de la aplicación entre
el modelo (`TaskManager`) y la vista (`TaskView`).

Responsabilidades:
- interpretar la entrada del usuario
- validar entradas básicas
- delegar operaciones al `TaskManager`
- formatear y delegar salidas a la `TaskView`
"""

import pandas as pd

from organizando_mi_mundo.models.task_manager import TaskManager
from organizando_mi_mundo.views.task_view import TaskView


class TaskController:
    """Controlador que maneja la lógica entre el modelo y la vista."""

    def __init__(self):
        # Delegamos la colección y operaciones sobre tareas a TaskManager
        self.manager = TaskManager()
        self.view = TaskView()

    def run(self):
        """Inicia el bucle principal del programa."""
        self.view.display_message("Bienvenido a Organizando Mi Mundo")

        while True:
            self.view.display_menu()
            choice = input("Selecciona una opción: ").strip()

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.export_tasks()
            elif choice == "5":
                self.exit_program()
                break
            else:
                self.view.display_message("Opción no válida. Intenta de nuevo.")

    def create_task(self):
        """Crea una nueva tarea usando datos ingresados por el usuario."""
        title, description = self.view.ask_for_task_data()

        if not title:
            self.view.display_message("El título no puede estar vacío.")
            return

        try:
            self.manager.add_task(title, description)
        except ValueError as error:
            self.view.display_message(str(error))
            return

        self.view.display_message("Tarea creada correctamente.")

    def list_tasks(self):
        """Muestra todas las tareas guardadas."""
        self.view.display_tasks(self.manager.list_tasks())

    def complete_task(self):
        """Marca una tarea como completada según el índice ingresado."""
        if self.manager.count() == 0:
            self.view.display_message("No hay tareas para marcar como completadas.")
            return

        self.view.display_tasks(self.manager.list_tasks())
        choice = self.view.ask_for_task_index()

        if not choice.isdigit():
            self.view.display_message("Debes escribir un número válido.")
            return

        index = int(choice) - 1
        try:
            self.manager.complete_task(index)
        except IndexError:
            self.view.display_message("Número de tarea inválido.")
            return

        self.view.display_message("Tarea marcada como completada.")

    def export_tasks(self):
        """Exporta las tareas actuales a un archivo CSV usando pandas."""
        if self.manager.count() == 0:
            self.view.display_message("No hay tareas para exportar.")
            return

        filename = self.view.ask_for_export_filename()
        if not filename:
            filename = "tareas.csv"

        data = [
            {
                "Título": task.title,
                "Descripción": task.description,
                "Completada": task.completed,
            }
            for task in self.manager.list_tasks()
        ]

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        self.view.display_message(f"Tareas exportadas a [bold green]{filename}[/bold green]")

    def exit_program(self):
        """Finaliza el programa mostrando un mensaje de despedida."""
        self.view.display_message("Gracias por usar Organizando Mi Mundo. ¡Hasta luego!")
