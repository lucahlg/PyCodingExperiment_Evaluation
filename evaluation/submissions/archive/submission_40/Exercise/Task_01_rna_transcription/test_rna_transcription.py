import unittest
from rna_transcription import to_rna

class TestRnaTranscription(unittest.TestCase):
    def test_to_rna(self):
        self.assertEqual(to_rna("ACGTGGTCTTAA"), "UGCACCAGAAUU")
        self.assertEqual(to_rna("GCTA"), "CGAU")
        self.assertEqual(to_rna("AAGCTT"), "UUCGAA")

if __name__ == '__main__':
    unittest.main()