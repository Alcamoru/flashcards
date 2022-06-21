import logging
# initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = '%(levelname)s -> %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


def hypotenuse(a, b):
    h = round(((a ** 2 + b ** 2) ** 0.5), 2) 
    # call the logger
    logging.info(f"Hypotenuse of {a} and {b} is {h}")
    return h
