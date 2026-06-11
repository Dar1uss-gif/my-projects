from abc import ABC, abstractmethod
from typing import Sequence
from filemanager.core.filesystem import FileSystemService

class FileSystemCommand(ABC):
    def __init__(self, filesystem: FileSystemService):
        self.filesystem = filesystem
    
    @abstractmethod
    def execute(self, args: Sequence[str]) -> None:
        '''Execute command with arguments.'''
        pass
    
    @abstractmethod
    def help(self) -> str:
        '''Return help string for command.'''
        pass