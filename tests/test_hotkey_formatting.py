"""Tests for hotkey formatting utilities"""
import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def format_hotkey(hotkey: str) -> str:
    """Format hotkey with angle brackets around each key component

    Extracted from HotkeysTab._format_hotkey for testing.
    e.g. 'ctrl+shift+]' -> '<ctrl>+<shift>+<]>'
    """
    hotkey = hotkey.strip()
    if not hotkey:
        return hotkey

    # Split by + and wrap each part in brackets if not already
    parts = hotkey.split('+')
    formatted_parts = []

    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Remove existing brackets if present
        if part.startswith('<') and part.endswith('>'):
            part = part[1:-1]
        # Add brackets
        formatted_parts.append(f"<{part}>")

    return '+'.join(formatted_parts)


class TestHotkeyFormatting:
    """Tests for hotkey format function"""

    def test_simple_hotkey(self):
        """Test single key"""
        assert format_hotkey("f1") == "<f1>"

    def test_modifier_plus_key(self):
        """Test modifier + key"""
        assert format_hotkey("ctrl+1") == "<ctrl>+<1>"

    def test_two_modifiers(self):
        """Test two modifiers + key"""
        assert format_hotkey("ctrl+shift+a") == "<ctrl>+<shift>+<a>"

    def test_three_modifiers(self):
        """Test three modifiers"""
        assert format_hotkey("ctrl+alt+shift+x") == "<ctrl>+<alt>+<shift>+<x>"

    def test_already_formatted(self):
        """Test already formatted hotkey is preserved"""
        assert format_hotkey("<ctrl>+<alt>+<1>") == "<ctrl>+<alt>+<1>"

    def test_partially_formatted(self):
        """Test mixed format is normalized"""
        assert format_hotkey("<ctrl>+shift+1") == "<ctrl>+<shift>+<1>"

    def test_special_keys(self):
        """Test special keys like brackets"""
        assert format_hotkey("ctrl+shift+]") == "<ctrl>+<shift>+<]>"
        assert format_hotkey("ctrl+shift+[") == "<ctrl>+<shift>+<[>"

    def test_empty_string(self):
        """Test empty input"""
        assert format_hotkey("") == ""

    def test_whitespace_handling(self):
        """Test whitespace is stripped"""
        assert format_hotkey("  ctrl + shift + 1  ") == "<ctrl>+<shift>+<1>"

    def test_function_keys(self):
        """Test function keys"""
        assert format_hotkey("shift+f5") == "<shift>+<f5>"
        assert format_hotkey("ctrl+f12") == "<ctrl>+<f12>"

    def test_numpad_keys(self):
        """Test numpad keys"""
        assert format_hotkey("ctrl+numpad1") == "<ctrl>+<numpad1>"


class TestHotkeyEdgeCases:
    """Edge cases for hotkey formatting"""

    def test_empty_parts(self):
        """Test handling of empty parts from multiple +'s"""
        result = format_hotkey("ctrl++shift")
        # Should skip empty parts
        assert result == "<ctrl>+<shift>"

    def test_single_plus(self):
        """Test single + key"""
        assert format_hotkey("+") == ""

    def test_only_modifiers(self):
        """Test only modifiers without key"""
        assert format_hotkey("ctrl+alt+") == "<ctrl>+<alt>"

    def test_unusual_keys(self):
        """Test unusual key names"""
        assert format_hotkey("ctrl+pause") == "<ctrl>+<pause>"
        assert format_hotkey("alt+printscreen") == "<alt>+<printscreen>"
