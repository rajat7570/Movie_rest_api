# Movie_rest_api  
## Movie detail rest api.
Some key points:
  * Built using django rest framework
  * Movie data api. 
  * Need login to view api data.
  * User registration
  * searching the movies based on title
  * detail info of each movie
  * authenticate user can perform CRUD operation easily.  
  
To start the api on your local server 
  
   * open command prompt and go to project directory
   * turn on the virtual environment
      > myvenv\Scripts\activate
   * migrate the data
      > python manage.py makemigrations
      
      > python manage.py migrate
   * run the server
      > python manage.py runserver

### User visit api
![](ScreenShots/Home.png)
### User Registration  
![](ScreenShots/registration.png)  
### After successful registration  
![](ScreenShots/after_regis.png)
### User Login to api
![](ScreenShots/Login.png)  
### Now data in api are visible and user can see all data and can post new data to existing data  
![](ScreenShots/index.png)
### Accessing indivisual data and can perform update and delete operation  
![](ScreenShots/indivi.png)
### Search movie title  
![](ScreenShots/search.png)  
![](ScreenShots/search_res.png)
