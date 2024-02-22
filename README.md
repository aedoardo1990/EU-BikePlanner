# EuroBike

Welcome to EuroBike!

EuroBike is a bike planning app designed to help bikers to travel long distance across Europe. The function of the app is twofold: provide biking routes across multiple European States and remove the hassle of what to pack for a long trip. It is targeted towards bikers of all levels (basic, intermediate, pro) offering different packing solutions for each of them. 
The site acts as a repository for trips where users can store all the data for the organisation of their next trips.

The live link of our site can be found here - [EuroBike](https://eu-bike-planner-4c87e2f122b8.herokuapp.com/)

## ![Responsive Mockup](static/images/readme/mock-up.png)

## Table of Contents
- [EuroBike](#eurobike)
  * [User Experience (UX)](#user-experience-ux)


## User Experience (UX)

An user of EuroBike would be someone who is passionate about biking long distance and who likes travelling by bike for multiple days. For such trips, packing smartly to reduce weight and use less space is essential. Or alternatively, packing everything you need could be for some bikers top priority rather than weight. 
On top of that, a visitor of EuroBike can find in the app a map of the chosen route. 

### User Stories

#### As a user I want to:

- log in or log out of my account so that my account is safe
- register an account so that I can add, edit or delete my bike tour plans
- login so that I can access my booked bike tour plans
- view a list of all the bike routes
- view the description and map of each route so that I can choose which route suits me
- select bike routes from a list so that I can plan which route to do
- select among different options for different categories of items to organise what to pack for the trip
- add additional items if anything is missing in the preselected packing options
- view the list of items for the trip so that I can ensure if things need to be added or deleted
- update a list item so that I can adjust accordingly my iventory for the trip
- delete a trip from the my booked trips, if I am not going to do it anymore
- contact Site's Admin so that I can send my questions/ feedback regarding the use of the application

#### As a site administrator I want to:
- allow only registered users to use the website so that they can only access their own bike trip plans
- access the admin panel so that I can check and manage the items of the bike tour plans of each user
- manage the list of bike routes and items so that I can keep up-to-date routes and lists of items
- review messages sent by users so that I can address their requests
- delete read & actioned users messages so that I do not action the same message twice

## Design

The site has a clean and simple design to provide users with easy access to essential information for their trips. 

### Color scheme

The main colors chosen for the website are those of the Europe Union flag. This aims at conveying the fact that the project wants to help bikers travelling across Europe.

![Colour Palette](static/images/readme/palette.png)

The background image of the homepage has different shades of blue, aiming at fitting with the blue color of the header and the footer. Blue is a calming color and the image wants to remind bikers of the calming and freeing sensation of biking, with wind in the hair and the feeling that there are no boundaries when you bike. 


The Gold metallic color of the European Union flag can be found as well in the footer: social media icons turn to Gold when the user hover over them. 

### Imagery

The background image of the homepage display 2 bikers in a beautiful natural landscape. The purpose is to motivate bikers to discover Europe and its immense beauty by slow travelling on their bike. Slow travelling can allow to experience at 360 degrees the new surroundings in which someone cycles.

In the Routes page there is an image for each Route. Different images for each route want to communicate the richness and diversity that exist in Europe, from Stockholm to Rome, from Lisbon to Moscow. 

A map with all the Routes is available in the Homepage. Individual map of each Route can be displayed in the site (for more details about it, check the Features section). 

### Fonts

The Font chosen for the site is Montserrat. The font was imported via Google Fonts. The back-up font is sans-serif.

### Structure

The project consists of one Django application - named bike_planner. The website has the following pages and each page the corresponding functions:

- index.html -> home page containing essential info about the website
- add-trip.html -> to create a trip by choosing route and selecting which items to pack 
- trip-details.html -> when the trip is booked, the user is redirected to this page, where all the booked info are visible + a map of the selected route
- my-trips.html -> each logged in user can check here his/her booked trips
- edit-trip.html -> to edit the details of a booked trip
- delete-trip.html -> to delete a booked trip from my-trips.html
- routes.html -> to view a list of all the routes. This page is accessible both from logged in and logged out users. 
- route_details.html -> to check the details of each route (photo, description and map). This page can be viewed both from logged in and logged out users. 
- contact.html -> to allow the user to send messages about the site to Admin. This page can be displayed both from logged in and logged out users. 
- contact-received.html -> when the contact form is sent, this page is displayed

There are also a few customised pages related to user's authentication option with Alluath:

- login.html
- logout.html
- signup.html


### Wireframes

The wireframes for the "EuroBike" website were created with Figma.

<details>

<summary>Homepage</summary>

![Homepage](static/images/readme/homepage-figma.png)
</details>

<details>

<summary>Routes</summary>

![Routes](static/images/readme/routes-figma.png)
</details>


<details>

<summary>Add Trip</summary>

![Add Trip](static/images/readme/addtrip-figma.png)
</details>

<details>

<summary>My Trips</summary>

![My Trips](static/images/readme/mytrips-figma.png)
</details>

<details>

<summary>Trip Details</summary>

![Trip Details](static/images/readme/tripdetails-figma.png)
</details>

<details>

<summary>Contact</summary>

![Contact page](static/images/readme/contact-figma.png)
</details>

## Agile Methodology 

Github projects was used to manage the development process using an agile approach. Please click <a href=" https://github.com/users/aedoardo1990/projects/3" alt="link to Kanban Board"> here</a> to view the User Stories in the Kanban board.

A Github Issue was created for each User Story. Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. Not all the User Stories were completed exactly as defined when they were first created. However the differences between the conception of the User Stories and the Final Site are documented in the comments of each User Story. 

## Data Model

Principles of Object-Oriented Programming were used throughout this project. 

Django AllAuth was used for the user authentication system.

The main Model of the app is the Trip model. It allows users to add trips. The trip author is a foreign key to the User model given a trip can only have one author.

The following 9 models are linked by a Foreign Key to the Trip Model and they enable the below actions to a site visitor:
- Route -> choose a route from a preselected list 
- Bike -> choose a bike type from a preselected list
- Clothes  -> select clothing equipment from a preselected list
- Repair -> choose a repair kit from a preselected list
- Bags -> select a bag type from a preselected list
- Sleep -> select a sleeping kit from a preselected list
- Electric -> choose a set of electronics from a preselected list
- Toilet -> choose a set of toiletries from a preselected list
- Cook  -> select a cooking kit from a preselected list

The Route model allows as well to display all the routes under the Routes tab and to view the photo, the description and the map of each route. 

On the top of the mentioned models, there is as well a Contact model, which enables the User to send messages to the Admin, and the Admin to view and manages the messages of site visitors. This model can be accessed by a logged out User too. On the contrary, when the User is logged in, the Name and Email fields will be autopopulated with the User's data.

The diagram below is a detailed view of the database schema.

![Diagram](static/images/readme/EuroBikeDiagram.png)

## Messages and interaction with users 

<details>
    <summary>Messages updating the user when an action has been completed.</summary>

- Login successful
![Login](static/images/readme/login.png)

- Trip created
![Trip created](static/images/readme/trip-created.png)

- Date can not be in the past
![Date not in the past](static/images/readme/date-past.png)

- Trip edited
![Trip edited](static/images/readme/trip-edited.png)

- Trip deleted
![Trip deleted](static/images/readme/trip-deleted.png)

- Contact form sent
![Contact form sent](static/images/readme/form-sent.png)

- Logout successful 
![Logout successful ](static/images/readme/logout.png)

</details>

## Admin Panel - Superuser 

In the Admin Panel the Admin/ Superuser has full access to CRUD functionality to create, edit or delete users' trips and the available packing options in the website regarding the following items: bags, bike types, clothes, cooking kit, electronics, toiletries, repair kit, routes, sleeping kit. 
In the Admin Panel the Superuser can as well address messages sent by site visitors via the contact form.

![Admin Panel](static/images/readme/superuser.png)

## Technologies used 

- [Heroku](https://www.heroku.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://gitpod.io/) 
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [draw.io](https://app.diagrams.net/) - to create the Database diagram
- [Colors](https://coolors.co/) - to create the color palette of the readme
- [iloveimg](https://www.iloveimg.com/) - to compress and crop images
- [tiny-img](https://tiny-img.com/webp/) - to convert images to webp format - since there are lots of images in the site, the webp format allows the website to be lighter when loading 
- [Figma](https://www.figma.com/)

### Languages

- HTML
- CSS
- JavaScript
- Python

### Libraries & Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

### Django Packages

- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Summernote](https://summernote.org/)
- [Cloudinary](https://cloudinary.com/)





## Testing 

### HTML Validator
<details>

<summary>The website was validated by URI into the validator. No errors found.</summary>

- index.html
![HTML Validation](static/images/readme/index.png)

- add-trip.html
![HTML Validation](static/images/readme/add-trip.png)

- my-trips.html
![HTML Validation](static/images/readme/my-trips.png)

- trip-details.html
![HTML Validation](static/images/readme/trips-details.png)

- routes.html
![HTML Validation](static/images/readme/routes.png)

- route_details.html
![HTML Validation](static/images/readme/routes-details.png)

- contact.html
![HTML Validation](static/images/readme/contact.png)


</details>

### CSS Validator
<details>

<summary>No errors found for the CSS validator. There are 6 warnings, code from those lines was taken from the Bootstrap Rosie walkthrough of CI</summary>

![CSS Validation](static/images/readme/css-validator.png)

</details>

### PEP 8 Validator
<details>

<summary>No error found for the PEP8 validator</summary>

1- bike_project:
- urls.py
![PEP8 Validation](static/images/readme/urls-py.png)

2- bike_planner app
- admin.py - imports from .models have been divided on 2 lines (line 2 and 3 of admin.py) to reduce line 2 to less than 80 digits and to pass PEP validator
![PEP8 Validation](static/images/readme/admin-py-.png)

- forms.py
![PEP8 Validation](static/images/readme/forms-py.png)

- models.py
![PEP8 Validation](static/images/readme/models-py.png)

- views.py
![PEP8 Validation](static/images/readme/views-py.png)

- urls.py
![PEP8 Validation](static/images/readme/bike-planner-urls-py.png)

</details>

### Lighthouse Testing 

Here below the score resulting from Lighthouse testing for the Website.

![Lighthouse testing](static/images/readme/lighthouse.jpeg)

### Browser testing

The Website was tested on Google Chrome, Microsoft Edge, Safari, and Firefox with no issues.

### Device testing

The Website was tested on the following devices, OnePlusNord10, iPhone13 mini, MacBook, laptop Acer Swift SF314-43 and created for the following screen sizes: 320px, 576px, 768px, 992px, 1240px and up.

### Mentor, family and friends testing

My mentor, my family and friends checked the site and helped to identify bugs and get a feeling about how the user-experience is perceived by visitors of the site.





## Features

### Existing Features 

#### Maps
user when clicking on a Route in the Routes page. When an user will create a new trip, the map of the selected route will appear. 













