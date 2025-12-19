class Driver_Manager:
    _driver = None

    @classmethod
    def set_driver(cls, driver):
        cls._driver = driver

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            raise Exception('Driver Not Set')
        return cls._driver


