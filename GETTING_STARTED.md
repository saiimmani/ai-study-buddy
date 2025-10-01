# Getting Started with Study Spark

## Welcome! 🎓

This guide will help you get Study Spark running in just a few minutes.

## Prerequisites Check

Before starting, make sure you have:
- [ ] Python 3.8 or higher installed
- [ ] Internet connection
- [ ] A Google account (to get API key)

## Step-by-Step Setup

### Step 1: Get Your Google Gemini API Key (5 minutes)

1. Open your browser and go to: **https://makersuite.google.com/app/apikey**
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Click **"Create API key in new project"** (or select existing project)
5. **Copy the API key** that appears (it starts with "AI...")
6. Keep this key safe - you'll need it in the next step!

### Step 2: Install Dependencies (2 minutes)

Open PowerShell in this folder and run:

```powershell
pip install -r requirements.txt
```

Wait for all packages to install. You should see:
- ✅ streamlit installed
- ✅ google-generativeai installed
- ✅ python-dotenv installed

### Step 3: Configure Your API Key (1 minute)

**Option A: Using .env file (Recommended for beginners)**

1. Create a new file named `.env` (no extension, just `.env`)
2. Open it in Notepad or VS Code
3. Add this line:
   ```
   GOOGLE_API_KEY=paste_your_api_key_here
   ```
4. Replace `paste_your_api_key_here` with your actual API key
5. Save the file

**Option B: Using Streamlit secrets**

1. Create a file at `.streamlit/secrets.toml`
2. Add this line:
   ```toml
   GOOGLE_API_KEY = "paste_your_api_key_here"
   ```
3. Save the file

### Step 4: Run the Application (30 seconds)

In PowerShell, run:

```powershell
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Step 5: Test the Features (5 minutes)

Try each feature:

1. **🧠 Concept Explainer**
   - Type: "What is photosynthesis?"
   - Click "Explain"

2. **📝 Note Summarizer**
   - Click "Upload File"
   - Upload `sample_notes.txt`
   - Click "Summarize"

3. **❓ Quiz Generator**
   - Paste content from `sample_notes.txt`
   - Set questions to 5
   - Click "Generate Quiz"
   - Take the quiz!

4. **🃏 Flashcard Creator**
   - Paste content from `sample_notes.txt`
   - Click "Generate Flashcards"
   - Flip through the cards

## 🎉 Success!

If all features work, you're ready to go!

## ❌ Troubleshooting

### "pip is not recognized"

**Solution**: Install Python from python.org and check "Add Python to PATH" during installation

### "No module named 'streamlit'"

**Solution**: Run `pip install -r requirements.txt` again

### "No API key found"

**Solution**: 
1. Make sure your `.env` file is in the same folder as `app.py`
2. Check that there are no typos in `GOOGLE_API_KEY`
3. Verify your API key is correct

### App won't open in browser

**Solution**: Manually go to http://localhost:8501

### "Port 8501 is already in use"

**Solution**: 
```powershell
streamlit run app.py --server.port 8502
```

## 🚀 Next Steps

Once everything works:
1. ✅ Read the full `README.md`
2. ✅ Check out `TESTING.md` for thorough testing
3. ✅ Follow `DEPLOYMENT.md` to deploy online
4. ✅ Share your app with friends!

## 📚 More Help

- **Full Documentation**: See `README.md`
- **Testing Guide**: See `TESTING.md`
- **Deployment Guide**: See `DEPLOYMENT.md`
- **Setup Checklist**: See `SETUP_CHECKLIST.md`

## 💡 Tips

- **Study Material**: Use `sample_notes.txt` for testing
- **Best Results**: Provide detailed text (200+ words) for quizzes and flashcards
- **API Calls**: Each AI generation uses your API quota (but Gemini is free!)
- **Saving Work**: The app doesn't save history (add this feature yourself!)

---

**Ready to start? Follow the steps above! 🚀**

If you get stuck, check the troubleshooting section or refer to the detailed guides.

**Happy Studying! 🎓✨**
