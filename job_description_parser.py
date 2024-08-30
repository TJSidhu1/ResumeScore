# src/job_description_parser.py

def parse_job_description(job_description_text):
    """
    This function processes the job description text to extract relevant
    data such as required skills, qualifications, and keywords.
    """
    # Example: Splitting the job description into words and filtering out common words
    words = job_description_text.lower().split()
    keywords = [word for word in words if len(word) > 2]  # simple example

    return keywords
