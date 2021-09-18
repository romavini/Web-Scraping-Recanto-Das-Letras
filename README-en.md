## 🤖🧰 Web Scraping | [Recanto das Letras](https://www.recantodasletras.com.br/) 📓✒
### [Leia em Português aqui](README.md).
![version](https://img.shields.io/badge/relise-v1.0.0-important)

**Web Scraping** **Python** project for the Recanto das Letras website, a social network for sharing stories, poetry and texts in general.

[![License: CC-BY-NC-SA](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

[![Psycopg](https://img.shields.io/badge/lib-Psycopg-yellowgreen)](https://www.psycopg.org/) [![SQLalchemy](https://img.shields.io/badge/lib-SQLalchemy-darkred)](https://www.sqlalchemy.org/) [![Selenium](https://img.shields.io/badge/lib-Selenium-darkgreen)](https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/) [![Pandas](https://img.shields.io/badge/lib-Pandas-white)](https://pandas.pydata.org/) [![NumPy](https://img.shields.io/badge/lib-NumPy-darkblue)](https://numpy.org/)

![WebScraping](images/web_scraping.gif)

## Features

 - Collect and catalogs **all texts** from a **personal profile**, storing the following text data:
   - id [automatically generated]
   - Title;
   - Text content;
   - URL to text;
   - Category;
   - Publication date;
   - Views.
 - Stores into **PostgreSQL** server.

![postgres](images/postgreSQL.jpg)

## To Add

 - Collect other profiles.

# Running 🏁

 1. Download the webdriver for use from the Selenium library, available [here](https://chromedriver.chromium.org/downloads).
 2. Create a `.env` file in the repository root folder containing the following information:

```python
# Login Recanto das Letras
user =   # User
password =   # Password

# Webdriver
chrome_driver_path =   # Path to Webdriver (e.g. C:\Users\user\.google\chromedriver.exe)

# PostgreSQL
user_db =   # User to Database
password_db =   # Password
host_db =   # Host (localhost)
port_db =   # Port
database_db =   # Database
```
 3. Install dependencies and run.

```
$ pip install -r requirements.txt
$ python getpoetry/main.py
```

# Testing 🚧

- Install developer dependencies.

```
$ pip install -r requirements-dev.txt
$ pytest getpoetry
```
