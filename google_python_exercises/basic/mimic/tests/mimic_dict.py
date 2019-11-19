import os
import unittest
from tempfile import NamedTemporaryFile

from google_python_exercises.basic.mimic import mimic


class MimicDictTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        tmpfile = NamedTemporaryFile(delete=False)
        cls.filename = tmpfile.name
        tmpfile.write(
            """tudo bem ou Tudo ótimo?\n\n\n""".encode('utf-8')
        )
        tmpfile.close()

    @classmethod
    def tearDownClass(cls) -> None:
        os.unlink(cls.filename)

    def test_mimic_exists(self):
        self.assertTrue(callable(mimic.mimic_dict))
        self.assertTrue(callable(mimic.print_mimic))

    def test_map(self):
        result = mimic.mimic_dict(self.filename)
        self.assertDictEqual(result, {
            '': ['tudo'],
            'tudo': ['bem', 'ótimo?'],
            'bem': ['ou'],
            'ou': ['Tudo'],
            'ótimo?': [''],
        })
        mimic.print_mimic(result, '')
