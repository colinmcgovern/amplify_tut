from flask import Flask
import os
import subprocess

app = Flask(__name__)

# Run download wayback downloader in background and
# return data (as csv) and date of last update
@app.route('/')
def get():
    cache_folders = os.listdir('wayback-machine-downloader/websites/')
    os.system('wayback_machine_downloader https://www.dataroma.com/m/managers.php -s;')
    return 'Hello, World!'

    