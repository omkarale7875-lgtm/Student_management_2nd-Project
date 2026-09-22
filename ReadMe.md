# Student Result Management System (SRMS) 🎓

A full-featured desktop GUI application built using **Python**, **Tkinter**, **SQLite3**, and **Pillow (PIL)**. This system simplifies managing student profiles, course registration, exam marks entry, and marksheet generation for educational institutions.

---

## 🌟 Key Features

- 🔐 **Employee Authentication & Recovery:** Secure login, registration, and password recovery via security questions.
- 📊 **Interactive Dashboard:** Live counts for total courses, students, and results along with a dynamic dynamic analog clock.
- 📚 **Course Management:** Add, update, view, and delete available institutional courses.
- 👨‍🎓 **Student Management:** Register and maintain detailed student profiles (Roll No, Email, Address, Course, etc.).
- 📝 **Automated Result Calculation:** Auto-calculates aggregate percentage scores based on obtained and full marks.
- 📑 **Report Generation & Search:** Instant search for student marksheets by roll number with print and delete capabilities.

---

## 🛠️ Tech Stack & Requirements

- **Python:** 3.x
- **GUI Engine:** Tkinter (`ttk`)
- **Database:** SQLite3 (`rms.db`)
- **Image Library:** Pillow (PIL)

---

## 📂 Project Structure

```text
├── images/          # Background images, icons, and dynamic clock assets
├── create_db.py     # Database initializer (Creates tables: employee, course, student, result)
├── register.py      # New user registration screen
├── login.py         # Login and password recovery interface
├── dashboard.py     # Main application dashboard
├── course.py        # Course CRUD management module
├── student.py       # Student profile management module
├── result.py        # Exam marks entry and percentage calculator
├── report.py        # Marksheet lookup and report management
└── rms.db           # SQLite database file
