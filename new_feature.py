# test_new_feature.py

import unittest
from new_feature import sample_function

class TestNewFeature(unittest.TestCase):

    def test_sample_function(self):
        # چون sample_function فقط چیزی را پرینت می‌کند، نمی‌توانیم از assert برای بررسی آن استفاده کنیم.
        # اینجا فقط به عنوان نمونه تست تعریف شده است.
        self.assertIsNone(sample_function())  # چون این تابع None برمی‌گرداند.

if __name__ == '__main__':
    unittest.main()
