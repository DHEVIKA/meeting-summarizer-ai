Meeting Summarizer AI 🤖📝

Version: 0.1.0
Tech Stack: Python, FastAPI, HuggingFace Transformers, PyTorch

🚀 Project Overview

Tired of reading long meeting transcripts? This AI-powered agent summarizes meeting discussions in seconds, giving you concise, actionable insights.

It uses state-of-the-art NLP models from HuggingFace to generate summaries while preserving the key points.

💡 Features

Automatic Summarization: Converts long meeting transcripts into short, readable summaries.

FastAPI REST API: Easy-to-use /summarize endpoint.

Supports JSON Input/Output: Can be integrated with other apps or bots.

HuggingFace Transformers: Leverages pre-trained NLP models for high-quality summarization.

📦 Installation

Clone this repository:

git clone https://github.com/<YourUsername>/meeting-summarizer-ai.git
cd meeting-summarizer-ai


Create a virtual environment:

python -m venv .venv


Activate the virtual environment:

Windows:

.venv\Scripts\activate


Mac/Linux:

source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

🏃 Running the API
uvicorn main:app --reload


Open the browser and go to http://127.0.0.1:8000/docs
 to access Swagger UI and test the /summarize endpoint.

Example POST request:

{
  "transcript": "Today we discussed the quarterly sales report. John will prepare the next report. The team agreed to increase marketing budget."
}


Example response:

{
  "summary": "The team agreed to increase marketing budget. John will prepare the next report."
}

🛠️ Tech Stack

Python 3.13+

FastAPI - for building the REST API

Uvicorn - ASGI server for running FastAPI

Transformers - HuggingFace models for summarization

PyTorch - backend for model execution

HuggingFace Hub - model downloading and caching

📈 Demo

<img width="1913" height="955" alt="Screenshot 2025-10-21 152724" src="https://github.com/user-attachments/assets/787d0e7e-7a56-4fc1-8f25-5bd0242db2e3" />
<img width="1899" height="944" alt="Screenshot 2025-10-21 152744" src="https://github.com/user-attachments/assets/9d6533f2-c7ce-4d2e-b368-7fc8de442789" />
<img width="1898" height="959" alt="Screenshot 2025-10-21 152835" src="https://github.com/user-attachments/assets/a5fdd371-41c5-47b2-974e-7d6925272f60" />

📈 WEBSITE
🔹 Features:

Summarizes meeting transcripts instantly

Easy-to-use web interface

Accessible online: [Hugging Face Space link]

💡 Technologies used: Python, Gradio, Hugging Face Transformers
<img width="1917" height="957" alt="Screenshot 2025-10-21 172616" src="https://github.com/user-attachments/assets/4dfa1aa2-e696-4211-bdda-61d7a1288bf1" />

<img width="1919" height="963" alt="Screenshot 2025-10-21 172926" src="https://github.com/user-attachments/assets/2fae235f-562a-4b9f-890b-37b87410f99a" />
