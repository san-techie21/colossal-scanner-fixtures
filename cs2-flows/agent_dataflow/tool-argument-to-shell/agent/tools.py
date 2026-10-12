import subprocess

from langchain_core.tools import tool


@tool
def run_shell(command: str) -> str:
    """Run a shell command on the build host."""
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout
