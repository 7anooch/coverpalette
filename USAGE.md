# Usage Guide

This package can generate matplotlib color maps from album artwork.

## Command line

After installing the package, run the `coverpalette` command to quickly
obtain a palette. Use `--preview` to see a plot and the album art before saving.

```bash
coverpalette "artist" "album" -n 5 --save mypalette.json
coverpalette "artist" "album" -n 5 --preview
```

This prints the hex codes of the palette and saves them to a file if a path is
provided. The preview option pops up a panel showing the album artwork, a
sample plot using the colors and a color bar.

## Python

You can also use the high level function `get_cmap` to create a colormap in one
call:

```python
from covers2colors import get_cmap

cmap = get_cmap("Nirvana", "Nevermind", n_colors=4)
print(cmap.colors)
```

The underlying `CoverPalette` class offers additional methods for more complex
workflows.
