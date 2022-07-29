*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
# Variables   vars.py
# Variables   auth.py
# Library     Browser
Resource    run.robot
# Variables   run.py

*** Variables ***
${browser}  Chrome
${options}      add_argument("--ignore-certificate-errors")      



*** Test Cases ***

Open browser with proxy  
    FOR     ${user}     IN         @{users}[1:2]         @{websites}
        Open browser with proxy with user       ${user}
        Log to console      1
    END