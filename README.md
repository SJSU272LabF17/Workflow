# Workflow Automation App
A web app built with Django on the server which provides automatic workflow and actions in a business process.

Instructions

1. Make sure Python(Python 2 >=2.7.9 or Python 3 >=3.4) is installed.
2. In terminal, cd to app root folder where requirements.txt is located.
3. Run: "pip install -r requirements.txt" in your shell, to install required packages.
4. Run: "python manage.py runserver" to start server (still in app root folder where manage.py is located).
5. Go to http://localhost:8000/ in the browser and check out the homepage.

Problem Statement

Process 9 is a process workflow automation. Process 9 will make the process workflow automation a template based service that can be deployed in a public cloud using container. The main features will be creating the process template, running instances of the template as a checklist and track progress and perform collaboration with your team. The purpose of Process 9 is to make the collaboration between each members in the team more efficient. Each members will be able to track and follow their tasks throughout Process 9. 

Architecture - MTV

1. Model (apps/first_app/models.py): builds database tables and handles all interaction with the database. It's now using sqlite for development and data is stroed locally in app/db.sqlite3 file. Mysql will be used to replace sqlite for final deployment. 
2. Templates (apps/first_app/templates): are served in their complete form to the client with all the html template files. Images and css stylesheets are located in apps/first_app/static folder.
3. Views (apps/first_app/views.py): get the right data for the right route delivered in the right form. Views handle the data we deliver to the user to view. Routes file which lists urls and the corresponding functions in the vews to run is located at apps/first_app/urls.py.

Technologies Used

HTML5, CSS3, Javascript, Jquery, Python, Django, Amazon Cloud

Features

1. The user can create a new checklist for the process or select a sample checklist.
2. The user can assign checklist tasks to team members.
3. The user can track the progress of the checklist and the work completed by each person to which the checklist is assigned.
4. A statistics and analysis report of the checklist is visible to the user who has created the checklist.




Contributors

1. Rohan Kelkar
2. Uttara Vishwas Kulkarni
3. Lu Yu
4. Hsien Fang Liu


