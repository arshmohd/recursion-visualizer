import os
import subprocess
import injectCode as ij 


def runCode(inputCode, inputFunctionName, inputFunctionCall):
    # On the frontend, we will parse the input to get the 
    # - function name 
    # - single function call
    #       - we will truncate this function call line and add it as a seperate parameter


    # All the inputs we will collect from the frontend:
    # inputCode here is truncated to exclude the single function call. 
    
    print(inputCode)

    readyToExe = ij.injectCode(inputCode, inputFunctionName, inputFunctionCall)


    with open("run.py", "w") as p: 
        p.write(readyToExe)
        p.flush()
    
    try:
        output = str(subprocess.check_output(["python3", "run.py"])) 
        output = output[3:len(output) - 4]
        return (True, output)
    except: 
        return (False, "Check that syntax is correct, or perhaps there is an issue in your specific implementation.")