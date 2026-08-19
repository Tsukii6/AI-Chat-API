# Model-Agnostic AI Chat API

A production-structured AI API built with FastAPI and LiteLLM.
Switch AI providers by changing two lines. Zero application code changes.

## Tech Stack
- Python, FastAPI, LiteLLM, Instructor, Groq

## Setup

### Clone the repo
git clone <your-repo-url>
cd ai-chat-api

#### Create virtual environment
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Configure environment
cp .env.example .env
### Add your API key to .env

### Run
uvicorn app.main:app --reload

## Once app runs in local, click below
[Localhost](http:localhost:8000/docs)

## API

POST /api/v1/chat
General purpose chat with a configurable system prompt.

POST /api/v1/explain
Explains any topic tailored to a given audience (e.g. "explain black holes to a 5 year old").
System prompt is built internally — caller never controls AI behavior directly.

POST /api/v1/extract
Extracts structured data from unstructured customer support text
(name, age, order number, email, issue, sentiment) using schema-enforced
structured output. Returns a validated JSON object, not free text.
