from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

count = 0
while True:
	print(count)
	# print("Received type: ")
	# print(received["type"])
	# print("Received encoded value: ")
	# print(received["encoded"])
	if received["type"]=="bigint":
		x = codecs.decode(long_to_bytes(int(received["encoded"],16)))
	elif received["type"]=="rot13":
		x = codecs.decode(received["encoded"],'rot_13')
	elif received["type"]=="utf-8":
		x = "".join([chr(x) for x in received["encoded"]])
	else:
		x = codecs.decode(codecs.encode(received["encoded"]),encoding=received["type"]).decode()

	# print(x)
	# print(received["encoded"].encode().decode(encoding=received["type"]))

	to_send = {
	    "decoded": x
	}
	json_send(to_send)

	received  = json_recv()
	count+=1

	if "flag" in received:
		print(received["flag"])
		break
