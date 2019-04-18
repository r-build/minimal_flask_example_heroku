import json
from flask import Flask, request
from serve import useless_function  
from serve import get_keywords_api_python
from serve import get_keywords_api_r

# create an instance of Flask
app = Flask(__name__)

# Define our "ping" end point
@app.route('/ping')
def useless_output():
  return(useless_function())


# load our pre-trained model & function
keywords_api_r = get_keywords_api_r()
keywords_api_python = get_keywords_api_python()


# Define a post method for our API.
@app.route('/extractpackages_python', methods=['POST'])
def extractpackages_python():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json

    # use our API function to get the keywords
    output_data = keywords_api_python(input_data)

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response

# Define a post method for our API.
@app.route('/extractpackages_r', methods=['POST'])
def extractpackages_r():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json

    # use our API function to get the keywords
    output_data = keywords_api_r(input_data)

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response
