# Twilight cursors
This is an x-cursor theme inspired by macOS and
based on [capitaine-cursors](https://github.com/keeferrourke/capitaine-cursors).

## Installation
To install the cursor theme simply copy the compiled theme to your icons
directory. For local user installation:

```
./install.sh
```

For system-wide installation for all users:

```
sudo ./install.sh
```

Then set the theme with your preferred desktop tools.

## Building from source
You'll find everything you need to build and modify this cursor set in
the `src/` directory. To build the xcursor theme from the SVG source
run:

```
./build.sh
```

This will generate the pixmaps and appropriate aliases.
The freshly compiled cursor theme will be located in `dist/`

`build.sh` also generates `dist/cursors_scalable/`, the SVG cursor format
introduced by [KDE Breeze](https://github.com/KDE/breeze/blob/master/cursors/svg-cursor-format.md).
GNOME Shell 51 and later only load cursors in this format and fall back to
Adwaita otherwise. To regenerate it alone (no Inkscape needed):

```
python3 build-scalable.py dist/cursors_scalable
```

## Preview
![Lyra](preview-1.png)
![Lyra](preview-2.png)
