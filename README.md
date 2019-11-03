# Single page Django polls app using rest framework and vue js

## Project requirements
* Python 3.7.2
* Django 2.2.6
* Vue cli 3.10.0

## Steps to run the project
## backend
1. Install and activate python virtualenv
2. Install python package dependencies using below command
    ```python
    pip install -r requirements.txt
    ```
4. Migrate db changes by 
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Create superuser
    ```python
    python manage.py createsuperuser
    ```
5. Run django server and go to admin site url. Add few questions and choices under polls.
## frontend

### Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Run your tests
```
npm run test
```

#### Lints and fixes files
```
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
