from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class OpenPark(Command):

    def __init__(self, time: str) -> None:
        self._time = time

    def execute(self) -> None:
        print(f'Park has been opened at {self._time}')


class ClosePark(Command):

    def __init__(self, time: str) -> None:
        self._time = time

    def execute(self) -> None:
        print(f'Park has been closed at {self._time}')


class BuildCage(Command):

    def __init__(self, engineer: Engineer, bears: int, wolves: int, rabbits: int) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        """

        self._engineer = engineer
        self._bears = bears
        self._wolves = wolves
        self._rabbits = rabbits

    def execute(self) -> None:
        """
        Команды могут делегировать выполнение любым методам получателя.
        """

        self._engineer.build_bear_house(self._bears)
        self._engineer.build_wolves_house(self._wolves)
        self._engineer.build_rabbits_house(self._rabbits)


class Engineer:
    """
    Классы Получателей содержат некую важную бизнес-логику. Он отыгрывает роль получателя — команды делегируют
    ему свои действия.
    """

    def build_bear_house(self, qty: int) -> None:
        print(f"The house for {qty} bears has been built")

    def build_wolves_house(self, qty: int) -> None:
        print(f"The house for {qty} wolves has been built")

    def build_rabbits_house(self, qty: int) -> None:
        print(f"The house for {qty} rabbits has been built")


class ParkManager:
    """
    Отправитель хранит ссылку на объект команды и обращается к нему, когда нужно выполнить какое-то действие.
    Отправитель работает с командами только через их общий интерфейс.
    Он не знает, какую конкретно команду использует, так как получает готовый объект команды.
    """

    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def perform(self):
        self.command.execute()


# app layer
john_engeneer = Engineer()  # receiver

command_open_park = OpenPark(time='9.00 AM')  # concrete command
command_close_park = ClosePark(time='6.00 PM')  # concrete command
command_build_cages_by_john = BuildCage(engineer=john_engeneer, bears=1, wolves=2, rabbits=6)  # concrete command

manager = ParkManager(command_open_park)  # invoker
manager.perform()
manager.set_command(command_build_cages_by_john)
manager.perform()
manager.set_command(command_close_park)
manager.perform()

# command -> concrete commands + receiver -> invoker set and perform each command
