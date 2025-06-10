# Test Django Project with SQLite

This project is Django application with SQLite database  for creating threads with messages.

For quick setup and easy test use management commands via a Makefile.

---

## 🚀 Quick Start

- download project
```bash
  git clone git@github.com:KostiaMakh/isi_test.git
```
- put `.env` to the project root
- run command
```bash
  make start
```

Make sure you have installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- GNU Make

---

## 📦 Available Makefile Commands

All commands listed below are executed using:
---

### ▶️ Start project

```bash
  make start
```
Build and run the Docker containers for the project.

Automatically create superuser with default login and password set `.env`
To specify custom superuser `email` and `password` specify `DEFAULT_SUPERUSER_EMAIL` and `DEFAULT_SUPERUSER_PASSWORD` in the `.env`

---

### ⏹️ Stop project

```bash
  make down
```
Stop and remove all running Docker containers.

---

### 🔁 Rebuild project

```bash
  make build
```
Rebuild the Docker image for the application.

---

### 📜 View logs

```bash
  make logs
```
Show real-time logs from the Docker containers.

---

### 💻 Open container shell

```bash
  make shell
```
Open an interactive Bash shell inside the running app container.

---

### 🧱 Make migrations

```bash
  make makemigrations
```
Run Django’s `makemigrations` to create migration files for model changes.

---

### 🧩 Apply migrations

```bash
  make migrate
```
Run Django’s `migrate` to apply database schema changes.

---

### 👤 Create superuser

```bash
  make createsuperuser
```
Launch Django’s CLI wizard to create an admin superuser.

---

### 💾 Create database dump

```bash
  make create_dump
```
Dump the current state of the database to `test_db/dump.json`.  
The container starts temporarily if not already running.

---

### 📥 Load database dump

```bash
  make load_dump
```
Load data from `test_db/dump.json` into the database.  
The container starts temporarily if not already running.

---

## 🛠 Data Management Notes

- Dump file is saved to `test_db/dump.json`
- `create_dump` and `load_dump` automatically start/stop the container if needed
- Content types and permission tables are excluded from the dump for portability
- Ensure `test_db/` directory exists before dumping or loading

---