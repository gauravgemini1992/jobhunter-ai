from typing import Dict, List


class SectionParser:

    @staticmethod
    def split_sections(
        lines: List[str],
        section_headers: Dict[str, List[str]],
        clean_line,
    ) -> Dict[str, List[str]]:

        sections = {
            "requirements": [],
            "responsibilities": [],
            "education": [],
            "experience": [],
            "other": [],
        }

        current = "other"

        for raw in lines:

            line = clean_line(raw)

            if not line:
                continue

            lower = line.lower()

            matched = False

            for name, headers in section_headers.items():

                if lower in headers:
                    current = name
                    matched = True
                    break

            if matched:
                continue

            sections[current].append(line)

        return sections
