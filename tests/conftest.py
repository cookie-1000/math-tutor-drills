# pytest configuration file to ensure src/ is on sys.path for local imports
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
