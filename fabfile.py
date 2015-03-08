from fabric.api import env, put

DEPLOY_DIR = "/home/iotissue"
APP_DIR = "/home/iotissue/iotissue_app"
APP_NAME = "iotissue_app"

env.hosts = ['iotissue@iotissue.com']


def deploy():
    put("index.html", APP_DIR)
    put("style.css", APP_DIR)
    put("images", APP_DIR)
