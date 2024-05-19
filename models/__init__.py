#!/usr/bin/python3
"""the module __init__.py"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

