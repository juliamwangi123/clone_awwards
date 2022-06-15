# clone_awwards
## Description
This a webiste that allow users to view , submit and also rate other other users sites.Its uses django restframework to create an api endpoint [api](http://127.0.0.1:8000/sites):api link and  the api is consumed internally


#### Features
1. [Python](https://www.python.org/): programming language.
2. [Django](https://www.djangoproject.com/): web framework.
3. [Bootstrap](https://getbootstrap.com/): front-end framework.
4. [Javascript](https://www.javascript.com/) -programming language




### User Story

1. User registers
2. User Logins
3. User Edit their profile
5. User can submit their site
6. User can view other users site and review
7. user Can logout

### Installation
1. Clone this Github repository:
```
    git clone https://github.com/juliamwangi123/clone_awwards.git
     
    cd awwards

```

2. Install the pre-requisites:

```
      pip install -r requirements.txt
```


3. Copy the settings template to create your local settings:

```
    cp awwards/settings_local.template awwards/settings_local.py
```


4. Edit the local settings file with your settings:
```
     vi awwards/settings_local.py
```


5. Create the database and admin user:
```
    python manage.py syncdb
```



6. Collect static files:

```
   python manage.py collectstatic
```


7. Configure your web server to serve static files from the directory specified in the local settings file. 



8. Launch the application using the built-in runserver, or deploy using gunicorn, which is the application server of choice:

```
web: gunicorn awwards.wsgi --log-file -
```

#### Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

### Author
~ julia Mwangi

### Licence
Click this [link](LICENSE) to view licence information.

### Contact Information
juliahwambui3@gmail.com