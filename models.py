"""
models.py - Определение классов для компонентов компьютера
"""

from dataclasses import dataclass
from typing import List
from enum import Enum


class ComponentType(Enum):
    """Типы компонентов"""
    DETAIL = "Деталь"
    PROCESSOR = "Процессор"
    MOTHERBOARD = "Материнская плата"
    RAM = "ОЗУ"
    STORAGE = "Накопитель"
    PSU = "Блок питания"


@dataclass
class Detail:
    """Базовый класс для любой детали"""
    name: str
    component_type: ComponentType
    manufacturer: str
    specifications: dict

    def get_info(self) -> str:
        return f"{self.name} ({self.component_type.value}) от {self.manufacturer}"

    def __repr__(self) -> str:
        return f"Detail({self.name})"


class Processor(Detail):
    """Процессор"""

    def __init__(self, name: str, manufacturer: str, cores: int, frequency_ghz: float):
        super().__init__(
            name=name,
            component_type=ComponentType.PROCESSOR,
            manufacturer=manufacturer,
            specifications={"cores": cores, "frequency_ghz": frequency_ghz}
        )


class RAM(Detail):
    """Оперативная память"""

    def __init__(self, name: str, manufacturer: str, capacity_gb: int, speed_mhz: int):
        super().__init__(
            name=name,
            component_type=ComponentType.RAM,
            manufacturer=manufacturer,
            specifications={"capacity_gb": capacity_gb, "speed_mhz": speed_mhz}
        )


class Motherboard(Detail):
    """Материнская плата"""

    def __init__(self, name: str, manufacturer: str, socket: str, max_ram_gb: int):
        super().__init__(
            name=name,
            component_type=ComponentType.MOTHERBOARD,
            manufacturer=manufacturer,
            specifications={"socket": socket, "max_ram_gb": max_ram_gb}
        )


class Computer:
    """Главный класс - компьютер"""

    def __init__(self, name: str):
        self.name = name
        self.components: List[Detail] = []

    def add_component(self, component: Detail) -> None:
        """Добавить компонент"""
        self.components.append(component)
        print(f"✓ Добавлен: {component.get_info()}")

    def list_components(self) -> None:
        """Вывести все компоненты"""
        print(f"\n=== Компоненты {self.name} ===")
        for component in self.components:
            print(f"  - {component.get_info()}")
            print(f"    Характеристики: {component.specifications}")

    def __repr__(self) -> str:
        return f"Computer({self.name}, {len(self.components)} компонентов)"