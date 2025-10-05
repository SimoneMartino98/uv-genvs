from ..config import get_global_envs_dir
import subprocess

def cmd_create(args):
    envs_dir = get_global_envs_dir()
    target_dir = envs_dir / args.name

    cmd = ["uv", "venv", str(target_dir)]
    if args.python:
        cmd.extend(["--python", args.python])

    subprocess.run(cmd, check=True)