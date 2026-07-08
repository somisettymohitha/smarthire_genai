# 💼 SmartHire GenAI

AI-Powered Resume Analyzer & Career Mentor

## Features

- **Resume Parser**: Extract and analyze information from PDF resumes
- **Job Matching**: Find jobs that match your skills and experience
- **Resume Suggestions**: Get AI-powered recommendations to improve your resume
- **Career Mentor**: Ask questions and get personalized career advice
- **Safety Guardrails**: Ensures safe and appropriate use of the platform

## Installation

1. Clone the repository:
```bash
git clone https://github.com/somisettymohitha/smarthire_genai.git
cd smarthire_genai
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

## Project Structure

```
smarthire_genai/
├── streamlit_app.py          # Main application
├── requirements.txt          # Project dependencies
├── README.md                 # This file
└── src/
    ├── parsing/
    │   └── resume_parser.py  # Resume parsing module
    ├── search/
    │   └── job_search.py     # Job search and matching
    ├── generate/
    │   └── cv_suggestions.py # Resume improvement suggestions
    ├── mentor/
    │   └── rag_chain.py      # AI career mentor
    └── safety/
        └── guardrails.py     # Safety and content filtering
```

## Modules

### Resume Parser (`src/parsing/resume_parser.py`)
- Extracts text from PDF resumes
- Parses skills, experience, education, and contact information
- Returns structured resume data

### Job Search (`src/search/job_search.py`)
- Matches jobs based on resume skills
- Calculates skill match scores
- Returns ranked job listings

### CV Suggestions (`src/generate/cv_suggestions.py`)
- Analyzes resume strengths and weaknesses
- Identifies missing sections
- Provides actionable recommendations
- Calculates overall resume score

### Career Mentor (`src/mentor/rag_chain.py`)
- Retrieves relevant career advice
- Provides personalized guidance
- Supports multi-turn conversations

### Safety Guardrails (`src/safety/guardrails.py`)
- Detects toxic and inappropriate content
- Validates input length
- Sanitizes user inputs
- Ensures safe application usage

## Configuration

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_api_key_here
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ by SmartHire Team**
