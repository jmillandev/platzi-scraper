# MyPyppertter

## Install project
```sh
pip install -r requirements.txt
./init.local.sh build
```

## Run Scraper
### Open Browser

If you are using WSL see the next [post](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx) and [this](https://code.luasoftware.com/tutorials/x-server/xming-client-4-rejected-from-ip/) if you hace any problem with the permissions with Xming

Export required vars
```sh
# For UNIX
export DATABASE_URL=''
export BROWSER_IP='127.0.0.1'

# For Windows(CMD) - Create vars and reset CMD
setx DATABASE_URL "anything"
setx BROWSER_IP "127.0.0.1"
```

Launch Browser
```sh
# Use python 3.8(equal dockerfile)
python console.py  pyppeteer:open_browser --gui
```

# Login on Database
`psql -U $POSTGRES_USER -h $POSTGRES_HOST -d $POSTGRES_DB -W`
