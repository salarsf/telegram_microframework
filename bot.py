"""
A simple microframework for working with telegram api to receive messages and reply
"""


import requests
import json
import configparser as cfg


class TelegramBot():
    def __init__(self, config):
        self.token = self.get_token_from_cfg(config)
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_token_from_cfg(self,config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')
    
    def get_updates(self, offset:int = None):
        url = self.base_url + "getUpdates"
        if offset:
            url += f"?offset={offset + 1}"
        request = requests.get(url)
        return json.loads(request.content)

    def send_message(self,text:str, chat_id:int):
        url = self.base_url + f"sendMessage?text={text}&chat_id={chat_id}"
        request = requests.get(url)