from flask import Flask, render_template, request, redirect, url_for
import cv2
import pytesseract

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        return redirect(url_for("result"))
    else:
        return render_template("home.html")
    
@app.route("/result", methods=["GET","POST"])
def result():
    if request.method == "POST":
        i = request.form["image"]
        img = cv2.imread(i)
        text = pytesseract.image_to_string(img)
        return render_template("result.html", text=text)
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
