import argparse
import yaml
from video_downloader import download_video
from audio_processor import analyze_audio
from video_analyzer import analyze_video
from utils.logger import configure_logger

logger = configure_logger(__name__)

def combine_results(audio_data, video_data):
    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)
    
    return {
        "metadata": {
            "category": determine_category(audio_data, video_data),
            "subcategories": [],
            "sentiment": audio_data["sentiment"],
            "key_topics": extract_topics(audio_data["transcript"]),
            "content_flags": {
                "violence": video_data["violence_percent"] > config["rating_rules"]["violence_threshold"],
                "profanity": audio_data["profanity_count"] > config["rating_rules"]["profanity_threshold"]
            },
            "predicted_rating": determine_rating(video_data, audio_data, config)
        }
    }

def determine_rating(video_data, audio_data, config):
    if video_data["violence_percent"] > config["rating_rules"]["violence_threshold"]:
        return "TV-MA"
    if audio_data["profanity_count"] > config["rating_rules"]["profanity_threshold"]:
        return "TV-14"
    return "TV-PG"

def extract_topics(transcript):
    from nltk.tokenize import word_tokenize
    return list(set([word.lower() for word in word_tokenize(transcript) if len(word) > 4]))

def determine_category(audio_data, video_data):
    return "Educational" if video_data["violence_percent"] < 5 else "Entertainment"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)

    try:
        video_path = download_video(args.url)
        audio_data = analyze_audio(video_path)
        video_data = analyze_video(video_path, config)
        print(f"Analysis Complete:\n{combine_results(audio_data, video_data)}")
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()