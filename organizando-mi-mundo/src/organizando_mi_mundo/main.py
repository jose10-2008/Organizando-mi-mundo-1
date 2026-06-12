"""Punto de entrada ejecutable para la aplicación "Organizando Mi Mundo".

Este módulo se encarga de inicializar el `TaskController` y arrancar el
bucle principal de la aplicación de consola.

Ejecución:

    python src/organizando_mi_mundo/main.py

Nota: `conftest.py` para las pruebas añade `src/` al `PYTHONPATH`. Aquí
se añade la carpeta padre del paquete al `sys.path` solo cuando se ejecuta
directamente como script para permitir la ejecución desde la carpeta del
proyecto sin instalar el paquete.
"""

import sys
from pathlib import Path

# Añade la carpeta `src` al path cuando se ejecuta el módulo como script.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from organizando_mi_mundo.controllers.task_controller import TaskController


def main() -> None:
    """Inicia la aplicación creando el controlador principal.

    La función no devuelve valores; lanza el bucle interactivo que gestiona
    la entrada del usuario hasta que éste seleccione salir.
    """
    controller = TaskController()
    controller.run()


if __name__ == "__main__":
    main()
