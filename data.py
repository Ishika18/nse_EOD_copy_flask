from flask import send_file


def download_file(given_dataframe):
    given_dataframe.to_csv('niftyfut.csv')
    path = "niftyfut.csv"
    return send_file(path, as_attachment=True)