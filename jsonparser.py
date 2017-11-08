import json
from pprint import pprint

class jsonparse(object):
	def __init__(self,path):
		with open(path) as data_file:
			self.data = json.load(data_file)

	
	def getting_keys_from_dictionary(self):
		self.keys=[]
		for k,v in self.data.items():
			self.keys.append(k)
		return self.keys

	def getting_attributes_of_phones(self,list_index):
		self.getting_keys_from_dictionary()
		self.device_attribute=self.data[self.keys[list_index]]
		return self.device_attribute
		print self.device_attribute
	


	def get_values_from_json(self,key):
		self.getting_attributes_of_phones()
		self.title=self.device_attribute[key]
		return self.title
		