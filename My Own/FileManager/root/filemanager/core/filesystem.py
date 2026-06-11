import shutil
from pathlib import Path
from .errors import *

class FileSystemService:
    def __init__(self):
        self.current_path = Path(Path.cwd())
        
    def list_directory(self, path: str | Path | None=None) -> list[Path]:
        path = Path(path) if path else self.current_path
        
        if not path.exists():
            raise PathNotFoundError(path)
        
        if not path.is_dir():
            raise DirectoryExpectedError(path)
        
        if not path:
            return list(self.current_path.iterdir())
        
        return list(path.iterdir())
    
    def change_directory(self, path: str | Path) -> Path:
        path = Path(path)
        
        absolute_path = path.resolve()
        
        if not absolute_path.exists():
            raise PathNotFoundError(path)
        
        if not absolute_path.is_dir():
            raise DirectoryExpectedError(path)
        
        self.current_path = absolute_path
        
        return path
        
    def make_directory(self, path: str | Path) -> Path:
        path_to_dir = self.current_path / path
        path_to_dir.mkdir(exist_ok=True)
        
        return path_to_dir
    
    def create_file(self, path: str | Path) -> None:
        path_to_file = self.current_path / path
        
        try:
            path_to_file.touch()
            
        except FileExistsError:
            raise FileAlreadyExistsError(path)
    
    def remove(self, path: str | Path):
        path = Path(path)
        
        try:
            if not path.is_dir():
                path.unlink()
                
            else:
                shutil.rmtree(path)
                
        except PermissionError:
            raise PermissionDeniedError(path)
    
    def copy(self, source: str | Path, destination: str | Path) -> Path:
        source = Path(source)
        destination = Path(destination)
        
        try:
            if not source.exists():
                raise PathNotFoundError(source)
            
            if not destination.exists():
                raise PathNotFoundError(destination)
            
            if not source.is_dir():
                shutil.copy(source, destination)
                
            else:
                shutil.copytree(source, destination, dirs_exist_ok=True)
        except PermissionError:
            raise PermissionDeniedError(source or destination)
            
        return destination
    
    def move(self, source: str | Path, destination: str | Path) -> Path:
        source = Path(source)
        destination = Path(destination)
        
        try:
            if not source.exists():
                raise PathNotFoundError(source)
            
            shutil.move(source, destination)
            
            return destination
    
        except PermissionError:
            raise PermissionDeniedError(source or destination)
    
    def get_current_directory(self) -> Path:
        return self.current_path