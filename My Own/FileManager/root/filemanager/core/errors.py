from pathlib import Path

class FileManagerError(Exception):
    '''Base exception for FileManager.'''
    
    def __init__(self, path: str | Path, message: str):
        self.path: Path = Path(path)
        super().__init__(message)

class PathNotFoundError(FileManagerError):
    '''Raised when path does not exist.'''
    
    def __init__(self, path):
        super().__init__(path, f'Path {path} does not exist.')

class DirectoryExpectedError(FileManagerError):   
    '''Raised when expected directory but got file.'''
    
    def __init__(self, path):
        super().__init__(path, f'{path} not a directory.')
        
class FileAlreadyExistsError(FileManagerError):
    '''Raised when trying to create file that already exists.'''
    
    def __init__(self, path):
        super().__init__(path, f'File {Path(path).name} already exists.')
        
class PermissionDeniedError(FileManagerError):
    '''Raised when operation is not permitted'''
    
    def __init__(self, path):
        super().__init__(path, f'permission denied: {path}')