# email_checker_api
Email Checker API runs on Python 3.7

## Install Requirements
`pip install -r requirements.txt`

## Run API Server
`python api.py`

## Send List of Emails to Server
`curl -H "Content-Type: application/json" -X POST -d '{"email_list": ["test.email@gmail.com", "test.email+spam@gmail.com", "testemail@gmail.com", "alfonso@gmail.com"]}' http://127.0.0.1:5000/`

## Run Test Suite
`python test_email_list_checker.py`