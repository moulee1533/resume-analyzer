📄 README.md

# Resume Analyzer 💼📊

An AI-powered web application that intelligently analyzes resumes using Natural Language Processing (NLP) and machine learning. This tool extracts key information like skills, experience, and education, and provides feedback or job-match insights based on the data.

## 🚀 Features

- 🧠 Resume parsing using NLP
- 🔍 Extracts skills, education, and work experience
- 📊 Suggests job roles or improvements
- 🌐 Web-based interface for uploading and analyzing resumes
- 🧾 Supports PDF and DOCX formats

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Libraries & Tools:** spaCy, PyPDF2, docx2txt, scikit-learn, Flask, pandas

## 📁 Project Structure

resume-analyzer/

├── app.py # Flask app and routing

├── resume_parser.py # Core resume analysis logic

├── templates/

│ └── index.html # UI for uploading resumes

├── static/

│ └── style.css # CSS styling

├── utils/

│ └── job_matcher.py # Optional: job role matching logic

├── sample_resumes/ # Test resumes

├── requirements.txt # Dependencies



## ⚙️ Installation

1. **Clone the Repository**
       ```bash
       git clone https://github.com/yourusername/resume-analyzer.git
       cd resume-analyzer

2. **Create Virtual Environment** 
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Requirements**

   pip install -r requirements.txt

4.**Download spaCy Language Model**

       python -m spacy download en_core_web_sm

**5.Run the App**
    
    python app.py

**6.Open in Browser**

       Visit: http://localhost:5000

**🧪 Example Use Cases**
    HR screening automation

    Resume quality check and improvement suggestions

    Job portal integration for candidate matching

**📬 Supported Formats**
    .pdf
    
    .docx

**🙌 Acknowledgements**
    spaCy
    
    Flask
    
    scikit-learn
