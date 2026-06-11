from .filesystemcommand import FileSystemCommand
from typing import Sequence
from rich import print

class MkDirCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        if not args:
            print('mkdir: missing directory name.')
            return
        
        try:
            self.filesystem.make_directory(args[0])
            
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('mkdir <dir_name> - make directory.')