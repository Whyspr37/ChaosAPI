
import os
import re
import json
from collections import defaultdict, Counter

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

def extract_phrases(text, phrase_list):
    found = []
    for phrase in phrase_list:
        if phrase in text.lower():
            found.append(phrase)
    return found

def build_haunt_index(notes_folder="notes", top_n=10):
    haunt_phrases = [
        "mirror", "storm", "blood", "shadow", "fire", "silence", "light", "cold", "grief", "rage", "mother", "ghost",
        "burn", "shatter", "haunt", "scream", "void", "hunger", "wound", "bruise", "wild", "flood", "static"
    ]

    haunt_counts = Counter()
    context_data = defaultdict(list)

    for root, _, files in os.walk(notes_folder):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    phrases = extract_phrases(content, haunt_phrases)
                    haunt_counts.update(phrases)
                    for phrase in phrases:
                        excerpt = content[:500].replace("\n", " ")
                        context_data[phrase].append({"file": file, "excerpt": excerpt})
                except Exception as e:
                    continue

    most_common = haunt_counts.most_common(top_n)
    haunt_index = []
    for phrase, count in most_common:
        haunt_index.append({
            "phrase": phrase,
            "count": count,
            "examples": context_data[phrase][:3]
        })

    return {"haunt_index": haunt_index}
