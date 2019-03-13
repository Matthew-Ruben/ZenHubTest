
def main():
	room1 = HotelRoom("Room 1")
	print(f'{room1.}')
	
if __name__ == '__main__':
	main()



class HotelRoom:
	
	
	room_count = 0  # class variable
	
	def __init__(self, room_name):
		"""
		Initialize the room with a name
		:param room_name: (string) name the room will be assigned
		"""
		self.name = room_name
		self.price = 0
		self.status = 'Unbooked'
		self.merge_conflict_checker
		self.add_room()
	
	@classmethod
	def add_room(cls):
		"""
		Increments room counter
		"""
		cls.room_count += 1
