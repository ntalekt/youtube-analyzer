# YouTube Video Analyzer

AI-powered video content analysis system that automatically generates metadata and predicts content ratings.

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Stargazers](https://img.shields.io/github/stars/ntalekt/youtube-analyzer?style=flat)](https://github.com/ntalekt/youtube-analyzer/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ntalekt/youtube-analyzer?style=flat)](https://github.com/ntalekt/youtube-analyzer/commits/master)

## Features ✨
- Video category/subcategory detection
- Sentiment analysis from audio
- Visual object detection
- Content rating prediction (US standards)
- Key topic extraction

## Components
- **Core AI**:
  - OpenAI CLIP (visual analysis)
  - Whisper (audio transcription)
  - YOLOv8 (object detection)
- **Processing**:
  - OpenCV (video frame extraction)
  - FFmpeg (video processing)
- **Backend**:
  - FastAPI (REST API)
  - Redis (caching)

## Quick Start 🚀 

### 1. Clone the Repository
```bash
git clone https://github.com/ntalekt/youtube-analyzer
cd youtube-analyzer
```

### (Optional) Create venv
```bash
python -m venv venv
```

### 2. Install dependencies
```bash
pip3 install -r requirements.txt --no-cache-dir
python -m nltk.downloader punkt punkt_tab wordnet
```

## Usage
```bash
python src/main.py --url "https://youtube.com/watch?v=..."
```

## Example Output
```json
{
  "metadata": {
    "category": "Educational",
    "subcategories": [
      "Cooking Tutorial"
    ],
    "sentiment": "positive",
    "key_topics": [
      "baking",
      "oven safety"
    ],
    "content_flags": {
      "weapons": 0,
      "violence": 0,
      "nudity": 0
    },
    "predicted_rating": "TV-G"
  }
}
```
## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Support 📞

For issues or questions, please [open an issue](https://github.com/ntalekt/order-flow-analysis-tool/issues)

---

**Disclaimer**: This tool is not officially affiliated with YouTube. Use responsibly and in accordance with airline policies.