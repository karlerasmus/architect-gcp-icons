Architect-GCP-icons
===================

## Requirements
+ Chrome browser installed
+ Chrome driver installed
+ Selenium
+ BeautifulSoup
+ lxml parser
+ Java
+ plantuml.jar

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
Deactivate virtual environment
```python
deactivate
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


