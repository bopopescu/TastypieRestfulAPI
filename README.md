<head>
  <style>

  ul {margin-left:40px;line-height: 20px;list-style-type: none;}
  ul li{padding-bottom:10px;}


  </style>
</head>
<div style = "padding:80px;">
<h1>Purpose</h1><br><br>

This project is an exercise in making a barebones Restful API. Simple authentication and lightweight processing through the TastyPie django library. Documentation is as follows: <br><br>

<h1>QuickStart</h1>

There are a few endpoints each with their own purpose. Here is a quick start guide:

Setup
<ul>
    <li>  post_data = {'info': 'Bought Two scoops of Djangoa'} </li>
    <li>  headers = {'Content-type': 'application/json'} </li>

    <li>  See Below for further implementation instructions </li>
</ul>
<h3>Endpoints</h3>
<ul>
      <li style="text-decoration:underline;">Note: All of these can be done via browser</li>
    <li>    Logging In --> https://testerapi.herokuapp.com/signup/{{ USERNAME }}/PASSWORD </li>
    <li style = "margin-left:100px;">                  Replace PASSWORD with desired values </li>

    <li>    Logging out --> https://testerapi.herokuapp.com/logout </li>

    <li>    Get Records (Get) --> https://testerapi.herokuapp.com/api/v1/entry/?format=json&username={{ USERNAME }}&api_key={{ API_KEY }} </li>
    <br><li > <span style = "text-decoration:underline;"> All of these need to be done programmatically. </span><span style = "text-decoration:none;"> (You need to pass in the header and data attributes which can only be done with CURL, requests or other HTML library)</span> </li>
    </ul>
    <ul>
    <li>    Create a Record (Post) --> https://testerapi.herokuapp.com/api/v1/entry/?username={{ USERNAME }}&api_key={{ API_KEY }} </li>

    <li>    Edit a Record (Put) --> https://testerapi.herokuapp.com/api/v1/entry/NUMBER?username={{ USERNAME }}&api_key={{ API_KEY }} </li>

    <li>

      Delete a Record (Delete) --> https://testerapi.herokuapp.com/api/v1/entry/NUMBER/?username={{ USERNAME }}&api_key={{ API_KEY }} </li>
</ul>

<h1>How To Use</h1>

<ul>
<li><b>Step 1:</b> Get an Access key

go to https://testerapi.herokuapp.com/signup/username/password where you put whatever username and password you want to do. From there you can get your Access key

</li>
<li><b>Step 2:</b> Make a Post Transaction
<ul>
<li>
</li><li>    The Post Request will come through a headers based http response. This must be done programmatically through the curl library or requests library. I have included instructions for both.

</li><li>
                   curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"info":"this is a new comment"}'

          </li><li>         -or-
</li><li>
</li><li>        $python
</li><li>        >>> post_data = {'info': 'Bought Two scoops of Djangoa'}
</li><li>        >>> headers = {'Content-type': 'application/json'}
</li><li>        >>> #Note: Remember to switch the below username and api-key to your specific credentials.
</li><li>        >>> r = requests.post("http://localhost:8000/api/v1/entry/?username={{ USERNAME }}&api_key={{ API_KEY }}", data=json.dumps(post_data),

</li>
</ul>
<li><b>Step 3:</b> Check to see your transaction worked

        The Post Request will respond a 201 created response. To check this navigate your browser to https://testerapi.herokuapp.com/pi/v1/entry/?username={{ USERNAME }}&api_key={{ API_KEY }}

</li>
<li><b>Step 4:</b> Experiment with other Endpoints

        Now that you have your API-Key interacting with data your create is a snitch! You will only have access to your user's data so if you want to create a new user you can just renavigate to https://testerapi.herokuapp.com/signup/{{ USERNAME }}/PASSWORD and you will get a new {{ API_KEY }} specific to that person's scope.

      https://testerapi.herokuapp.com/pi/v1/entry/?username={{ USERNAME }}&api_key={{ API_KEY }}
  </li>

</ul>




<br><br>

<h2>Curl Documentation</h2><br><br>

This project was built on Django and Python on the backend. Custom CSS/HTML, mobile responsive front end, and a Postgres Database. The application is hosted on Heroku's free tier service and the static files hosted on AWS servers.
<ul>

  <li>

 POST (Create)
 curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"info":"text"}' http://localhost:8000/api/v1/entry/
</li><li>
 PUT (Edit)
 curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"info": "This will probably be my last post." }' http://localhost:8000/api/v1/entry/4/
</li><li>
 Collection of PUT
 curl --dump-header - -H "Content-Type: application/json" -X PUT --data '{"info": 'goodday'}' http://localhost:8000/api/v1/entry/
</li><li>
 Deleting a Record
 curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/4/
</li><li>
 Deleteing many Records
 curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/entry/
</li>

</ul>

<h2>Requests Library</h2><br><br>



  <ul><li>
    POST (Create):
    <li> post_data = {'info': 'Bought Two scoops of Djangoa'}
    </li>
    <li> headers = {'Content-type': 'application/json'}</li>
    <li>
        r = post("http://localhost:8000/api/expense/?username={{ USERNAME }}&api_key={{ API_KEY }}", data=json.dumps(post_data), headers=headers)
</li><li>


Other Endpoints can be found above...
