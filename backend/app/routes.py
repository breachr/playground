from app import app

from flask import Flask, url_for, render_template, jsonify, request, make_response
import json


@app.route('/')
def landing():
    """
    Render index.html
    """
    return render_template('index.html')
