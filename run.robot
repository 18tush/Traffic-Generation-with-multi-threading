*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Variables   vars.py
Variables   auth.py
Library     Browser

*** Variables ***
${browser}  Chrome
${options}      add_argument("--ignore-certificate-errors")      



***Keywords***
Open browser with proxy with user
    [Arguments]     ${user}        ${websites}
        ${caps}=  Evaluate  sys.modules['selenium.webdriver'].DesiredCapabilities.CHROME  sys, selenium.webdriver
        ${proxy}=  Create dictionary  proxyType=MANUAL  sslProxy=${ip_port}         httpProxy=${ip_port}
        Set to dictionary  ${caps}  proxy=${proxy}
        SeleniumLibrary.Open Browser  https://ip.zscaler.com        browser=Chrome  desired_capabilities=${caps}       options=add_argument("--ignore-certificate-errors")               
        maximize browser window

        input text      xpath://*[@id="username_input"]         ${user}[0]
        click element   xpath:/html/body/div/div/div/form/table[2]/tbody/tr/td/table[1]/tbody/tr[5]/td/table/tbody/tr/td[1]/input
        input text      xpath:/html/body/div/div/form/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td/div[2]/table[2]/tbody/tr/td/div/input   ${user}[1]
        click element   xpath:/html/body/div/div/form/table[2]/tbody/tr/td/table[1]/tbody/tr[3]/td/input

        Sleep       2
        ${from}=        Evaluate    ${counter}*${per_user}
        ${to}=          Evaluate    ${counter}*${per_user}+${per_user}
        FOR    ${website}      IN      @{websites}
                Log to console      ${website}
                SeleniumLibrary.Execute Javascript          window.open("${website}")
        END
        ${counter}=     Evaluate    ${counter}+1
        Log to console  ${counter}
        Log to console  ${from},${to},${user}
        Sleep       10
        SeleniumLibrary.close browser
