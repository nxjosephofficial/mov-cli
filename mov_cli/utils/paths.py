from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .platform import SUPPORTED_PLATFORMS

import os
from pathlib import Path

__all__ = (
    "get_appdata_directory", 
    "get_temp_directory"
)

def get_appdata_directory(platform: SUPPORTED_PLATFORMS) -> Path:
    """Returns the path to the mov-cli appdata folder on multiple platforms."""
    appdata_dir = None

    if platform == "Windows":
        user_profile = Path(os.getenv("USERPROFILE"))
        appdata_dir = user_profile.joinpath("AppData", "Local")

    elif platform == "Darwin": # NOTE: Path maybe incorrect
        user_profile = Path.home()
        appdata_dir = user_profile.joinpath("Library", "Application Support")

    elif platform == "iOS":
        user_profile = Path(os.getenv("HOME"))
        appdata_dir = user_profile.joinpath("Library")

        appdata_dir.mkdir(exist_ok = True)

    elif platform == "Linux" or platform == "Android":
        user_profile = Path(os.getenv("HOME"))
        appdata_dir = user_profile.joinpath(".config")

        appdata_dir.mkdir(exist_ok = True) # on android the .config file may not exist.

    appdata_dir = appdata_dir.joinpath("mov-cli")
    appdata_dir.mkdir(exist_ok = True)

    return appdata_dir

def get_temp_directory(platform: SUPPORTED_PLATFORMS) -> Path:
    """
    Returns the temporary directory where mov-cli can dump stuff. 
    Files stored here WILL get cleared / deleted automatically by the operating system.
    """
    temp_directory = None

    if platform == "Windows":
        temp_directory = Path(os.getenv("TEMP"))

    elif platform == "Darwin": # NOTE: Path maybe incorrect
        temp_directory = Path(os.getenv("TMPDIR"))

    elif platform == "iOS":
        # TODO: Add temp directory for "iSH".
        raise NotImplementedError("Temp directory isn't implemented for iOS!")

    elif platform == "Linux":
        temp_dir_env = os.getenv("TMPDIR") # Respect the TMPDIR environment variable on Linux: https://unix.stackexchange.com/a/362107

        if temp_dir_env is None:
            temp_directory = Path("/tmp")

        temp_directory = Path(temp_dir_env)

    elif platform == "Android":
        temp_directory = Path("$PREFIX/tmp")

    temp_directory = temp_directory.joinpath("mov-cli-temp")
    temp_directory.mkdir(exist_ok = True)

    return temp_directory