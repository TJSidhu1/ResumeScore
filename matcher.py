# src/matcher.py

def calculate_similarity(resume_data, job_data):
    """
    This function compares the keywords extracted from the resume and the job
    description to calculate a similarity score.
    """
    # Example: Calculate the number of matching keywords
    matching_keywords = set(resume_data) & set(job_data)
    total_keywords = len(set(resume_data) | set(job_data))

    if total_keywords == 0:
        return 0

    similarity_score = len(matching_keywords) / total_keywords

    return similarity_score
