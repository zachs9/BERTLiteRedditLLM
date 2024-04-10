# Import necessary libraries and modules
from flask import Flask, render_template, request, redirect
import gpt_2_simple as gpt2
import tensorflow as tf

# Create an instance of Flask
app = Flask(__name__)

# Define routes and corresponding functions

# Route for the home page and index.html
@app.route('/')
@app.route('/index.html')
def index():
    """
    Render the index.html template with the title 'Zachs Project'.
    """
    return render_template('index.html', the_title='Zachs Project')

# Route for the thankyou.html page
@app.route('/thankyou.html')
def thankyou():
    """
    Render the thankyou.html template with the title 'Thank You'.
    """
    return render_template('thankyou.html', the_title='Thank You')

# Route for the gpt.html page, handles both GET and POST requests
@app.route('/gpt.html', methods=["GET", "POST"])
def gpt():
    """
    Render the gpt.html template with generated text based on user input.
    """
    text = ""  # Initialize the generated text
    title = ""  # Initialize the title

    # If the request method is POST, process the form data
    if request.method == "POST": 
        # Get the input with name = "context" from the HTML form
        context = request.form.get("context") 
        
        # Generate text using GPT-2 model
        with graph.as_default():
            g = gpt2.generate(sess, checkpoint_dir="/Users/zacharysegal/OutInTech/checkpoint/",
                              return_as_list=True, prefix=startt + context + endt + startb,
                              truncate="<|end")[0]
        
        # Extract the generated text from the result
        text = g.split(">")[-1]
        title = context  # Set the title to the user input context
    
    # Render the gpt.html template with the generated text and title
    return render_template("gpt.html", text=text, title=title) 

# Main block of code
if __name__ == '__main__':
    # Additional imports and setup
    
    # Define some variables
    startt = ""  # Initialize startt
    endt = ""    # Initialize endt
    startb = "Sorry, English is not my first language because I am a computer, so I apologize in advance for my grammar and spelling."
    text = ""    # Initialize text
    title = ""   # Initialize title
    
    # Start a TensorFlow session
    sess = gpt2.start_tf_sess()
    
    # Load the GPT-2 model
    gpt2.load_gpt2(sess=sess, checkpoint_dir="/Users/zacharysegal/OutInTech/checkpoint/")   # model is saved into current directory under /models/117M/
    
    # Create a default TensorFlow graph
    graph = tf.get_default_graph()
    
    # Run the Flask app in debug mode
    app.run(debug=True)
