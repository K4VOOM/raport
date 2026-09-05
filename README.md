# Raport

🇺🇦 [Українська](#українська) | 🇬🇧 [English](#english)

---

## Українська

Десктопний застосунок на **PySide6** для ведення списку особового складу (рапорту). Дозволяє додавати, переглядати та видаляти бійців із зазначенням ПІБ і звання. Дані зберігаються локально в базі даних **SQLite**, тож список не втрачається після закриття програми.

### Функціонал

- 📋 Перегляд списку бійців у головному вікні
- ➕ Додавання нового бійця через окреме діалогове вікно (ПІБ + звання зі списку)
- ➖ Видалення обраного бійця зі списку
- 💾 Автоматичне збереження всіх змін у базі даних SQLite
- 🔄 Автоматичне завантаження збережених даних при запуску програми

### Встановлення

#### 1. Клонувати репозиторій

```bash
git clone https://github.com/K4VOOM/raport.git
cd raport
```

#### 2. Створити віртуальне середовище

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

#### 3. Встановити залежності

```bash
pip install -r requirements.txt
```

#### 4. Запустити застосунок

```bash
python main.py
```

### Структура проєкту

```
raport/
├── .venv/                  # віртуальне середовище (не в репозиторії)
├── data/                   # база даних SQLite (raport.db)
├── src/                    # логіка застосунку
│   ├── database.py         # робота з базою даних
│   └── add_dialog.py       # логіка діалогового вікна додавання
├── ui/                     # вихідні файли Qt Designer
│   ├── main.ui
│   └── dialog.ui
├── ui_generated/           # згенеровані з .ui файли (pyside6-uic)
│   ├── ui_form.py
│   └── ui_dialog.py
├── .gitignore
├── main.py                 # точка входу в застосунок
├── requirements.txt        # залежності проєкту
└── README.md
```

### Технології

- [Python 3](https://www.python.org/)
- [PySide6](https://doc.qt.io/qtforpython/) — GUI-фреймворк (Qt для Python)
- [SQLite](https://www.sqlite.org/) — вбудована база даних (через модуль `sqlite3`)

---

## English

A desktop application built with **PySide6** for managing a personnel roster. It allows adding, viewing, and removing soldiers along with their full name and rank. Data is stored locally in an **SQLite** database, so the list persists after closing the app.

### Features

- 📋 View the list of soldiers in the main window
- ➕ Add a new soldier via a separate dialog window (full name + rank from a dropdown)
- ➖ Remove a selected soldier from the list
- 💾 Automatically saves all changes to the SQLite database
- 🔄 Automatically loads saved data on app startup

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/K4VOOM/raport.git
cd raport
```

#### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the application

```bash
python main.py
```

### Project Structure

```
raport/
├── .venv/                  # virtual environment (not in the repository)
├── data/                   # SQLite database (raport.db)
├── src/                    # application logic
│   ├── database.py         # database operations
│   └── add_dialog.py       # add-soldier dialog logic
├── ui/                     # Qt Designer source files
│   ├── main.ui
│   └── dialog.ui
├── ui_generated/           # generated from .ui files (pyside6-uic)
│   ├── ui_form.py
│   └── ui_dialog.py
├── .gitignore
├── main.py                 # application entry point
├── requirements.txt        # project dependencies
└── README.md
```

### Tech Stack

- [Python 3](https://www.python.org/)
- [PySide6](https://doc.qt.io/qtforpython/) — GUI framework (Qt for Python)
- [SQLite](https://www.sqlite.org/) — built-in database (via the `sqlite3` module)

test