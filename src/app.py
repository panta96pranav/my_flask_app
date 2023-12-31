#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)
app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input" placeholder="Please enter something.">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "<center><h3>You entered:</h3> <br>" + input_text+"</center>"
    
