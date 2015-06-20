# world/map classes here
import csv

class Room():
	def __init__(self, filename):
		self.filename = filename
		
	def get_room_data(self):
		self.data = {}
		with open(self.filename, 'rb') as file:
			reader = csv.DictReader(file)
			for row in reader:
				self.data[row['Room Name']] = int(row['Room Size'])
		return self.data
	
	def start_tile_create(self):
		self.startboard = []
		v = self.data['Start']
		for num in range(v):
			self.startboard.append(["[]"] * v)
			def start_tile_print(self):		
				for row in self.startboard:
					print(" ".join(row))
		print("\n")			
		return start_tile_print(self)
	
	def key_tile_create(self):
		self.keyboard = []
		v = self.data['Key']
		for num in range(v):
			self.keyboard.append(["[]"] * v)
			def key_tile_print(self):
				for row in self.keyboard:
					print (" ".join(row))
		print("\n")		
		return key_tile_print(self)
	
	def gold_tile_create(self):
		self.goldboard = []
		v = self.data['Gold']
		for num in range(v):
			self.goldboard.append(["[]"] * v)
			def gold_tile_print(self):
				for row in self.goldboard:
					print (" ".join(row))
		print("\n")			
		return gold_tile_print(self)
	
	def exit_tile_create(self):
		self.exitboard = []
		v = self.data['Exit']
		for num in range(v):
			self.exitboard.append(["[]"] * v)
			def exit_tile_print(self):
				for row in self.exitboard:
					print (" ".join(row))
		print("\n")
		return exit_tile_print(self)