from collections import Counter
from pathlib import Path

def word_count(filepath):
    text = Path(filepath).read_text(encoding='utf-8').lower()
    words = text.split()
    return Counter(words)
