"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a positive integer quantity parsed from *value*.

    Raises ValueError for non-numeric input or quantities that are zero
    or negative.
    """
    result = int(value.strip())
    if result <= 0:
        raise ValueError(f"Quantity must be a positive integer, got {result}")
    return result
