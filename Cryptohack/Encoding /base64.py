from Crypto.Util.number import *
import codecs

s ="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b64 = codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()
print(b64)