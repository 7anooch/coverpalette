# Usage Guide

This package can generate matplotlib color maps from album artwork.

## Command line

After installing the package, run the `coverpalette` command to quickly
obtain a palette. By default a preview window will open so you can inspect
the colors before deciding whether to save them. Use `--save` to bypass the
preview and store the palette immediately.

The artist and album can be entered without quotes by separating them with a
single dash (`-`).

```bash
coverpalette artist - album -n 5       # preview then optionally save
coverpalette artist - album -n 5 --save  # save directly
coverpalette artist - album -n 5 --hue   # maximize hue separation
coverpalette artist - album --hue --light  # bright colors only
coverpalette artist - album --bold        # saturated colors
coverpalette artist - album --max-colors 8  # search fewer candidate colors
```

This prints the hex codes of the palette and reports whether the colors are
color-blind friendly. Palettes saved via the command line are recorded in
``~/.covers2colors/palettes/index.json`` along with metadata.
The preview window displays the album artwork, a sample plot using the colors
and a color bar. If you run the command without ``--save`` you'll be asked
whether to store the palette so you don't need to rerun the command.

To list previously saved palettes run:

```bash
coverpalette list
```

Each entry is shown with a numeric ``id`` which can be used to load or delete
palettes.  Add ``--pdf`` to generate a PDF that displays every palette with a
horizontal color bar. The PDF is stored under
``~/.covers2colors/palettes/palettes.pdf``.
Palettes created before numeric ids were introduced will automatically be
numbered the next time they are listed or loaded.

To remove a saved palette use:

```bash
coverpalette delete ID
```

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

### Checking palettes for color-blind users

Every palette generation method automatically evaluates color-blind
friendliness and stores the result on ``CoverPalette.is_colorblind_friendly``.
You can also use the :func:`covers2colors.colorblind.is_colorblind_friendly`
function or ``CoverPalette.colorblind_friendly`` for manual checks.
