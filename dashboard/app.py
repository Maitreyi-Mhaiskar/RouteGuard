from flask import Flask,render_template

import sys

sys.path.append("../detector")

from hijack_detector import detect_hijack



app=Flask(__name__)



@app.route("/")
def home():

    result=detect_hijack()


    return render_template(
        "index.html",
        result=result
    )



if __name__=="__main__":

    app.run(
        debug=True,
        port=5000
    )
