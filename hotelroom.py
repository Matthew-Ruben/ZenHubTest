
def main():
	room1 = HotelRoom("Room 1")
	print(f'{room1.}')
	
if __name__ == '__main__':
	main()

  # First commit fom this branch

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
		self.add_room()
	
	@classmethod
	def add_room(cls):
		"""
		Increments room counter
		"""
		cls.room_count += 1
	
	def __lt__(self, other):
        """
        Compares 2 Room objects using their prices
        :param other: (HotelRoom) room to compare self against
        :return: (boolean) true if price of object is less than other
        """
        return self.price < other.price

    def __eq__(self, other):
        """
        Checks 2 rooms for equality
        :param other: (HotelRoom) room to compare self against
        :return: (boolean) if the two rooms are equal
        """
        return self.name == other.name and self.price == other.price

    def __add__(self, other):
        """
        Combines 2 rooms together to make a multi-room booking using
        existing rooms' name and price
        :param other: (HotelRoom) Room to combine with self
        :return: (HotelRoom) new HotelRoom combining 2 existing rooms
        """
        new_room = HotelRoom(f'{self.name} & {other.name}')
        new_room.set_price(self.price + other.price)
        if self.status == 'Booked' or other.status == 'Booked':
            new_room.book_room()
        return new_room
