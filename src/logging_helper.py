import logging
import time

logging.basicConfig(filename='.log', level=logging.DEBUG)


def function_logs(func):
    def wrapper(*args, **kwargs):

        output = None

        try:
            start_time = time.time()
            output = func(*args, **kwargs)
            total_time_taken = time.time() - start_time
            logging.debug(f'[function] completed %s, in %d, output: {output}' % (func.__name__, total_time_taken))

        except Exception as err:
            logging.error(f'[function] error %s : %s' % (func.__name__, err))

        return output

    return wrapper


def info(data: any) -> None:
    logging.info(data)


def debug(data: any) -> None:
    logging.debug(data)


def warning(data: any) -> None:
    logging.warning(data)


def error(data: any) -> None:
    logging.error(data)
