# 🧠 Smart Deal Tracker

Telegram bot + FastAPI backend for tracking the best deals, sales, and crypto drops in real time.

## 🚀 Features
- Asynchronous scraping (Steam, EpicGames, Amazon, etc.)
- PostgreSQL + SQLAlchemy
- REST API (FastAPI)
- Telegram notifications via Aiogram
- Dockerized deployment

## 🛠 Installation
```bash
git clone https://github.com/<your-username>/smart-deal-tracker
cd smart-deal-tracker
cp .env.example .env
docker-compose up --build
