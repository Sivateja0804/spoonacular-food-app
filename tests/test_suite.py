import unittest
import os
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(os.getcwd())
    runner = unittest.TextTestRunner()
    runner.run(suite)
