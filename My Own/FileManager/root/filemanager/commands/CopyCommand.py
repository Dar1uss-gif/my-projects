from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class CopyCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        if not args:
            print('cp: missing directory name.')
            return
        
        try:
            self.filesystem.copy(args[0], args[1])
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('cp <path_to_dir> <destination> - copy file/directory to other path')