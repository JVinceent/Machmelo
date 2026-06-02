"""
config.py — Central configuration for MachMelo.
All paths and app-wide settings live here. Import this anywhere.
"""

import os

# ── Paths ────────────────────────────────────────────────────────────────────

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DB_DIR     = os.path.join(BASE_DIR, "db")
BACKUP_DIR = os.path.join(DB_DIR, "backups")

DB_PATH     = os.path.join(DB_DIR, "melody_match.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")
CSV_PATH    = os.path.join(BASE_DIR, "dataset.csv")

LOGO_PATH          = os.path.join(ASSETS_DIR, "logo.png")
DEFAULT_COVER_PATH = os.path.join(ASSETS_DIR, "default_cover.png")

# ── Import settings ───────────────────────────────────────────────────────────

IMPORT_LIMIT = 100  # Max rows to pull from dataset.csv at once

# ── Audio analysis ────────────────────────────────────────────────────────────

AUDIO_ANALYSIS_DURATION = 30   # Seconds of audio to load for feature extraction
DEFAULT_TEMPO            = 120.0
DEFAULT_ENERGY           = 0.5

# ── UI / theme ────────────────────────────────────────────────────────────────

APP_TITLE      = "MachMelo"
WINDOW_SIZE    = "1000x600"
APPEARANCE     = "Dark"
COLOR_THEME    = "blue"

THEME_PINK     = "#E91E63"
THEME_PINK_HOV = "#C2185B"
THEME_BLUE     = "#2980b9"
THEME_BLUE_HOV = "#3498db"
THEME_DANGER   = "#c0392b"

# ── Artist nationality pool ───────────────────────────────────────────────────

COUNTRIES = [
    "USA", "UK", "Canada", "South Korea", "Japan",
    "France", "Brazil", "Germany", "Australia", "Philippines",
]

# ── Genre mapping ─────────────────────────────────────────────────────────────

GENRE_CATEGORIES = {
    "Rock":        ["alt-rock", "alternative", "grunge", "hard-rock", "metal", "punk", "rock", "indie"],
    "Pop":         ["pop", "k-pop", "j-pop", "indie-pop", "synth-pop", "cantopop"],
    "Hip-Hop/R&B": ["hip-hop", "r-n-b", "rap", "soul", "funk", "trap"],
    "Electronic":  ["dance", "edm", "house", "techno", "trance", "electro", "dubstep"],
    "Jazz/Blues":  ["jazz", "blues", "soul"],
    "Classical":   ["classical", "piano", "opera"],
    "Mood":        ["acoustic", "chill", "sleep", "study", "happy", "sad", "romance"],
}
