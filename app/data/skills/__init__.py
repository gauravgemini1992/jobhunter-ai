"""
JobHunter AI Skills Database
Master Loader
"""

from .ai import AI_SKILLS
from .programming import PROGRAMMING_SKILLS
from .frontend import FRONTEND_SKILLS
from .backend import BACKEND_SKILLS
from .mobile import MOBILE_SKILLS
from .cloud import CLOUD_SKILLS
from .devops import DEVOPS_SKILLS
from .database import DATABASE_SKILLS
from .analytics import ANALYTICS_SKILLS
from .cybersecurity import CYBERSECURITY_SKILLS
from .customer_success import CUSTOMER_SUCCESS_SKILLS
from .crm import CRM_SKILLS
from .sales import SALES_SKILLS
from .business import BUSINESS_SKILLS
from .project_management import PROJECT_MANAGEMENT_SKILLS
from .marketing import MARKETING_SKILLS
from .finance import FINANCE_SKILLS
from .hr import HR_SKILLS
from .erp import ERP_SKILLS
from .softskills import SOFT_SKILLS

SKILLS = {}

for module in (
    AI_SKILLS,
    PROGRAMMING_SKILLS,
    FRONTEND_SKILLS,
    BACKEND_SKILLS,
    MOBILE_SKILLS,
    CLOUD_SKILLS,
    DEVOPS_SKILLS,
    DATABASE_SKILLS,
    ANALYTICS_SKILLS,
    CYBERSECURITY_SKILLS,
    CUSTOMER_SUCCESS_SKILLS,
    CRM_SKILLS,
    SALES_SKILLS,
    BUSINESS_SKILLS,
    PROJECT_MANAGEMENT_SKILLS,
    MARKETING_SKILLS,
    FINANCE_SKILLS,
    HR_SKILLS,
    ERP_SKILLS,
    SOFT_SKILLS,
):
    SKILLS.update(module)