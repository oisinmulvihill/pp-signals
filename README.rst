pp-signals
==========

.. contents::


Introduction
------------

This provides the namespaced package: pp.signals


Testing
-------

Activate the dev environment and change into pp-signals.

Run all tests
~~~~~~~~~~~~~

From here you can do::

    python runtests.py -s


signals-admin
-------------

This tool provides some admin functions to test publish and subscribing via
Redis PubSub::

    # listen to redis.channels subscripts from config:
    signal-admin -c conf.ini listen

    # Send a message to a channel:
    signal-admin -c conf.ini publish <channel> <message string>


Configuration
`````````````

This is a typical example of conf.ini::

    [signal-admin]
    redis.host = 0.0.0.0
    redis.port = 6379
    redis.db = 0
    redis.channels = test,

