# 🎓 Study Spark - AI-Powered Study Buddy

An intelligent web application that helps high school and college students understand complex topics, summarize notes, and test their knowledge through AI-powered interactive tools.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

## 🌟 Features

### 🧠 Concept Explainer
- **Input any concept or question** you're learning about
- Get clear, easy-to-understand explanations tailored for students
- Uses analogies and simple examples to make complex topics accessible

### 📝 Note Summarizer
- **Paste text or upload files** (.txt, .md)
- Choose summary length: Short, Medium, or Detailed
- Get concise, bullet-point summaries highlighting key ideas
- Perfect for lecture notes, articles, and textbook chapters

### ❓ Quiz Generator
- **Generate custom quizzes** from your study material
- Multiple-choice questions with 3-4 options
- Instant feedback with explanations for each answer
- Track your score and performance
- Interactive question-by-question format

### 🃏 Flashcard Creator
- **Automatically extract key terms** from your notes
- Beautiful, interactive digital flashcards
- Flip cards to reveal answers
- Navigate through your deck easily
- Perfect for memorization and quick review

## 🚀 Live Demo

**Deployed Application:** [Your Streamlit App URL will go here after deployment]

## 📋 Prerequisites

- Python 3.8 or higher
- A Google Generative AI API key (Gemini)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saiimmani/ai-study-buddy.git
cd ai-study-buddy
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Your Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 5. Configure API Key

**For Local Development:**

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

**OR**

Create `.streamlit/secrets.toml`:

```bash
# Copy the example file
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml` and add your API key:
```toml
GOOGLE_API_KEY = "your_actual_api_key_here"
```

### 6. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

## 🌐 Deployment to Streamlit Community Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Initialize git and push your code:

```bash
git init
git add .
git commit -m "Initial commit - Study Spark app"
git branch -M main
git remote add origin https://github.com/yourusername/ai-study-buddy.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch (main), and main file (app.py)
5. Click "Advanced settings"
6. Add your secrets in the "Secrets" section:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```
7. Click "Deploy"

Your app will be live in a few minutes!

## 📁 Project Structure

```
ai-study-buddy/
│
├── app.py                          # Main application file
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── .env.example                    # Example environment file
├── README.md                       # This file
│
└── .streamlit/
    └── secrets.toml.example        # Example secrets configuration
```

## 🎯 Usage Guide

### Concept Explainer
1. Select "🧠 Concept Explainer" from the sidebar
2. Type your concept or question
3. Click "Explain"
4. Read the AI-generated explanation

### Note Summarizer
1. Select "📝 Note Summarizer" from the sidebar
2. Choose to paste text or upload a file
3. Enter your text or upload a `.txt` or `.md` file
4. Select summary length (Short/Medium/Detailed)
5. Click "Summarize"

### Quiz Generator
1. Select "❓ Quiz Generator" from the sidebar
2. Paste your study material or describe a topic
3. Choose the number of questions (3-10)
4. Click "Generate Quiz"
5. Answer each question and get instant feedback
6. Review your final score

### Flashcard Creator
1. Select "🃏 Flashcard Creator" from the sidebar
2. Paste your study material or describe a topic
3. Choose the number of flashcards (5-15)
4. Click "Generate Flashcards"
5. Click "Show Answer" to flip each card
6. Navigate with Previous/Next buttons

## 🔧 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Generative AI (Gemini)](https://ai.google.dev/)** - AI model for content generation
- **[Python](https://www.python.org/)** - Programming language
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues & Troubleshooting

### API Key Issues
- **Error: "No API key found"**
  - Make sure you've created `.env` or `.streamlit/secrets.toml`
  - Verify the API key is correctly formatted
  - For Streamlit Cloud, check the secrets in your app settings

### Quiz/Flashcard Generation Issues
- **Empty or malformed output**
  - The AI sometimes returns text outside JSON format
  - The app attempts to extract JSON automatically
  - Try rephrasing your input or providing more context

### File Upload Issues
- **File not reading correctly**
  - Ensure the file is in `.txt` or `.md` format
  - Check that the file encoding is UTF-8

## 💡 Tips for Best Results

- **Be specific** with your questions and inputs
- **Provide sufficient context** for quizzes and flashcards (at least 200-300 words)
- **Use clear, well-formatted text** for better summaries
- **Try different summary lengths** to find what works best for you

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact the maintainer.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Inspired by the need to make studying more efficient and engaging for students

---

**Happy Studying! 🎓✨**
