import unittest

import pipeline.utils.db as db

# 16 types of phone number 
class TestUDF(unittest.TestCase):

		function = "phone"

		def test_basic1(self):
			phone_string = '(202) 957-8741'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('DC', result)

		def test_basic2(self):
			phone_string = '(202)555-7766'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('DC', result)

		def test_basic3(self):
			phone_string = '5417522520'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('OR', result)

		def test_basic4(self):
			phone_string = '907-632-1268'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('AK', result)

		def test_basic5(self):
			phone_string = '12029974555'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('DC', result)

		def test_basic6(self):
			phone_string = '301.775.8616'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('MD', result)	

		def test_basic7(self):
			phone_string = ' 563-302-5771'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('IA', result)

		def test_basic8(self):
			phone_string = '9074635080  9077238267'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('AK', result)

		def test_basic9(self):
			phone_string = '907-723-1494  907 723 1494 ' 
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('AK', result)

		def test_basic10(self):
			phone_string = '9074635080  9077238267  9077238267'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('AK', result)

		def test_basic11(self):
			phone_string = '(404) 817 - 8500'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('GA', result)

		def test_basic12(self):
			phone_string = '(512)4433675'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('TX', result)

		def test_basic13(self):
			phone_string = '(919) 313-8500 x8530'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('NC', result)

		def test_basic14(self):
			phone_string = '225-344-0381 ext. 221'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('LA', result)

		def test_basic15(self):
			phone_string = '703-112-9971x27'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('VA', result)

		def test_basic16(self):
			phone_string = '275-6427'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual(None, result)

		def test_basic17(self):
			phone_int = 7031139971
			query = f"SELECT {self.function}(CAST('{phone_int}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('VA', result)

		def test_basic18(self):
			phone_int = 17032756427
			query = f"SELECT {self.function}(CAST('{phone_int}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual('VA', result)

		def test_basic19(self):
			phone_string = '000-275-6427'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual(None, result)

		def test_basic20(self):
			phone_string = '111-222-3333'
			query = f"SELECT {self.function}(CAST('{phone_string}' AS varchar)) as result;"
			result = db.execute(query).result[0]
			self.assertEqual(None, result)	

if __name__ == '__main__':
	unittest.main()