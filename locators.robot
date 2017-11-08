*** Settings ***
Library      jsonparser.jsonparse    ${path}    WITH NAME    source_attribute
Library    Collections

*** Variables ***
${path}    sample_json.json
*** Keywords ***
Initialise variable
    [Arguments]
    #Storing all the keys from json
    @{list_result} =    source_attribute.getting_keys_from_dictionary
    [Return]       ${list_result}
    set suite variable    ${list_result}
    EXTRACT_LIST_VARIABLES

EXTRACT_LIST_VARIABLES
    #Getting the lengh of list
    ${NUM}=  Get Length  ${list_result}
    :For  ${list_item}  IN RANGE    0    ${NUM}
    \   ${source_result} =    source_attribute.getting_attributes_of_phones    ${list_item}
    \    set suite variable    ${source_result}
    \    Getting Inside List


Getting Inside List
    #Extracting the keys
    :FOR  ${item}  IN  ${source_result}
    \    LOG    ${item}
    \    Extract the key and assign values

Extract the key and assign values
    :FOR    ${key}    IN    @{source_result.keys()}
    \    ${value}=    Get From Dictionary    ${source_result}    ${key}
    \    Set suite Variable    ${${key}}    ${value}
    \    Log    ${key},${value}
