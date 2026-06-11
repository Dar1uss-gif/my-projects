from .filesystemcommand import FileSystemCommand
from rich import print
from typing import Sequence

class CatCommand(FileSystemCommand):
    def execute(self, args: Sequence[str]) -> str:
        if  args:
            path_to_file = args[0]
            try:
                with open(path_to_file, 'r') as file:
                    content = file.read()
                    
                    print(content)
                
            except Exception as e:
                print(f'[white on red][ERROR][/white on red] {e}')
        
        else:
            print('cat - missing file path')        
            
    def help(self) -> str:
        print('cat <path_to_file> - print content of file.')