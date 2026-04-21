# 355 Awards — Class Literary Rankings

Class literary awards for the top **Literary Fiction** and **Genre Fiction** readings of the semester, ranked using a weighted voting system.

## Weighted Scoring System

Each group ranked up to three titles per category:

| Place | Points |
|-------|--------|
| 1st   | 3 pts  |
| 2nd   | 2 pts  |
| 3rd   | 1 pt   |

Scores are tallied across all four voting groups. For the **Combined Rankings**, each category's raw scores are normalised by the category maximum (÷ highest score in that category) and then summed, so Literary and Genre titles can be compared on a common scale.

## Files

| File | Description |
|------|-------------|
| `rank.py` | Python script that encodes all votes and prints the ranked results |
| `index.html` | Visual HTML page displaying all three ranked lists |

## Running the Script

```bash
python3 rank.py
```

The script prints:
1. **Literary Fiction Rankings** — weighted points per title
2. **Genre Fiction Rankings** — weighted points per title
3. **Combined Rankings** — single list across both categories using normalised scores

## Results Summary

### Literary Fiction
1. Tokyo Ueno Station — 8 pts
2. An Artist of the Floating World — 6 pts
3. Ten Nights Dreaming / The Precious Incense and Autumn Flowers of Sendai — 3 pts (tied)

### Genre Fiction
1. Bamboo Sword — 5 pts
2. Fisherman of the Inland Sea — 4 pts
3. Crimson Cloak / Ikemen Sengoku / Tokyo Ueno Station — 3 pts (tied)

### Combined (Literary & Genre)
1. Tokyo Ueno Station
2. Bamboo Sword
3. Fisherman of the Inland Sea
