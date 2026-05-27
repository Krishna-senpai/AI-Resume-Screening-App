# AI Resume & JD Matcher

A lightweight, Flask-based web application that helps recruiters and job seekers analyze how well a resume matches a specific Job Description (JD). The application extracts text from a PDF resume and utilizes Natural Language Processing (NLP) techniques to compute a matching percentage.

## 🚀 Features
* **PDF Text Extraction:** Automatically extracts text content from uploaded PDF resumes.
* **NLP-powered Matching:** Uses TF-IDF Vectorization to convert text into numerical vectors.
* **Similarity Score:** Computes the precise matching percentage using Cosine Similarity.
* **Clean UI/UX:** Simple web interface to upload a resume and paste a job description.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Text Processing:** PyPDF2
* **Machine Learning / NLP:** Scikit-learn (TfidfVectorizer, cosine_similarity)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Resume-JD-Matcher.git](https://github.com/YOUR_USERNAME/Resume-JD-Matcher.git)
   cd Resume-JD-Matcher
