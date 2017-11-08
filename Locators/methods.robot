*** Settings ***
Library    Selenium2Library
*** Variables ***
*** Keywords ***
Open Browser and login
    Log    ${FirefoxProfile}
    open browser    ${SiteUrl}    ${Browser}    ${FirefoxProfile}
    ${present}=  Run Keyword And Return Status    Element Should Be Visible    xpath=    ${Element_presence}
    Log ${present}
    Selenium2Library.Click Element    xpath=${user_login_xpath}
    Selenium2Library.Click Element    xpath=${user_password_xpath}
    Selenium2Library.Click Element    xpath=${user_password_xpath}
    Selenium2Library.Click Element    xpath=${Login_button}

Navigate to side menu
    Selenium2Library.Click Element    xpath=${side_menu}

Selecting from drop down
    Selenium2Library.Click Element    xpath=${ms3_xpath}
    Selenium2Library.Click Element    xpath=${operations}
    Selenium2Library.Click Element    xpath=${saveScenario}

Putting values in text boxes
    Selenium2Library.Click Element    xpath=${Test_input_Send_Keys}
    Selenium2Library.Click Element    xpath=${Sample_Input_Send_Keys}






