# uv-genvs

`uv-genvs` is a lightweight command-line helper that streamlines the management of "global" virtual environments created with [`uv`](https://github.com/astral-sh/uv). Environments are stored under `~/.uv-genvs` so they can be reused across multiple projects without rebuilding them each time.

## Prerequisites

- Python 3.8 or newer
- The [`uv`](https://docs.astral.sh/uv/getting-started/installation/) executable available on your `PATH`

## Installation

Install `uv-genvs` from a local clone of the repository:

```bash
# Clone the repository (if you have not already)
git clone https://github.com/SimoneMartino98/uv-genvs.git
cd uv-genvs

uv tool install .
```

If you want `vs-code` or `zed` editors to automatically detect the environments add this on your `.bashrc`/`.zshrc`:
```bash
if [ -d "$HOME/.uv-genvs" ]; then
    for env_bin in "$HOME/.uv-genvs"/*/bin; do
        [ -d "$env_bin" ] && PATH="$env_bin:$PATH"
    done
fi
export PATH
```
You may need to reboot the editor before you can see the new environment created.

## Uninstallation

Remove `uv-genvs` from your system with:

```bash
uv tool uninstall uv-genvs
```

Environments created in `~/.uv-genvs` are not deleted automatically; delete them manually if you no longer need them.

## Usage

After installation, the main entry point is `genvs`. All operations happen through the subcommands described below.

### Create a new global environment

```bash
genvs create <environment-name> [--python <version>]
```

- `<environment-name>`: name of the environment.
- `--python <version>` (optional): select the Python version to use (for example `3.11`). When omitted, the default `uv` interpreter is used.

### List available environments

```bash
genvs list
```

Displays a table with the environment name, detected Python version, and last modified timestamp.

### Remove an environment

```bash
genvs remove <environment-name>
```

Recursively deletes the selected environment folder from `~/.uv-genvs`. The operation cannot be undone, so make sure no projects still depend on that environment.