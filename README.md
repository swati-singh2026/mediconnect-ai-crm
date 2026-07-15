# 🩺 MediConnect AI CRM

AI-first Healthcare Professional (HCP) CRM platform powered by **React, FastAPI, LangGraph, LangChain, and Groq LLM**.

---

# 🚀 Project Overview

MediConnect AI CRM is an AI-powered Customer Relationship Management system designed for Healthcare Professionals (HCPs). It enables medical representatives to log interactions, manage doctors, and leverage AI to generate summaries and recommendations.

---

# 🛠 Tech Stack

## Frontend

- React
- Redux Toolkit
- Tailwind CSS _(Planned)_

## Backend

- FastAPI
- SQLAlchemy
- SQLite _(Development)_
- Pydantic
- Uvicorn

## AI

- LangChain
- LangGraph
- Groq LLM (Gemma2-9B-IT)

---

# 📂 Project Structure

```
mediconnect-ai-crm/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── config/
│   │   ├── core/
│   │   ├── database/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tools/
│   │   └── main.py
│   │
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   └── mediconnect.db
│
├── frontend/
├── README.md
└── PROJECT_NOTES.md
```

---

# ✨ Features

## Current

- ✅ FastAPI Backend
- ✅ SQLAlchemy Integration
- ✅ SQLite Database
- ✅ Interaction CRUD APIs
- ✅ Swagger Documentation
- ✅ Environment Configuration

## Planned

- 🤖 AI Chat Assistant
- 🧠 AI Interaction Summary
- 👨‍⚕️ HCP Management
- 📅 Interaction Timeline
- 📊 Dashboard & Analytics
- 🔐 Authentication

---

# 📌 API Endpoints

| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| GET    | `/`                  | Health Check         |
| POST   | `/interactions/`     | Create Interaction   |
| GET    | `/interactions/`     | Get All Interactions |
| PUT    | `/interactions/{id}` | Update Interaction   |

---

# 📈 Development Progress

## ✅ Hour 1

- Project setup
- Backend architecture
- FastAPI configuration
- LangChain installation
- LangGraph installation
- Groq SDK installation

## ✅ Hour 2

- SQLAlchemy setup
- SQLite integration
- Interaction model
- CRUD APIs
- Swagger API testing

## ⏳ Upcoming

- Groq API Integration
- LangGraph Workflow
- AI Agent
- React Frontend
- Dashboard UI

---

# 📄 License

This project is being developed for learning, portfolio, and demonstration purposes.
