import unittest
from new_feature import some_function  # فرض کن که در فایل new_feature.py تابعی به نام some_function داری

class TestNewFeature(unittest.TestCase):
    
    def test_some_function(self):
        result = some_function(5)  # مقدار نمونه‌ای برای تست
        self.assertEqual(result, 10)  # انتظار داری که خروجی برابر با 10 باشد

if __name__ == '__main__':
    unittest.main()
