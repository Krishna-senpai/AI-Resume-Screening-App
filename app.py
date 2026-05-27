from flask import Flask, render_template, request, jsonify
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    file = request.files['resume']
    jd = request.form['jd']
    
    resume_text = extract_text(file)
    vectors = TfidfVectorizer().fit_transform([resume_text, jd])
    score = round(cosine_similarity(vectors)[0][1] * 100, 2)
    
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(debug=True)