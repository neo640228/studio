# Studio 安裝

基本設定
--
設定sudo免密碼

    $ su -
    登入root
    $ vi /etc/sudoers
    加入一行  
    ossf	ALL=NOPASSWD: ALL
啟動ssh
--

    $ sudo apt-get install -y ssh

確認git, curl都安裝可使用

    $ sudo apt install -y git
    $ sudo apt install -y curl
clone Studio
--
將[studio repo](https://github.com/learningequality/studio) Fork一份到自己的git帳號中
然後把它clone回來

###最簡單的做法

    $ git clone https://github.com/neo640228/studio

* 缺點：慢
* 優點：簡單易用，沒有很多設定
### 正規做法

    $ git clone git@github.com:neo640228/studio.git

* 缺點：設定麻煩
* 優點：快

studio會是我們的專案目錄

* 可能遇到的問題 git@github.com: Permission denied (publickey).

    * 問題發生原因
        1. 本機沒有生成ssh key
        2. 本機的ssh key沒有上傳到你的github帳戶
    * 解決方法

            $ ssh-keygen

        然後一直enter或根據你自己的喜好修改(這邊範例是用預設值，自己有改動檔案名請將id_rsa改掉)

            $ more ~/.ssh/id_rsa.pub

        將內容複製，內容應該會是ssh-rsa開頭，如下示範

            ssh-rsa AAAAB3
    * 登入你的github，在右上角的下拉選單中選擇settings
    * 選擇左方列表中的 SSH and GPG keys
    * 點選右上的New SSH key按鈕
    * 把剛剛id_rsa.pub的內容貼進去然後存擋
    * 你應該可以透過剛剛上面的指令clone回來了

Install softwar prerequisites
--
下面的清單是需要事先安裝的軟體
* python(2.7)
* python-pip
* nodejs(10.x)
* Postgres DB
* redis
* minio server
* nginx
* ffmpeg
* python-tk
* libmagickwand-dev
* yarn

#安裝需求軟體

    # Install minio
    $ sudo wget https://dl.minio.io/server/minio/release/linux-amd64/minio -O /usr/local/bin/minio
    $ sudo chmod +x /usr/local/bin/minio

    # Install node PPA
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

    # Install packages
    $ sudo apt-get install -y  python python-pip python-dev python-tk \
        postgresql-server-dev-all postgresql-contrib postgresql-client postgresql \
        ffmpeg nodejs libmagickwand-dev nginx redis-server wkhtmltopdf
#設定python依賴環境
* 安裝pipenv

        可能會發生無法使用pip的情況．可以選擇登出再登入．或是更新環境變數
        $ source .profile
        $ source .bashrc
        $ pip install -U pipenv

* 設定pipenv

        $ cd studio
        $ pipenv shell
        $ pipenv sync
        可能會發生
        ERROR: Pipfile.lock not found! You need to run $ pipenv lock before you can continue.
        $ pipenv lock
        $ pipenv sync

#設定pre-commit

    $ pip install pre-commit
    $ pre-commit install

#安裝Javascript相關套件


    $ yarn install

* 這個指令需要蠻長時間才能執行完畢
* 可能會遇到沒有yarn指令，或是出現如下的錯誤

        ERROR: [Errno 2] No such file or directory: 'install'

* 修正yarn的安裝即可

        $ sudo apt remove cmdtest
        $ sudo apt remove yarn
        $ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        $ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        $ sudo apt-get update && sudo apt-get install yarn

* 然後再執行一次yarn install

# 設定database並啟動redis

* 啟動postgresql

        $ service postgresql start

* 切換到postgres帳號，並進入postgresql介面

        $ sudo su postgres
        $ psql

* 建立learningequality帳號kolibri為密碼，並建立資料庫kolibri-studio

        CREATE USER learningequality with NOSUPERUSER INHERIT NOCREATEROLE CREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'kolibri';
        CREATE DATABASE "kolibri-studio" WITH TEMPLATE = template0 ENCODING = "UTF8" OWNER = "learningequality";

* 建立完成後ctrl+D或是輸入\q離開psql介面

#資料整合並建立環境常數

* 接下來要在兩個不同的視窗中執行，確認兩個視窗都在專案目錄中．並且確認pipenv有啟動

        pipenv shell
* 在第一個視窗執行以下指令

        $ yarn run services
* 在第二個視窗中執行以下指令

        $ yarn run devsetup
#啟動dev server

    $ yarn run devserver
    當你在畫面中看到以下訊息
    Starting development server at http://0.0.0.0:8080/
    Quit the server with CONTROL-C.

表示可以進行登入了

開啟瀏覽器
輸入http://IP:8080/
帳號輸入a@a.com密碼a
