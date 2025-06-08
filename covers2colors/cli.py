import argparse
from .convert import CoverPalette


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create color palettes from album covers"
    )
    parser.add_argument("artist", nargs="?", help="Name of the artist")
    parser.add_argument("album", nargs="?", help="Name of the album")
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
    parser.add_argument(
        "--list",
        action="store_true",
        help="List saved palettes and exit",
    )
    args = parser.parse_args()

    if args.list:
        entries = CoverPalette.list_palettes()
        if not entries:
            print("No saved palettes found")
            return
        for entry in entries:
            name = entry.get("name")
            n = entry.get("n_colors")
            path = entry.get("path")
            print(f"{name} ({n} colors) - {path}")
        return

    if not args.artist or not args.album:
        parser.error("artist and album are required unless --list is used")

    palette = CoverPalette(args.artist, args.album)
    cmap = palette.generate_cmap(
        n_colors=args.n_colors, random_state=args.random_state
    )
    print("Hexcodes:", " ".join(palette.hexcodes))

    save_path = args.save
    should_save = args.save is not None

    if args.preview:
        palette.preview_palette(cmap)
        if args.save is None:
            ans = input("Save this palette? [y/N] ").strip().lower()
            if ans in {"y", "yes"}:
                should_save = True

    if should_save:
        palette.save_palette(save_path)
        if save_path:
            print(f"Palette saved to {save_path}")
        else:
            print("Palette saved")


if __name__ == "__main__":
    main()
