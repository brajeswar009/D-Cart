# D-Cart

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

>D-Cart is an e-commerce website with ease of navigation and product selection with equal features as most used shopping sites.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This project is completely build with python as a core. The sole aim is to create a full fleged e-commerce website with django which will help me to get some experience on django work flow and frontend technologies. This project is made for testing the knowledge regarding python and django application.
	
## Technologies
Project is created with:
* Python version: 3.7 or higher (3.8 recommended)
* Django version: 2.2 or higher (3.0 recommended)
* database : sqlite3 or any as you like
* HTML and CSS
* Javascript version: ES 6 or ES 7
* jQuery library version: 3.3.1 (uncompressed)
* Bootstrap library version: 4.2 or 4.3
* any IDE can be used but VS Code is recommended.
	
## Setup
To run this project, fisrt install python from [https://www.python.org/](https://www.python.org/).
After successful installation of python, install django using pip command.
```
$ pip install django
```
to see the project in action, just run the below code in console;
First run makemigrations to package all your model related changes into specific migrations file
```
$ python manage.py makemigrations
```
then run migrate to apply all those migrations file to commit changes into database.
```
$ python manage.py migrate
```
atlast just type runserver in your console to see the D-Cart in action;
```
$ python manage.py runserver
```
Do not forget to setup your SECRET_KEY in settings.py. If it aleady set then ok.
Now you are good to go. Having knowledge on frontend technologies such as Javascript and jQuery is added benefit but you can use google for need as I did.
## Features!

  - Products appear on the home page with an indicated carousel effect.
  - Add product of any number of quantity to the cart from the homepage.
  - Search facility with accurate result.
  - Checkout page with total bill details and address form.
  - Track your ordered product with provided order_id


You can also:
  - Contact us with your query in Contact Us section.
  - Know more about D-Cart and me in About Us section.
  - Quick view the product to get the complete product description.

## Status
This project is finished for the time being. But if some idea comes up to my mind this will be reflected into it.

## Inspiration
I got my main inspiration at looking at [https://www.amazon.in/](https://www.amazon.in/) and [https://www.flipkart.com/](https://www.flipkart.com/) websites. I took many references by various web searches from Google and problem solutions from stackoverflow.
The fronted technologes credits goes to [https://www.w3schools.com/html/](https://www.w3schools.com/html/). For pyhton and django youtube channels such as Programming with Mosh, freecodecamp.org and ProgrammingwithHarry etc.

## Contact
- Brajeswar Lenka- LinkedIn(https://www.linkedin.com/in/brajeswar-lenka-4a28851b2/)
- Gmail (brajeswar.lenka@gmail.com) Feel free to contact me!

### Development
If you want to help me out with any development or bug fix, feel free to give a pull request I will be happy to collaborate with any python enthusiast.

