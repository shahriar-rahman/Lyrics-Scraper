===========================================================================
# Lyrics Scraping
## ! Work in Progress... !

</br></br>
## Project Organization
---------------------------------------------------------
	──────────────────────────────────────────────────────────────────────────────────────────
	|
    ├── LICENSE		# MIT License
	|
	|                         		
    ├── README.md		# The top-level README for developers using this project.
	|
	|
    ├── files		# Contains related project files. 
    │                          		
    │
    ├── requirements.txt	# Requirements file for reproducing the analysis environment.
    │                         			
	│                         		
    ├── setup.py		# Makes project pip installable (pip install -e .), so source folder can be imported.
	│                         			
	│  
    ├── lyrics_crawler	# Source code for use in the project.
    │   │
    │   ├── __init__.py	# Makes 'lyrics_crawler' a Python module.
    │   │
    │   │
    │   ├── lyrics_crawler	# Primary Scrapy folder.
    │   │             │
    │   │             ├── __init__.py		
    │   │             │
    │   │             ├── spiders		# Folder which holds the spider scripts.
    │   │             │          └── __init__.py	
    │   │             │          └── _xp_01.py	# Spider for testing a basic Crawling procedure.
    │   │             │
    │   │             ├── items.py	# Item containers
    │   │             │
    │   │             ├── middlewares.py	# Middleware Settings	
    │   │             │
    │   │             ├── pipelines.py	# Database Connection
    │   │             │
    │   │             └── settings.py	# Scrapy Settings such as Proxies, User Agents, etc.
    │   │
    │   │
    │   ├── Lyrics_Scraping.egg-info        # Contains additional package information
    │   │
    │   │
    │   └── scrapy.cfg	# Scrapy Configuration File
    │  
	└─────────────────────────────────────────────────────────────────────────────────────────
--------

</br></br>

## Package Installation
### ◘ Requirements
* setuptools~=68.1.0
* scrapy~=2.10.0

</br></br>


### ◘ Module Installation (setup.py)
1. To use the *setup.py* file in Python, the first objective is to have the *setuptools* module installed. It can be accomplished by running the following command:
```
pip install setuptools                                     
```
2. Once the setuptools module is installed, use the setup.py file to build and distribute the Python package by running the following command:
```
python setup.py sdist bdist_wheel
```
If any error is encountered, then use the following command.
```
python setup.py sdist
```
3. In order to install all the requirements, run the following command:
```
pip install .                                 
```

<br/><br/>

### ◘ Python Library Installation (using pip)
In order to *install* the required packages on the local machine, Open pip and run the following commands separately:
```
> pip install scrapy                            
```

<br/><br/>

### ◘ Supplementary Resources
For more details, visit the following links:
* https://docs.scrapy.org/en/latest/intro/install.html
* https://pypi.org/project/Scrapy/

<br/><br/>

### ◘ MIT License
Copyright (c) 2023 Shahriar Rahman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

===========================================================================