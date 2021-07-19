# AWWWARDS
### Star--Awwwards 

## Author
Juma Allan.

## Description
Star--awwwards is a Django web application where  registerd users can post project(s) they have created and get it reviewed/rated by their peers.


## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.8.10
3. Postgres
4. python virtual environment (virtual:venv).
5. Text editor - preferably Visual Studio Code Editor.

### Clone the  project Repo
Run the following command on the terminal:
`git clone https://github.com/juma-moringa/Star-Awwwards..git`
* cd Instagram

###  Install and activate virtual environment
Activate virtual environment using python3.8 
1. Install
* python3 -m venv virtual
2. Activate
* source virtual/bin/activate

### Install dependancies
Install  all dependancies that will make the app run/function
* pip install -r requirements.txt

### Create the Database
* psql
* CREATE DATABASE STAR-AWWWARDS;


### Make Migrations
* python3 manage.py makemigrations starproject(App name)
* python3 manage.py migrate

### Run the app
* python3 manage.py runserver
* open your browser with the local host; `127.0.0.1:8000` provided on the terminal

## Testing the application
* python3 manage.py test starproject

## Admin dashboard
* The admin dashboard can be accessed from the dropdown menu just below the profile icon.
* Firstly you must be on the homepage to access it.
`Username: Admin`
`Password: Access254`

## Technologies used
    - Python 3.8.10
    - HTML
    - Django 3.2.5
    - Bootstrap 3
    - Heroku
    - Postgresql
    - GIT

## Enjoy :)


## Live Link

[View Live Site.]()

## License

Star--Awwwards is under the [MIT](LICENSE) license.

@Jaycreations-2021.