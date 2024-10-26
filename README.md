# THIS BRANCH IS MADE TO IMPORT LEGACY DATA (JUPYTER NOTEBOOK)
## 1.Installations
> [!WARNING]
> Remember to create virtualenv using **virtualenv env** before installing these packages

> [!WARNING]
> Remember to enter virtualenv using **env\Scripts\activate** before installing these packages
```
    pip install -r requirements.txt
```
> [!WARNING]
> Now install Jupyter notebook dependencies
```
    pip install django-extensions jupyter notebook==6.5.6 psycopg[binary] tqdm
```



## 2.How to use
```
python manage.py shell_plus --notebook
```



# Notes
#### Important notes that might be helpful when using the project 
 - Jupyter notebook can be used as an alternative to Django shell by: 
	  - Running this in a separate (virtual environmented) command prompt **`python manage.py shell_plus --notebook`**
	- Then **add this** to your first cell 
```
		import os, django
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
		os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
		django.setup()
```