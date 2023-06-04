# django-basics-batch-2-repo
```
python3 -m venv my_project_env
source my_project_env/bin/activate (linux) or source my_project_env/Scripts/activate (windows using git bash)
pip install django
pip freeze > requirements.txt
django-admin startproject my_project .
python3 manage.py runserver
```


```
Top Right click on "+" buton create new repo
Give repo name and desc
Do not click on add readme.md
copy instructions and paste
git add .
git commit -m "first commit"
git push
```

```
git add <filename> is used to stage the files
git commit -m "<commit_name>" is used to commit the staged files
git push is used to push the code to github
git pull is used to pull the code from github
git fetch is just used to update the status between local and remote
use git status after git fetch to know the status
```
```
.gitignore is used to ignore the code files / folders which we don't require on repo
for example db file , env folder
```

```
Concept of django table and models
DB table (sql) <=> Django Models (python)
sql queries <=> Django ORM
```

```
command to create app
python3 manage.py startapp <your_app_name>
```


