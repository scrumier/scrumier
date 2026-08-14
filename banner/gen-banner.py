#!/usr/bin/env python3
"""Génère la bannière du profil, en clair et en sombre.

GitHub rend du markdown : tout ce qui n'est pas du texte doit être une image.
Les deux versions sortent d'ici et jamais d'un éditeur, pour que la phrase
affichée soit toujours celle du moment, et pas celle d'il y a six mois.

Les polices sont celles des sites de Sonam, embarquées dans le dépôt pour qu'il
soit autonome, et converties à la volée parce que PIL ne lit pas le woff.
"""

from __future__ import annotations

import io
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"

WIDTH, HEIGHT = 1280, 320
SCALE = 2  # rendu au double puis réduit, faute d'antialiasing dans PIL

NAME = "SONAM CRUMIÈRE"
TITLE = ("Your files don’t know", "what your teams know.")
STACK = "AGENTS · CORPORA · RULES · GRENOBLE"

VIOLET = "#863bff"

THEMES = {
    "light": dict(bg="#f8f3ea", ink="#211c18", muted="#6b6259", chip="#d7ff44", out="banner-light.png"),
    "dark": dict(bg="#14110f", ink="#f6f1e7", muted="#9b9187", chip="#d7ff44", out="banner-dark.png"),
}

# La crête, dans un carré de 500 comme partout ailleurs. Elle sort par la droite
# et par le bas : coupée par le cadre, elle se lit comme un relief qui continue,
# alors qu'un contour entier posé dans le vide se lit comme un logo mal centré.
RIDGE = [(0, 392), (155, 218), (272, 320), (500, 68), (500, 500), (0, 500)]


def load(family: str, size: int) -> ImageFont.FreeTypeFont:
    font = TTFont(FONTS / family)
    font.flavor = None
    buffer = io.BytesIO()
    font.save(buffer)
    buffer.seek(0)
    return ImageFont.truetype(buffer, size * SCALE)


def tracked(draw: ImageDraw.ImageDraw, xy, text: str, font, fill, spacing: float) -> None:
    """Écrit avec de l'interlettrage, que PIL ne sait pas faire tout seul."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=font, fill=fill, anchor="ls")
        x += draw.textlength(char, font=font) + spacing * SCALE


def ridge_at(x: float, y: float, size: float) -> list[tuple[float, float]]:
    return [((x + px * size / 500) * SCALE, (y + py * size / 500) * SCALE) for px, py in RIDGE]


def draw_banner(theme: dict) -> Image.Image:
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), theme["bg"])
    draw = ImageDraw.Draw(image)

    # La crête, à droite, coupée par le bord bas du cadre.
    draw.polygon(ridge_at(900, 34, 420), fill=VIOLET, outline=theme["ink"], width=3 * SCALE)

    plex = load("ibm-plex-sans-latin-700-normal.woff", 15)
    spectral = load("spectral-latin-600-normal.woff", 50)
    mono = load("jetbrains-mono-latin-400-normal.woff", 14)

    x = 72 * SCALE
    tracked(draw, (x, 74 * SCALE), NAME, plex, theme["ink"], 3.2)
    draw.text((x, 172 * SCALE), TITLE[0], font=spectral, fill=theme["ink"], anchor="ls")
    draw.text((x, 232 * SCALE), TITLE[1], font=spectral, fill=theme["ink"], anchor="ls")

    width = draw.textlength(STACK, font=mono) + 40 * SCALE
    draw.rectangle(
        [x, 262 * SCALE, x + width, 294 * SCALE],
        fill=theme["chip"],
        outline=theme["ink"],
        width=2 * SCALE,
    )
    draw.text((x + 20 * SCALE, 284 * SCALE), STACK, font=mono, fill="#211c18", anchor="ls")

    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main() -> None:
    for name, theme in THEMES.items():
        draw_banner(theme).save(ROOT / theme["out"], optimize=True)
        print(f"{theme['out']} écrit")


if __name__ == "__main__":
    main()
