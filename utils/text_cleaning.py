import re
import nltk
import string
from nltk.corpus import stopwords

# Download stopwords if not already available
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(resume_text):
    """
    Clean the input resume text by removing URLs, numbers,
    punctuation, and stopwords.
    """
    # Remove URLs
    resume_text = re.sub(r'http\S+|www\S+|https\S+', '', resume_text, flags=re.MULTILINE)
    
    # Remove special characters and numbers
    resume_text = re.sub(r'\W', ' ', resume_text)
    resume_text = re.sub(r'\d+', ' ', resume_text)
    
    # Remove punctuation
    resume_text = resume_text.translate(str.maketrans('', '', string.punctuation))
    
    # Lowercase
    resume_text = resume_text.lower()
    
    # Remove stopwords
    resume_text = ' '.join([word for word in resume_text.split() if word not in stop_words])
    
    return resume_text.strip()
