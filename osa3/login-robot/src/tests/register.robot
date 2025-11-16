*** Settings ***
Resource  resource.robot
Test Setup Register Setup

*** Keywords ***
Register Setup
    Input New Command
    
*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle
    Input  New Command
    Input Credentials  kalle  jgjrlgr
    Output Should Contain  User with username kalle already exists