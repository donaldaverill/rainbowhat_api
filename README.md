
sudo systemctl status rainbowhat_api.service

sudo systemctl daemon-reload
sudo systemctl restart rainbowhat_api.service

sudo journalctl -u rainbowhat_api.service -b --no-pager


DEVELOPMENT
source /home/donald/rainbowhat_api/env/bin/activate

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

