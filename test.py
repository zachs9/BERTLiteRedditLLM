from flask import Flask, render_template, request, redirect
import gpt_2_simple as gpt2
import tensorflow as tf

import os
checkpoint_dir = "/Users/zacharysegal/Desktop/basic-flask-app-master/Techy/checkpoint/"
path = os.path.join(checkpoint_dir, "run1")
open(os.path.join(path, 'encoder.json'), 'r')

startt = "<|startoftitle|>"
endt = "<|title|>"
startb = "<|body|>"
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess = sess, checkpoint_dir = checkpoint_dir)   # model is saved into current directory under /models/117M/
graph = tf.get_default_graph()
with graph.as_default():
    g = gpt2.generate(sess, checkpoint_dir = checkpoint_dir, return_as_list = True, prefix = startt + "You're gay"  +endt + startb, truncate = "<|end" )[0]
print(g.split(">")[-1])
