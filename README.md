# London Metropolitan Weblearn Scraper

This tools log into weblearn (https://student.londonmet.ac.uk/weblearn/) and search for all the links relative to the student's modules. 
It create a HTML file (londonmet.html) on the main folder with the direct links to the weekly learning materials. It will help to easily download the materials. 
### Usage (Windows - Python3)
```
python londonmet_weblearn_scraper.py -u USERNAME -p PASSWORD
```
### Help
```
python londonmet_weblearn_scraper.py -h
```

```
usage: londonmet_weblearn_scraper.py [-h] -u USER -p PASSWORD

London Metropolitan Module Scaper

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Londonmet user name
  -p PASSWORD, --password PASSWORD  Londonmet password
```


### Screenshots

#### HTML file
<p align="center">
  <img src="https://github.com/Ryuk-dev75/London_metropolitan_weblearn_scraper/blob/main/screenshots/output.JPG?raw=true">
</p>

#### Terminal
<p align="center">
  <img src="https://github.com/Ryuk-dev75/London_metropolitan_weblearn_scraper/blob/main/screenshots/terminal_output.JPG?raw=true">
</p>

