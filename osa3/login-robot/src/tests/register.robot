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

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalleyippee
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle wow  tyjgelkge
    Output Should Contain  Password needs to include numbers

Register With Valid Username And Too Short Password
    Input Credentials  kalle  ty
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  tyjgelkge
    Output Should Contain  Password needs to include numbers