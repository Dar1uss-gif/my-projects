from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class RemoveCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        if not args:
            print('rm: missing file/directory name.')
            return 
        
        try:
            self.filesystem.remove(args[0])
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('rm <file/dir_name> - remove file/directory.')