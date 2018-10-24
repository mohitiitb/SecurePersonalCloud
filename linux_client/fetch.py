import sys,json
import requests,pickle
from termcolor import colored

base_path = sys.path[0]+'/'

cjs = json.load(open(base_path+'client.js'))
sjs = json.load(open(base_path+'server.js'))

#bad way but just do it for now

username = cjs['username']
password = cjs['password']


def print_tree(T,indent):
    if T == "None" :
        return
    for k,v in sorted(T.items()):
        res = colored(k,'blue') if v != "None" else colored(k,'green')
        print(colored('|---'*indent,'red') + res)
        print_tree(v,indent+1)


def viewUploads():

    url = sjs["base_url"] + 'file_view'
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


        return "#FAIL:Not Logged In"

def download(fpath):
    url = sjs['base_url'] + 'file_download/'
    data = {'fpath':fpath}
    try:
        pickle_in = open(base_path+'session.p','rb')
        s = pickle.load(pickle_in)
        pickle_in.close()
        res = s.post(url=url,data=data).text
        pickle_out = open(base_path+'session.p','wb')
        pickle.dump(s,pickle_out)
        pickle_out.close()

        if res.startswith('#FAIL'):
            print('Not logged in')
            return None
        else:
            print(res)

    except:
        return "#FAIL:Not Logged In"




if sys.argv[1]=='0':
    res = viewUploads()
    if isinstance(res,str) and res.startswith('#FAIL'):
        print(res)
    else:
        #print_tree(json.loads(res.replace("\'","\"")),0)
        #print(res.replace("\'","\"").replace('""','"root"'))
        #print_tree(res,0)
        res= res.replace('\0', '').replace("\'","\"")
        print_tree(json.loads(res),0)


else:
    download(input('Enter the path you want to download : '))
