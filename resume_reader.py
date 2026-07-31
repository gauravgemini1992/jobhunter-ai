import re
from docx import Document


def clean_text(text):
    """
    Cleans resume text extracted from DOCX.
    """

    if not text:
        return ""

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Replace non-breaking spaces
    text = text.replace("\xa0", " ")

    # Collapse multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def read_resume(file_path):
    """
    Reads a DOCX resume and returns cleaned text.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        text = clean_text(paragraph.text)

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


if __name__ == "__main__":

    try:
        resume = read_resume("resume.docx")

        print("=" * 60)
        print("CLEANED RESUME")
        print("=" * 60)
        print(resume)

    except FileNotFoundError:
        print("❌ resume.docx not found.")