import subprocess
from subprocess import STDOUT, check_call
import sys
import os


def app_get(filetoinstall):
    check_call(['apt-get', 'install', '-y', filetoinstall],stdout=open(os.devnull,'wb'), stderr=STDOUT) 


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package],stdout=open(os.devnull,'wb'), stderr=STDOUT)
    
if __name__ == "__main__":
    uninstall("tensorflow")
    uninstall("tensorflow-gpu")
    install("opencv-python==4.2.0.34")
    install("librosa==0.7.0")
    install("opencv-contrib-python>=4.2.0.34")
    install("opencv-python==4.1.0.25")
    install("torch==1.1.0")
    install("torchvision==0.3.0")
    install("tqdm==4.45.0")
    install("numba==0.48")
    app_get("libgl1-mesa-dev")
    app_get("libsndfile1-dev")
    app_get("ffmpeg")
    app_get("libsm6")