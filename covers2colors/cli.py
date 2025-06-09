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
        list_parser.add_argument(
            "--pdf", action="store_true", help="Show a PDF of all palettes"
        )
        args = list_parser.parse_args(sys.argv[2:])

        if args.pdf:
            path = CoverPalette.create_palettes_pdf()
            if not path:
                print("No saved palettes found")
                return
            try:
                import os
                import subprocess

                if sys.platform.startswith("darwin"):
                    subprocess.run(["open", str(path)], check=False)
                elif os.name == "nt":
                    os.startfile(str(path))  # type: ignore[attr-defined]
                else:
                    subprocess.run(["xdg-open", str(path)], check=False)
            except Exception:
                print(f"PDF saved to {path}")
            return

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

    # Support an unquoted "artist - album" form by rewriting sys.argv
    args = sys.argv[1:]
    if "-" in args:
        dash = args.index("-")
        artist_tokens = args[:dash]
        rest = args[dash + 1 :]
        album_tokens = []
        options = []
        for i, token in enumerate(rest):
            if token.startswith("-"):
                options = rest[i:]
                break
            album_tokens.append(token)
        if artist_tokens and album_tokens:
            sys.argv = (
                [sys.argv[0], " ".join(artist_tokens), " ".join(album_tokens)]
                + options
            )

    parser = argparse.ArgumentParser(
        description="Create color palettes from album covers"
    )
    parser.add_argument("artist", help="Name of the artist")
    parser.add_argument("album", help="Name of the album")
    parser.add_argument("-n", "--n-colors", type=int, default=4, help="Number of colors")
    parser.add_argument("--random-state", type=int, default=None, help="Random seed")
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save without previewing the palette",
    )
    args = parser.parse_args()

    palette = CoverPalette(args.artist, args.album)
    cmap = palette.generate_cmap(n_colors=args.n_colors, random_state=args.random_state)
    print("Hexcodes:", " ".join(palette.hexcodes))

    if args.save:
        palette.save_palette()
        print("Palette saved")
    else:
        palette.preview_palette(cmap)
        ans = input("Save this palette? [y/N] ").strip().lower()
        if ans in {"y", "yes"}:
            palette.save_palette()
            print("Palette saved")


if __name__ == "__main__":
    main()
