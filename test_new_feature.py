import unittest
from new_feature import sample_function

class TestNewFeature(unittest.TestCase):
    def test_sample_function(self):
        result = sample_function()
        self.assertIsNone(result)  # انتظار می‌رود خروجی None باشد

if __name__ == '__main__':
    unittest.main()
