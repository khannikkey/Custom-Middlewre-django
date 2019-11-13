# Custom-Middlewre-django
How To Create Custome Middleware in Django
What is Middleware?

Middleware is a framework of hooks(plugin) into Django request-response processing. it is a lightweight, low-level plugin system for globally altering Django's input-output.

When to want to use Middleware?

if you want to change any activity during Pre-processing and Post-processing of request then we should go for Middleware

If You want to Run some funtionality before your View function execute then we will Use Middleware.

the main purpose is to alter request and response information

Now I think I have to keep it simple

So let's start.

    create a file in your app named as 'middleware.py'
    create a Class

eg. " class xyzFlowMiddleware():"

3. after that you have to define two mandatory functions

first one

    def __init__(self, get_response):

    self.get_response = get_response

this is because we want to work with the response and alter the response

second one

    def __call__(self, request):

    print("This is Before View Execute")


    response = self.get_response(request)


    print("This Code Will Execute After view Execute")


    return response

after defining call function, whatever code you write will execute at the time of sending the request from url to views

self.get_response will get the response from previous middleware

after getting the response whatever you will write will go with that response to user

don't forget to return the response

your middleware creation is done. now we have to register this

goto middleware section in setttings.py

if you want to register, follow the pattern

    #AppName.FileName.ClassName

    'CustMidApp.middleware.XyzFlowMiddleware',


for better understanding please refer my middleware code  
