# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Argus Overview Windows
Build with: pyinstaller Argus_Overview.spec
"""

import sys
from pathlib import Path

block_cipher = None

# Get the project root
PROJ_ROOT = Path(SPECPATH)

a = Analysis(
    ['src/main.py'],
    pathex=[str(PROJ_ROOT / 'src')],
    binaries=[],
    datas=[
        ('assets/icon.ico', 'assets'),
        ('assets/icon_256.png', 'assets'),
    ],
    hiddenimports=[
        'win32api',
        'win32con',
        'win32gui',
        'win32event',
        'win32process',
        'winerror',
        'pynput.keyboard._win32',
        'pynput.mouse._win32',
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'scipy',
        'pandas',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Argus_Overview',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Windowed application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',
    version='version_info.txt',
)
