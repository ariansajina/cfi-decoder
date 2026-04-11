"""Core decode function for ISO 10962 CFI codes."""

from ._data import ATTRIBUTES, CATEGORIES, GROUPS


def decode(cfi_code: str) -> str:
    """Decode an ISO 10962 CFI code into human-readable descriptions.

    Args:
        cfi_code: A 6-character CFI code string.

    Returns:
        Pipe-separated description string, e.g.
        ``"Equities | Shares (Common/Ordinary) | Voting | ..."``.

    Raises:
        TypeError: If *cfi_code* is not a string.
        ValueError: If the code length is not 6 or any character is unrecognised.
    """
    if not isinstance(cfi_code, str):
        raise TypeError(f"Expected str, got {type(cfi_code).__name__}")

    code = cfi_code.upper()

    if len(code) != 6:
        raise ValueError(f"CFI code must be exactly 6 characters, got {len(code)}")

    cat_char = code[0]
    grp_char = code[1]

    category = CATEGORIES.get(cat_char)
    if category is None:
        raise ValueError(f"Unknown category: {cat_char!r}")

    group_map = GROUPS.get(cat_char)
    if group_map is None or grp_char not in group_map:
        raise ValueError(f"Unknown group {grp_char!r} for category {cat_char!r}")
    group = group_map[grp_char]

    attr_defs = ATTRIBUTES.get((cat_char, grp_char))
    if attr_defs is None:
        raise ValueError(
            f"No attribute definitions for category {cat_char!r}, group {grp_char!r}"
        )

    parts: list[str] = [category, group]
    for i, (label, values) in enumerate(attr_defs):
        char = code[i + 2]
        desc = values.get(char)
        if desc is None:
            raise ValueError(
                f"Unknown attribute {char!r} at position {i + 3} "
                f"({label}) for category {cat_char!r}, group {grp_char!r}"
            )
        parts.append(desc)

    return " | ".join(parts)
