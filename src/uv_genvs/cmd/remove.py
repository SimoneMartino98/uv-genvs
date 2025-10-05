from ..config import get_global_envs_dir
import subprocess

def cmd_remove(args):
    envs_dir = get_global_envs_dir()
    target_dir = envs_dir / args.name

    cmd = ["rm", "-rf", str(target_dir)]

    subprocess.run(cmd, check=True)