from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://task-manager-backend-sdkm.onrender.com",
    "https://*.onrender.com",
    "https://*.vercel.app",
    "http://localhost:5173",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://task-manager-frontend.vercel.app",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
