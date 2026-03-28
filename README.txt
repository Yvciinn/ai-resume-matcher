================================================
        ResumeMatch — AI Resume Job Matcher
================================================

DESCRIPTION
-----------
ResumeMatch is a local AI-powered web app that compares your resume
against job descriptions and gives you a similarity score for each one.
It uses sentence embeddings and cosine similarity to measure how well
your resume matches each job — no API keys, no cloud, runs entirely
on your machine.


HOW IT WORKS
------------
1. You paste your resume text
2. You add one or more job titles and descriptions
3. The AI encodes your resume and each job into vector embeddings
4. It computes cosine similarity between your resume and each job
5. Results are ranked and displayed with a score from 0 to 1


TECH STACK
----------
Backend:
  - Python
  - FastAPI          (REST API server)
  - Sentence-Transformers (all-MiniLM-L6-v2 model)
  - scikit-learn     (cosine similarity)
  - pandas           (data handling)
  - NLTK             (text cleaning / stopword removal)

Frontend:
  - HTML / CSS / JavaScript (vanilla, no frameworks)


PROJECT STRUCTURE
-----------------
project-1/
├── app.py              # FastAPI backend and API endpoints
├── model.py            # Embedding model and matching logic
└── frontend/
    ├── index.html      # Main UI
    ├── style.css       # Styles
    └── js.js           # Frontend logic and API calls


INSTALLATION
------------
1. Clone or download the project

2. Install dependencies:
   pip install fastapi uvicorn sentence-transformers scikit-learn pandas nltk

3. Run the backend from the project root:
   cd project-1
   uvicorn app:app --reload

4. Open the frontend:
   - Open frontend/index.html with Live Server in VS Code
   - OR open it directly in your browser

5. Make sure the backend shows:
   INFO: Uvicorn running on http://127.0.0.1:8000
   INFO: Application startup complete.


USAGE
-----
1. Paste your resume into the resume text box
2. Fill in a job title and job description
3. Click "Add Job" to add more jobs (up to as many as you want)
4. Click "Submit" to get your match scores
5. Results appear ranked from highest to lowest match


NOTES
-----
- The first request after starting the server is slower because the
  model loads into memory. Subsequent requests are faster.
- The model runs entirely locally — no data is sent to any external server.
- For best results, paste the full resume text including skills,
  experience, and education sections.


AUTHOR
------
Yassine KHEMIRI
================================================