from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..media import Media
    from ..config import Config

import subprocess
from devgoldyutils import Colours

from .player import Player, PlayerNotFound, PlayerNotSupported

__all__ = ("VLC",)

class VLC(Player):
    def __init__(self, config: Config) -> None:
        super().__init__(Colours.ORANGE.apply("VLC"), config)

    def play(self, media: Media) -> subprocess.Popen:
        try:
            if self.platform == "Linux" or self.platform == "Windows":

                return subprocess.Popen([
                    "vlc",
                    f'--http-referrer="{media.referrer}"',
                    f'"{media.url}"',
                    f'--meta-title="mov-cli:{media.title}"',
                    "--no-terminal",
                ])

            raise PlayerNotSupported(self, self.platform)

        except ModuleNotFoundError:
            raise PlayerNotFound(self)