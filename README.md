# 🧰 Multi-Utility ToolKit
### *Your All-in-One Python Powerhouse!*

---

## 📌 Project Overview

The **Multi-Utility ToolKit** is a Python-based console application that brings together the power of multiple built-in modules and a custom package into one easy-to-use, menu-driven interface. Whether you need to track time ⏱️, crunch numbers 🔢, generate passwords 🔐, create unique IDs 🆔, or manage files 📁 — this toolkit has you covered!

This project was built to demonstrate Python's modular structure, showcasing how standard libraries, custom modules, and packages can all work together seamlessly in one clean program.

---

## ✨ Features at a Glance

| 🔢 Option | 📋 Feature |
|-----------|------------|
| 1 | 🕒 Datetime & Time Operations |
| 2 | ➗ Mathematical Operations |
| 3 | 🎲 Random Data Generation |
| 4 | 🆔 Generate Unique Identifiers (UUID) |
| 5 | 📁 File Operations (Custom Module) |
| 6 | 🔍 Explore Module Attributes (dir()) |
| 7 | 🚪 Exit |

---

## 📂 Project Structure

```
Multi-Utility-ToolKit/
│
├── main.py                  # Main script — all functions + menu-driven interface
│
└── geometric_shaps/         # Custom package for geometric area calculations
    ├── __init__.py          # Initializes the package
    ├── circle.py            # Circle area calculator
    ├── rectangle.py         # Rectangle area calculator
    └── triangle.py          # Triangle area calculator
```

---

## 🛠️ Modules Used

### 🔧 Built-in Modules
| Module | Purpose |
|--------|---------|
| `datetime` | Date & time display, formatting, difference |
| `time` | Stopwatch and countdown timer |
| `math` | Factorial, trigonometry (sin, cos, tan) |
| `random` | Random numbers, lists, passwords, OTPs |
| `uuid` | Unique identifier generation (UUID4) |

### 📦 Custom Package
- **`geometric_shaps`** — A self-built Python package containing:
  - `circle.py` → calculates area using **π × r²**
  - `rectangle.py` → calculates area using **length × width**
  - `triangle.py` → calculates area using **½ × base × height**

---

## 🚀 How to Run

1. **Clone or download** this repository
2. Make sure **Python 3.10+** is installed
3. Ensure the `geometric_shaps/` folder is in the **same directory** as `main.py`
4. Open your terminal and run:

```bash
python main.py
```

---

## 📸 Program Walkthrough

### 🏠 Main Menu
When you run the program, you'll see the main menu with 7 options to choose from.


<img width="964" height="385" alt="Screenshot 2026-03-05 194156" src="https://github.com/user-attachments/assets/a5bb5679-5bcc-4ac5-99b8-bd2f15c3dd35" />

---

## 1️⃣ Datetime & Time Operations 🕒

A complete time management section using Python's `datetime` and `time` modules. From checking the current time to running a live stopwatch — it's all here!


<img width="890" height="336" alt="Screenshot 2026-03-05 194208" src="https://github.com/user-attachments/assets/cbd8a164-d127-4241-be52-b1e68a1fbb0b" />

---

### 📅 Display Current Date & Time
Shows the current date and time in a clean `YYYY-MM-DD HH:MM:SS` format.

<img width="774" height="315" alt="Screenshot 2026-03-05 194232" src="https://github.com/user-attachments/assets/b327e44f-a53a-4842-94b4-4904c3bc70e0" />

---

### 📆 Difference Between Two Dates
Enter any two dates (year, month, day) and the program calculates the exact number of days between them.

<img width="898" height="532" alt="Screenshot 2026-03-05 194323" src="https://github.com/user-attachments/assets/80970a33-c316-42aa-b051-7226be6711e3" />

---

### 🗓️ Format Date into Custom Format
Displays today's date formatted as **DD-MM-YYYY** using Python's `strftime`.


<img width="836" height="314" alt="Screenshot 2026-03-05 194346" src="https://github.com/user-attachments/assets/f6d8051b-37b4-41f9-a6dd-da9f3cb5f838" />

