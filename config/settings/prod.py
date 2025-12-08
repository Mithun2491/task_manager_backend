from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

# TRUST FRONTEND DOMAINS (React dev + Vercel prod)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
    "https://*.vercel.app",
    "http://localhost:5173",
]

# CORS FOR FRONTEND ACCESS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://task-manager-frontend.vercel.app",  # change when deployed
]

# OPTIONAL (during development to avoid issues)
CORS_ALLOW_ALL_ORIGINS = True

# Ensure corsheaders is installed in base.py, but add middleware here
if "corsheaders" not in INSTALLED_APPS:
    INSTALLED_APPS += ["corsheaders"]

# Insert middleware at top
if "corsheaders.middleware.CorsMiddleware" not in MIDDLEWARE:
    MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

# Whitenoise static serving (already correct in base.py)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
