from flask import Blueprint, render_template

data = Blueprint("data", __name__, static_folder="static", template_folder="templates")


def download_file(json_data):
    pass