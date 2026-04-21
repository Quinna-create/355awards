#!/usr/bin/env python3
"""355 Awards — Weighted Ranking Calculator

Combines Literary Fiction and Genre Fiction class votes using a
positional point system (1st = 3 pts, 2nd = 2 pts, 3rd = 1 pt) and
produces a single combined ranked list for both categories.
"""

# ---------------------------------------------------------------------------
# Voting data — each entry is one group's ballot
# ---------------------------------------------------------------------------
VOTES = [
    {
        "literary": [
            "An Artist of the Floating World",
            "The Precious Incense and Autumn Flowers of Sendai",
            "Date's Black Ships",
        ],
        "genre": [
            "Tokyo Ueno Station",
            "Fisherman of the Inland Sea",
            "Ten Nights Dreaming",
        ],
    },
    {
        "literary": [
            "Ten Nights Dreaming",
            "Tokyo Ueno Station",
            "An Artist of the Floating World",
        ],
        "genre": [
            "Crimson Cloak",
            "Bamboo Sword",
            "The Girl Who Leapt through Time",
        ],
    },
    {
        "literary": [
            "Tokyo Ueno Station",
            "An Artist of the Floating World",
        ],
        "genre": [
            "Bamboo Sword",
        ],
    },
    {
        "literary": [
            "Tokyo Ueno Station",
            "Bamboo Sword",
            "The Precious Incense and Autumn Flowers of Sendai",
        ],
        "genre": [
            "Ikemen Sengoku",
            "Fisherman of the Inland Sea",
            "The Girl Who Leapt through Time",
        ],
    },
]

# Points awarded for each rank position (index 0 = 1st place, etc.)
POINTS = [3, 2, 1]


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------

def calculate_scores(votes, category):
    """Return a dict of {title: total_points} for the given category."""
    scores = {}
    for ballot in votes:
        for rank, title in enumerate(ballot.get(category, [])):
            if rank < len(POINTS):
                scores[title] = scores.get(title, 0) + POINTS[rank]
    return scores


def rank_scores(scores):
    """Return a list of (title, points) sorted descending by points."""
    return sorted(scores.items(), key=lambda x: (-x[1], x[0]))


# ---------------------------------------------------------------------------
# Calculate per-category rankings
# ---------------------------------------------------------------------------

literary_scores = calculate_scores(VOTES, "literary")
genre_scores = calculate_scores(VOTES, "genre")

literary_ranked = rank_scores(literary_scores)
genre_ranked = rank_scores(genre_scores)

# ---------------------------------------------------------------------------
# Build a single combined list
#
# Strategy: normalise each category's raw scores to a 0–1 scale (dividing by
# the highest score in that category), then sum the normalised scores so that
# books appearing in both Literary and Genre ballots can be compared fairly
# against books that only appear in one category.
# ---------------------------------------------------------------------------

max_lit = max(literary_scores.values(), default=1)
max_gen = max(genre_scores.values(), default=1)

combined = {}
for title, score in literary_scores.items():
    combined[title] = combined.get(title, 0) + score / max_lit
for title, score in genre_scores.items():
    combined[title] = combined.get(title, 0) + score / max_gen

combined_ranked = sorted(combined.items(), key=lambda x: (-x[1], x[0]))


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def _category_label(title):
    """Return category tag(s) for a title in the combined list."""
    tags = []
    if title in literary_scores:
        tags.append("Literary")
    if title in genre_scores:
        tags.append("Genre")
    return " & ".join(tags)


def print_ranked(header, ranked):
    width = 56
    print(f"\n{'=' * width}")
    print(f"  {header}")
    print(f"{'=' * width}")
    for i, (title, score) in enumerate(ranked, 1):
        pts = f"{score:.2f}" if isinstance(score, float) else f"{score}"
        print(f"  {i:>2}. {title}  ({pts} pts)")


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print_ranked("Literary Fiction Rankings", literary_ranked)
    print_ranked("Genre Fiction Rankings", genre_ranked)

    print(f"\n{'=' * 56}")
    print("  Combined Rankings — Literary & Genre Fiction")
    print(f"{'=' * 56}")
    for i, (title, score) in enumerate(combined_ranked, 1):
        tag = _category_label(title)
        print(f"  {i:>2}. {title}  [{tag}]  ({score:.2f})")
