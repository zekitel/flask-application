

from flask import Flask,request
app = Flask(__name__)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode



@app.route('/')
@cross_origin()
def helloworld():
    return "Helloworld"

def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


@app.route('/encrypt')
@cross_origin()
def encryption():

    pubkey=request.args.get('publickey')
    currentline = ""
    for line in pubkey:
        line = line.rstrip('\n')
        currentline = currentline + line
    currentline=currentline.replace(" ","+")
    pubkey=currentline
    message=request.args.get('message')
    keyDER = b64decode(pubkey)
    keyPub = RSA.importKey(keyDER)
    encrypted = b64encode(encrypt(message.encode(), keyPub))
    return encrypted

@app.route('/decrypt')
@cross_origin()
def decryption():
    privateKey=request.args.get('privatekey')
    print(privateKey)
    currentline = ""
    for line in privateKey:
        line = line.rstrip('\n')
        currentline = currentline + line
    currentline = currentline.replace(" ", "+")
    privateKey = currentline
    message = request.args.get('message')
    message = message.replace(" ", "+")
    keyDER2 = b64decode(privateKey)
    keyPriv = RSA.importKey(keyDER2)
    decrypted = decrypt(b64decode(message), keyPriv)
    return decrypted

def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


