from pathlib import Path 
from typing import List

HOME_DIRECTORY = Path.home()
REPOSITORY_DIRECTORY = Path(__file__).parent

def create_paths(list_dirs: List[Path]):
    """
    Creates dirs for user data outside the
    terminal if they don't exist
    """
    for dirs in list_dirs:
        if not dirs.exists():
            dirs.mkdir(
                parents=True,
            )

def create_files(list_files: List[Path]):
    """
    Creates files outside the terminal if they don't exist
    """
    for filename in list_files:
        if not filename.is_file():
            with open(str(filename), "w"):
                pass
