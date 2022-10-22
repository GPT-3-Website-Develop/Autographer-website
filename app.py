from flask import Flask, render_template, request
import openai
from contextAndExamples import *
import random
import os
import json

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
            if maxTokens > 2048:
                maxTokens = 2048
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
        except:
            prompt = "Divide A by B stored in a variable result"

        # 40 0.09 1.0 Divide A by B stored in a variable result
        print(maxTokens, temperature, probability, prompt)

        openai.api_key = "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"

        response = openai.Completion.create(
            model="code-davinci-002",
            prompt="",
            temperature=0,
            max_tokens=256,
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
        print(str(response))
        # print(response.choices)
        json_data = json.loads(str(response))
        print(json_data)
        choicesDict = response["choices"][0]
        # json_data2 = json.loads(str(choicesDict))

        resultToDisplay = (choicesDict["text"])

    else:
        print("Working Get")
        outputColour = "bg-none"
        maxTokens = 40
        temperature = 0.09
        probability = 1.0
        resultToDisplay = False

    return render_template("index.html", outputColour = outputColour, maxTokens = maxTokens, temperature = temperature, probability = probability, response = resultToDisplay)
  

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)