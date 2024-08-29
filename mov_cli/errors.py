from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx

from devgoldyutils import Colours

from .logger import mov_cli_logger

__all__ = (
    "MovCliException",
    "SiteMaybeBlockedError",
    "ReferrerNotSupportedError"
)

class MovCliException(Exception):
    """Raises whenever there's a known error in mov-cli."""
    message: str

    def __init__(self, message: str) -> None:
        self.message = message

        mov_cli_logger.critical(message)

        super().__init__(
            Colours.RED.apply_to_string(self.message)
        )

class SiteMaybeBlockedError(MovCliException):
    """Raises when a connection is looked like to be blocked by a DNS or ISP provider's DNS."""
    def __init__(self, url: str, error: httpx.ConnectError) -> None:
        message = f"A connection error occurred while making a GET request to '{url}'.\n" \
            "There's most likely nothing wrong with mov-cli. Your ISP's DNS could be blocking this site or perhaps the site is down. " \
                f"{Colours.GREEN}SOLUTION: Use a VPN or switch DNS!{Colours.RED}\n" \
                    f"Actual Error >> {error}"

        super().__init__(message)

class ReferrerNotSupportedError(MovCliException):
    """
    Raised by some players on platforms like Android and 
    iOS where players don't support the passing of referrer urls.
    """
    ...