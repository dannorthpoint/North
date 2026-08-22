from __future__ import annotations


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def blend(foreground: tuple[int, int, int], background: tuple[int, int, int], alpha: float) -> tuple[int, int, int]:
    return tuple(round(f * alpha + b * (1 - alpha)) for f, b in zip(foreground, background))


def linear(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (linear(channel) for channel in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


noir = hex_to_rgb("#0d0b08")
paper = hex_to_rgb("#f4efe3")
ivory = hex_to_rgb("#f2ecdf")
champagne = hex_to_rgb("#c8a96e")
brass_ink = hex_to_rgb("#77602e")
ink = hex_to_rgb("#14110c")
ink_soft = hex_to_rgb("#4e4736")

samples = [
    ("Ivory on noir", ivory, noir),
    ("Ivory 86% on noir", blend(ivory, noir, 0.86), noir),
    ("Ivory 64% on noir", blend(ivory, noir, 0.64), noir),
    ("Champagne on noir", champagne, noir),
    ("Brass ink on paper", brass_ink, paper),
    ("Ink on paper", ink, paper),
    ("Ink soft on paper", ink_soft, paper),
]

for label, foreground, background in samples:
    ratio = contrast(foreground, background)
    normal_aa = "pass" if ratio >= 4.5 else "fail"
    large_aa = "pass" if ratio >= 3 else "fail"
    print(f"{label}: {ratio:.2f}:1 | normal AA {normal_aa} | large-text AA {large_aa}")
