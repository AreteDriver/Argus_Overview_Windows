# Argus Overview - Windows Edition

Professional multi-boxing tool for EVE Online on Windows.

## Features

- Real-time window previews at 30 FPS
- Auto-discovery of EVE clients
- Per-character hotkeys
- Layout presets and grid patterns
- EVE settings synchronization
- System tray integration
- Activity alerts and session timers

## Requirements

- Windows 10/11
- Python 3.11+
- EVE Online

## Installation

```bash
pip install -e .
```

## Usage

```bash
python src/main.py
```

## Build Standalone EXE

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name=Argus_Overview src/main.py
```

## License

MIT
