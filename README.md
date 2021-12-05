#### After project is installed setup the virtual environment (venv)
```sh 
cd /path/to/the/project/DjangoBrokenAccessControl
```
#### Execute the following command in your terminal to run the project

```sh
python3 manage.py runserver
```

## All URLs
- http://127.0.0.1:8000 - Home page
- http://127.0.0.1:8000/login - If already logged in you should be redirected to customer page
- http://127.0.0.1:8000/register - If already logged in you should be redirected to customer page
- http://127.0.0.1:8000/customer - Login required
- http://127.0.0.1:8000/allusers - Admin only page
