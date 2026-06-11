import sys
import argparse
from rich import print
from typing import Sequence
from filemanager.core.errors import FileManagerError
from filemanager.commands.ChangeDirCommand import ChangeDirCommand
from filemanager.commands.CopyCommand import CopyCommand
from filemanager.commands.ListCommand import ListCommand
from filemanager.commands.MkdirCommand import MkDirCommand
from filemanager.commands.MoveCommand import MoveCommand
from filemanager.commands.PwdCommand import PwdCommand
from filemanager.commands.RemoveCommand import RemoveCommand
from filemanager.core.filesystem import FileSystemService
from filemanager.commands.TouchCommand import TouchCommand
from filemanager.commands.HelpCommand import HelpCommand
from filemanager.commands.CatCommand import CatCommand

class Dispatcher:
    
    commands = {
        'cd': ChangeDirCommand,
        'cp': CopyCommand,
        'ls': ListCommand,
        'mkdir': MkDirCommand,
        'mv': MoveCommand,
        'pwd': PwdCommand,
        'rm': RemoveCommand,
        'touch': TouchCommand,
        'help': HelpCommand,
        'cat': CatCommand
    }
    
    def __init__(self, filesystem: FileSystemService):
        self.filesystem = filesystem
    
    def parse_line(self,mode: str,  arr: Sequence[str]) -> None:
        
        if mode.lower() == 'static':
            
            if not arr:
                return
            
            cmd_name = arr[1]
            args = arr[2:]
            cmd_class = self.commands.get(cmd_name)
            
            if cmd_class is None:
                print(f'[white on red][ERROR][/white on red] unknown command: {cmd_name}')
                return
            
            try:
                
                if '-h' in args:
                    command = cmd_class(self.filesystem)
                    command.help()
                
                else:
                    command = cmd_class(self.filesystem)
                    command.execute(args)
            
            except Exception as e:
                print(f'[ERROR] {e}')
                
        if mode.lower() == 'interactive':
            
            if not arr:
                return
            
            cmd_name = arr[0]
            args = arr[1:-1]
            cmd_class = self.commands.get(cmd_name)
            
            if cmd_class is None:
                print(f'[white on red][ERROR][/white on red] unknown command: {cmd_name}')
            
            try:
                
                if '-h' in args:
                    command = cmd_class(self.filesystem)
                    command.help()
                
                else:
                    command = cmd_class(self.filesystem)
                    command.execute(args)
            
            except FileManagerError as e:
                print(f'[ERROR] {e}')         