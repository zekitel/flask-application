from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from flask import Flask,request
app = Flask(__name__)

def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)
@app.route('/')
def helloworld():
    return "Helloworld"

@app.route('/encrypt')
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

app.run(host='0.0.0.0', port= 81)
"""
pubkey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuGKtS8Yt1zgsT9s6OyGz3IqVrNncCsO4YBJqLbzoKcLdXZhRa/L53PaVWt4cdwPayTx5RnNmWN2DtjFI84yMTRwijKEResAeiloYFd1ha0IhQJtAqu26wXLI1Oz1HxQkHx/Rimd5JWiahYevssOcNHKNM9Y0Oj6OqmPcj2TY/0wIDAQAB'
privateKey='MIICXQIBAAKBgQCuGKtS8Yt1zgsT9s6OyGz3IqVrNncCsO4YBJqLbzoKcLdXZhRa/L53PaVWt4cdwPayTx5RnNmWN2DtjFI84yMTRwijKEResAeiloYFd1ha0IhQJtAqu26wXLI1Oz1HxQkHx/Rimd5JWiahYevssOcNHKNM9Y0Oj6OqmPcj2TY/0wIDAQABAoGAZEq914hiqLjL1PJnSAXaD/ybgsnbgWdfoeJ1DUJEE2Ofmu+pZkkXiCWxK+WKJu/Urh+5/ZX4GvtIEVC2x3Cp8SmAUm4w65cQPi/MX3Lb8feOyuTvcaohfSWLGm4OwQKFrFwVse9UOVO2ehfIDUyL924V8MZavs74vkYErUZXANECQQDyL01ko7Dpvu+hdnkvqfBB+ekgO1d6YgFb7m63JCF2w068CaSCY+K1v3uPa5BSLgOVAM2tVT/tsp/QUwrukB/dAkEAuAcNHKLSsGIhxI+kJ0YDrtBZTaeeCq/0gxo3a8ZEqUdfEVrQgFIh6b58JyM6EahssOSd+7iQxF0XbnNjqRq7bwJAAR+XDFB2EZ+BHQ6foUj4hFXUbwHXdgneV77TZKYWQabGRrkEulYcRxuMRy4IjVkJSzelvJgYo9GgTCcWdeTVQQJBAKpcbLj7ysvarKQIzdBFspcc7e9Dor0GEvdjR7cP/vQuzEWGqsqAPkDjRI/+vn0mTCieG9qyC+Kcw1pOnA4qXyUCQQDKb42+SFqE0jbTYARapptJHDh2QpPRSU6AW0HghxPIaWMeQswtDxsTwR0AQdy9G7q/R0r0IUlZicWrBcLtVz0u'

def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)



msg1 = "berkan adamin dibidir"

keyDER = b64decode(pubkey)
keyPub = RSA.importKey(keyDER)

keyDER2 = b64decode(privateKey)
keyPriv = RSA.importKey(keyDER2)

encrypted = b64encode(encrypt(msg1.encode(), keyPub))
decrypted = decrypt(b64decode(encrypted), keyPriv)

print(encrypted)
print(decrypted)
"""