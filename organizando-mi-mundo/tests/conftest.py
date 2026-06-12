import sys
from pathlib import Path

# Agrega la carpeta src al PYTHONPATH para que pytest pueda importar el paquete.
ROOT = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(ROOT))
