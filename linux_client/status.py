import json,os,sys,hashlib
import pickle

import requests

base_path = sys.path[0]+'/'

cjs = json.load(open(base_path+'client.js'))
sjs = json.load(open(base_path+'server.js'))

#bad way but just do it for now

username = cjs['username']
password = cjs['password']


def get_all_files_on_server():

    url = sjs["base_url"] + 'get_md5'
    try:
        pickle_in = open(base_path+'session.p','rb')
        s = pickle.load(pickle_in)
        pickle_in.close()
        res = s.post(url=url).json()
        pickle_out = open(base_path+'session.p','wb')
        pickle.dump(s,pickle_out)
        pickle_out.close()
        return res
    except:


        print("#FAIL:Not Logged In")
        sys.exit()

print(set(get_all_files_on_server().items()))
