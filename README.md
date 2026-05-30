# 🤖 AI-Powered Resume & JD Matcher

An enterprise-ready, lightweight Flask web application engineered to streamline technical recruitment and ATS (Applicant Tracking System) optimization. By leveraging advanced Natural Language Processing (NLP) techniques, the system automates the evaluation process, extracting unstructured text from PDF resumes and mathematically benchmarking it against standard Job Descriptions (JDs).

---

## 🚀 Key Features

* **Automated PDF Parsing:** Seamlessly extracts raw text from multi-page PDF documents using `PyPDF2` without data loss.
* **Vector Space Modeling:** Implements `TfidfVectorizer` to tokenize text, eliminate stop-words, and convert textual data into normalized numerical feature vectors.
* **Mathematical Matching Matrix:** Computes the precise angular distance between vector representations using `Cosine Similarity` to yield an objective match percentage ($0\%$ to $100\%$).
* **Intuitive Minimalist UI:** A clean, responsive, and user-friendly web interface tailored for quick document uploading and real-time processing.


## 🛠️ System Architecture & Workflow

The application operates on a pipeline that bridges text processing with vector space mathematics:
1. **Ingestion:** The Flask backend securely catches the multipart form data (PDF file and string text).
2. **Feature Extraction:** Statistical importance is assigned to words using the Term Frequency-Inverse Document Frequency algorithm:
   $$TF-IDF(t, d, D) = TF(t, d) \times IDF(t, D)$$
3. **Similarity Quantification:** The application evaluates the cosine of the angle between the Resume vector ($\mathbf{A}$) and JD vector ($\mathbf{B}$):
   $$\text{Similarity}(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

---

## 🛠️ Tech Stack

* **Core Backend Framework:** Python 3.x, Flask
* **Text Processing Pipeline:** PyPDF2
* **Mathematical & ML Libraries:** Scikit-learn (`TfidfVectorizer`, `cosine_similarity`), NumPy

---

## 📦 Quick Installation & Environment Setup

### 1. Configure Environment and Dependencies
Ensure you have your virtual environment activated, then install the required production-ready packages directly via `pip`:

```bash pip install flask PyPDF2 scikit-learn
