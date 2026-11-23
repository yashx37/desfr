# desfr

A dead simple command-line file reader.

## Installation

```bash
pip install desfr
```

## Usage

Read a text file:

```bash
desfr read filename.txt
```

Read and render a markdown file:

```bash
desfr read filename.md
```

You can also provide an absolute path:

```bash
desfr read /path/to/filename.txt
desfr read /path/filename.md
```

Currently supports `.txt` and `.md` files.