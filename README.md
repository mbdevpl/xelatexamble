
# Platform-specific remarks


## Linux

When using pythontex (inline minted), after the first build run:

```
pythontex document.tex
```

or if it breaks, run one of below (depending on your Python version...):

```
python3 $(which pythontex)
python3.6 $(which pythontex)
```

and then rebuild to get correct document.


## Windows

No remarks.


## macOS

No remarks.


# Tools

The `beamer_make_printable_slides.py` is a Python script that enables creation of...
printable slides, when using beamer! You can guess that form the filename though.

Run `python3 beamer_make_printable_slides.py -h` to see how to use it.