---

### ⏱️ Stopwatch
A fully working live stopwatch with **Start**, **Stop/Pause**, **Reset**, and **Quit** controls. The timer displays in real-time as `HH:MM:SS`.

> 💡 Tip: Press `Ctrl + C` to interrupt while the stopwatch is running!
le showing the live HH:MM:SS stopwatch display while running -->

<img width="979" height="832" alt="Screenshot 2026-03-05 194457" src="https://github.com/user-attachments/assets/204d076a-714e-48ab-9599-c78d7c7fb449" />

---

### ⏳ Countdown Timer
Enter the number of seconds and watch it count down live — finishing with a **"Time is up!"** message.


<img width="822" height="334" alt="Screenshot 2026-03-05 194548" src="https://github.com/user-attachments/assets/06b761a8-fc4a-4885-8c40-ab1c2643610a" />

---

## 2️⃣ Mathematical Operations ➗

A powerful math section using Python's built-in `math` module and the custom `geometric_shaps` package.

<img width="731" height="261" alt="Screenshot 2026-03-05 194651" src="https://github.com/user-attachments/assets/39bf90e3-caaf-4b9b-9a96-343bdfc2dda4" />


---

### 🔢 Factorial Calculator
Enter any number and get its factorial calculated using a loop.

<!-- 📷 SCREENSHOT: Console showing "Enter Number: 5" → "Factorial of given number: 120" -->
![Factorial]()

<img width="810" height="310" alt="Screenshot 2026-03-05 194715" src="https://github.com/user-attachments/assets/07756e93-196d-4083-84d1-d4046dda1264" />

---

### 💰 Compound Interest Calculator
Enter your **principal**, **interest rate (%)**, and **time in years** — and get your final compounded amount instantly.

<img width="769" height="313" alt="Screenshot 2026-03-05 194744" src="https://github.com/user-attachments/assets/51d3f793-6301-4826-b860-6fc812efe7cd" />

---

### 📐 Trigonometric Calculations
Enter any angle in **degrees** and get the **Sin**, **Cos**, and **Tan** values — computed using `math.radians()`.


<img width="848" height="318" alt="Screenshot 2026-03-05 194803" src="https://github.com/user-attachments/assets/265a2b03-3610-46cf-bd59-7fb383b4ff2e" />

---

### 🔷 Area of Geometric Shapes (Custom Package!)
Powered by our own `geometric_shaps` package! Choose a shape and enter dimensions to get the area.

- ⭕ **Circle** → Enter radius
- 🟦 **Rectangle** → Enter length & width
- 🔺 **Triangle** → Enter base & height

<img width="844" height="397" alt="Screenshot 2026-03-05 194831" src="https://github.com/user-attachments/assets/1f4697a2-9a50-4b55-8767-4b5df46c95d4" />

---

## 3️⃣ Random Data Generation 🎲

Generate all kinds of random data — from numbers to secure passwords and OTPs!

<img width="831" height="249" alt="Screenshot 2026-03-05 194857" src="https://github.com/user-attachments/assets/ecf02e89-4e57-43d2-8e09-831102a8bcea" />

---

### 🎯 Generate Random Number
Generates a random float number instantly using `random.random()`.

<img width="770" height="300" alt="Screenshot 2026-03-05 194911" src="https://github.com/user-attachments/assets/3de3a08a-59b8-47d8-8d43-990d1763fa5d" />

---

### 📋 Generate Random List
Generates a list of **10 random integers** between 1 and 100.

<img width="929" height="263" alt="Screenshot 2026-03-05 194925" src="https://github.com/user-attachments/assets/a9ad4052-1ff6-4ede-9c28-4ff67805b832" />

---

### 🔐 Random Password Generator
Enter your desired password length and get a strong password made from:
- 🔡 Lowercase letters (`a-z`)
- 🔠 Uppercase letters (`A-Z`)
- 🔢 Digits (`0-9`)
- 💠 Special symbols (`#@$!_%`)


<img width="816" height="289" alt="Screenshot 2026-03-05 195208" src="https://github.com/user-attachments/assets/b902101b-bc9b-4b57-b585-20e7766c2379" />

