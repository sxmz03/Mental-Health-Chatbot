# Mental Health Chatbot — Therabuddy

A desktop chatbot application built with Python and Tkinter that supports users' mental wellbeing by tracking moods and delivering personalised feedback via SMS.

## Overview

Therabuddy is a GUI-based mental health support tool. Users create accounts, log in, and interact with the chatbot to track their mood. The app integrates SMS messaging to send supportive feedback directly to the user's phone.

## Features

- Tkinter GUI with a clean login and account creation flow
- Secure account system — credentials checked against stored records
- Mood tracking and personalised chatbot responses
- SMS delivery of feedback via phone number integration
- Modular codebase — each screen is a separate module

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Tkinter | Desktop GUI |
| SMS API | Delivering feedback messages to users |

## Application Flow

```
Login Page
  ├── Existing user → Phone verification → Chatbot
  └── New user → Create Account → Chatbot

Chatbot
  └── Mood tracking → Personalised response → SMS feedback
```

## Setup

```bash
pip install tkinter
```

> Tkinter is included with most Python distributions. If using the SMS feature, configure your SMS provider credentials in `phonenumber.py`.

Run the application:

```bash
python main.py
```

## Files

| File | Description |
|------|-------------|
| `main.py` | Entry point — login page |
| `createaccount.py` | Account registration screen |
| `phonenumber.py` | Phone number entry and SMS integration |
| `chatbot.py` | Core chatbot logic and mood tracking |
| `details.py` | User details handling |
| `createmessage.py` | SMS message construction |
| `wrongusername.py` | Error screen for invalid login |
| `takenusername.py` | Error screen for duplicate usernames |
