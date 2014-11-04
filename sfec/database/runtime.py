# -*- coding: utf-8 -*-

from sfec.database.settings import test_settings, default_settings

# Singleton pattern, grants only one conection to the database.
_default_store = None


def get_default_store():
    """Returns the single store maintained by the application"""
    global _default_store
    if _default_store is None:
        _default_store = default_settings.get_store()

    return _default_store


_test_store = None


def get_test_store():
    global _test_store
    if _test_store is None:
        _test_store = test_settings.get_store()

    return _test_store
