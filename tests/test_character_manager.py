"""Tests for character and team management"""
import json
import tempfile
from pathlib import Path

import pytest

# Add src to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from argus_overview.core.character_manager import Character, Team, CharacterManager


class TestCharacterDataclass:
    """Tests for Character dataclass"""

    def test_character_creation(self):
        """Test basic character creation"""
        char = Character(name="TestPilot")
        assert char.name == "TestPilot"
        assert char.account == ""
        assert char.role == "DPS"
        assert char.is_main is False
        assert char.window_id is None

    def test_character_with_all_fields(self):
        """Test character with all fields populated"""
        char = Character(
            name="MainPilot",
            account="Account1",
            role="Logi",
            notes="Main logistics character",
            is_main=True,
            window_id="0x12345",
            last_seen="2025-01-01T00:00:00"
        )
        assert char.name == "MainPilot"
        assert char.account == "Account1"
        assert char.role == "Logi"
        assert char.is_main is True
        assert char.window_id == "0x12345"

    def test_character_to_dict(self):
        """Test character serialization"""
        char = Character(name="TestPilot", role="Scout")
        data = char.to_dict()
        assert data["name"] == "TestPilot"
        assert data["role"] == "Scout"
        assert "account" in data
        assert "is_main" in data

    def test_character_from_dict(self):
        """Test character deserialization"""
        data = {
            "name": "ImportedPilot",
            "account": "Acc2",
            "role": "Miner",
            "notes": "",
            "is_main": False,
            "window_id": None,
            "last_seen": None
        }
        char = Character.from_dict(data)
        assert char.name == "ImportedPilot"
        assert char.account == "Acc2"
        assert char.role == "Miner"

    def test_character_roundtrip(self):
        """Test to_dict -> from_dict preserves data"""
        original = Character(
            name="RoundtripPilot",
            account="TestAcc",
            role="Hauler",
            notes="Test notes",
            is_main=True
        )
        restored = Character.from_dict(original.to_dict())
        assert restored.name == original.name
        assert restored.account == original.account
        assert restored.role == original.role
        assert restored.is_main == original.is_main


class TestTeamDataclass:
    """Tests for Team dataclass"""

    def test_team_creation(self):
        """Test basic team creation"""
        team = Team(name="MiningFleet")
        assert team.name == "MiningFleet"
        assert team.description == ""
        assert team.characters == []
        assert team.layout_name == "Default"
        assert team.color == "#4287f5"

    def test_team_with_members(self):
        """Test team with character list"""
        team = Team(
            name="PvPSquad",
            description="Main PvP fleet",
            characters=["DPS1", "Logi1", "Scout1"],
            color="#ff0000"
        )
        assert len(team.characters) == 3
        assert "DPS1" in team.characters
        assert team.color == "#ff0000"

    def test_team_to_dict(self):
        """Test team serialization"""
        team = Team(name="TestTeam", characters=["Char1", "Char2"])
        data = team.to_dict()
        assert data["name"] == "TestTeam"
        assert data["characters"] == ["Char1", "Char2"]

    def test_team_from_dict(self):
        """Test team deserialization"""
        data = {
            "name": "ImportedTeam",
            "description": "Test",
            "characters": ["A", "B"],
            "layout_name": "Custom",
            "color": "#00ff00",
            "created_at": "2025-01-01T00:00:00"
        }
        team = Team.from_dict(data)
        assert team.name == "ImportedTeam"
        assert team.characters == ["A", "B"]
        assert team.layout_name == "Custom"


