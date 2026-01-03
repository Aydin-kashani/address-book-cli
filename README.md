# Simple Address Book (CLI) — Python

**Version:** 0.1.0

A simple command-line address book built with Python.  
It allows you to store contacts with details such as **first name**, **last name**, **phone number**, **email address**, and **notes**, 
then manage them using basic actions like **viewing**, **searching**, and **deleting**.

---

## Why I built this
I built this project to practice working with a simple data model (contacts) and a complete CLI flow.
It also helped me get used to writing a program that can be extended later (validation, search improvements, saving to file).

## What I learned
- How to structure a small CLI project with clear actions (add / view / search / delete)
- How to think about data fields (name, phone, email, notes) and keep things organized
- How to plan improvements like JSON storage, better search, and cleaner code

---

## What this project does

This educational CLI project supports the following actions:

- **Add a contact**
- **View contacts**
- **Search contacts**
- **Delete a contact**
- **Exit the program**

---

## How to run

Make sure you have Python 3 installed.

After starting the program, you’ll see a text-based menu.
Choose an option by entering its number and follow the prompts.

Run the script:

```bash
python address-book.py
```
---

## Features (current version)

The current version includes:

- Add contact
- Show contacts
- Search contact
- Delete contact
- Exit program

---

## Requirements

- Python 3.x
- No external libraries required

---

## Roadmap (Future improvements)

- Planned improvements for upcoming versions:
- Delete confirmation (ask before removing a contact)
- Partial search (match even with one character / substring search)
- Input validation (prevent saving empty required fields)
- Sorted display (show contacts sorted by first name)
- Edit contact (update an existing contact after saving)
- Persistent storage (save/load contacts using a JSON file)
- Refactor & cleanup (simplify logic and reduce unnecessary lines)
- Optional: GUI version (a small graphical version later)

---

### Known Issues

- Empty input handling: in some cases, submitting empty fields may still cause unexpected behavior.
- Error handling: some invalid inputs are not handled gracefully yet and may produce unclear messages.

---

## Technologies used

- Language: Python
- IDE: Spyder

---

## Project status

This is the first version of the program.
I built it as a learning project while studying Python and basic programming concepts. The code is intentionally simple and still has a lot of room to grow. 
I plan to improve it step by step as I learn more and add better structure, validation, and persistence.

## Version history

- v0.1.0 — Initial release
