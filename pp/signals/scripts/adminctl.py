# -*- coding: utf-8 -*-
"""
"""
import os
import logging
import ConfigParser

import cmdln


class AdminCtl(cmdln.Cmdln):
    """Usage:
        signal-admin -c / --config <conf.ini> SUBCOMMAND [ARGS...]
        signal-admin help SUBCOMMAND

    ${command_list}
    ${help_list}

    """
    name = "signal-admin"

    def __init__(self, *args, **kwargs):
        cmdln.Cmdln.__init__(self, *args, **kwargs)
        self.log = logging.getLogger("{}.AdminCmds".format(__name__))

    def get_optparser(self):
        """Parser for global options (that are not specific to a subcommand).
        """
        optparser = cmdln.CmdlnOptionParser(self)

        optparser.add_option(
            '-c', '--config', action='store',
            dest="config_filename",
            default="conf.ini",
            help='The global config file %default'
        )

        return optparser

    def postoptparse(self):
        """runs after parsing global options"""

    @property
    def config(self):
        """Return a config instance when called.

        Implement file change and reloading here?

        """
        cfg_filename = self.options.config_filename
        rc = {}

        if os.path.isfile(cfg_filename):
            config = ConfigParser.ConfigParser()
            self.log.debug("config: recovering from <%s>" % cfg_filename)
            config.read(cfg_filename)
            rc = dict(config.items(self.name))

        else:
            self.log.warn(
                "confg: file not found <%s> using defaults." % cfg_filename
            )

        return rc

    # @cmdln.option(
    #     "-d", "--deindent", action="store_true", dest="deindent",
    #     default=False,
    #     help="Don't indent the JSON written to file (default: %default)."
    # )
    def do_listen(self, subcmd, opts):
        """${cmd_name}: Listen and log traffic on the configured channels.

        ${cmd_usage}
        ${cmd_option_list}

        """
        from pp.signals.signals import Listener
        Listener(config=self.config).run()

    def do_publish(self, subcmd, opts, channel, message):
        """${cmd_name}: Publish a message to a channel.

        ${cmd_usage}
        ${cmd_option_list}

        """
        from pp.signals.signals import Listener
        Listener(config=self.config).publish(channel, message)
