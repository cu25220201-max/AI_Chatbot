from pypdf import PdfReader

def read_resume(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(text):
    skills = ["python", "java", "machine learning", "ai", "sql"]

    found = []
    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    return found