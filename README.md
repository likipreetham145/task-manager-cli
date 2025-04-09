# 📝 Task Manager CLI

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple and powerful command-line tool to manage tasks efficiently — add priorities, due dates, and keep your productivity on track, all using Python and SQLite.

---

## 📚 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Preview](#-preview)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features

- ➕ Add tasks with optional `--priority` and `--due` date
- 📋 List all tasks with their status, priority, and due date
- ✅ Mark tasks as complete
- 🗑️ Delete tasks by ID
- 💾 Stores everything locally in a lightweight SQLite database

---

## 🛠️ Installation

### Requirements
- Python 3.10 or higher

### Clone the Repository


git clone https://github.com/likipreetham145/task-manager-cli.git
cd task-manager-cli

🚦 Usage
➕ Add a Task

python main.py add "Buy groceries"
python main.py add "Submit application" --priority=High --due=2025-04-12

📋 List Tasks

python main.py list

✅ Complete a Task

python main.py complete <task_id>

🗑️ Delete a Task

python main.py delete <task_id>

📂 Project Structure

task-manager-cli/
├── main.py
├── db.py
├── task.py
├── utils.py
├── commands/
│   ├── add.py
│   ├── list.py
│   ├── complete.py
│   └── delete.py
├── tasks.db (auto-generated)
├── screenshots/
│   └── demo.png (optional)
├── LICENSE
└── README.md

🤝 Contributing
Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repo

2. Create your feature branch (git checkout -b feature/awesome-feature)

3. Commit your changes (git commit -m 'Add awesome feature')

4. Push to the branch (git push origin feature/awesome-feature)

5. Open a pull request

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
---

#### 💾 Step 3: Save and Push the Changes

In PowerShell:

```powershell
git add README.md
git commit -m "Update README with usage, structure, preview, and license"
git push
