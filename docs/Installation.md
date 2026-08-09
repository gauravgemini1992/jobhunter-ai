# ⚙️ Installation Guide

---

# Introduction

This guide explains how to install and run **JobHunter AI** on your local machine.

The application is developed in Python and currently runs as a Command Line Interface (CLI).

---

# System Requirements

Minimum Requirements

- Python 3.10 or later
- Git
- pip
- macOS, Linux or Windows

Recommended

- Visual Studio Code
- Cursor IDE
- Python Extension

---

# Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/JobHunter-AI.git
```

Move into the project.

```bash
cd JobHunter-AI
```

---

# Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

---

# Verify Installation

Verify the Python installation.

```bash
python3 --version
```

Expected output

```text
Python 3.10+
```

---

# Project Structure

```text
JobHunter-AI/

├── app/
├── assets/
├── docs/
├── output/
├── sample_data/
├── tests/
├── main.py
├── version.py
└── requirements.txt
```

---

# Running the Application

Launch JobHunter AI.

```bash
python3 main.py
```

The application starts with:

```
🚀 JobHunter AI
```

---

# Available Modules

Version 1.0 includes:

- Resume Review
- ATS Engine
- Resume Optimizer
- Job Finder
- Company Research

---

# Sample Files

Use the files inside:

```text
sample_data/
```

to test the application.

---

# Updating Dependencies

Upgrade installed packages.

```bash
pip install --upgrade -r requirements.txt
```

---

# Troubleshooting

## Python Not Found

Verify Python installation.

```bash
python3 --version
```

---

## Module Import Error

Install dependencies again.

```bash
pip install -r requirements.txt
```

---

## Permission Error

Use a virtual environment.

```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

# Future Installation

Future releases will provide:

- Windows Installer
- macOS Package
- Docker Image
- Web Deployment
- Cloud Deployment

---

# Version

Installation Guide Version **1.0.0**