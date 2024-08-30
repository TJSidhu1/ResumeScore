# src/resume_parser.py

def parse_resume(resume_text):
    """
    This function processes the resume text to extract relevant data
    such as keywords, skills, and experience.
    """
    # Example: Splitting the resume text into words and filtering out common words
    words = resume_text.lower().split()
    keywords = [word for word in words if len(word) > 2]  # simple example

    return keywords
