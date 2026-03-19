# 🚀 AI-Powered Trade Opportunities API
<img width="1919" height="867" alt="Screenshot 2026-03-19 123514" src="https://github.com/user-attachments/assets/36fc010c-d641-4d5e-8476-015edb927491" />
<img width="1919" height="875" alt="Screenshot 2026-03-19 123546" src="https://github.com/user-attachments/assets/04360dcf-99ba-4c55-9826-4f661923138d" />
<img width="1919" height="877" alt="Screenshot 2026-03-19 123621" src="https://github.com/user-attachments/assets/735f7fb7-d387-4bcf-acba-f0a1485fa175" />
<img width="1918" height="872" alt="Screenshot 2026-03-19 123649" src="https://github.com/user-attachments/assets/bc8a079e-ed1f-4907-ac11-c8ab2581d386" />

## 📌 Overview

The AI-Powered Trade Opportunities API is a FastAPI-based backend service that analyzes market data for different sectors in India and generates AI-driven trade opportunity reports.

The API accepts a sector name (e.g., technology, pharmaceuticals, agriculture) and returns a structured **markdown report** containing insights such as market trends, opportunities, and risks.

This project demonstrates backend development, API design, AI integration, and production-level features like authentication and rate limiting.

---

## ⚙️ Features

- 🔍 Sector-based market analysis
- 🤖 AI-generated insights using Groq (LLaMA 3.1)
- 📄 Structured markdown reports
- 🔐 API key authentication
- 🚦 Rate limiting (5 requests per minute)
- ⚡ FastAPI with automatic Swagger documentation
- ❗ Error handling for external API failures

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI
- **Programming Language:** Python
- **AI Model:** Groq (LLaMA 3.1)
- **HTTP Requests:** Requests library
- **Rate Limiting:** SlowAPI

---

## 📂 Project Structure


trade-api/
│── main.py
│── README.md
│── requirements.txt


---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd trade-api
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install fastapi uvicorn requests groq slowapi
4️⃣ Add Your API Key

Open main.py and replace:

client = Groq(api_key="YOUR_GROQ_API_KEY")

with your actual Groq API key.

5️⃣ Run the Server
python -m uvicorn main:app --reload
🧪 API Usage
🔗 Base URL
http://127.0.0.1:8000
📌 Endpoint
GET /analyze/{sector}
🔐 Required Header
x-api-key: secret123
📥 Example Request
GET /analyze/technology
📤 Example Response
{
  "sector": "technology",
  "report": "# Technology Sector Report\n\n## Overview\n...\n\n## Current Trends\n...\n\n## Opportunities\n...\n\n## Risks\n..."
}
