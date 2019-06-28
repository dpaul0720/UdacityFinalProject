## Project Linux Server Configuration

The purpose of this project was to take a baseline installation of a Linux server and prepare it to host my web application. I had to secure my server from a number of attack vectors, install and configure a database server, and deploy my existing web applications onto it.


## Running the project

The IP address for this project is 

```
3.219.218.32
```

The SSH port used for this server was 
```
2200
```
The complete URL to my application is 
```
http://3.219.218.32/
```

Access the server with the ssh key in the in the "notes to reviewer" field by
```
ssh grader@3.219.218.32 -p 2200 -i ~/.ssh/finalproject
```

The software installed is as following
```
Apache2
mod_wsgi
SQLAlchemy
oauth2client
psycopg2
python
pip
Flask
PostgreSQL
Flask-SQLAlchemy
```

The Configurations is as following
```
Pass-phrase - grader
Database username and password - catalog:catalog
Database name - itemcatalog
```

Configurations changed:
```
Created new user grader and gave sudo access
Updated applications
Changed SSH port to 2200
Configured firewall
Deployed existing flask application
Changed Timezone to UTC
```

## Design

The design of this program was straightfoward. I first set up an server instance with amazon lightsail. Then I added and configured a user that met the specification. Then I used postgresql for my database and deployed my existing flask application.

## Authors

* **Paul Lee**

