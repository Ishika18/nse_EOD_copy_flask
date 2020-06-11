from flask import Flask, render_template, request
from flask_datepicker import datepicker
from datetime import date
from nsepy import get_history
from data import data

app = Flask(__name__)
app = Flask(__name__)
datepicker(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/data", methods=["POST", "GET"])
def show_data():
    if request.method == "POST":
        download = request.form["download"]
        stock_fut = get_history(symbol=request.form["symbol"],
                                start_date=date(request.form["start_date"]),
                                end_date=date(request.form["end_date"]),
                                expiry_date=date(request.form["expiry_date"]))
        if download == "on":
            download_file(stock_fut)
        return f"{download}"


if __name__ == '__main__':
    app.run(debug=True)
