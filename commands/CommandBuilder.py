import pathlib
from typing import Optional

import pandas as pd

from commands import Command

COMMANDS_PATH = pathlib.Path(__file__).parent / 'commands.txt'


class CommandBuilder:

    def __init__(self):
        self._root: Optional[Command] = None

    def get_root(self):
        return self._root

    def build(self, file_path=COMMANDS_PATH):
        df = self._load_data(file_path)
        commands = self._create_raw_commands(df)
        self._root = self._join_commands(commands)
        return self._root

    @staticmethod
    def _load_data(file_path: pathlib.Path):
        df = pd.read_csv(file_path, dtype=str, sep=';', header=None)
        df = df.fillna('')
        return df

    def _create_raw_commands(self, df):
        commands = {}
        for index, row in df.iterrows():
            command, children_names = self._make_command_tuple(row)
            commands[command.get_main_name()] = command, children_names
        return commands

    @staticmethod
    def _make_command_tuple(row):
        name = row[0]
        alternative_names = row[1].split(',')
        children_names = row[2].split(',')
        return Command(name, alternative_names), children_names

    @staticmethod
    def _join_commands(commands: dict[str, tuple[Command, list[str, ...]]]):
        for _, (command, children_names) in commands.items():
            children_commands = [commands[name][0] for name in commands.keys() if name in children_names]
            command.add_children(children_commands)
        return commands['main'][0]