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

