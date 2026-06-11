from abc import ABC, abstractmethod
from typing import Sequence

class BaseCommand(ABC):
    def __init__(self, filesystem: None = None):
        self.filesystem = filesystem
        
    @abstractmethod
    def execute(self, args: Sequence[str]):
        '''Execute command with arguments.'''
        pass
    
    @abstractmethod
    def help(self):
        '''Return help string for command.'''
        pass