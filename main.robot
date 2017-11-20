*** Settings ***
Library    Selenium2Library
Resource    Locators/all.robot
Suite Setup    Initialise variable

*** Variables ***
#${Browser}    Chrome
#${SiteUrl}    http://demo.mahara.org
*** Test Cases ***
Login_Test
   [documentation]
    [Tags]    Sanity Test    Integration Test
    Log    ${Hello4}
    Open Browser and login

Login_to_second_page
    [Documentation]
    [Tags]    Integration Test
    Navigate to side menu

Login_to_third_page
    [Documentation]
    [Tags]    Production Test
    Selecting from drop down

Filling_text_boxes
    [Documentation]
    [Tags]    Defect
    Putting values in text boxes
