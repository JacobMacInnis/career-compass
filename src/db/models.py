from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class UserEntry(Base):
    __tablename__ = 'user_entries'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

    # Input fields
    Age = Column(String)
    Accessibility = Column(String)
    EdLevel = Column(String)
    Gender = Column(String)
    MentalHealth = Column(String)
    MainBranch = Column(String)
    YearsCode = Column(Integer)
    YearsCodePro = Column(Integer)
    Country = Column(String)
    PreviousSalary = Column(Float)
    ComputerSkills = Column(Integer)
    Skill_JavaScript = Column(Integer)
    Skill_Docker = Column(Integer)
    Skill_HTML_CSS = Column(Integer)
    Skill_SQL = Column(Integer)
    Skill_Git = Column(Integer)
    Skill_AWS = Column(Integer)
    Skill_Python = Column(Integer)
    Skill_PostgreSQL = Column(Integer)
    Skill_MySQL = Column(Integer)
    Skill_TypeScript = Column(Integer)
    Skill_Node_js = Column(Integer)
    Skill_React_js = Column(Integer)
    Skill_Java = Column(Integer)
    Skill_Bash_Shell = Column(Integer)
    Skill_CSharp = Column(Integer)
    Skill_Microsoft_SQL_Server = Column(Integer)
    Skill_SQLite = Column(Integer)
    Skill_jQuery = Column(Integer)
    Skill_Microsoft_Azure = Column(Integer)
    Skill_MongoDB = Column(Integer)

    Employed = Column(Integer)  # Ground truth label
