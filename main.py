from os import environ as env
from pathlib import Path
import click
from rich.console import Console
from todo import TodoList

console = Console()

@click.group()
def todo(list_path: str = ''):
    if list_path == '':        
        file_path = Path(env.get('USERPROFILE')).joinpath('my-list.todo')        
    else:        
        file_path = Path(list_path)

    if not file_path.exists():
        console.warning('File %s does not exist, creating', file_path)
        with open(file_path, 'w') as f:
            f.write(TodoList([], file_path).to_json())
            

