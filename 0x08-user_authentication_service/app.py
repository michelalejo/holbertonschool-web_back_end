#!/usr/bin/env python3
"""
Flask app.
"""
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def Bienvenue() -> str:
    """Bienvenue."""
    return jsonify({"message": "Bienvenue"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
