# Study Spark - Setup Checklist

## ✅ Setup Checklist

Use this checklist to ensure everything is configured correctly:

### 1. Environment Setup
- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)

### 2. API Configuration
- [ ] Google Gemini API key obtained from https://makersuite.google.com/app/apikey
- [ ] `.env` file created with `GOOGLE_API_KEY=your_key`
- [ ] OR `.streamlit/secrets.toml` created with API key

### 3. Test the Application
- [ ] Run `streamlit run app.py`
- [ ] App opens in browser at http://localhost:8501
- [ ] All four features visible in sidebar
- [ ] No error messages about missing API key

### 4. Test Each Feature
- [ ] **Concept Explainer**: Enter a question and get an explanation
- [ ] **Note Summarizer**: Paste text and generate a summary
- [ ] **Quiz Generator**: Create and take a quiz
- [ ] **Flashcard Creator**: Generate and flip through flashcards

### 5. Prepare for Deployment (Optional)
- [ ] Code pushed to GitHub repository
- [ ] Repository is public
- [ ] Streamlit Community Cloud account created
- [ ] API key added to Streamlit Cloud secrets

## 🔍 Quick Test Commands

Test that all dependencies are installed:
```bash
python -c "import streamlit; import google.generativeai; print('✅ All dependencies installed!')"
```

Check Python version:
```bash
python --version
```

## 🐛 Common Issues

### "No module named 'streamlit'"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### "No API key found"
**Solution**: Create `.env` file or `.streamlit/secrets.toml` with your API key

### App won't start
**Solution**: 
1. Check if port 8501 is already in use
2. Try: `streamlit run app.py --server.port 8502`

### Quiz/Flashcards not generating
**Solution**: 
1. Check your internet connection
2. Verify API key is valid
3. Try with more detailed input text (200+ words)

## 📞 Getting Help

If you encounter issues:
1. Check the full README.md
2. Review the error message in the terminal
3. Verify your API key is correct
4. Try restarting the application

## 🎉 Ready to Deploy?

Once everything works locally, follow the deployment guide in README.md to publish your app to Streamlit Community Cloud!
