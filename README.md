# cfi-decoder

Offline decoder for ISO 10962 CFI (Classification of Financial Instruments) codes.

## How It Works

The decoder takes a 6-character CFI code and maps each position to human-readable descriptions:

- **Position 1:** Financial instrument category (e.g., `E` = Equities, `D` = Debt)
- **Position 2:** Subcategory/group within that category (e.g., `S` = Shares for Equities)
- **Positions 3-6:** Specific attributes based on the category-group combination

The `decode()` function returns a pipe-separated string of descriptions for each position.

### Example

```python
from cfi_decoder import decode

result = decode("ESVUFR")
# Output: "Equities | Shares (Common/Ordinary) | Voting | Free | Fully Paid | Registered"
```

### Implementation

The decoder is implemented as a series of dictionary lookups against lookup tables defined in [`src/cfi_decoder/_data.py`](src/cfi_decoder/_data.py). The tables map CFI code characters to their human-readable descriptions for each position.

## Models Used

This project was developed using Claude AI:

- Claude Opus 4.6
- Claude Sonnet 4.6
- Claude Haiku 4.5
