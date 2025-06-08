import argparse
import sys
from .convert import CoverPalette


def main() -> None:
    """Entry point for the ``coverpalette`` command."""
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        list_parser = argparse.ArgumentParser(
            prog="coverpalette list", description="List saved palettes"
        )
        list_parser.add_argument("--page", type=int, default=1, help="Page number")
        list_parser.add_argument(
            "--per-page", type=int, default=10, help="Palettes per page"
        )
        args = list_parser.parse_args(sys.argv[2:])
        entries = CoverPalette.list_palettes(page=args.page, per_page=args.per_page)
        if not entries:
            print("No saved palettes found")
            return
        for entry in entries:
            name = entry.get("name")
            n = entry.get("n_colors")
            path = entry.get("path")
            print(f"{name} ({n} colors) - {path}")
        return

    parser = argparse.ArgumentParser(
        description="Create color palettes from album covers"
    )
    parser.add_argument("artist", help="Name of the artist")
    parser.add_argument("album", help="Name of the album")
    parser.add_argument("-n", "--n-colors", type=int, default=4, help="Number of colors")
    parser.add_argument("--random-state", type=int, default=None, help="Random seed")
    parser.add_argument("--save", type=str, default=None, help="Save palette to a file")
    parser.add_argument(
        "--preview", action="store_true", help="Show a preview before optionally saving"
    )
    args = parser.parse_args()

    palette = CoverPalette(args.artist, args.album)
    cmap = palette.generate_cmap(n_colors=args.n_colors, random_state=args.random_state)
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
