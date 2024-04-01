# covers2colors

## Installation

Clone the repo, navigate inside it and run ``pip install .``

### API access to album covers
Before you install anything, consider setting up some API keys if you so wish.

To get album covers I try 3 different APIs (Last.fm, MusicBrains, and Discogs), two of which require API keys (Last.fm and discogs). To set up your API keys, you will want to rename `covers2colors/keys_template.json` to `covers2colors/keys.json` and add in your API keys in there. Once the file is renamed the package will assume it contains valid api keys and will attempt to use them.

If you would rather not bother getting any API keys, things should still work fine and artwork will attempt to be fetched from MusicBrainz only.

## Basic Usage

**Create colormaps from album covers in three lines of code!**

First, the ``CoverColors`` class makes calls to various APIs in order to fetch album artwork, and converts the image to arrays of RGB values.
Then, ``generate_cmap`` creates a matplotlib [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib-colors-listedcolormap).


    from covers2colors import CoverColors

    covercolors = CoverColors('closure in moscow', "pink lemonade")
    cmap = covercolors.generate_cmap(n_colors=5, random_state=42)

Now, use the colormap in your plots!

    import matplotlib.pyplot as plt

    colors = cmap.colors

    with plt.style.context("dark_background"):
        for i, color in enumerate(colors):
            plt.plot(range(10), [_+i+1 for _ in range(10)], color=color, linewidth=4)


Plot the image and a colorbar side by side with the following method:

    covercolors.display_with_colorbar(cmap)

## Other colormap methods

### generate_optimal_cmap

You can extract the optimal number of colors from the image using the ``generate_optimal_cmap`` method.
Under the hood this performs the [elbow method](https://en.wikipedia.org/wiki/Elbow_method_(clustering))
to determine the optimal number of clusters based on the sum of the squared distances between each pixel
and it's cluster center.


    cmaps, best_n_colors, ssd = covercolors.generate_optimal_cmap(max_colors=10, random_state=42)

    best_cmap = cmaps[best_n_colors]


### get_distinct_colors

Suppose you have a collection of colors in your color palette, but you only want to select a subset from them. This method will select the most distinct colors out of the palette for your new, smaller color palette.


    cmap = cmaps[10]
    distinct_colors, distinct_cmap = covercolors.get_distinct_colors(cmap, 5)

### generate_distinct_optimal_cmap

Another method you can use to get a color map. This method employs the generate_optimal_cmap and then finds the most distinct set of ``n_distinct_colors`` colors.


    distinct_colors, distinct_cmap = covercolors.generate_distinct_optimal_cmap(n_distinct_colors=6)


The different methods of obtaining a palette will often return different palettes for the name number of colors, ``generate_distinct_optimal_cmap``appears to be the one that performs the best imo, but results vary (which is why there are options!).

### Hexcodes

When running the ``generate_cmap`` or the ``generate_optimal_cmap`` methods the CoverColors object will automatically
capture the resulting hexcodes from the colormap and store them as an attribute.



    from cover2colors import CoverColors

    covercolors = CoverColors('Nirvana', Nevermind)
    covercolors.generate_cmap(n_colors=4, random_state=42)
    print(covercolors.hexcodes)

Output:


    ['#0ea1c1', '#456a78', '#0269ae', '#091a2d']
