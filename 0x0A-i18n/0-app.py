#!/usr/bin/env python3
""" Flask App"""
from flask import Flask, render_template
from os import getenvs


app = Flask(__name__)


@app.route('/')
def index():
    """Render index.html."""
    return return render_template("0-index.html", message="Welcome to Holberton")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
