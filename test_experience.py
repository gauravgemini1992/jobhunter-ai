from pprint import pprint

from resume_parser import parse_resume
from experience_parser import parse_experience

resume = parse_resume("resume.docx")

jobs = parse_experience(resume["experience"])

pprint(jobs)