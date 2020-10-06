Description: This package contains all the dependencies for the web application ‘Routelanta’. 
    Routelanta allows users to choose their location and desired level of run difficulty on an interactive map of Atlanta. Based on the user’s input parameters, suggested routes will be returned to them. Included in the package is an ‘activities.txt’ file that contains a toy sample of API called routes in JSON format. This is where future routes can be added.
    There is also a python script called ‘project_csv_writer.py’ that will convert the JSON file into a csv file called ‘acts_rows.csv’ which is then passed into the main javascript found in ‘index.html’ The ‘d3-tip.min.js’ and ‘d3.min.js’ are necessary for handling the data and the ‘Polyline.encoded.js’ is needed for putting the routes onto the map.

Installation: Once the package has been downloaded, unzip the file to the location of your choosing. 
    No outside packages need to be installed to run the application, but some might need to be installed for adding/manipulating the underlying data.

Execution: Assuming that you have some version of python installed on your computer and added to your path, the quickest way to demo the application is by starting a local host server. 
    To do this, simply start the command prompt and cd into the ‘Code’ folder. After you have changed to this directory, type the following into the command prompt and hit enter: ‘python -m http.server 8888’. This will start a local server on your computer that should be running ‘index.html’. To access this server, start google chrome and navigate to the following URL: ‘localhost:8888’.
