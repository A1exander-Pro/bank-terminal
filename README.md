# Bank security terminal

This is an internal repository for bank employees. If you got this repository by accident, <br> 
then you won`t  be able to use it, because you do not have access to database. But you can explore how <br>
made requests to database or html code.

---
## How to install:
- Recommended to use for isolation of your project [virtualenv/venv](https://docs.python.org/3/library/venv.html)
- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies: <br>
```pip install -r requirements.txt```
- To run local server you need to write in console(terminal):<br>
```your_directory your_username$ python3 manage.py runserver 0.0.0.0:8000``` <br>
- For environment variables used package python-dotenv. This package will be installed form requirements.txt
- For connection to Databases using [DJ-Database-URL](https://github.com/jacobian/dj-database-url#id7) utility. For manually installation use: <br>
```your_directory your_username$ pip install dj-database-url```
To use it, please read usage [README.rst](https://github.com/jacobian/dj-database-url/blob/master/README.rst) of this utility.
- Also for use, you need to make .env file in this directory ```project/.env```, and put there: <br>
```SECRET_KEY=******```<br>
```DEBUG=****``` it will be True or False<br>
```DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME``` for connecting to DB 

---

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).