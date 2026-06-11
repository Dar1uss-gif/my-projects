from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class ChangeDirCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        if not args:
            print('cd: missing directory name.')
            return
        
        try:
            self.filesystem.change_directory(args[0])
        
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('cd <dir name> - change directory.')