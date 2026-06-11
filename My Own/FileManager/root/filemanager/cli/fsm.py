import sys
from .dispatcher import Dispatcher
from filemanager.core.filesystem import FileSystemService

filesystem = FileSystemService()
dispatcher = Dispatcher(filesystem)

class CLIApplication:
                   
    def run(self) -> None:
        
        if len(sys.argv) < 2:
            print('Usage: ush <command> <args>')
            return
            
        dispatcher.parse_line('static', sys.argv)
    