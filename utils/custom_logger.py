import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists(r"C:\Users\ASUS\Desktop\Projects\PythonSeleniumFramework\Logs"):
            os.makedirs(r"C:\Users\ASUS\Desktop\Projects\PythonSeleniumFramework\Logs")

        logging.basicConfig(
            filename=r"C:\Users\ASUS\Desktop\Projects\PythonSeleniumFramework\\Logs\\automation.log",
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            force=True
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
