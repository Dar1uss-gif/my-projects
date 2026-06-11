from .filesystemcommand import FileSystemCommand
from typing import Sequence
from datetime import datetime
from rich import print

class ListCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> None:
        
        try:
            
            if args and len(args[0]) > 2:
                arr = self.filesystem.list_directory(args[0])
            
            else:
                arr = self.filesystem.list_directory()
                
            print(f'Directory of {self.filesystem.current_path}\n')

            for item in arr:
                metadata = item.stat()
                size = metadata.st_size
                time = datetime.fromtimestamp(metadata.st_mtime)
                print(f'\t{'<DIR>' if item.is_dir() else '<FILE>'} {item.name} | {size} bytes ({size / 1000:.2f} KB)')
        
        except Exception as e:
            print(f'[white on red][ERROR][/white on red]: {e}')
            
    def help(self) -> None:
        print('ls <dir_name> - list directory')