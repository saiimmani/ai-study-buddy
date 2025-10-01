# 🚀 Deployment Guide - Study Spark

This guide will walk you through deploying your Study Spark application to Streamlit Community Cloud.

## Prerequisites

- ✅ Application working locally
- ✅ GitHub account
- ✅ Google Gemini API key
- ✅ Git installed on your computer

## Step-by-Step Deployment

### Step 1: Initialize Git Repository

Open PowerShell in your project directory and run:

```powershell
git init
git add .
git commit -m "Initial commit: Study Spark AI Study Buddy"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right
3. Select **New repository**
4. Fill in the details:
   - **Repository name**: `ai-study-buddy` (or your preferred name)
   - **Description**: "AI-Powered Study Buddy with concept explainer, note summarizer, quiz generator, and flashcard creator"
   - **Visibility**: Public (required for free Streamlit hosting)
   - **Do NOT** initialize with README (we already have one)
5. Click **Create repository**

### Step 3: Push Code to GitHub

Copy the commands from GitHub (they'll look similar to this):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/ai-study-buddy.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**Enter your credentials when prompted.**

### Step 4: Deploy to Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Click **Sign in** with your GitHub account
3. Authorize Streamlit to access your GitHub
4. Click **New app** (top right)

### Step 5: Configure Your App

Fill in the deployment form:

1. **Repository**: Select `YOUR_USERNAME/ai-study-buddy`
2. **Branch**: `main`
3. **Main file path**: `app.py`
4. **App URL** (optional): Choose a custom URL like `your-study-spark`

### Step 6: Add Secrets (IMPORTANT!)

1. Click **Advanced settings** before deploying
2. In the **Secrets** section, paste your API key in TOML format:

```toml
GOOGLE_API_KEY = "your_actual_google_api_key_here"
```

⚠️ **Important**: Replace `your_actual_google_api_key_here` with your real API key from Google AI Studio.

### Step 7: Deploy!

1. Click **Deploy**
2. Wait 2-5 minutes for the app to build and deploy
3. Your app will be live at: `https://your-study-spark.streamlit.app`

## 🎉 Success!

Your app is now live and accessible to anyone with the link!

## 📝 Post-Deployment

### Update Your README

Edit `README.md` and add your live app URL:

```markdown
**Deployed Application:** https://your-study-spark.streamlit.app
```

Push the change:

```powershell
git add README.md
git commit -m "Add deployed app URL"
git push
```

### Share Your App

Share the link with:
- Friends and classmates
- On social media
- In your portfolio
- On LinkedIn

## 🔄 Updating Your Deployed App

Whenever you make changes locally:

1. Test the changes locally first
2. Commit your changes:
   ```powershell
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. Streamlit Cloud will automatically rebuild and redeploy your app!

## 🛠️ Managing Your Deployed App

### Access App Dashboard

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Find your app in the dashboard
3. You can:
   - View logs
   - Restart the app
   - Update secrets
   - Delete the app

### Update Secrets

If you need to change your API key:

1. Go to your app dashboard on Streamlit Cloud
2. Click the **...** menu
3. Select **Settings**
4. Go to **Secrets**
5. Update your API key
6. Click **Save**
7. The app will restart automatically

### View Logs

If something goes wrong:

1. Go to your app dashboard
2. Click on your app
3. Click **Manage app** in the bottom right
4. View logs to see error messages

## 🐛 Troubleshooting Deployment

### "Module not found" Error

**Cause**: Missing dependency in `requirements.txt`

**Solution**: 
1. Add the missing module to `requirements.txt`
2. Push changes to GitHub

### "API Key Not Found" Error

**Cause**: Secrets not configured correctly

**Solution**:
1. Check that secrets are in correct TOML format
2. Verify no extra spaces or quotes
3. Restart the app from the dashboard

### App Won't Start

**Cause**: Various possible issues

**Solution**:
1. Check logs in Streamlit dashboard
2. Verify app works locally
3. Ensure all files are pushed to GitHub
4. Try restarting the app

### Slow Loading

**Cause**: Cold start after inactivity

**Solution**: 
- Free tier apps sleep after inactivity
- First visit after sleep takes 30-60 seconds
- Subsequent visits are fast

## 💡 Tips for a Better Deployment

### 1. Add a Custom Favicon

Create `favicon.ico` and update `app.py`:

```python
st.set_page_config(
    page_title="Study Spark",
    page_icon="🎓",  # or path to favicon
    ...
)
```

### 2. Add Analytics (Optional)

Track usage with Google Analytics or Streamlit's built-in analytics.

### 3. Custom Domain (Advanced)

Streamlit apps can be connected to custom domains. Check Streamlit documentation for details.

### 4. Monitor Usage

Check your app's usage stats in the Streamlit dashboard to see:
- Number of visitors
- App uptime
- Resource usage

## 📊 Resource Limits (Free Tier)

Streamlit Community Cloud free tier includes:
- **1 GB** of resources per app
- **Unlimited** public apps
- **Apps sleep** after inactivity (automatically wake on visit)
- **No time limit** on how long apps can run

## 🎓 Next Steps

1. Share your app link in your README
2. Add screenshots to your README
3. Consider adding more features
4. Get feedback from users
5. Iterate and improve!

## 📞 Need Help?

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Forum**: https://discuss.streamlit.io
- **GitHub Issues**: Create an issue in your repository

---

**Congratulations on deploying your app! 🎉**
