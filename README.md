# 🩺 MediConnect AI CRM

An AI-first Healthcare Professional (HCP) CRM platform built using **React, FastAPI, LangGraph, LangChain, Redux Toolkit, and Groq LLM**.

---

# 🚀 Project Overview

MediConnect AI CRM enables medical representatives to record doctor interactions, manage HCP engagement, and leverage AI to summarize conversations, retrieve interaction history, and generate intelligent follow-up recommendations.

---

# 🏗 Architecture

```
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
LangGraph Workflow
      │
      ▼
AI Tools
      │
      ▼
SQLite Database
```

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Redux Toolkit
- React Router
- Tailwind CSS

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## AI

- LangChain
- LangGraph
- Groq LLM (Llama 3.1 8B Instant)

---

# 📂 Folder Structure

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
│   │   ├── graph/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tools/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env.example
│   └── mediconnect.db
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── features/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── store/
│   │   └── App.tsx
│
├── README.md
└── PROJECT_NOTES.md
```

---

# 🤖 How LangGraph Works

The AI workflow is implemented using LangGraph.

```
User Input
      │
      ▼
Intent Detection
      │
      ▼
Router
      │
      ▼
Selected Tool
      │
      ▼
Response
```

Current workflow includes:

- Intent Detection
- Intent Routing
- Tool Execution
- Response Generation

---

# ▶️ How to Run

## Backend

```bash
cd backend

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 📌 API Endpoints

| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| GET    | `/`                  | Health Check         |
| POST   | `/interactions/`     | Create Interaction   |
| GET    | `/interactions/`     | Get All Interactions |
| PUT    | `/interactions/{id}` | Update Interaction   |
| POST   | `/ai/summary`        | Generate AI Summary  |

---

# 🧰 AI Tools

The application currently includes five AI tools.

### 1. Log Interaction

Logs doctor interactions and extracts structured information.

### 2. Edit Interaction

Updates existing interaction details.

### 3. Search Interaction

Retrieves previous interaction history.

### 4. Summarize HCP

Generates an overall summary of doctor interactions.

### 5. Generate Follow-up

Suggests:

- Next Action
- Questions to Ask
- Material to Carry

---

# 📈 Development Progress

## ✅ Project Foundation

- Project setup
- Git repository initialization
- Frontend and backend architecture
- Environment configuration
- Project documentation

---

## ✅ Backend Development

- FastAPI application
- SQLAlchemy integration
- SQLite database
- CRUD APIs
- Swagger documentation
- Pydantic schemas

---

## ✅ AI Integration

- Groq LLM integration
- LangChain prompt templates
- AI interaction summary service
- Healthcare CRM AI assistant

---

## ✅ Frontend Development

- React application
- TypeScript setup
- Tailwind CSS
- HCP Interaction page
- Structured interaction form
- AI Chat interface

---

## ✅ LangGraph Workflow

- Graph state
- Intent detection
- Router
- Tool execution
- Response generation

---

## ✅ AI Tooling

- Log Interaction
- Edit Interaction
- Search Interaction
- Summarize HCP
- Generate Follow-up

---

## ✅ State Management

- Redux Toolkit
- Interaction slice
- Current chat state
- Loading state
- Error handling

---

## 🚀 Upcoming

- Connect frontend with backend APIs
- Integrate LangGraph tools with live database
- Authentication & authorization
- Dashboard and analytics
- Deployment

---

# 📄 License

This project is developed for learning, portfolio, and demonstration purposes.
