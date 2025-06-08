from .convert import CoverPalette
from .album_art import get_best_cover_art_url


def get_cmap(artist: str, album: str, n_colors: int = 4, random_state: int | None = None):
    """Return a colormap for ``artist`` and ``album`` in a single call."""

    palette = CoverPalette(artist, album)
    return palette.generate_cmap(n_colors=n_colors, random_state=random_state)

__version__ = "0.1"
