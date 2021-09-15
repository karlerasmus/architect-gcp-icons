Setup
=====

## Requirements
+ Chrome browser installed
+ Chrome driver installed
+ Selenium
+ BeautifulSoup
+ lxml parser
+ Java
+ plantuml.jar

## Chromedriver install
https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/

## Running

### Virtual environment

Make virtual environment
```python
python3 -m venv env
```
Activate virtual environment
```python
source env/bin/activate
```
Install requirements
```python
pip3 install -r requirements.txt
```

Deactivate virtual environment
```python
deactivate
```

Remove virtual env
```sh
rm -rf env
```

Snapshot requirements
```python
pip3 freeze > requirements.txt
```

Install pipdeptree for requirements management
```python
pip3 install pipdeptree
```
Generate requirements.txt
```python
python3 -m pipdeptree -f --warn silence | grep -P '^[\w0-9\-=.]+' > requirements-dev.txt
```

Scrape gcp product icons
```python
python3 src/scrape.py
```

Save icon images
```python
python3 src/save_icons.py
```

Create uml lib
```python
python3 src/uml.py
```
