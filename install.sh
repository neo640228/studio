#!/usr/bin/env bash

user= neo@640228
sudo apt install -y git
sudo apt install -y curl

git clone git@github.com:$user/studio.git

cd studio

sudo wget https://dl.minio.io/server/minio/release/linux-amd64/minio -O /usr/local/bin/minio
sudo chmod +x /usr/local/bin/minio

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y  python python-pip python-dev python-tk \
    postgresql-server-dev-all postgresql-contrib postgresql-client postgresql \
    ffmpeg nodejs libmagickwand-dev nginx redis-server wkhtmltopdf

source .bashrc
source .profile

pip install -U pipenv

pipenv shell
pipenv sync

pip install pre-commit

sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn

yarn install

service postgresql start

sudo su postgres
psql
#CREATE USER learningequality with NOSUPERUSER INHERIT NOCREATEROLE CREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'kolibri';
#CREATE DATABASE "kolibri-studio" WITH TEMPLATE = template0 ENCODING = "UTF8" OWNER = "learningequality";

yarn run services
# 背景執行方法
#nohup yarn run services < /dev/null 2>&1 &

# console 2
#yarn run devsetup
#yarn run devserver
# 背景執行方法
#nohup yarn run devserver < /dev/null devserver.log 2>&1 &
