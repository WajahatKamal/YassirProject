import os
import json


class Settings(object):
    """Simple singleton class for managing and accessing settings"""

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_settings.json')) as f:
            setting = json.load(f)
            self.browser = setting['browser']
            self.driver_timeout = int(setting['driver_timeout'])
            self.wait_time = setting['wait_time']


settings = Settings()
