import threading 
from threading import*
import time

store = {} # key-value dictionary to store key-value pairs

# create operation 

def create(key,value,timeout=0):
    if key in store:
        print("Error: Key already exists in the store") 
    else:
        if(key.isalpha()):
            if len(store)<(1024*1024*1024) and value<=(16*1024*1024):  # for checking store size less than 1GB and value size less than 16KB
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: # constraints for input key_name capped at 32chars
                    store[key]=l
                print("Key value successfully created!")
            else:
                print("Error: Memory limit exceeded!")
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

# read operation
            
def read(key):
    if key not in store:
        print("Error: The key does not exist in the store. Please enter a valid key")
    else:
        temp=store[key]
        if temp[1]!=0:
            if time.time()<temp[1]: 
                strval=str(key)+":"+str(temp[0]) 
                return strval
            else:
                print("Error: time-to-live of ",key," has expired") 
        else:
            strval=str(key)+":"+str(temp[0])
            return strval

# delete operation

def delete(key):
    if key not in store:
        print("Error: Can't perform delete operation! Given key does not exist in the store.") 
    else:
        temp=store[key]
        if temp[1]!=0:
            if time.time()<temp[1]: #comparing the current time with expiry time
                del store[key]
                print("Key is successfully deleted from the store")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del store[key]
            print("Key is successfully deleted from the store")
