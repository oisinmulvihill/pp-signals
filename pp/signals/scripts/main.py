# -*- coding: utf-8 -*-
"""
The admin tool main as configured in the setup.py

"""
import sys
import logging

from .adminctl import AdminCtl


def main():
    """bookingsys-admin main script as set up in the 'setup.py'."""
    log = logging.getLogger()
    hdlr = logging.StreamHandler()
    fmt = '%(asctime)s %(name)s %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.setLevel(logging.DEBUG)
    log.propagate = False

    while True:
        try:
            app = AdminCtl()
            sys.exit(app.main())

        except KeyboardInterrupt:
            log.info("Exit time.")
            break
