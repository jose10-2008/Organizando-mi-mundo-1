class Task:
    """Modelo que representa una tarea dentro de Organizando Mi Mundo."""

    def __init__(self, title: str, description: str):
        """Inicializa una nueva tarea.

        Args:
            title (str): El título o nombre de la tarea.
            description (str): Una descripción breve de la tarea.

        Raises:
            ValueError: Si el título está vacío.
        """
        title = title.strip()
        if not title:
            raise ValueError("El título de la tarea no puede estar vacío.")

        self.title = title
        self.description = description.strip()
        self.completed = False

    def mark_completed(self):
        """Marca la tarea como completada."""
        self.completed = True

    def __str__(self):
        """Devuelve una representación en texto de la tarea."""
        estado = "Completada" if self.completed else "Pendiente"
        return f"{self.title} - {estado}: {self.description}"
