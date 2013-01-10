# -*- coding: utf-8 -*-
"""

"""
import signal
import logging
import threading

import redis


class Listener(threading.Thread):
    """This subscribes specific channels on Redis PUB/SUB.

    The listener will set up SIGHUP, SIGINT & SIGTERM handler which will
    cause the run() to exit.

    """
    def __init__(self, config={}):
        """Set up the listener's Redis config.

            config = {
                "redis.host": "...",
                "redis.port": ...,
                "redis.db": ...,
                "redis.channels": "abc, efg, ..."
            }

        """
        threading.Thread.__init__(self)
        self.log = logging.getLogger("{}.Listener".format(__name__))

        host = config.get("redis.host", "0.0.0.0")
        port = int(config.get("redis.port", 6379))
        db = config.get("redis.db", 0)
        channels = config.get("redis.channels", "")
        channels = [c.strip() for c in channels.split(',') if c]
        self.log.info("Config host: {0}, port: {1}, channels: {2!r}".format(
            host, port, channels
        ))

        signal.signal(signal.SIGINT, self.syssig_handler)
        signal.signal(signal.SIGHUP, self.syssig_handler)
        signal.signal(signal.SIGTERM, self.syssig_handler)

        self.redis = redis.StrictRedis(host, port=port, db=db)
        self.pubsub = self.redis.pubsub()
        if channels:
            self.subscribe(channels)
        self.exitTime = False

    def subscribe(self, channels):
        """A pass through to the PubSub object subscribe."""
        self.pubsub.subscribe(channels)

    def unsubscribe(self, channels=[]):
        """A pass through to the PubSub object unsubscribe."""
        self.pubsub.unsubscribe(channels)

    def publish(self, channel, message):
        """A pass through to the PubSub object publish."""
        self.redis.publish(channel, message)

    def syssig_handler(self, sig, frame):
        """Catch SIGINT, SIGHUP & SIGTERM and stop and exit cleanly."""
        self.log.warn(
            "signal_handler: signal<{!r}> caught, stopping PubSub.".format(sig)
        )
        self.shutdown()

    def shutdown(self):
        """Set the exitTime flag and cause the PubSub listener to exit."""
        self.exitTime = True
        self.pubsub.close()

    def handle(self, item):
        print item['channel'], ":", item['data']

    def run(self):
        self.exitTime = False
        try:
            for item in self.pubsub.listen():
                self.handle(item)

        except AttributeError:
            # if its exit time this will be raised by listen as pubsub.close
            # was called. This is fine and we can ignore this exception.
            if not self.exitTime:
                raise
