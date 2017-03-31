from __future__ import absolute_import

def add_generators(pelican_object):
    from .generator import SQLGenerator
    return SQLGenerator

def register():
    from pelican import signals
    signals.get_generators.connect(add_generators)
