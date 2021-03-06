from __future__ import absolute_import, division, print_function, unicode_literals


class TransportError(Exception):
    pass


class TransportFileNotFound(OSError):
    pass


class TransportNotFound(TransportError):
    pass


class TransportLoadError(TransportError):
    pass


class TransportRequirementError(TransportError):
    pass


class ReceiverError(Exception):
    pass


class ConfigError(Exception):
    pass