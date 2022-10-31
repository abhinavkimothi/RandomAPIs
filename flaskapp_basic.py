from flask import Flask

'''
Flask is a web framework, it’s a Python module that lets you develop web applications easily.
Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions.
jinja2 is a popular template engine for Python
'''

#Flask Constructor
app = Flask(__name__) #The flask constructor takes the name of the current module

'''
To now create URL for accessing the functions we'll have to specify routes.
App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
In flask we use the @app.route decorator which will take the URL as a parameter
'''

#First create the root URL using '/' as the address. This will be the homepage
#In this example, because we're deploying on localhost:5000, the response of this function will be on localhost:5000
@app.route('/')
def index():
    return 'Application Works'


#Next, let's route to a sub-page called hello. We'll use '/hello' as the address in app.route decorator
#In this example, this function will respond at localhost:5000/hello
@app.route('/hello/')
def hello():
    return 'Hello World!'

#Another functionality is dynamic URLs. In this case if the response is dependent on an url entity, we can pass the entity in <>
#In this example, localhost:5000/hello/foo will generate a response of Hello foo! and localhost:5000/hello/bar

@app.route('/hello/<user>/')
def userf(user):
    return f'Hello {user}!'



'''
Finally to run the application we use app.run
app.run allows you to set the host address, the port number, debug and other options
By default the application will run on localhost and port 5000 with debug mode off
if __name__ == “main”: is used to deploy the app only if the file was run directly, and not imported
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

'''    
You will get a WARNING: This is a development server. Do not use it in a production deployment
To use a WSGI server you can use serve as mentioned in the lines below

    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
'''



