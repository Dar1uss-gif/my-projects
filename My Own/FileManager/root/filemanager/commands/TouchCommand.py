from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class TouchCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]):
        if not args:
            print('touch: missing file path.')
            return
        
        try:
            self.filesystem.create_file(args[0])
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('touch <path_to_file> - create file')