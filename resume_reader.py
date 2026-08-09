"""
============================================================
JobHunter AI
Resume Reader
============================================================
"""

import os

from docx import Document


# ==========================================================
# Resume Reader
# ==========================================================


def read_resume(file_path):
    """
    Reads the contents of a resume file.

    Currently Supported:
        • DOCX

    Future Support:
        • PDF
    """

    if not file_path:
        raise ValueError(
            "Resume path was not provided."
        )

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Resume not found:\n{file_path}"
        )

    extension = os.path.splitext(file_path)[1].lower()

    # ------------------------------------------------------
    # DOCX
    # ------------------------------------------------------

    if extension == ".docx":

        try:

            document = Document(file_path)

            paragraphs = []

            for paragraph in document.paragraphs:

                text = paragraph.text.strip()

                if text:

                    paragraphs.append(text)

            return "\n".join(paragraphs)

        except Exception as error:

            raise RuntimeError(
                f"Unable to read DOCX resume.\n{error}"
            )

    # ------------------------------------------------------
    # PDF (Coming Soon)
    # ------------------------------------------------------

    if extension == ".pdf":

        raise NotImplementedError(
            "PDF resume support will be available in v1.1."
        )

    # ------------------------------------------------------
    # Unsupported Format
    # ------------------------------------------------------

    raise ValueError(
        "Unsupported resume format.\n"
        "Supported formats: .docx"
    )


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    path = input("Resume Path: ").strip()

    try:

        text = read_resume(path)

        print()
        print("=" * 60)
        print("Resume Loaded Successfully")
        print("=" * 60)

        print(text[:1000])

    except Exception as error:

        print()
        print("❌", error)