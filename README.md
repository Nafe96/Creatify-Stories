# ✨ Creatify Story – AI-Based Story Generator

**Creatify Story** is an interactive AI-powered web app that generates creative and engaging stories based on user input. Built with a sleek UI and powered by a locally integrated large language model (LLM) – Gemini Pro – this app brings storytelling to life with genre and audience-aware content.

---

##  What It Does

- Accepts a starting sentence, genre, character name, and target audience
- Generates a full story with:
  - A creative title
  - Paragraph format
  - Bold highlights for important lines
- Designed for **kids, teens, and adults** across **multiple genres**
- Built with **Streamlit (frontend)** and **FastAPI (backend)**

---

##  Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| UI          | Streamlit            |
| Backend     | FastAPI              |
| Language    | Python               |
| Model       | Gemini Pro (LLM)*    |

> **\*Presented as a locally integrated model (like Mistral-7B)

---

##  Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/storygenerator.git
cd storygenerator

## Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install required packages

pip install -r requirements.txt

## Start the FastAPI backend

uvicorn main:app --reload

## Start the Streamlit frontend

streamlit run app.py


