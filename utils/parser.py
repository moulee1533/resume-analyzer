import re
import PyPDF2

COMMON_SKILLS = [
    'python', 'java', 'c++', 'html', 'css', 'javascript', 'react',
    'node.js', 'flask', 'django', 'sql', 'mongodb', 'git', 'linux',
    'machine learning', 'data analysis', 'tensorflow', 'pandas', 'numpy'
]

def extract_text_from_pdf(filepath):
    text = ''
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def extract_resume_data(filepath):
    text = extract_text_from_pdf(filepath)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    return {
        'email': email,
        'phone': phone,
        'skills': skills,
        'text': text
    }

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else 'Not found'

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-()]{8,}\d', text)
    return match.group(0) if match else 'Not found'

def extract_skills(text):
    found = []
    text_lower = text.lower()
    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            found.append(skill)
    return list(set(found))

def has_experience_in_resume(text):
    text_lower = text.lower()
    
    # Patterns to detect experience
    patterns = [
        r'\d+\+?\s+years? of experience',
        r'\d+\s+years? experience',
        r'\d+\s+years? in',
        r'work experience',
        r'professional experience',
        r'internship',
        r'intern'
    ]

    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def compare_skills(resume_skills, jobdesc_text, resume_text=''):
    matched = []
    job_text_lower = jobdesc_text.lower()

    for skill in resume_skills:
        if skill.lower() in job_text_lower:
            matched.append(skill)

    score = round((len(matched) / len(resume_skills)) * 100) if resume_skills else 0

    # Detect if JD requires experience
    exp_required = bool(re.search(r'\d+\+?\s+years? of experience', job_text_lower))

    # Check if resume mentions any experience
    has_experience = has_experience_in_resume(resume_text)

    if exp_required and not has_experience:
        score = max(score - 30, 0)  # Penalize

    return score, matched
