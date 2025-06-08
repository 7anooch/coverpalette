import argparse
from .convert import CoverPalette


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create color palettes from album covers"
    )
    parser.add_argument("artist", help="Name of the artist")
    parser.add_argument("album", help="Name of the album")
    parser.add_argument(
        "-n", "--n-colors", type=int, default=4, help="Number of colors"
    )
    parser.add_argument(
        "--random-state", type=int, default=None, help="Random seed"
    )
    parser.add_argument(
        "--save", type=str, default=None, help="Save palette to a file"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Show a preview before optionally saving",
    )
    args = parser.parse_args()

    palette = CoverPalette(args.artist, args.album)
    cmap = palette.generate_cmap(
        n_colors=args.n_colors, random_state=args.random_state
    )
    print("Hexcodes:", " ".join(palette.hexcodes))

    if args.preview:
        palette.preview_palette(cmap)

    if args.save:
        palette.save_palette(args.save)
        print(f"Palette saved to {args.save}")


if __name__ == "__main__":
    main()
