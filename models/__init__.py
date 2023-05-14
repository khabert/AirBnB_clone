#!/usr/bin/env python3
"""
initialises the models storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
