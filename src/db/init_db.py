import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

create_table_query = """
CREATE TABLE IF NOT EXISTS submissions (
    id SERIAL PRIMARY KEY,
    Age VARCHAR(10),
    Accessibility VARCHAR(10),
    EdLevel VARCHAR(50),
    Gender VARCHAR(10),
    MentalHealth VARCHAR(50),
    MainBranch VARCHAR(50),
    YearsCode INT,
    YearsCodePro INT,
    Country VARCHAR(50),
    PreviousSalary FLOAT,
    ComputerSkills INT,
    Skill_JavaScript INT,
    Skill_Docker INT,
    Skill_HTML_CSS INT,
    Skill_SQL INT,
    Skill_Git INT,
    Skill_AWS INT,
    Skill_Python INT,
    Skill_PostgreSQL INT,
    Skill_MySQL INT,
    Skill_TypeScript INT,
    Skill_Node_js INT,
    Skill_React_js INT,
    Skill_Java INT,
    Skill_Bash_Shell INT,
    Skill_CSharp INT,
    Skill_Microsoft_SQL_Server INT,
    Skill_SQLite INT,
    Skill_jQuery INT,
    Skill_Microsoft_Azure INT,
    Skill_MongoDB INT,
    Employed INT
);
"""

if __name__ == "__main__":
    try:
        print('database_url:', DATABASE_URL)
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("✅ Table created successfully (or already exists).")
    except Exception as e:
        print(f"❌ Error creating table: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
