import pytest

from organizando_mi_mundo.models.task import Task


def test_task_creation():
    task = Task("Prueba", "Descripción")
    assert task.title == "Prueba"
    assert task.description == "Descripción"
    assert not task.completed


def test_mark_completed():
    task = Task("Prueba", "Descripción")
    task.mark_completed()
    assert task.completed


def test_task_creation_invalid_title():
    with pytest.raises(ValueError, match="título de la tarea no puede estar vacío"):
        Task("", "Descripción")
