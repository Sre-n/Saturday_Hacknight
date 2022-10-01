import os


SECRET_KEY = os.environ.get("SECRET_KEY")



ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUD_API_KEY"),
    'API_SECRET': os.environ.get("CLOUD_API_SECRET")
}