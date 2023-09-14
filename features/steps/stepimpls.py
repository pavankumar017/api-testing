
from behave import *
import requests

@given('the book details are present')
def step_impl(context):
    context.payload = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bcdadf",
        "aisle": "227",
        "author": "John foe"
    }

@when(u'we execute the Addbook API call')
def step_impl(context):
    context.req = requests.post('http://216.10.245.166/Library/Addbook.php', json=(context.payload), headers={'Content-Type' : 'application/json;charset=UTF-8'})
    

@then(u'book is successfully added')
def step_impl(context):
    request_response = context.req.json()
    print((request_response))
    