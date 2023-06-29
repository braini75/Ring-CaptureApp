"""

"""
import logging
import capture_server
import ast
import threading
from configparser import ConfigParser

config = ConfigParser()
config.read('etc/settings.cfg')

log_file = config['logging'].get('access_log_file')
level = config['logging'].get('log_level')
port_list = ast.literal_eval(config['main'].get('port_list'))


def main():
    # Get a list of all sections
    logging.basicConfig(filename=log_file, level=logging.getLevelName(level))
    logging.info('Started')
    # do something
    for port in port_list:
        srv = threading.Thread(target=capture_server.run_server, args=("", port,))
        srv.start()
        #srv.join()
        #capture_server.run_server("", port)

    srv.join()
    logging.info('Finished')


if __name__ == '__main__':
    main()
    