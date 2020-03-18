import collections
import string
import base64
import binascii
import urllib.parse

def rot_p(encode_or_decode,message):
	allrot = ''
	for i in range(0, 26):
		upper = collections.deque(string.ascii_uppercase)
		lower = collections.deque(string.ascii_lowercase)
		upper.rotate((- i))
		lower.rotate((- i))
            
		upper = ''.join(list(upper))
		lower = ''.join(list(lower))
		translated = message.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))
		allrot += '{}: {}\n'.format(i, translated)
	return str(allrot)


def hex_p(encode_or_decode,string):
	if encode_or_decode == 'decode':
		string = string.replace(" ", "")
		decoded = binascii.unhexlify(string).decode('ascii')
		return decoded
	if encode_or_decode == 'encode':
		byted = string.encode()
		encoded = binascii.hexlify(byted).decode('ascii')
		return	encoded


def bin_p(encode_or_decode,string):
	if encode_or_decode == 'decode':
		string = string.replace(" ", "")
		data = int(string, 2)
		decoded = data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()
		return (decoded)
        
	if encode_or_decode == 'encode':
		encoded = bin(int.from_bytes(string.encode(), 'big')).replace('b', '')
		return encoded

def bs64_p(encode_or_decode,string):
	byted_str = str.encode(string)
	if encode_or_decode == 'decode':
		decoded = base64.b64decode(byted_str).decode('utf-8')
		return (decoded)

	if encode_or_decode == 'encode':
		encoded = base64.b64encode(byted_str).decode('utf-8').replace('\n', '')
		return (encoded)


def atbash_p(encode_or_decode,message):
	normal = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	changed = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
	trans = str.maketrans(normal, changed)
	atbashed = message.translate(trans)
	return (atbashed)

def url_p(encode_or_decode,string):
	if encode_or_decode == 'decode':
		if '%20' in message:
			message = message.replace('%20', '(space)')
			return (urllib.parse.unquote(message))
		else:
			return urllib.parse.unquote(message)
	if encode_or_decode == 'encode':
		return urllib.parse.quote(message)
