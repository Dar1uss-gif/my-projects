from .filesystemcommand import FileSystemCommand
from typing import Sequence
from pathlib import Path
from rich import print

class PwdCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        try:
            print(self.filesystem.get_current_directory())
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('pwd - return current directory.')