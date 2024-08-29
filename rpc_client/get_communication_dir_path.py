import os
import re
from pathlib import Path
from tempfile import gettempdir


def get_communication_dir_path(name: str) -> Path:
    """Returns directory that is used for RPC communication

    Returns:
        Path: The path to the communication dir
    """
    suffix = ""

    # NB: We don't suffix on Windows, because the temp dir is user-specific
    # anyways
    if hasattr(os, "getuid"):
        suffix = f"-{os.getuid()}"

    print(Path(gettempdir()) / f"{name}{suffix}")
    return Path(gettempdir()) / f"{name}{suffix}"


def clean_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "-", name).lower()
