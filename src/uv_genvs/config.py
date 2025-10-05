from pathlib import Path

def get_global_envs_dir() -> Path:
    base_dir = Path.home() / ".uv-genvs"

    if not base_dir.exists():
        base_dir.mkdir(parents=True, exist_ok=True)

    return base_dir
