# Python_Selenium_Json_Robotframework

This sample framework is designed in such a way that it act as a starting point for some one who is new to the framework side and want to have a sample framework.

Framework is divided into for components

1) Xpath Data for all the pages 

sample_json.json will contains all the xpaths which user is going to have for their automation setup
each node is named after each pages , so suppose if you want xpath for login page , you can define that in login_node.

2) Json parser in python to parse the json data

A json parser which will parse the json data and will bring them to be usd by robotframe work

3) Bunch of Robot files which will have the test cases and keywords to run the show 

Locators->methods.robot have all the keywords 
Locators->locators.robot intialises all the locators as variables
main.robot->this is the main script which will run


4)Bokeh.py to do the data analytics 
this Bokeh file will automatically process the "output.xml" generated after running of robot framework and plot the data graphically
if you wish to use anyother robotfile which is not in current directory , then you need to edit this file and replace 'output.xml' from 'path/output.xml'


Run ->

1)pybot main.robot
2)Python Bokeh.py