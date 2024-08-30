# from resume_parser import parse_resume
# from job_description_parser import parse_job_description
# from matcher import calculate_similarity

# def main():
#     # Prompt the user to input resume text
#     print("Please enter your resume text (press Enter twice when done):")
#     resume_lines = []
#     while True:
#         line = input()
#         if line:
#             resume_lines.append(line)
#         else:
#             break
#     resume_text = "\n".join(resume_lines)

#     # Prompt the user to input job description text
#     print("Please enter the job description text (press Enter twice when done):")
#     job_description_lines = []
#     while True:
#         line = input()
#         if line:
#             job_description_lines.append(line)
#         else:
#             break
#     job_description_text = "\n".join(job_description_lines)

#     # Process and match
#     resume_data = parse_resume(resume_text)
#     job_data = parse_job_description(job_description_text)
#     score = calculate_similarity(resume_data, job_data)

#     # Display the result
#     print(f"Resume Match Score: {score * 100:.2f}%")

# if __name__ == "__main__":
#     main()
import re
from resume_parser import parse_resume
from job_description_parser import parse_job_description
from matcher import calculate_similarity

def clean_input(text):
    """
    Remove special characters, including bullet points, from the input text.
    """
    # Replace bullet points and other non-alphanumeric characters with a space
    cleaned_text = re.sub(r'[^\w\s.,]', ' ', text)
    return cleaned_text

def main():
    # Prompt the user to input resume text
    print("Please enter your resume text (press Enter twice when done):")
    resume_lines = []
    while True:
        line = input()
        if line:
            resume_lines.append(line)
        else:
            break
    resume_text = "\n".join(resume_lines)

    # Prompt the user to input job description text
    print("Please enter the job description text (press Enter twice when done):")
    job_description_lines = []
    while True:
        line = input()
        if line:
            job_description_lines.append(line)
        else:
            break
    job_description_text = "\n".join(job_description_lines)

    # Clean the inputs
    cleaned_resume_text = clean_input(resume_text)
    cleaned_job_description_text = clean_input(job_description_text)

    # Process and match
    resume_data = parse_resume(cleaned_resume_text)
    job_data = parse_job_description(cleaned_job_description_text)
    score = calculate_similarity(resume_data, job_data)

    # Display the result
    print(f"Resume Match Score: {score * 100:.2f}%")

if __name__ == "__main__":
    main()
