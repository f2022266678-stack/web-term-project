# Netlify Deployment Guide

## Important Note

**Netlify is primarily designed for static sites and serverless functions.** Deploying a full Django application to Netlify requires using serverless functions, which has limitations. For a production Django portfolio, consider alternatives like:
- **Render** (recommended for Django)
- **Railway**
- **Heroku**
- **PythonAnywhere**

However, if you need to use Netlify, follow the steps below.

## Prerequisites

1. Git repository with your Django project
2. Netlify account
3. All deployment files created (requirements.txt, netlify.toml, runtime.txt)

## Steps to Deploy to Netlify

### 1. Prepare Your Repository

Ensure all files are committed to Git:
```bash
git add .
git commit -m "Prepare for Netlify deployment"
git push origin main
```

### 2. Connect Repository to Netlify

1. Go to [Netlify Dashboard](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect your Git provider (GitHub, GitLab, or Bitbucket)
4. Select your repository

### 3. Configure Build Settings

In Netlify's build settings:
- **Build command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Publish directory:** `staticfiles`
- **Python version:** `3.9` (specified in runtime.txt)

### 4. Set Environment Variables

In Netlify Dashboard → Site settings → Environment variables, add:
- `DEBUG`: `False` (for production)
- `SECRET_KEY`: Your Django secret key (generate a new one for production)
- `DJANGO_SETTINGS_MODULE`: `portfolio_project.settings`

### 5. Set Site Name to f2022266678

1. Go to **Site settings** → **Change site name**
2. Change the site name to: `f2022266678`
3. Your site will be available at: `https://f2022266678.netlify.app`

### 6. Deploy

1. Click **"Deploy site"**
2. Netlify will build and deploy your site
3. Monitor the build logs for any errors

## Alternative: Using Netlify Serverless Functions

For a full Django app, you may need to use Netlify Functions. However, this requires additional configuration and may have limitations.

## Troubleshooting

- **Build fails:** Check build logs in Netlify dashboard
- **Static files not loading:** Ensure `collectstatic` runs successfully
- **Database issues:** SQLite may not work well on Netlify; consider using a cloud database
- **Media files:** Netlify doesn't support persistent file storage; use cloud storage (S3, Cloudinary)

## Recommended: Use Render Instead

For Django applications, **Render** is more suitable:
1. Sign up at [render.com](https://render.com)
2. Create a new Web Service
3. Connect your Git repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn portfolio_project.wsgi:application`
6. Deploy!

Render provides:
- Full Django support
- Persistent storage
- Database support
- Better performance for Django apps
