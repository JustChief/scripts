#
#usage: md5-script.py <url>

#use requests to get the url
import requests
#use sys to create variables which can then be used as an argument with the script
import sys
#hashlib is used to convert the string to  the desired hash value
import hashlib

url = sys.argv[1]
#use the same session ID, this allows us to submit the result using the same session ID, so our request does not time out
s = requests.Session()
rget = s.get(url)

encode_this = rget.content.split(b"<h3 align=\'center\'>")[1].split(b'<')[0]
print ("Results to encode: ")
print (encode_this.decode("utf-8")+"\n")

res = hashlib.md5(encode_this).hexdigest()
print ("Hashed results: ")
print (res+"\n")

rpost = s.post(url, data={'hash':res})
print ("HTML post results converted to text: ")
print (rpost.text+"\n")

flag = rpost.content.split(b"</h3><p align=\'center\'>")[1].split(b'<')[0]
print ("Flag: ")
print  (flag.decode("utf-8"))
