# Argus Overview - Windows Edition

Professional multi-boxing tool for EVE Online on Windows.

[![Build Windows EXE](https://github.com/AreteDriver/Argus_Overview_Windows/actions/workflows/build.yml/badge.svg)](https://github.com/AreteDriver/Argus_Overview_Windows/actions/workflows/build.yml)
[![Release](https://img.shields.io/github/v/release/AreteDriver/Argus_Overview_Windows)](https://github.com/AreteDriver/Argus_Overview_Windows/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Download

**[Download Latest Release](https://github.com/AreteDriver/Argus_Overview_Windows/releases/latest)**

| Option | File | Description |
|--------|------|-------------|
| **Portable** | `Argus_Overview.exe` | Just download and run - no installation needed |
| **Installer** | `Argus_Overview_Setup_*.exe` | Creates Start Menu shortcuts, optional Desktop shortcut, proper uninstall |

Choose **Portable** if you want simplicity. Choose **Installer** if you want shortcuts and Windows integration.

## Features

- **Real-time Window Preview** - 30 FPS capture of all EVE windows
- **Auto-Discovery** - Automatically detects new EVE clients
- **Character Management** - Organize characters, create teams, track accounts
- **Smart Layouts** - 7 grid patterns (2x2, 3x1, Main+Sides, Cascade, etc.)
- **Global Hotkeys** - Control windows with customizable hotkey bindings
- **Alert Detection** - Visual alerts for red flashes (damage) and screen changes
- **Settings Sync** - Synchronize EVE settings between characters with backup
- **System Tray** - Minimize to tray with quick access menu
- **Multi-Monitor Support** - Works across multiple displays
- **Themes** - Dark, Light, and EVE themes

## Requirements

- Windows 10/11 (64-bit)
- EVE Online installed

## Quick Start

1. Download `Argus_Overview.exe` from [Releases](https://github.com/AreteDriver/Argus_Overview_Windows/releases/latest)
2. Run the executable
3. Launch your EVE clients - Argus will auto-detect them

That's it! No installation needed.

## Default Hotkeys

| Hotkey | Action |
|--------|--------|
| `Ctrl+Alt+1-9` | Activate window 1-9 |
| `Ctrl+Alt+M` | Minimize all windows |
| `Ctrl+Alt+R` | Restore all windows |
| `Ctrl+Alt+F5` | Refresh all previews |
| `Ctrl+Alt+]` | Next layout |
| `Ctrl+Alt+[` | Previous layout |
| `Ctrl+Alt+A` | Toggle alerts |
| `Ctrl+Alt+T` | Toggle always on top |

*All hotkeys are customizable in Settings > Hotkeys*

## Configuration

Settings are stored in:
```
%LOCALAPPDATA%\argus-overview\
├── settings.json          # Application settings
├── characters.json        # Character database
├── teams.json             # Team definitions
└── layout_presets.json    # Saved layouts
```

## Building from Source

```cmd
# Clone repository
git clone https://github.com/AreteDriver/Argus_Overview_Windows.git
cd Argus_Overview_Windows

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -e .

# Run application
python src/main.py

# Build standalone .exe
pip install pyinstaller
pyinstaller Argus_Overview.spec
# Output: dist/Argus_Overview.exe
```

## Troubleshooting

### Windows Defender Warning
If Windows Defender blocks the .exe:
1. Open Windows Security
2. Virus & threat protection > Manage settings
3. Add exclusion > Add folder > Select Argus-Overview folder

### No Windows Detected
- Make sure EVE Online clients are running
- Run Argus Overview as Administrator if needed
- Check that windows are not minimized

### Hotkeys Not Working
- Check for conflicts with other applications
- Verify hotkey syntax in Settings
- Some keys may be reserved by Windows

## Related Projects

- [Argus Overview (Linux)](https://github.com/AreteDriver/Argus_Overview) - Linux version with X11/Wayland support

## Support Development

If you find Argus Overview useful, consider supporting development:

**[Buy Me a Coffee](https://buymeacoffee.com/aretedriver)**

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Made by [AreteDriver](https://github.com/AreteDriver)**
