from pydantic import BaseModel

class UserProfileBase(BaseModel):
    Age: str
    Accessibility: str
    EdLevel: str
    Gender: str
    MentalHealth: str
    MainBranch: str
    YearsCode: int
    YearsCodePro: int
    Country: str
    PreviousSalary: float
    ComputerSkills: int
    Skill_JavaScript: int = 0
    Skill_Docker: int = 0
    Skill_HTML_CSS: int = 0
    Skill_SQL: int = 0
    Skill_Git: int = 0
    Skill_AWS: int = 0
    Skill_Python: int = 0
    Skill_PostgreSQL: int = 0
    Skill_MySQL: int = 0
    Skill_TypeScript: int = 0
    Skill_Node_js: int = 0
    Skill_React_js: int = 0
    Skill_Java: int = 0
    Skill_Bash_Shell: int = 0
    Skill_CSharp: int = 0
    Skill_Microsoft_SQL_Server: int = 0
    Skill_SQLite: int = 0
    Skill_jQuery: int = 0
    Skill_Microsoft_Azure: int = 0
    Skill_MongoDB: int = 0

class UserProfileWithEmployment(UserProfileBase):
    Employed: int  # 0 or 1
