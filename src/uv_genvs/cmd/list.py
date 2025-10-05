from datetime import datetime
from pathlib import Path

from ..config import get_global_envs_dir

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"

def _read_python_version(env_path: Path) -> str:
    pyvenv_cfg = env_path / "pyvenv.cfg"
    if not pyvenv_cfg.exists():
        return "unknown"

    for line in pyvenv_cfg.read_text(encoding="utf-8").splitlines():
        if line.startswith("version_info ="):
            return line.split("=", 1)[1].strip()

    return "unknown"


def _format_mtime(env_path: Path) -> str:
    timestamp = env_path.stat().st_mtime
    return datetime.fromtimestamp(timestamp).isoformat(sep=" ", timespec="seconds")


def cmd_list(_: object) -> None:
    envs_dir = get_global_envs_dir()

    envs = [p for p in envs_dir.iterdir() if p.is_dir()]
    if not envs:
        print("No global environments found.")
        return

    envs.sort(key=lambda path: path.name.lower())

    rows = [
        (env.name, _read_python_version(env), _format_mtime(env))
        for env in envs
    ]

    headers = ("Environment", "Python Version", "Last Modified")
    widths = [
        max(len(header), max(len(row[idx]) for row in rows))
        for idx, header in enumerate(headers)
    ]

    header_line = "  ".join(header.ljust(widths[idx]) for idx, header in enumerate(headers))
    separator_line = "  ".join("-" * widths[idx] for idx in range(len(headers)))
    print(f"{BOLD}{GREEN}Global environments installed:{RESET}\n")
    print(f"{GREEN}{header_line}{RESET}")
    print(separator_line)
    for row in rows:
        print("  ".join(value.ljust(widths[idx]) for idx, value in enumerate(row)))
