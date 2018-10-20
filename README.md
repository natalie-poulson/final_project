# OutPACK


## Scope:
OutPACK is an app that allows users to plan, log and share all of their outdoor backpacking adventures in one place!

## Getting Started:
To run OutPACK on your local machine, clone the repository, then:

* Install requirements:
  * `pip3 install -r requirements.txt`

* Install PostGIS (https://postgis.net/install/):
  * `brew install postgis`

* Make migrations:
  * `python3 manage.py makemigrations`
  * `python3 manage.py migrate`
  * `python3 manage.py runserver`


## Built With:

* Django/Python

* Javascript/JQuery

* HTML/CSS/SASS

* PostgreSQL/PostGIS


## Third Party Apps:

* crispy_forms

* mapwidgets


## Users:
Our user is someone who enjoys the outdoors, traveling, planning, keeping track of memories, & sharing and receiving ideas for their next adventure. 


## Features:
* User signup, login, logout
* User profile create & edit
* Upload profile picture (default picture provided if left blank)
* View other user's profiles
* Create, edit, delete a new trip
  * Displays name of trail, permit info (optional), dates of trip, length of trip, and a section to plan what gear and food  to pack 
  * User's can select a point on a map to store the location of their trip
* Create, edit, delete posts about trips
  * Upload photos or write about your trip after you get back
* Search page allows users to view other user's trips to get ideas for their next adventure
* Users can share trips and posts with friends and family on Facebook and Google+ 
* Pretty URLs


## User Story: 
* A user will visit our landing where they have an option to sign-in or sign up
 * A first-time user will select the ‘sign up’ link which will bring them to a form that requests a username and password, which then goes through validation and confirmation before advancing 
  * When preliminary sign-up data is submitted, the user will be redirected to a profile page where they can create a profile customized with a profile picture, bio (optional), and current city (optional) information 
* If the user selects the  ‘sign-in’ button, they will be redirected to their profile page
 * Users can select icons from the nav bar containing links to:  
  * Profile: 
    * A user’s profile page showing their information, trips, posts and a map
  * Trips:
    * Displays all of the user's trips, both completed and upcoming
  * Start a New Trip:
    * User can create a trip by entereing a trail name, permit info (optional), dates, whether the trip has been completed, and the specific location by placing a marker on a map 
  * Search:
    * Users can search the trip database to see where other user's have gone to get ideas for their next adventure
    * Search resutlts return a link to matching trips and the profile page of the user who took the trip
  * Logout:
    * User can logout and will be redirected to the landing page
  
  
## Unsolved Problems...
* Modal glitches and design challenges with Django forms
* Google Maps Widget on load isn't correct size
* Deploying with GIS to Heroku
* Allow user's to break food planning down by day
* Add logic to check trip date and automatically change status of trip complete if date has passed
* Make delete confirmation notices more elegant
  

## Still to Come...
* Allow user's to opt out of sharing their trips and/or profile with other users
* Make the search feature dynamic and implement autocomplete
* Display a map on each user's profile page that displays pins from all of their completed trips
* Display maps on each trip page to show the general location of the trip
* Allow user's to draw lines (instead of a point) to capture their trip more precisely, especially useful for section hiking
* Sync with Google Calendar 
* Allow users to add collaborators to a trip, allowing for mutual editing/editing/memory storing
* Allow user's to upload videos
* Add commenting
* Add likes
* Add follows and a feed page
* Integrate a Weather API


## Links:

### Wireframes/Project Planning
* [Here](OutPACK.pdf)


### Herkou Link
* https://outpack.herokuapp.com/


### Created By
* [Natalie Poulson](https://github.com/natalie-poulson)
