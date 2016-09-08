<h1>Purpose</h1><br><br>

This project is an exercise in making a barebones Restful API. Simple authentication and lightweight processing through the TastyPie django library. Documentation is as follows:

Setup

There are a few endpoints each with their own purpose. Here is a quickstart guide:

Setup

      post_data = {'infoa': 'Bought Two scoops of Djangoa'}
      headers = {'Content-type': 'application/json'}

      See Below for further implementation instructions

Endpoints

        Logging In --> https://testerapi.herokuapp.com/signup/USERNAME/PASSWORD
                      Replace username and password with desired values

        Logging out --> https://testerapi.herokuapp.com/logout

        Get Records (Delete) --> https://testerapi.herokuapp.com/api/v1/entry/username=USERNAME&api_key=API_KEY

        Create a Record (Post) --> https://testerapi.herokuapp.com/api/v1/entry/?username=USERNAME&api_key=API_KEY

        Edit a Record (Put) --> https://testerapi.herokuapp.com/api/v1/entry/NUMBER?username=USERNAME&api_key=API_KEY

        ??Delete a Record (Delete) --> https://testerapi.herokuapp.com/api/v1/entry/NUMBER?username=USERNAME&api_key=API_KEY


<h1>How To Use</h1>


Step 1: Get an Access key

go to https://testerapi.herokuapp.com/signup/username/password where you put what ever username and password you want to do. From there you can get your Access key


Step 2: Make a Post Transaction

        The Post Request will come through a headers based http response. This must be done programmatically through the curl library or requests library. I have included instructions for both.


                   curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"info":"this is a new comment"}'

                   -or-

                  $python
                  >>> post_data = {'infoa': 'Bought Two scoops of Djangoa'}
                  >>> headers = {'Content-type': 'application/json'}
                  >>> #Note: Remember to switch the below username and api-key to your specific credentials.
                  >>> r = requests.post("http://localhost:8000/api/v1/entry/?username=USERNAME&api_key=API_KEY", data=json.dumps(post_data),


Step 3: Check to see your transaction worked

        The Post Request will respond a 201 created response. To check this navigate your browser to https://testerapi.herokuapp.com/pi/v1/entry/?username=sheryl&api_key=API_KEY


Step 4: Experiment with other Endpoints

        Now that you have your API-Key interacting with data your create is a snitch! You will only have access to your users data so if you want to create new user you can just renavigate to https://testerapi.herokuapp.com/signup/USERNAME/PASSWORD and you will get a new API_KEY specific to that persons scope.

         https://testerapi.herokuapp.com/pi/v1/entry/?username=sheryl&api_key=API_KEY





<br><br>

<h1>Design</h1><br><br>

This project was built on Django and Python on the backend. Custom CSS/HTML, mobile responsive front end and a Postgres Database. The application is hosted on Heroku's free tier service and the static files hosted on AWS servers.


 POST (Create)
 curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"sdf":"sdlkfj","hashtag": "Another Post","user": "/api/v1/user/1/"}' http://localhost:8000/api/v1/entry/

 PUT (Edit)
 curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"body": "This will probably be my last post.", "pub_date": "2011-05-22T00:46:38", "slug": "another-post", "title": "Another Post", "user": "/api/v1/user/1/"}' http://localhost:8000/api/v1/entry/4/

 Collection of PUT
 curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"objects": [{"body": "Welcome to my blog!","id": "1","pub_date": "2011-05-20T00:46:38","resource_uri": "/api/v1/entry/1/","slug": "first-post","title": "First Post","user": "/api/v1/user/1/"},{"body": "I'm really excited to get started with this new blog. It's gonna be great!","id": "3","pub_date": "2011-05-20T00:47:30","resource_uri": "/api/v1/entry/3/","slug": "my-blog","title": "My Blog","user": "/api/v1/user/2/"}]}' http://localhost:8000/api/v1/entry/

 Deleting a Record
 curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/4/

 Deleteing many Records
 curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/

 r = post("http://localhost:8000/api/expense/?username=sheryl&api_key=1a23", data=json.dumps(post_data), headers=headers)

 http://localhost:8000/api/v1/entry?format=json&username=sheryl&api_key=1a23
 post_data = {'infoa': 'Bought Two scoops of Djangoa'}
 headers = {'Content-type': 'application/json'}
 r = requests.post("http://localhost:8000/api/v1/entry/?username=sheryl&api_key=1a23", data=json.dumps(post_data), headers=headers)


 r = requests.post("http://localhost:8000/api/v1/entry/?username=kevin&api_key=1a23", data=json.dumps(post_data), headers=headers)
 http://localhost:8000/api/v1/expense/?format=json&username=kevin&api_key=1a23


 r = requests.post("http://localhost:8000/api/v1/expense/?username=kevin&api_key=1a23", data=json.dumps(post_data), headers=headers)
