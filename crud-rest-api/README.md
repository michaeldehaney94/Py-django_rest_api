Install django framework - pip install django djangorestframework<br/>
Create django project - django-admin startproject [project name]<br/>
'cd' into django project created<br/>
Create django app - django-admin startapp [app name] <br/>
Add 'rest_framework' and 'api' app folder to the INSTALLED_APPS array in 'settings.py'<br/>
Create data models for fields <br/>
Create database migration - py manage.py makemigrations <br/>
Create the serializer file in the api folder. The serializer will transform the model data into json data.<br/>
Create your views to handle the server logic for API endpoints <br/>
Add a 'url.py' file to api folder to run API HTTP request <br/>
Add path in the original 'url.py' file in the project folder to link the app.url in the project.url <br/>
Create superuser to access database in django admin <br/>
<br/>
Create User (POST HTTP method)<br/>
<img src="/assets/createuser.jpg" /><br/>
<br/>
Get User (Get HTTP method)<br/>
<img src="/assets/getuser.jpg" /><br/>
<br/>
Get User Details (Get HTTP method)<br/>
<img src="/assets/userdetails.jpg" /><br/>
<br/>
Click here:
<a href="https://www.youtube.com/watch?v=NoLF7Dlu5mc" target="_blank">Watch Python Django REST API tutorial in 30mins</a>