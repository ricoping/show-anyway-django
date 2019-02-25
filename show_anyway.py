import subprocess, os, time

############################

PROJECT_NAME = "myproject"
APP_NAME = "myapp"
PYTHON_CMD = "python3"

############################

print("Hello!")
try:
	import django; print("Django Version: ", django.get_version())
except:
	print("Please install django")


command = "django-admin startproject " + PROJECT_NAME + ";cd " + PROJECT_NAME + ";" + PYTHON_CMD + " manage.py startapp " + APP_NAME + "; mkdir templates; mkdir static ; mkdir static/js; mkdir static/css; mkdir static/img; touch " + APP_NAME + "/urls.py; touch templates/base.html; touch templates/index.html"
proc = subprocess.Popen(command, shell=True)

time.sleep(3)

path = os.path.dirname(os.path.abspath(__file__))

#############SETTINGS

settings_file = open(os.path.join(path, PROJECT_NAME, PROJECT_NAME, "settings.py"))
settings = settings_file.read()
print("ALLOWED_HOSTS = [] ---->   ALLOWED_HOSTS = ['*']")
settings = settings.replace("ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")

print("INSTALLED_APPS -----> + " + APP_NAME)
settings = settings.replace("    'django.contrib.staticfiles',", "    'django.contrib.staticfiles',\n    '" + APP_NAME+ "',")

print("'DIRS': [], ----> 'DIRS': [os.path.join(BASE_DIR, 'templates')],")
settings = settings.replace("'DIRS': [],", "'DIRS': [os.path.join(BASE_DIR, 'templates')],")

settings += '\n' + "STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n"

settings_file.close()

new_settings_file = open(os.path.join(path, PROJECT_NAME, PROJECT_NAME, "settings.py"), "w")
new_settings_file.write(settings)
new_settings_file.close()

#############END SETTINGS



#############URLS

urls_file = open(os.path.join(path, PROJECT_NAME, PROJECT_NAME, "urls.py"))
urls = urls_file.read()

urls = urls.replace("from django.urls import path", "from django.urls import include, path")

urls = urls.replace("    path('admin/', admin.site.urls),", "    path('admin/', admin.site.urls),\n    path('" + APP_NAME + "/', include('" + APP_NAME + ".urls')),")

urls_file.close()

new_urls_file = open(os.path.join(path, PROJECT_NAME, PROJECT_NAME, "urls.py"), "w")
new_urls_file.write(urls)
new_urls_file.close()

#############END URLS



#############URLS

app_urls_file = open(os.path.join(path, PROJECT_NAME, APP_NAME, "urls.py"))
app_urls = """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""


app_urls_file.close()

new_app_urls_file = open(os.path.join(path, PROJECT_NAME, APP_NAME, "urls.py"), "w")
new_app_urls_file.write(app_urls)
new_app_urls_file.close()

#############END URLS



############VIEWS

app_views_file = open(os.path.join(path, PROJECT_NAME, APP_NAME, "views.py"))
app_views = """
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'index.html', {
		"hello": "Hello Django!"
		})
"""


app_views_file.close()

new_app_views_file = open(os.path.join(path, PROJECT_NAME, APP_NAME, "views.py"), "w")
new_app_views_file.write(app_views)
new_app_views_file.close()

#############END VIEWS



############TEMPLATES BASE

base_file = open(os.path.join(path, PROJECT_NAME, "templates", "base.html"))
base = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %}</title>
</head>

<body>
    <main>
        {% block main %}
        {% endblock %}
    </main>
</body>
</html>
"""


print(base)
base_file.close()

base_file = open(os.path.join(path, PROJECT_NAME, "templates", "base.html"), "w")
base_file.write(base)
base_file.close()

#############END TEMPLATES

############TEMPLATES INDEX

index_file = open(os.path.join(path, PROJECT_NAME, "templates", "index.html"))
index = """
{% extends 'base.html' %}
{% block title %}
My First Django
{% endblock %}

{% block main %}
<h1>{{ hello }}</h1>
{% endblock %}
"""

index_file.close()

index_file = open(os.path.join(path, PROJECT_NAME, "templates", "index.html"), "w")
index_file.write(index)
index_file.close()

#############END TEMPLATES
print("-"*80)
print("You need to do :")
print("DB setting in " + PROJECT_NAME + "/settings.py")
print("cd " + PROJECT_NAME)
print(PYTHON_CMD + " manage.py makemigrations")
print(PYTHON_CMD + " manage.py migrate")
print(PYTHON_CMD + " manage.py runserver localhost:8000")
print("-"*80)
print("You may need to do:")
print(PYTHON_CMD + " manage.py collectstatic")
print("Add : STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) in " + PROJECT_NAME + "/settings.py")
print("-"*80)
print("You may use :")
print("{% load static %}")
print("{% static 'static/css/example.css' %}")

