import os
import tempfile

from unittest import TestCase


class FileTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        file_ = tempfile.NamedTemporaryFile(delete=False)
        cls.filename = file_.name
        file_.close()

    @classmethod
    def tearDownClass(cls) -> None:
        os.unlink(cls.filename)
