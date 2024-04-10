# Import necessary libraries and modules
from flask import Flask, render_template, request, redirect
import gpt_2_simple as gpt2
import tensorflow as tf
import os

# Create an instance of Flask
app = Flask(__name__)

# Define routes and corresponding functions

# Route for the home page and index.html
@app.route('/')
@app.route('/index.html')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

# Route for the thankyou.html page
@app.route('/thankyou.html')
def thankyou():
    """
    Render the thankyou.html template.
    """
    return render_template('thankyou.html')

# Route for the gpt.html page, handles both GET and POST requests
@app.route('/gpt.html', methods=["GET", "POST"])
def gpt():
    """
    Render the gpt.html template with generated text based on user input.
    """
    text = ""  # Initialize the generated text

    # If the request method is POST, process the form data
    if request.method == "POST": 
        # Get the input with name = "context" from the HTML form
        context = request.form.get("context") 
        
        # Generate text using GPT-2 model
        with graph.as_default():
            g = gpt2.generate(sess, checkpoint_dir=checkpoint_dir,
                              return_as_list=True, prefix=startt + context + endt + startb,
                              truncate="<|end")[0]
        
        # Extract the generated text from the result
        text = g.split(">")[-1]
    
    # Render the gpt.html template with the generated text
    return render_template("gpt.html", text=text) 

# Main block of code
if __name__ == '__main__':
    # Load the GPT-2 model
    checkpoint_dir = "/Users/zacharysegal/Desktop/basic-flask-app-master/Techy/checkpoint/"
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess=sess, checkpoint_dir=checkpoint_dir)   # model is saved into current directory under /models/117M/
    graph = tf.get_default_graph()
    
    # Example usage of GPT-2 to generate text
    startt = ""  # Prefix
    endt = ""    # Suffix
    startb = ""  # Beginning of the text to generate
    with graph.as_default():
        g = gpt2.generate(sess, checkpoint_dir=checkpoint_dir, return_as_list=True,
                          prefix=startt + "You're gay" + endt + startb, truncate="<|end")[0]
    
    # Print the generated text
    print(g.split(">")[-1])

    # Run the Flask app in debug mode
    app.run(debug=True)
