# My Poll Project
A django website app to host polls

## Table of Contents
1. Usage
2. Run With Virtual Environment
3. Run With Docker
4. Preview
5. Contributing

## Usage
This website app will allow polls to be hosted for any variety of topics (the current website hosts Soccer Polls and a preview will be shown in the Preview section).
However, at this stage, access to Soccer Polls will only be given on request.

# Run With Venv
The first step to run this website app with a virtual environment is to create a local directory and clone this repository into the local directory. 

Create a virtual environment by running the following commands: (NB! make sure the working directory is the directory with this cloned repository)

pip install venv --user

Now that the python package for a virtual environment is installed, create the virtual environment:

python -m venv virtual_environment_name  

Run the following command to activate the virtual environment:

(Windows) source virtual_environment_name/Scripts/activate
(Linux) source virtual_environment_name/bin/activate

Now that the virtual environment is activated, install Django using the requirements.txt file:

pip install -r requirements.txt 

After all requirements all installed, change to the 'poll_project' folder (the project folder) and run this command to start up the server and go to the website by clicking on the link provided:

python manage.py runserver 

The website can now be viewed on localhost.

## Run With Docker
A repository in Docker Hub already exists with a docker container to run the website app. 

Using Docker locally:
Install Docker Desktop and follow the installation setup steps.

Once installation has been completed, open a terminal and run the following command:

docker run -it -p 80:8000 --name docker_name cgopal1/level-3-capstone-1

Click on the link provided to go to the website app.

Using Docker Playground:
Click on this link:

[Docker Playground](https://labs.play-with-docker.com/)

Create a Docker Hub account and sign in.

Add an instance and run this command (same as above):

docker run -it -p 80:8000 --name docker_name cgopal1/level-3-capstone-1

Click on the link provided to go to the website app.

## Preview
Here is a preview of Soccer Polls:

![soccer_polls](soccer_polls.png)

## Contributing
All ARE WELCOME TO CONTRIBUTE