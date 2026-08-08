import importlib
from pathlib import Path

TASKS_DIR = Path (__file__).parent.parent / "tasks"

def discover_tasks() -> list[str]:
    return [
        f.stem for f in TASKS_DIR.glob('*.py')
        if not f.stem.startswith("_")
    ]
def load_task (task_name: str):
    module = importlib.import_module(f"tasks.{task_name}")
    return module