from typing import List


def percentage(matched: int, total: int) -> int:
    if total == 0:
        return 100

    return round((matched / total) * 100)


def overall_score(
    skill: int,
    experience: int,
    education: int,
    responsibility: int,
    keyword: int,
) -> int:

    return round(
        (
            skill * 0.40
            + experience * 0.20
            + education * 0.10
            + responsibility * 0.20
            + keyword * 0.10
        )
    )


def strengths(skills: List[str]) -> List[str]:
    return sorted(skills)


def weaknesses(skills: List[str]) -> List[str]:
    return sorted(skills)