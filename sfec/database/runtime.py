# -*- coding: utf-8 -*-

from sfec.database.settings import default_settings

_default_store = None


def get_default_store():
    """Returns the single store maintained by the application"""
    global _default_store
    if _default_store is None:
        _default_store = default_settings.get_store()

    return _default_store
