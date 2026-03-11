# 🎯 Number Game — Setup & Deploy Guide

## 📁 Your Final Folder Structure
```
Number_Game/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
├── mygame/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── game/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── game/
            └── play.html
```

---

## STEP 1 — Copy files into your VS Code project

Copy ALL the files from this zip into your `D:\num\Number_Game\` folder.
Make sure the folder structure matches what's shown above.

---

## STEP 2 — Test locally on your PC

Open PowerShell in VS Code terminal and run:

```powershell
# Install dependencies
pip install django gunicorn whitenoise

# Run the server
python manage.py runserver
```

Open your browser → http://127.0.0.1:8000
You should see the game! Test it, play it. ✅

---

## STEP 3 — Push to GitHub

In the VS Code terminal (you're already in D:\num\Number_Game):

```powershell
git add .
git commit -m "Add Number Guessing Game - Django"
git push origin main
```

---

## STEP 4 — Deploy on Railway.app

1. Go to https://railway.app and sign up / log in with GitHub

2. Click **"New Project"**

3. Click **"Deploy from GitHub repo"**

4. Select your **Number_Game** repo

5. Railway will auto-detect it's a Python app and start building

6. Go to **Settings → Environment Variables** and add:
   - `SECRET_KEY` = any long random string like `my-super-secret-key-12345abcxyz`
   - `DEBUG` = `False`

7. Go to **Settings → Networking** → click **"Generate Domain"**

8. Wait ~2 minutes → your game is LIVE! 🎉

Share the URL with your friends!

---

## 🔄 Every time you update the game:

```powershell
git add .
git commit -m "Update game"
git push origin main
```

Railway auto-redeploys. Done! ✅
