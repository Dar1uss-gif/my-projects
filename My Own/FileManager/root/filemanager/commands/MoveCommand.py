from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class MoveCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        if not args:
            print('mv: missing directory name.')
            return
        
        try:
            self.filesystem.move(args[0], args[1])
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('mv <file/dir_name> - move file/directory.')