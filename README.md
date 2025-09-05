# 🧠 Resume Screening App

A **Streamlit-based Machine Learning App** that automatically screens resumes by predicting job roles and calculating a **fit score**.  
It also highlights key skills matched from resumes, helping recruiters and HR managers speed up candidate shortlisting.

---

## 📌 Project Overview
This project demonstrates how Natural Language Processing (NLP) and Machine Learning can be used to analyze resumes.  
It processes resumes in **PDF** or **DOCX** formats, extracts and cleans text, predicts the most likely job role, and provides a confidence-based **Fit Score**.

Key features:
- Upload **PDF/DOCX resumes**  
- Extract and clean text (stopwords, punctuation, URLs removed)  
- Predict job role with a trained ML model  
- Display **Fit Score (confidence %)**  
- Highlight **matched skills** relevant to the role  

---

## 📂 Project Structure
```

resume-screening-app/
│── app/
│   └── app.py                  # Main Streamlit app
│── utils/
│   ├── text\_cleaning.py        # NLP cleaning functions
│   └── extract\_text.py         # Resume text extraction
│── models/
│   └── resume\_classifier.joblib # Pre-trained ML model
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
│── UpdatedResumeDataSet.csv    # Training dataset (from Kaggle)

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Uzma-Perveen/resume-screening-app.git
cd resume-screening-app
````

### 2️⃣ (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
cd app
streamlit run app.py
```

Now the app will open in your browser at **[http://localhost:8501/](http://localhost:8501/)** 🎉

---

## 🛠 Requirements

* Python 3.8+
* Streamlit
* Pandas
* Scikit-learn
* NLTK
* Joblib
* Docx2txt
* PyPDF2

All dependencies are listed in `requirements.txt`.

---

## 📊 Example Workflow

1. Upload a resume (PDF/DOCX) in the app.
2. Extracted text is displayed for preview.
3. Model predicts the **job role** (e.g., Data Scientist, Software Engineer).
4. Fit Score is shown (confidence %).
5. Key matched skills are displayed from the resume text.

---

## 📁 Dataset Reference

This project uses the **[Updated Resume Dataset on Kaggle](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)** for model training.

---

## 🚀 Future Improvements

* Deploy app on **Streamlit Cloud / Heroku** for public use.
* Add support for **multiple resume uploads** at once.
* Expand skill-matching dictionary for richer insights.
* Enhance model with advanced NLP techniques like **BERT/Transformers**.

---

## 👩‍💻 Author

**Uzma Perveen**
Course Project: Resume Screening App

```

