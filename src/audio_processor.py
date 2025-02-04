import whisper
from better_profanity import profanity
from transformers import pipeline

profanity.load_censor_words()

def analyze_audio(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    
    return {
        "transcript": result["text"],
        "sentiment": analyze_sentiment(result["text"]),
        "profanity_count": count_profanity(result["text"])
    }

def analyze_sentiment(text):
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    return classifier(text[:512])[0]['label']

def count_profanity(text):
    return sum(1 for word in text.split() if profanity.contains_profanity(word))