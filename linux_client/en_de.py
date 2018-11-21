import sys
import AES
import pickle
# import RSA
# import DES

base_path = sys.path[0]+'/'


'''
    handles everything related to en-de

'''

def encrypt(file,schema,save_as):
        if schema=='AES':
            pickle_in = open(base_path+'aes.p','rb')
            passwd = pickle.load(pickle_in)
            pickle_in.close()
            AES.encrypt_AES(file,passwd,save_as)
        else :
            print('pending')
            sys.exit(2)


def decrypt(file,schema,save_as):
        if schema=='AES':
            pickle_in = open(base_path+'aes.p','rb')
            passwd = pickle.load(pickle_in)
            pickle_in.close()
            AES.decrypt_AES(file,passwd,save_as)
        else :
            print('pending')
            sys.exit(2)






if __name__=='__main__':

    cmd = sys.argv[1]

    if cmd == "list":
        print('#1)RSA')
        print('#2)AES')
        print('#3)DES')

    elif cmd == 'update':
        print('--pending--')

    elif cmd == 'dump':
        print('--pending--')
