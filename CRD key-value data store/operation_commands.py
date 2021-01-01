Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Users/vichu/Desktop/CRD key-value data store/functions.py ===
>>> import functions as object
>>> object.create("meena", 30)
Key value successfully created!
>>> object.create("rahul", 20)
Key value successfully created!
>>> object.create("rahul", 45)
Error: Key already exists in the store
>>> object.create("ram", 11110001111111111111111111111111111111111111111111111111111111111111111111111)
Error: Memory limit exceeded!
>>> object.create("12345", 45)
Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> object.read("meena")
'meena:30'
>>> object.read("ram")
Error: The key does not exist in the store. Please enter a valid key
>>> object.create("raju", 25, 30) # creation with timeout
Key value successfully created!
>>> object.read("raju")
Error: time-to-live of  raju  has expired
>>> object.delete("raju")
error: time-to-live of raju has expired
>>> object.delete("rahul")
Key is successfully deleted from the store
>>> object.read("rahul") # deleted rahul and it will not exist in the store
Error: The key does not exist in the store. Please enter a valid key
>>> 
