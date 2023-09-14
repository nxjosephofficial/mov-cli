from __future__ import annotations

from .media import Media

__all__ = ("Movie",)

class Movie(Media):
    """Represents a Film/Movie."""
    def __init__(
        self, 
        url: str, 
        title: str, 
        referrer: str, 
        year: int,
        subtitles: dict | None
    ) -> None:
        self.year = year
        """The year this film was released."""
        self.subtitles = subtitles

        super().__init__(
            url, title, referrer
        )