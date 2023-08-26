from flask import Flask, render_template
import openai

app= Flask(__name__)

openai.api_key= "hide_your_api_key"

@app.route('/')
def generate_image():
    prompt= "summer morning on wheat fields"

    response= openai.Image.create(prompt= prompt, n=1, size= "256x256")

    image_url= response['data'][0]['url']

    return render_template('image.html', image_url= image_url)

if __name__== "__main__":
    app.run(debug= True)