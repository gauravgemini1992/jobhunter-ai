from datetime import datetime


class ReportGenerator:

    def __init__(self, report, job):

        self.report = report
        self.job = job

    def stars(self, score):

        if score >= 90:
            return "★★★★★"

        if score >= 75:
            return "★★★★☆"

        if score >= 60:
            return "★★★☆☆"

        if score >= 40:
            return "★★☆☆☆"

        return "★☆☆☆☆"

    def print_report(self):

        print()
        print("=" * 75)
        print("                 JOBHUNTER AI ATS REPORT")
        print("=" * 75)

        print(f"Generated : {datetime.now().strftime('%d %b %Y %I:%M %p')}")

        print()

        print(f"Job Title : {self.job['job_title']}")
        print(f"Experience Required : {self.job['experience_required']} Years")

        print()

        print("-" * 75)

        overall = self.report["overall_score"]

        print(f"Overall ATS Score : {overall}% {self.stars(overall)}")

        print()

        exp = self.report["experience_match"]["score"]

        print(f"Experience Match : {exp}% {self.stars(exp)}")

        skill = self.report["skill_match"]["score"]

        print(f"Skills Match     : {skill}% {self.stars(skill)}")

        edu = self.report["education_score"]

        print(f"Education Match  : {edu}% {self.stars(edu)}")

        print()

        print("-" * 75)

        print("Matched Skills")

        print("-" * 75)

        matched = self.report["skill_match"]["matched"]

        if matched:

            for item in matched:
                print(f"✔ {item}")

        else:

            print("None")

        print()

        print("-" * 75)

        print("Missing Skills")

        print("-" * 75)

        missing = self.report["skill_match"]["missing"]

        if missing:

            for item in missing:
                print(f"✘ {item}")

        else:

            print("None")

        print()

        print("-" * 75)

        print("Recommendation")

        print("-" * 75)

        print(self.report["recommendation"])

        print()

        print(f"Interview Probability : {self.report['interview_probability']}%")

        print("=" * 75)