# CVSketcher

Sketch the uploaded Image


## Team members

[Sreni](https://github.com/Sre-n)

[Aanand S](https://www.github.com/unniznd/)



## How it Works

* Upload the image
* Use opencv to make image like sketch
* Render the sketched image

## How to Run locally

* Clone the repo
* Install the requirements ``` pip install -r requirements.txt ```
* Create a file ```dev_settings.py``` in ```backend``` folder with suitable variables

Model of ```dev_settings.py```
```
ALLOWED_HOSTS = ['localhost']
SECRET_KEY = 'add_secret_key_key'

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}
```
* Set ``` debug = False ``` in ```backend/settings.py```
* Run the server
```
python manage.py runserver 
```
