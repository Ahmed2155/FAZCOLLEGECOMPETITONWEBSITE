from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9$t47%u=eg&gcos=2f6iqrxl9na_h3%jtk-taf*5j2%fm&y-at'

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'fazcollegecompetitonwebsite.onrender.com',  # Your backend domain
]

# ✅ CORS (for cross-origin requests)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # For local Next.js frontend
    "https://fazcollege.vercel.app",  # Update to your actual Vercel frontend domain
]

CORS_ALLOW_CREDENTIALS = True  # Needed for session cookies

# ✅ CSRF (for form and session protection)
CSRF_TRUSTED_ORIGINS = [
    "https://fazcollege.vercel.app",
    "https://fazcollegecompetitonwebsite.onrender.com",
    "http://localhost:3000",
]

# ✅ Cookie security for cross-origin
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'

# ✅ Installed apps
INSTALLED_APPS = [
    'competition',
    'corsheaders',  # Ensure this comes before other Django middleware
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ✅ Middleware (corsheaders should be early)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be at the top
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FAZ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FAZ.wsgi.application'

# ✅ Database (development only)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'competition' / 'static' ]

# ✅ Email (for now, console only)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# ✅ Login/Logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ✅ Auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
