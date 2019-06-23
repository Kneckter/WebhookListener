#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import logging
import time
import configargparse
from time import strftime

log = logging.getLogger(__name__)

def get_args():
    # Pre-check to see if the -cf or --config flag is used on the command line.
    # If not, we'll use the env var or default value. This prevents layering of
    # config files as well as a missing config.ini.
    defaultconfigfiles = []
    if '-cf' not in sys.argv and '--config' not in sys.argv:
        defaultconfigfiles = [os.getenv('WEBHOOK_CONFIG', os.path.join(os.path.dirname(__file__), '../config/config.ini'))]
    parser = configargparse.ArgParser(default_config_files=defaultconfigfiles,auto_env_var_prefix='WEBHOOK_')
    parser.add_argument('-cf', '--config', is_config_file=True, help='Set configuration file')
    parser.add_argument('-H', '--host', help='Set web server listening host.', default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, help='Set web server listening port.', default=5000)
    parser.add_argument('--ssl-certificate', help='Path to SSL certificate file.')
    parser.add_argument('--ssl-privatekey', help='Path to SSL private key file.')
    parser.add_argument('--no-file-logs', help=('Disable logging to files. Does not disable --access-logs.'), action='store_true', default=False)
    parser.add_argument('--log-path', help=('Defines directory to save log files to.'), default='logs/')
    parser.add_argument('--log-filename', help=('Defines the log filename to be saved. Allows date formatting, and replaces <SN>'+
                        " with the instance's status name. Read the python time module docs for details. Default: %%Y%%m%%d_%%H%%M_<SN>.log."),
                        default='%Y%m%d_%H%M_<SN>.log'),
    parser.add_argument('--log-wysiwyg', help=('Tells the logger to write the logs as they show in console. Otherwise, just write the messages to the log.'), action='store_true', default=False)
    parser.add_argument('--log-webhook', help=('Tells the logger to display the full webhook in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-gmo-enc', help=('Tells the logger to display the encoded GetMapObjects in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-gmo-par', help=('Tells the logger to display the parsed GetMapObjects in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-gpr-enc', help=('Tells the logger to display the encoded GetPlayerResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-gpr-par', help=('Tells the logger to display the parsed GetPlayerResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-ggir-enc', help=('Tells the logger to display the encoded GymGetInfoResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-ggir-par', help=('Tells the logger to display the parsed GymGetInfoResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-fdr-enc', help=('Tells the logger to display the encoded FortDetailsResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-fdr-par', help=('Tells the logger to display the parsed FortDetailsResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-frs-enc', help=('Tells the logger to display the encoded FortSearchResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-frs-par', help=('Tells the logger to display the parsed FortSearchResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-encounter-enc', help=('Tells the logger to display the encoded EncounterResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('--log-encounter-par', help=('Tells the logger to display the parsed EncounterResponse in console and write it to the log file.'), action='store_true', default=False)
    parser.add_argument('-sn', '--status-name', default=str(os.getpid()), help=('Enable status page database update using STATUS_NAME as main worker name.'))

    parser.set_defaults(DEBUG=False)
    args = parser.parse_args()

    # Allow status name and date formatting in log filename.
    args.log_filename = strftime(args.log_filename)
    args.log_filename = args.log_filename.replace('<sn>', '<SN>')
    args.log_filename = args.log_filename.replace('<SN>', args.status_name)

    return args

def now():
    # The fact that you need this helper...
    return int(time.time())
