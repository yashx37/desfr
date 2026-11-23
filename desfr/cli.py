import argparse
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown

def main():
    parser = argparse.ArgumentParser(
          description="A dead simple file reader in CLI"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    read_parser = subparsers.add_parser("read", help="Read a text file")
    read_parser.add_argument("filename")

    args = parser.parse_args()

    console = Console()

    if args.command == "read":
        file = Path(args.filename)
        
        if file.suffix.lower() not in {".txt", ".md"}:
                    parser.error("Error: Only text and markdown files are supported.")
        
        if not file.exists():
            parser.error(f"Error: The File '{args.filename}' does not exist")
            return
        try:   
            content = file.read_text(encoding="utf-8")

            if file.suffix.lower() == ".md":
                 console.print(Markdown(content))
            else:
                print(content, end="")
                
        except OSError as e:
            parser.error(f"Cannot read file: {e}")

if __name__ == "__main__":
    main()