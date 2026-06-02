"""
data/models.py — Dataclasses that represent database rows.

Replace raw tuple indexing (song[2], song[9]) with named attributes
(song.title, song.cover_path) everywhere in the app.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Song:
    id:          int
    user_id:     int
    title:       str
    artist:      str
    genre:       str
    file_path:   str
    tempo:       float        = 120.0
    energy:      float        = 0.5
    duration_ms: int          = 0
    cover_path:  Optional[str] = None

    # ── Helpers ──────────────────────────────────────────────────────────────

    @property
    def is_real_file(self) -> bool:
        """True if this song has an actual audio file (not a dataset import)."""
        import os
        return (
            bool(self.file_path)
            and self.file_path != "N/A (Dataset Import)"
            and os.path.exists(self.file_path)
        )

    @property
    def display_duration(self) -> str:
        """Format duration_ms as M:SS."""
        if not self.duration_ms:
            return "0:00"
        seconds = int(self.duration_ms) // 1000
        return f"{seconds // 60}:{seconds % 60:02d}"

    @classmethod
    def from_row(cls, row: tuple) -> "Song":
        """Build a Song from a database row tuple (index-safe)."""
        return cls(
            id          = row[0],
            user_id     = row[1],
            title       = row[2],
            artist      = row[3],
            genre       = row[4],
            file_path   = row[5],
            tempo       = row[6] if len(row) > 6 else 120.0,
            energy      = row[7] if len(row) > 7 else 0.5,
            duration_ms = row[8] if len(row) > 8 else 0,
            cover_path  = row[9] if len(row) > 9 else None,
        )


@dataclass
class Playlist:
    id:    int
    title: str

    @classmethod
    def from_row(cls, row: tuple) -> "Playlist":
        return cls(id=row[0], title=row[1])


@dataclass
class User:
    id:        int
    username:  str
    first_name: str
    last_name:  str
    birth_date: Optional[str] = None
    email:      Optional[str] = None
    join_date:  Optional[str] = None
    is_banned:  bool          = False
    role:       str           = "user"

    @classmethod
    def from_row(cls, row: tuple) -> "User":
        return cls(
            id         = row[0],
            username   = row[1],
            first_name = row[2],
            last_name  = row[3],
            birth_date = row[4] if len(row) > 4 else None,
            email      = row[5] if len(row) > 5 else None,
            join_date  = row[6] if len(row) > 6 else None,
            is_banned  = bool(row[7]) if len(row) > 7 else False,
        )
