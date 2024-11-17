import unittest
from rna_transcription import to_rna

class TestRnaTranscription(unittest.TestCase):
    def test_to_rna(self):
        self.assertEqual(to_rna("ACGT"), "UGCA")
        self.assertEqual(to_rna("GGTCTAA"), "CCAGAUU")
        self.assertEqual(to_rna("AAGGCC"), "UUCCGG")
        self.assertEqual(to_rna("TTTT"), "AAAA")

if __name__ == '__main__':
    unittest.main()