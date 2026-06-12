# Contribuir al proyecto "Organizando Mi Mundo"

Gracias por querer contribuir. Sigue estas pautas para mantener el proyecto claro y consistente.

- Haz un fork del repositorio y crea una branch con nombre descriptivo (ej: `fix/validacion-titulo`).
- Escribe commits atómicos y con mensajes claros (en español o inglés).
- Antes de enviar un pull request, ejecuta:

```powershell
python -m pip install -r requirements.txt
python -m pytest
```

- Sigue el estilo existente en el código: nombres descriptivos, docstrings y separación MVC.
- Si añades funcionalidades, incluye pruebas unitarias en `tests/`.
- Si añades dependencias, actualiza `requirements.txt`.

Gracias por tu aporte.