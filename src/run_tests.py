﻿# -*- coding: utf-8 -*-
import unittest
import languageHandler

languageHandler.setLanguage("en")


testmodules = ["test.test_setup_py2exe", "test.test_base_interactor", "test.test_audiorecorder", "test.test_renderers"]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner(verbosity=2).run(suite)