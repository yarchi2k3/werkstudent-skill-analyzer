import re

SKILLS = {
    "python": ["python"],
    "java": ["java"],
    "javascript": ["javascript"],
    "sql": ["sql"],
    "git": ["git", "github", "gitlab"]
}

def normalize(text):
    lower_case = text.lower()
    cleanup = re.sub(r"[^a-z0-9\s]", " ", lower_case)
    return cleanup

def extract_skills(text):
    normalized_text = normalize(text)
    found = set()
    for skill, aliases in SKILLS.items():
        for alias in aliases:
            pattern = r"\b" + alias + r"\b"
            if re.search(pattern, normalized_text):
                found.add(skill)
    return found