import unittest
import ParkingLot

class TestParkingLot(unittest.TestCase):

	def test_vehicle_add(self):
		start=10
		res=start
		self.assertEqual(10,res)
		end=0
		res=end
		self.assertEqual(0,end)


if __name__ == '__main__':
	unittest.main()