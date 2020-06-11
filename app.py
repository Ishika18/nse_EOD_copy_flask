from flask import Flask, render_template, request
from flask_datepicker import datepicker
from datetime import date, datetime
from nsepy import get_history
import data
import pandas as pd

app = Flask(__name__)
app = Flask(__name__)
datepicker(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/data", methods=["POST", "GET"])
def show_data():
    if request.method == "POST":
        stock_fut = get_history(symbol=request.form["symbol"].strip().upper(),
                                start=datetime.strptime(request.form["start_date"], '%Y-%m-%d'),
                                end=datetime.strptime(request.form["end_date"], '%Y-%m-%d'),
                                expiry_date=datetime.strptime(request.form["expiry_date"], '%Y-%m-%d'))
        if request.form.get('download') == 'on':
            print("works", flush=True)
            data.download_file(stock_fut)
        print(request.form, flush=True)
        pd.set_option('display.max_rows', stock_fut.shape[0] + 1)
        return stock_fut.to_html()


if __name__ == '__main__':
    app.run(debug=True)
