from flask import Flask, render_template, request, redirect
import gpt_2_simple as gpt2
import tensorflow as tf
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Zachs Project')

@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html', the_title='Thank You')

@app.route('/gpt.html', methods=["GET", "POST"])
def gpt():
    text = ""
    title = ""


    if request.method == "POST": 
       # getting input with name = fname in HTML form 
        context = request.form.get("context") 
        with graph.as_default():
            g = gpt2.generate(sess, checkpoint_dir = "/Users/zacharysegal/OutInTech/checkpoint/", return_as_list = True, prefix = startt + context  +endt + startb, truncate = "<|end" )[0]
        text = g.split(">")[-1]
        title = context
    
    return render_template("gpt.html", text = text, title = title) 
    

if __name__ == '__main__':
    
    import tensorflow as tf
    import gpt_2_simple as gpt2
    startt = "<|startoftitle|>"
    endt = "<|title|>"
    startb = "<|body|>Sorry, English is not my first language because I am a computer, so I apologize in advance for my grammar and spelling."
    text = ""
    title = ""
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess = sess, checkpoint_dir = "/Users/zacharysegal/OutInTech/checkpoint/")   # model is saved into current directory under /models/117M/
    graph = tf.get_default_graph()
    
    app.run(debug=True)
