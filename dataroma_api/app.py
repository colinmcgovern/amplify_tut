from flask import Flask
import os
import subprocess
from shutil import rmtree
from datetime import datetime

app = Flask(__name__)

# Run download wayback downloader in background and
# return data (as csv) and date of last update
@app.route('/')
def get():
      
    return 'Hello, World!'

@app.route('/update_cache')
def update_cache():
	cache_folders = os.listdir('wayback-machine-downloader/websites/')
	for folder in cache_folders:
		if(len(folder.split("_"))!=2):
			print("removing: {}".format(os.path.join('wayback-machine-downloader/websites/',folder)))
			rmtree(os.path.join('wayback-machine-downloader/websites/',folder))
	cache_folders = os.listdir('wayback-machine-downloader/websites/')
	cache_dates = list(map(lambda x: x.split("_")[1],cache_folders))
	return cache_dates

	os.system('wayback_machine_downloader https://www.dataroma.com/m/managers.php -s;')