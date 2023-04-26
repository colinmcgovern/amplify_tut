echo 'Correct input is run.sh IP PORT'
if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    exit 1
fi
cd wayback-machine-downloader;
sudo gem install wayback_machine_downloader;
cd ..
source .venv/bin/activate
flask run --host=$1 --port=$2 --with-threads
