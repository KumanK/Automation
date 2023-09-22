*** Settings ***
Library    RPA.Windows
Library    RPA.Desktop.Windows
Library    RPA.Desktop
Library    RPA.Browser.Selenium
Library    config/json_parser.py


*** Variables ***
${EATON_CONFIG_FILE}=    config/eaton_config.json


*** Tasks ***
Open Eaton desktop application and login
    Open the Eaton desktop application
#    Validate the controller connection wizard opens successfuly
    Make controller connection
    Configure filter design conditions
*** Keywords ***
Open the Eaton desktop application
    ${path}=    get key from config	      ${EATON_CONFIG_FILE}  executable_path
    Windows Run     ${path}
    Control Window    name:"Manufacturing Suite"
    ${email}=    get key from config	      ${EATON_CONFIG_FILE}  email
    RPA.Desktop.Windows.Send Keys      ${email}
    RPA.Desktop.Press Keys     tab
    ${password}=    get key from config	      ${EATON_CONFIG_FILE}  password
    RPA.Desktop.Windows.Send Keys       ${password}
    RPA.Windows.Click        name:"Login"
    Sleep    3
Validate the controller connection wizard opens successfuly
    Control Window    name:"Manufacturing Suite"
    RPA.Desktop.Wait For Element        name:"Controller Connection"

Make controller connection
    Control Window    name:"Manufacturing Suite"
    RPA.Desktop.Press Keys     tab
    ${create_user_email}=    get key from config	      ${EATON_CONFIG_FILE}  create_user_email
    RPA.Desktop.Windows.Send Keys       ${create_user_email}
    RPA.Desktop.Press Keys     tab
    ${create_user_password}=    get key from config	      ${EATON_CONFIG_FILE}  create_user_password
    RPA.Desktop.Windows.Send Keys       ${create_user_password}
    RPA.Windows.Click        name:"Connect"

Configure filter design conditions
    Control Window    name:"Manufacturing Suite"
    Sleep    5
    Maximize Window
    RPA.Windows.Click        BoundingRectangle:"[l=2,t=669,r=396,b=764]"


