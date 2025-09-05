import streamlit as st
import joblib, json, tempfile, os
from utils.text_cleaning import clean_text
from utils.extract_text import extract_from_pdf
import docx2txt

# Set page configuration
st.set_page_config(page_title="Resume Screening App", page_icon="🧠", layout="centered")

# ---- Path Setup ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "resume_classifier.joblib")
SKILLS_PATH = os.path.join(BASE_DIR, "models", "top_skills_per_role.json")

# ---- Load Model + Skills ----
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)

    skills = {}
    if os.path.exists(SKILLS_PATH):
        with open(SKILLS_PATH, "r") as f:
            skills = json.load(f)
    return model, skills

model, top_skills = load_artifacts()

# ---- Streamlit UI ----
st.title("🧠 Resume Screening App")
st.write("Upload a **PDF** or **DOCX** resume to predict the job role and fit score.")

uploaded = st.file_uploader("Upload resume (.pdf / .docx)", type=["pdf", "docx"])

def extract_text_from_docx_streamlit(uploaded_file):
    """Helper to extract text from uploaded DOCX file inside Streamlit."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    text = docx2txt.process(tmp_path) or ""
    os.remove(tmp_path)
    return text

if uploaded is not None:
    # Extract text
    if uploaded.name.lower().endswith(".pdf"):
        text = extract_from_pdf(uploaded)
    else:  # DOCX
        text = extract_text_from_docx_streamlit(uploaded)

    st.subheader("Extracted Text (preview)")
    st.write(text[:2000] + ("..." if len(text) > 2000 else ""))

    # Clean & predict
    if text.strip():
        clean = clean_text(text)
        pred = model.predict([clean])[0]
        proba = model.predict_proba([clean]).max()
        fit_score = int(round(100 * proba))

        st.subheader("Prediction")
        st.markdown(f"**Predicted Role:** `{pred}`")
        st.markdown(f"**Fit Score:** `{fit_score}%`")

        # Matched skills (simple overlap with top skills list)
        if pred in top_skills and top_skills[pred]:
            matched = [s for s in top_skills[pred] if s.lower() in clean]
            st.subheader("Key Matched Skills")
            if matched:
                st.write(", ".join(sorted(set(matched))[:20]))
            else:
                st.write("No direct matches found. Consider adding role-specific keywords.")
