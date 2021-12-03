from __future__ import annotations


class Command:

    def __init__(self, command_name: str, alternative_names: list[str]):
        self._main_name = command_name
        self._all_names = alternative_names
        self._all_names.append(command_name)
        self._children: list[Command] = []

    def get_main_name(self):
        return self._main_name

    def add_children(self, commands: list[Command]):
        for command in commands:
            self.add_child(command)

    def add_child(self, command: Command):
        self._children.append(command)

    def get_child(self, name: str):
        return next(iter(child for child in self._children if name in child.get_main_name()), None)

    def __str__(self):
        return f'{self._all_names} => ' + str([child.get_main_name() for child in self._children])
