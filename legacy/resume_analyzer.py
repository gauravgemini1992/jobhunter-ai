from resume_reader import read_resume
from resume_parser import parse_resume

from app.data.skills import SKILLS
from app.data.skill_weights import SKILL_WEIGHTS
from app.engines.smart_skill_matcher import SmartSkillMatcher


def analyze_resume():

    matcher = SmartSkillMatcher()

    try:
        resume_text = read_resume("resume.docx").lower()
        resume = parse_resume("resume.docx")

    except FileNotFoundError:
        print("❌ resume.docx not found.")
        return

    personal = resume["personal"]
    experience = resume["experience"]
    education = resume["education"]
    resume_skills = resume["skills"].lower()

    combined_text = f"{resume_text}\n{resume_skills}"

    print()
    print("=" * 70)
    print("                    RESUME INFORMATION")
    print("=" * 70)

    print(f"👤 Name        : {personal.name}")
    print(f"📧 Email       : {personal.email}")
    print(f"📱 Phone       : {personal.phone}")
    print(f"💼 Experience  : {len(experience)} Positions")
    print(f"🎓 Education   : {education}")

    print()

    print("=" * 70)
    print("                AI RESUME ANALYSIS REPORT")
    print("=" * 70)

    total_weight = 0
    matched_weight = 0

    for category, skill_list in SKILLS.items():

        found = []
        missing = []

        category_total = 0
        category_matched = 0

        print()
        print(f"📂 {category}")
        print("-" * 70)

        for skill in skill_list:

            weight = SKILL_WEIGHTS.get(skill.lower(), 5)

            total_weight += weight
            category_total += weight

            if matcher.match(combined_text, skill):

                found.append((skill, weight))

                matched_weight += weight
                category_matched += weight

            else:

                missing.append((skill, weight))

        percent = round((category_matched / category_total) * 100) if category_total else 0

        print(
            f"Matched Score : {category_matched} / {category_total} ({percent}%)"
        )

        if found:

            print("\n✅ Skills Found")

            for skill, weight in found:
                print(f"✔ {skill} ({weight} pts)")

        if missing:

            print("\n❌ Missing Skills")

            for skill, weight in missing:
                print(f"✘ {skill} ({weight} pts)")

    score = round((matched_weight / total_weight) * 100) if total_weight else 0

    print()
    print("=" * 70)
    print(f"🎯 Weighted ATS Score : {score}%")
    print("=" * 70)

    if score >= 90:
        print("★★★★★ Excellent Resume")

    elif score >= 75:
        print("★★★★☆ Very Good Resume")

    elif score >= 60:
        print("★★★☆☆ Good Resume")

    elif score >= 40:
        print("★★☆☆☆ Average Resume")

    else:
        print("★☆☆☆☆ Needs Improvement")

    print()

    print("=" * 70)
    print("WORK EXPERIENCE")
    print("=" * 70)

    for i, job in enumerate(experience, start=1):

        print(f"\n{i}. {job.designation}")
        print(f"   Company : {job.company}")
        print(f"   Duration: {job.duration}")

    print()