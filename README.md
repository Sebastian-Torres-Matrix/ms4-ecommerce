# TITLE
![Multi Device Website Mockup]()
Visit the live website: [Electronic Demands](https://electronic-demands.herokuapp.com/) 

## Introduction 


## Table of Contents
* [UX](#ux)
    * [Project Goals](#project-goals)
    * [Site Owner Goals:](#site-owner-goals:)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
    * [Wireframes](#wireframes)
    * [Databases](#databases)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-implement)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libaries & Frameworks](#libaries-&-frameworks)
    * [Databases](#databases)
    * [Tools](#tools)

* [Testing](#testing)
 
* [Deployment](#deployment)


* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

* [Disclaimer](#disclaimer)

## UX 

### Project Goals :dart: 


### Site Owner Goals:


### User Stories :clapper: 
As a user i want to be able to.....
* :white_check_mark: view a list of all the products
* :white_check_mark: view a specific category of products
* :white_check_mark: view a list of products that are on sale
* :white_check_mark: sort the products by price
* :white_check_mark: sort the products by name
* :white_check_mark: sort products by category
* :white_check_mark: sort products by rating
* :white_check_mark: search products by name in a searchbox
* :white_check_mark: register to a personal account
* :white_check_mark: have a overview of my shopping bag and total amount
* :white_check_mark: change quantity of the product in the shopping bag
* :white_check_mark: to see an update of my shopping bag, when i add/delete a product
* :white_check_mark: have a pleasent, easy and secure payment process
* :white_check_mark: get an order confirmation, when payment/checkout process is confirmed 
* :white_check_mark: see my order history
* :white_check_mark: login and logout to my personal account
* :white_check_mark: read more about the company in a about page
* :white_check_mark: to contact the support if/when I have questions
* :white_check_mark: get more information about the product in a blog
* :white_check_mark: follow the company on social media

### Design Choices :art:

__Icons__


 __Typography__


__Color scheme__


### Wireframes
* The wireframes were created using [Balsamiq](https://balsamiq.com/).
    * Here is the link to see the [Wireframes]()

### Databases

__Users Collection__


__Reviews Collection__


## Features :mag_right:

### Existing Features


### Features Left to Implement


## Technologies Used :computer: 

### Languages
* HTML
* CSS 
* JavaScript 
* Python

### Libaries & Frameworks
* [Bootstrap](https://getbootstrap.com/) 
* [Django](https://www.djangoproject.com/) 
* [FontAwesome](https://fontawesome.com/)  
* [JQuery](https://jquery.com/) 


### Databases
* [PostgreSQL](https://www.postgresql.org/)
* [Sqlite3](https://www.sqlite.org/index.html)


### Tools :wrench:
* [Am I Responsive?](http://ami.responsivedesign.is/#) 
* [AWS S3 Bucket](https://aws.amazon.com/) 
* [Balsamiq](https://balsamiq.com/) 
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) 
* [Git](https://git-scm.com/) 
* [Github](https://github.com/) 
* [Gitpod](https://www.gitpod.io/) 
* [Google Fonts](https://fonts.google.com/)
* [Heroku](https://dashboard.heroku.com/apps) 
* [Stripe](https://stripe.com) 


## Testing :electric_plug:

## Deployment
### Run this project locally:

### Deploying MS4 Ecommerce to Heroku:
1. Create a requirements.txt file using the following command.
```
pip3 freeze > requirements.txt
```
2. Create a Procfile with the following command.
```
echo web: python3 app.py > Procfile
```
3. Push these created files to your repository.
4. Create a new app for this project on the Heroku Dashboard.
5. Select your deployment method by clicking on the deployment method button and select GitHub.
6. On the dashboard, set the following config variables:

Key | Value
-----|------
AWS_ACCESS_KEY_ID | <your_secret_key>
AWS_SECRET_ACCESS_KEY | <your_secret_key>
DATABASE_URL | <your postgres database url>
EMAIL_HOST_PASS | <your_value>
EMAIL_HOST_USER | <your_value>
SECRET_KEY | <your_secret_key>
STRIPE_PUBLIC_KEY | <your_value>
STRIPE_SECRET_KEY | <your_secret_key>
STRIPE_WH_SECRET | <your_secret_key>
USE_AWS | True

7. Click the deploy button on the Heroku dashboard.
8. The site has been deployed to Heroku.

## Credits 

### Content
* These websites, for the excellent content, with explanations and tutorials:
    * [StackOverflow](https://stackoverflow.com/)
    * [W3Schools](https://www.w3schools.com/)
    * [Youtube](https://www.youtube.com/results?search_query=django+tutorials)
    * [Django Documentation](https://docs.djangoproject.com/en/3.0/)
    * [Django-allauth Documentation](https://django-allauth.readthedocs.io/en/latest/) 
    * [Code Institute, Django module](https://courses.codeinstitute.net/program/FullstackWebDeveloper) 
 
### Media
* [Favicon.io](https://favicon.io/)
    * For the favicon used in the project.
* [Optimizilla](https://imagecompressor.com/)
    * Image compressor to shrink JPEG and PNG images. 
* [Pexels](https://www.pexels.com) 
    * For the background image used in the project.  
* [Amazon](https://www.amazon.com/s?k=smartwatch&ref=nb_sb_noss_1) 
    * For the product images used in the project.


### Acknowledgements
* Fellow Code Institute students on [Slack](https://slack.com/intl/en-se/). For the support and feedback.
* Tutor support and Student care from Code Institute. For the support, guidance and feedback.
* [Simen Daehlin](https://dehlin.dev/), for excellent mentorship, with great guidance and feedback. :trophy:
    * [Github](https://github.com/Eventyret)
    * [Linkedin](https://uk.linkedin.com/in/simendaehlin)


## Disclaimer 
* The content of this website is for educational purpose only. :heavy_exclamation_mark:

## Back to the top 
* [Table of Contents](#table-of-contents) :arrow_up: