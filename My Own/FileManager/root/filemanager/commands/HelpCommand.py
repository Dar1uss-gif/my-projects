from .basecommand import BaseCommand
from rich import print
from typing import Sequence

class HelpCommand(BaseCommand):
    def execute(self, args: Sequence[str]) -> None:
            print('''
For detailed information for specific command, type <cmd_name> -h\n
LS - list content of current directory
CD - change directory
CP - copy directory/file to other path
CAT - list content of file
MV - move directory/file to otehr path
PWD - list current directory
TOUCH - create new file
RM - remove directory/file
              ''')
            
    def help(self) -> None:
        print('[white on red]U serious? :/[/white on red]')