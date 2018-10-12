from __future__ import print_function, unicode_literals, absolute_import

import os
from os import path
import unittest
from shutil import rmtree
from tempfile import mkdtemp, mkstemp

from pelican import Pelican
from pelican.settings import read_settings

import pelicansqlgenerator


class TestSQLGenerator(unittest.TestCase):
    def setUp(self):
        self.temp_work = mkdtemp(prefix="pelican.")
        self.temp_path = mkdtemp(prefix="pelicantests.")
        self.temp_cache = mkdtemp(prefix="pelicancache.")

    def tearDown(self):
        rmtree(self.temp_work)
        rmtree(self.temp_path)
        rmtree(self.temp_cache)

    def test_run(self):
        """ Should run without any data without error """
        from peewee import SqliteDatabase
        from pelicansqlgenerator import models
        db_fd, db_fn = mkstemp(prefix="pelicandb.")
        db = SqliteDatabase(db_fn)
        db_url = "sqlite:///" + db_fn
        models.init_db(db)
        # test
        settings = read_settings(path=None, override=dict(
            PATH=self.temp_work,
            OUTPUT_PATH=self.temp_path,
            CACHE_PATH=self.temp_cache,
            PLUGINS=[pelicansqlgenerator],
            SQL_DATABASE=db_url,
        ))
        pelican = Pelican(settings=settings)
        pelican.run()
        # ----
        os.close(db_fd)
        os.unlink(db_fn)

    def test_with_sqlite(self):
        """ Should run without any data without error """
        test_db = path.join(path.dirname(__file__), "data.db")
        settings = read_settings(path=None, override=dict(
            PATH=self.temp_work,
            OUTPUT_PATH=self.temp_path,
            CACHE_PATH=self.temp_cache,
            PLUGINS=[pelicansqlgenerator],
            SQL_DATABASE="sqlite:///{}".format(test_db),
        ))
        pelican = Pelican(settings=settings)
        pelican.run()

