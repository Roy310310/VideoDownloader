import subprocess

import psycopg2
import requests
import spacy
from Cryptodome.Util import number
from flask import Flask, Response, jsonify
from flask import Flask, render_template, request, redirect, url_for
from jinja2 import ext

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")


@app.route('/favicon.ico')
def favicon():
    return Response('', status=200)

@app.route('/get_video_link',  methods=['POST', 'GET'])
def get_link():
    if request.method == 'POST':
        return redirect(url_for('submit_video_link'))
    elif request.method == 'GET':
        return render_template('userVideo.html')

@app.route('/video_link',  methods=['POST', 'GET'])
def submit_video_link():
    url = request.form.get('video_link')
    output_filename = f"C:/Users/User/Downloads/{url}.%(ext)s"
    command = ["yt-dlp", "-o", output_filename, url]
    subprocess.run(command)
    return "Video Succesfully Downloaded"