class TestCharacterManager:
    """Tests for CharacterManager"""

    @pytest.fixture
    def temp_config_dir(self):
        """Create temporary config directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    @pytest.fixture
    def manager(self, temp_config_dir):
        """Create CharacterManager with temp directory"""
        return CharacterManager(config_dir=temp_config_dir)

    def test_add_character(self, manager):
        """Test adding a character"""
        char = Character(name="NewPilot")
        result = manager.add_character(char)
        assert result is True
        assert "NewPilot" in manager.characters
        assert manager.get_character("NewPilot") is not None

    def test_add_duplicate_character(self, manager):
        """Test adding duplicate character fails"""
        char1 = Character(name="DupePilot")
        char2 = Character(name="DupePilot")
        manager.add_character(char1)
        result = manager.add_character(char2)
        assert result is False

    def test_remove_character(self, manager):
        """Test removing a character"""
        char = Character(name="ToRemove")
        manager.add_character(char)
        result = manager.remove_character("ToRemove")
        assert result is True
        assert "ToRemove" not in manager.characters

    def test_remove_nonexistent_character(self, manager):
        """Test removing non-existent character fails"""
        result = manager.remove_character("DoesNotExist")
        assert result is False

    def test_update_character(self, manager):
        """Test updating character properties"""
        char = Character(name="UpdateMe", role="DPS")
        manager.add_character(char)
        result = manager.update_character("UpdateMe", role="Logi", is_main=True)
        assert result is True
        updated = manager.get_character("UpdateMe")
        assert updated.role == "Logi"
        assert updated.is_main is True

    def test_get_all_characters(self, manager):
        """Test getting all characters"""
        manager.add_character(Character(name="Char1"))
        manager.add_character(Character(name="Char2"))
        manager.add_character(Character(name="Char3"))
        all_chars = manager.get_all_characters()
        assert len(all_chars) == 3

    def test_get_characters_by_account(self, manager):
        """Test filtering by account"""
        manager.add_character(Character(name="A1", account="Acc1"))
        manager.add_character(Character(name="A2", account="Acc1"))
        manager.add_character(Character(name="B1", account="Acc2"))
        acc1_chars = manager.get_characters_by_account("Acc1")
        assert len(acc1_chars) == 2

    def test_create_team(self, manager):
        """Test creating a team"""
        team = Team(name="NewTeam")
        result = manager.create_team(team)
        assert result is True
        assert "NewTeam" in manager.teams

    def test_delete_team(self, manager):
        """Test deleting a team"""
        team = Team(name="ToDelete")
        manager.create_team(team)
        result = manager.delete_team("ToDelete")
        assert result is True
        assert "ToDelete" not in manager.teams

    def test_add_character_to_team(self, manager):
        """Test adding character to team"""
        manager.add_character(Character(name="TeamMember"))
        manager.create_team(Team(name="Squad"))
        result = manager.add_character_to_team("Squad", "TeamMember")
        assert result is True
        team = manager.get_team("Squad")
        assert "TeamMember" in team.characters

    def test_add_nonexistent_character_to_team(self, manager):
        """Test adding non-existent character to team fails"""
        manager.create_team(Team(name="Squad"))
        result = manager.add_character_to_team("Squad", "Ghost")
        assert result is False

    def test_remove_character_from_team(self, manager):
        """Test removing character from team"""
        manager.add_character(Character(name="Leaver"))
        manager.create_team(Team(name="Squad", characters=["Leaver"]))
        result = manager.remove_character_from_team("Squad", "Leaver")
        assert result is True
        team = manager.get_team("Squad")
        assert "Leaver" not in team.characters

    def test_remove_character_removes_from_teams(self, manager):
        """Test deleting character removes from all teams"""
        manager.add_character(Character(name="InMultipleTeams"))
        manager.create_team(Team(name="Team1", characters=["InMultipleTeams"]))
        manager.create_team(Team(name="Team2", characters=["InMultipleTeams"]))
        manager.remove_character("InMultipleTeams")
        assert "InMultipleTeams" not in manager.get_team("Team1").characters
        assert "InMultipleTeams" not in manager.get_team("Team2").characters

    def test_assign_window(self, manager):
        """Test window assignment"""
        manager.add_character(Character(name="ActivePilot"))
        result = manager.assign_window("ActivePilot", "0xABCD")
        assert result is True
        char = manager.get_character("ActivePilot")
        assert char.window_id == "0xABCD"
        assert char.last_seen is not None

    def test_get_character_by_window(self, manager):
        """Test finding character by window ID"""
        manager.add_character(Character(name="WindowOwner"))
        manager.assign_window("WindowOwner", "0x1234")
        char = manager.get_character_by_window("0x1234")
        assert char is not None
        assert char.name == "WindowOwner"

    def test_get_active_characters(self, manager):
        """Test getting logged-in characters"""
        manager.add_character(Character(name="Online1"))
        manager.add_character(Character(name="Online2"))
        manager.add_character(Character(name="Offline"))
        manager.assign_window("Online1", "0x1")
        manager.assign_window("Online2", "0x2")
        active = manager.get_active_characters()
        assert len(active) == 2

    def test_persistence(self, temp_config_dir):
        """Test data persists across manager instances"""
        # Create and populate first manager
        manager1 = CharacterManager(config_dir=temp_config_dir)
        manager1.add_character(Character(name="Persistent"))
        manager1.create_team(Team(name="PersistentTeam", characters=["Persistent"]))

        # Create second manager, should load saved data
        manager2 = CharacterManager(config_dir=temp_config_dir)
        assert "Persistent" in manager2.characters
        assert "PersistentTeam" in manager2.teams
        assert "Persistent" in manager2.get_team("PersistentTeam").characters


class TestAutoAssignWindows:
    """Tests for window auto-assignment"""

    @pytest.fixture
    def manager(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            mgr = CharacterManager(config_dir=Path(tmpdir))
            mgr.add_character(Character(name="Pilot1"))
            mgr.add_character(Character(name="Pilot2"))
            mgr.add_character(Character(name="MainChar"))
            yield mgr

    def test_auto_assign_eve_format(self, manager):
        """Test auto-assign with EVE window title format"""
        windows = [
            ("0x1", "EVE - Pilot1"),
            ("0x2", "EVE - Pilot2"),
        ]
        assignments = manager.auto_assign_windows(windows)
        assert len(assignments) == 2
        assert assignments["Pilot1"] == "0x1"
        assert assignments["Pilot2"] == "0x2"

    def test_auto_assign_plain_format(self, manager):
        """Test auto-assign with plain character name"""
        windows = [("0x1", "MainChar")]
        assignments = manager.auto_assign_windows(windows)
        assert "MainChar" in assignments

    def test_auto_assign_unknown_character(self, manager):
        """Test auto-assign ignores unknown characters"""
        windows = [("0x1", "EVE - UnknownPilot")]
        assignments = manager.auto_assign_windows(windows)
        assert len(assignments) == 0
