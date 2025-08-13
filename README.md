# 🐞 Defect Management System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![Database](https://img.shields.io/badge/Database-MySQL-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A **full-stack web application** for tracking and managing software defects efficiently.  
Built with **Django**, this system enables **teams** to log, assign, and resolve defects in a structured workflow.

---

## 📌 Features
- **Role-based access** (Manager, Developer)
- **Create, view, and update defects**
- **Status tracking**: Pending, In-Progress, Resolved
- **Search and filter defects**
- **Responsive UI** with Bootstrap 5
- **Database** sqlite3
- **nontification** Email notifications on defect assignment

---

## 🛠 Tech Stack
| Technology | Purpose |
|------------|---------|
| Python     | Backend logic |
| Django     | Web framework |
| sqlite3    | Database |
| HTML, CSS, Bootstrap | Frontend styling |
| Git & GitHub | Version control |

---

## 📂 Project Structure
```plaintext
Defect_management_system/
│── defects/           # Main app
│── static/            # CSS, JS, images
│── templates/         # HTML templates
│── screenshots/       # App screenshots
│── manage.py
│── README.md


## 📷 Screenshots

> Below are some screenshots showcasing the application's main features and UI.

### 1️⃣ Login Page  
![Login Page](screenshots/Screenshot%202025-08-13%20232542.png)

### 2️⃣ Dashboard View  
![Dashboard](screenshots/Screenshot%202025-08-13%20232609.png)

### 3️⃣ All Defects List  
![All Defects](screenshots/Screenshot%202025-08-13%20232633.png)

### 4️⃣ Pending Defects Page  
![Pending Defects](screenshots/Screenshot%202025-08-13%20232653.png)

### 5️⃣ Add Defect Form  
![Add Defect](screenshots/Screenshot%202025-08-13%20232708.png)

### 6️⃣ Completed Defects Page  
![Completed Defects](screenshots/Screenshot%202025-08-13%20232721.png)

---
🚀 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Defect_management_system.git
cd Defect_management_system
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
