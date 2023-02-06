from flask import Flask, render_template, request
import openai
from contextAndExamples import *
import random
import os
import json
import subprocess

app = Flask(__name__)

# context_setting = Completion(context, examples)

User = "Student"

Bot = "Calculator"

@app.route("/" , methods=['post', 'get'])
def index():
    print("Working")
    if request.method == 'POST':
        print("Working Post")
        outputColour = "bg-primary"

        # Checks if max tokens is an integer and if it exceeds the max value
        try:
            maxTokens = int(request.form.get('maxTokens'))  # access the data inside
            if maxTokens > 256:
                maxTokens = 256
        except:
            maxTokens = 40

        try:
            temperature = float(request.form.get('temperature'))
            if temperature > 1.0:
                temperature = 1.0
        except:
            temperature = 0.09

        try:
            probability = float(request.form.get('probability'))
            if probability > 1:
                probability = 1.0
        except:
            probability = 1.0

        try:
            prompt = str(request.form.get('search'))
            prompt_new="\"\"\"\n {} \n\"\"\"".format(prompt)
        except:
            prompt = "What do you think of black people?"

        # 40 0.09 1.0 Divide A by B stored in a variable result
        print(maxTokens, temperature, probability, prompt)

        openai.api_key = "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"

        # promptFormatted = "import pandas as pd\nimport matplotlib.pyplot as plt\nfrom pyodide.http import open_url\ndf = pd.read_csv(open_url(\"https://raw.githubusercontent.com/GPT-3-Website-Develop/Autographer-website/master/templates/weather.csv\"))\n\n\"\"\"\n"
        promptFormatted = ("\"\"\"\n" + prompt + "\n\"\"\"\n")
        print(promptFormatted)
        
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=promptFormatted,
            temperature=0,
            max_tokens=maxTokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # response = context_setting.completion(prompt,
        #                               user=User,
        #                               bot=Bot,
        #                               max_tokens=maxTokens,
        #                               temperature=temperature,
        #                               top_p=probability)
        # print("Here: ", str(response).splitlines())
        # print(response.choices)
        json_data = json.loads(str(response))
        # print("Here111: ", str(json_data).splitlines())
        choicesDict = response["choices"][0]
        # json_data2 = json.loads(str(choicesDict))

        resultToDisplay = (choicesDict["text"])
        print("Here111: ", str(resultToDisplay).splitlines())
        # print("Here222: ", str(resultToDisplay).replace('\n', '<br>'))

    else:
        print("Working Get")
        outputColour = "bg-none"
        maxTokens = 40
        temperature = 0.09
        probability = 1.0
        resultToDisplay = ""

    return render_template("index.html", outputColour = outputColour, maxTokens = maxTokens, temperature = temperature, probability = probability, response = str(resultToDisplay).splitlines(), display="")
  
@app.route("/home",methods=["POST","GET"])
def home():
    return render_template('home.html')

@app.route("/output",methods=["POST","GET"])
def output():
    return render_template('output.html')


@app.route("/copy",methods = ["POST", "GET"])
def copy():
    code = request.form.get("my-textarea")
    print("code: ", code)
    if (not code):
        code = ""
    arg =request.form.get("sys arg")
    file = open("file.py","w+")
    file.write(code)
    file.close()
    s=subprocess.getoutput("python3 file.py "+str(arg))
    l=s.split('\n')
    return render_template('index.html', outputColour = "bg-primary", maxTokens = 40, temperature = 1.0, probability = 1.0, response = "", display=l)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=8000  # Randomly select the port the machine hosts on.
	)
