*** Settings ***
Library    Selenium2Library
*** Variables ***
${SiteUrl}    https://stackoverflow.com
${Browser}    Chrome
*** Test Cases ***
Test
    Open Browser and login
*** Keywords ***
Open Browser and login
    open browser    ${SiteUrl}    ${Browser} 