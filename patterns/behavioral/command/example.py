from abc import abstractmethod


class Data:
    _data = 0

    def __init__(self, value=0) -> None:
        Data._data += value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def __str__(self) -> str:
        return f"Present value: {self._data}"


class Addition(Data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def add(self, value):
        Data._data += value
        print("Addition is being performed...")

    def __str__(self) -> str:
        return super().__str__()


class Subtraction(Data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def subtract(self, value):
        Data._data -= value
        print("Subtraction is being performed...")

    def __str__(self) -> str:
        return super().__str__()


class Command():
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class SubtractionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.subtract(self.value)

    def undo(self, command_obj):
        command_obj.set_command(AdditionCommand(Addition(), self.value))
        command_obj.invoke()


class AdditionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.add(self.value)

    def undo(self, command_obj):
        command_obj.set_command(SubtractionCommand(Subtraction(), self.value))
        command_obj.invoke()


class ActionInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

    def undo(self):
        print("[!UNDO] ", end="")
        self.command.undo(self)


# app layer
obj = Data(100)
print(obj)

command_addition = AdditionCommand(Addition(), 70)  # concrete command
command_subtraction = SubtractionCommand(Subtraction(), 90)  # concrete command

action_invoker = ActionInvoker(command_addition)  # invoker
action_invoker.invoke()
print(obj)

action_invoker.set_command(command_subtraction)
action_invoker.invoke()
print(obj)

action_invoker.undo()
print(obj)
action_invoker.undo()
print(obj)
