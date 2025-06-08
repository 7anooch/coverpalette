# Usage Guide

This package can generate matplotlib color maps from album artwork.

## Command line

After installing the package, run the `coverpalette` command to quickly
obtain a palette. Use `--preview` to see a plot and the album art before saving.

```bash
coverpalette "artist" "album" -n 5 --save mypalette.json
coverpalette "artist" "album" -n 5 --preview
```

This prints the hex codes of the palette and saves them as JSON if you provide a
path. Palettes saved via the command line are also recorded in
``~/.covers2colors/palettes/index.json`` along with metadata. The preview
option pops up a panel showing the album artwork, a sample plot using the colors
and a color bar. When previewing without ``--save``, you'll be asked whether to
store the palette in this index so you don't need to rerun the command.

To list previously saved palettes run:

```bash
coverpalette list
```

Add ``--pdf`` to generate a PDF that displays every palette with a horizontal
color bar. The PDF is stored under ``~/.covers2colors/palettes/palettes.pdf``.

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
