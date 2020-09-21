import flask 
from flask import request
from flask_cors import CORS
import parseinput as pi
import remoteCodeRunner as rc

app = flask.Flask(__name__) 
CORS(app)

# for each flask request, we need: 
# - data in the body to represent function logic
# - data in the parameters to represent function name and function call
# if either is missing, we send back an error message. If the remote 
# code execution raises an error, we send back that error message as well. 

@app.route('/execute', methods=['POST'])
def execute(): 
    if 'funcName' in request.args and 'funcCall' in request.args: 
        funcName = request.args['funcName'] 
        funcCall = request.args['funcCall']
        body = str(request.data)
        inputCode = pi.parseInput(body)
        functionTrace = rc.runCode(inputCode, funcName, funcCall)

        if functionTrace[0]:  
            # success case
            # set response status to 200
            return functionTrace[1], 200
        else: 
            # case of invalid value
            # set reponse status to 403
            return functionTrace[1], 403
        return inputCode
    else: 
        # case of an invalid request
        return "Please specify both the function name and the initial function call."

if __name__ == "__main__": 
    app.run()