from app.data.skill_families import SKILL_FAMILIES


ALL_SKILLS = sorted(

    {

        skill

        for family in SKILL_FAMILIES.values()

        for skill in family

    },

    key=len,

    reverse=True,

)