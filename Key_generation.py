import string
import random
import json
import os
class Key:
	def __init__(self,file_name):
		self.f = file_name
		self.path = "static"
	def load_data(self):
		self.files=[]
		self.public_k=[]
		self.private_k=[]
		
		if "data.txt" in os.listdir(self.path):
			with open(self.path+"/"+'data.txt') as json_file:
				data = json.load(json_file)
		else:
			return False
		for key,values in data.items():
			self.files.append(key),self.public_k.append(values[0]),self.private_k.append(values[1])
		return self.files,self.public_k,self.private_k,data
	def create_data(self,d1):
		if "data.txt" in os.listdir(self.path):
			f,p,pr,d= self.load_data()
			if len(d)>0:
				d1.update(d)
			with open(self.path+"/"+'data.txt', 'w') as convert_file:
				convert_file.write(json.dumps(d1))
		else:
			with open(self.path+"/"+'data.txt', 'w') as convert_file:
				convert_file.write(json.dumps(d1))
	def generate(self):
		keys = list(string.ascii_letters+"!@#$*><&")
		public_key = random.sample(keys,16)
		public_key = "".join(public_key)
		private_key = random.sample(keys,17)
		private_key= "".join(private_key)
		if "data.txt" in os.listdir(self.path):
			f,p,pr,d= self.load_data()
			while True:
				if private_key not in pr:
					break
				else:
					private_key = random.sample(keys,17)
					private_key= "".join(private_key)
			while True:
				if public_key not in p:
					break
				else:
					public_key = random.sample(keys,16)
					public_key = "".join(public_key)
			d1 = {self.f:(public_key,private_key)}
			self.create_data(d1)
		else:
			d1 = {self.f:(public_key,private_key)}
			self.create_data(d1)
		return public_key,private_key