# 🩺 MediConnect AI CRM

AI-first Healthcare Professional (HCP) CRM platform powered by **React, FastAPI, LangChain, LangGraph, and Groq LLM**.

---

# 🚀 Project Overview

MediConnect AI CRM is an AI-powered Customer Relationship Management system designed for Healthcare Professionals (HCPs). It enables medical representatives to manage doctor interactions, maintain CRM records, and leverage AI to generate professional interaction summaries and follow-up recommendations.

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
- Groq LLM (Llama 3.1 8B Instant)

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
- ✅ AI Interaction Summary API
- ✅ Groq LLM Integration
- ✅ LangChain Prompt Templates
- ✅ Healthcare CRM AI Service
- ✅ Swagger Documentation
- ✅ Environment Configuration

## Planned

- 🤖 AI Chat Assistant
- 👨‍⚕️ HCP Management
- 📅 Interaction Timeline
- 📊 Dashboard & Analytics
- 🔐 Authentication
- 🌐 React Frontend
- 🔄 LangGraph Multi-Agent Workflow

---

# 📌 API Endpoints

| Method | Endpoint             | Description                     |
| ------ | -------------------- | ------------------------------- |
| GET    | `/`                  | Health Check                    |
| POST   | `/interactions/`     | Create Interaction              |
| GET    | `/interactions/`     | Get All Interactions            |
| PUT    | `/interactions/{id}` | Update Interaction              |
| POST   | `/ai/summary`        | Generate AI Interaction Summary |

---

# 🤖 AI Summary Response

The AI generates structured healthcare CRM summaries including:

- Professional Summary
- Next Action
- Priority Level
- Suggested Follow-up

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

## ✅ Hour 3

- Groq API integration
- LangChain ChatGroq configuration
- Prompt engineering
- AI Service implementation
- AI Interaction Summary API
- Healthcare CRM AI assistant

---

# 🚀 Upcoming

- React Frontend
- Dashboard UI
- LangGraph Workflow
- Multi-Agent AI System
- Authentication
- Deployment

---

# 📄 License

This project is being developed for learning, portfolio, and demonstration purposes.
