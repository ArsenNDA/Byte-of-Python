import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'Desktop', 'logging.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'Desktop', 'logging.log')

print(">>> Save in :", logging_file)

logging.basicConfig(filename=logging_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
