import subprocess

from langchain_core.tools import tool


@tool
def disk_usage(mount: str) -> str:
    """Report disk usage for one of the known mounts."""
    if mount not in {"/", "/srv", "/var"}:
        return "unknown mount"
    return subprocess.run(["df", "-h", mount], capture_output=True, text=True).stdout
