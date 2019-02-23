import unittest

import pipeline.utils.db as db

class TestUDF(unittest.TestCase):

	function = "city"

	def test_basic1(self):
		city_string = 'Richmond'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual('richmond', result)

	def test_basic2(self):
		city_string = 'This is an example that is too long and can not be a city name'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual(None, result)

	def test_basic3(self):
		city_string = '123-45'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual(None, result)

	def test_basic4(self):
		city_string = 'Winston–Salem'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual('winston–salem', result)

	def test_basic5(self):
		city_string = '700 14th St NW, Washington DC 20005'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual('washington', result)

	def test_basic6(self):
		city_string = 'Arlington VA'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual('arlington', result)

	def test_basic7(self):
		city_string = 'New York NY'
		query = f"SELECT {self.function}(CAST('{city_string}' AS varchar)) as result;"
		result = db.execute(query).result[0]
		self.assertEqual('new york', result)

if __name__ == '__main__':
	unittest.main()
