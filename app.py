import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from utils.parser import extract_resume_data, extract_text_from_pdf, compare_skills

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files.get('resume')
        jobdesc_pdf = request.files.get('jobdesc')
        jobdesc_text_input = request.form.get('jobdesc_text')

        if not resume:
            return "Please upload a resume."

        # Save resume
        res_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(resume.filename))
        resume.save(res_path)

        # Extract resume data (including text)
        resume_data = extract_resume_data(res_path)

        # Get job description text from input or PDF
        if jobdesc_text_input and jobdesc_text_input.strip():
            jobdesc_text = jobdesc_text_input.strip()
        elif jobdesc_pdf:
            jd_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(jobdesc_pdf.filename))
            jobdesc_pdf.save(jd_path)
            jobdesc_text = extract_text_from_pdf(jd_path)
        else:
            return "Please provide a job description (paste text or upload PDF)."

        # Match skills
        match_score, matched_skills = compare_skills(resume_data['skills'], jobdesc_text, resume_data['text'])

        # Add to resume_data
        resume_data['match_score'] = match_score
        resume_data['matched_skills'] = matched_skills
        resume_data['job_text'] = jobdesc_text

        # Return results with the resume_data
        return render_template('result.html', data=resume_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