---

### 📟 Random OTP Generator
Generates a secure **6-digit One-Time Password** — just like the OTPs you receive on your phone!


<img width="892" height="265" alt="Screenshot 2026-03-05 195007" src="https://github.com/user-attachments/assets/203b7f27-c9a4-4aba-973c-47b7850fa040" />

---

## 4️⃣ Generate Unique Identifiers (UUID) 🆔

Uses Python's `uuid` module to instantly generate a **UUID4** — a globally unique identifier perfect for files, records, and user sessions.

<img width="884" height="413" alt="Screenshot 2026-03-05 195037" src="https://github.com/user-attachments/assets/01dcc31d-da91-4a43-9f1e-115f00dac154" />

---

## 5️⃣ File Operations 📁

A complete file management section for creating, writing, reading, and appending to text files.

<img width="755" height="263" alt="Screenshot 2026-03-05 205315" src="https://github.com/user-attachments/assets/902a7a22-f641-4446-90c9-21e661aecc76" />

---

### 📄 Create a New File
Automatically creates `First.txt` and writes an initial line into it — no input needed!


<img width="662" height="85" alt="Screenshot 2026-03-05 205443" src="https://github.com/user-attachments/assets/6140c08a-5502-401e-a0a0-2c730784589e" />

---

### ✍️ Write to a File
Enter a filename, choose how many lines to add, then type your content line by line — all saved neatly.

<img width="1002" height="424" alt="Screenshot 2026-03-05 205729" src="https://github.com/user-attachments/assets/e2a4b0e5-beab-4d5d-8a10-f68bcda78a47" />

---

### 👁️ Read from a File
Enter a filename and the program reads and displays its full contents. Shows a clean error message if the file isn't found.

<img width="1061" height="473" alt="Screenshot 2026-03-05 205758" src="https://github.com/user-attachments/assets/321c19d8-7dec-40b9-811d-b0598c8613bb" />

---

### ➕ Append to a File
Add new content to the end of any existing file — without erasing what's already saved inside.

<img width="936" height="299" alt="Screenshot 2026-03-05 205839" src="https://github.com/user-attachments/assets/1aa69dce-a07d-421c-aae5-af56448a09e0" />

---

## 6️⃣ Explore Module Attributes — dir() 🔍

Type in any Python module name and this feature dynamically lists all of its available attributes and functions using `dir()` — a great way to discover what any module can do!

> 💡 Try typing: `math`, `random`, `os`, `datetime`, `uuid`

<img width="1589" height="630" alt="Screenshot 2026-03-05 205250" src="https://github.com/user-attachments/assets/9b227536-5d58-48c4-8d15-242ad94991d1" />

---

## 7️⃣ Exit 🚪

Selecting option 7 ends the program with a clean goodbye message.


<img width="994" height="369" alt="Screenshot 2026-03-05 212016" src="https://github.com/user-attachments/assets/024d0920-d68b-4a05-9b3d-950361a85972" />

---

## 💡 Key Concepts Demonstrated

- ✅ **Built-in Module Usage** — `datetime`, `time`, `math`, `random`, `uuid`
- ✅ **Custom Package** — `geometric_shaps` with `__init__.py` and 3 sub-modules
- ✅ **`if __name__ == "__main__"`** — Clean separation of reusable functions from main execution
- ✅ **`match/case` Statements** — Python 3.10+ structural pattern matching for clean menus
- ✅ **`dir()` for Dynamic Exploration** — Explore any module's attributes at runtime
- ✅ **Menu-Driven UI** — Intuitive nested console navigation
- ✅ **File Handling** — Create, write, read, and append to `.txt` files
- ✅ **Error Handling** — `try/except FileNotFoundError` for safe file operations

---

## 👨‍💻 Author

**Rensee Gajipara**
📌 Python Developer | CLI Tool Builder
📌 Developed a Multi-Utility Python Toolkit using Python Standard Libraries
📌 Focused on modular programming, automation tools, and clean code practices

---

*"Quality is our Motto."* ⭐
