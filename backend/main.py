from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
import pdfplumber

app = FastAPI()

# ✅ CORS (must be after app creation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Extract text from PDF
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# 2. MOCK AI analysis (NO OpenAI needed)
def analyze_resume(resume, job_desc):
    return """
Match Score: 25%

Missing Skills:
- React.js
- JavaScript
- HTML/CSS

Suggestions:
- Learn frontend development
- Build React projects
- Improve UI/UX knowledge
"""


# 3. API route
@app.post("/analyze")
async def analyze(file: UploadFile = File(...), job_desc: str = Form(...)):
    try:
        text = extract_text(file.file)
        result = analyze_resume(text, job_desc)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}