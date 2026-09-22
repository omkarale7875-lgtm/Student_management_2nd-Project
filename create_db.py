import sqlite3

from certifi import where

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()

    # Course Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS course (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        duration text,
        charges text,
        description text
    )
    """)
    con.commit()

    # Student Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        email text,
        gender text,
        dob text,
        contact text,
        admission text,
        course text,
        state text,
        city text,
        pin text,
        address text
    )
    """)
    con.commit()

    # Result Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result (
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll text,
        name text,
        course text,
        marks_ob text,
        full_marks text,
        per text
    )
    """)
    con.commit()

    # Employee / User Table (for Authentication)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name text,
        l_name text,
        contact text,
        email text,
        question text,
        answer text,
        password text
    )
    """)
    con.commit()

    con.close()
    print("Database and tables created successfully.")

   

if __name__ == "__main__":
    create_db()

