from pprint import pprint
from resume_parser import parse_resume

resume = parse_resume("resume.docx")

pprint(resume)