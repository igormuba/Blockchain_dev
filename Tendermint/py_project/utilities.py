'''
========================
utilities.py
========================
Created on Feb.10, 2020
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide utility function to support project.
@Reference: 
'''

from datetime import datetime, timedelta
import hashlib
import json
import pickle
import glob, os, fnmatch
import codecs


		
'''
TypesUtil class for data type format transfer
'''
class TypesUtil(object):
	#integer to hex
	@staticmethod
	def int_to_hex(int_data):
		return hex(int_data)
		
	#hex to integer
	@staticmethod
	def hex_to_int(hex_data):
		return int(hex_data, 16)
		
	#string to hex
	@staticmethod
	def string_to_hex(str_data):
		hex_data=str_data.hex()
		return hex_data
		
	#hex to string
	@staticmethod
	def hex_to_string(hex_data):
		str_data=bytes.fromhex(hex_data)
		return str_data
		
	#string to bytes
	@staticmethod
	def string_to_bytes(str_data):
		bytes_data=str_data.encode(encoding='UTF-8')
		return bytes_data
		
	#bytes to string
	@staticmethod
	def bytes_to_string(byte_data):
		str_data=byte_data.decode(encoding='UTF-8')
		return str_data

	# string-base64 to string-ASCII 
	@staticmethod
	def base64_to_ascii(str_data):
		bytes_data=str_data.encode(encoding='UTF-8')
		ascii_str=codecs.decode(bytes_data, 'base64').decode('ascii')
		return ascii_str

	# curl tx string to json
	@staticmethod
	def tx_to_json(tx_str):
		json_str = tx_str.replace("'",'"')
		json_data = json.loads(json_str)
		return json_data

	# curl tx string to json
	@staticmethod
	def json_to_tx(json_data):
		json_str = json.dumps(json_data)
		tx_str = json_str.replace('"', "'")
		return tx_str
		
	#string to json
	@staticmethod
	def string_to_json(json_str):
		json_data = json.loads(json_str)
		return json_data
		
	#json to string
	@staticmethod
	def json_to_string(json_data):
		json_str = json.dumps(json_data)
		return json_str

	#json list to string
	@staticmethod
	def jsonlist_to_string(json_list):
		list_str="|".join(TypesUtil.json_to_string(e) for e in json_list)
		return list_str

	#string to json list
	@staticmethod
	def string_to_jsonlist(str_data):
		list_data=str_data.split('|')
		json_list=[]
		for data in list_data: 
			json_list.append(TypesUtil.string_to_json(data))
		return json_list

	# get hashed json data
	@staticmethod
	def hash_json(json_block, hash_type='sha256'):
	    """
	    Create a SHA-256 hash of a json block
	    """
	    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
	    block_string = json.dumps(json_block, sort_keys=True).encode()
	    
	    if(hash_type=='sha1'):
	    	return hashlib.sha1(block_string).hexdigest()
	    elif(hash_type=='sha256'):
	    	return hashlib.sha256(block_string).hexdigest()
	    else:
	    	return None