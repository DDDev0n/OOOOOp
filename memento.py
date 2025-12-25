"""
memento.py - Реализация паттерна Memento для сохранения состояния
"""

from copy import deepcopy
from typing import Any, List
from datetime import datetime


class Memento:
    """Снимок состояния объекта"""

    def __init__(self, state: Any, timestamp: str = None):
        self._state = deepcopy(state)
        self._timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_state(self) -> Any:
        return self._state

    def get_timestamp(self) -> str:
        return self._timestamp

    def __repr__(self) -> str:
        return f"Memento({self._timestamp})"


class Caretaker:
    """Хранитель - управляет историей изменений"""

    def __init__(self):
        self._history: List[Memento] = []

    def save(self, state: Any) -> None:
        """Сохранить состояние"""
        memento = Memento(state)
        self._history.append(memento)
        print(f"✓ Состояние сохранено: {memento}")

    def restore(self, index: int) -> Any:
        """Восстановить состояние по индексу"""
        if 0 <= index < len(self._history):
            return self._history[index].get_state()
        raise IndexError("Индекс вне диапазона истории")

    def list_history(self) -> None:
        """Вывести историю"""
        print("\n=== История изменений ===")
        for i, memento in enumerate(self._history):
            print(f"  {i}: {memento.get_timestamp()}")

    def __len__(self) -> int:
        return len(self._history)
