from src.extraction import extract_skills

def test_extracts_python():
    text = "Gute Kenntnisse in Python"
    assert extract_skills(text) == {"python"}

def test_extracts_javascript():
    text = "Erfahrung mit JavaScript von Vorteil!"
    assert extract_skills(text) == {"javascript"}

def test_extracts_git():
    text = "Version Control mit Git."
    assert extract_skills(text) == {"git"}