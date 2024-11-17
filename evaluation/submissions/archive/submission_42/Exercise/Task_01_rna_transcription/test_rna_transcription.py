import unittest
from rna_transcription import to_rna

class TestRnaTranscription(unittest.TestCase):
    def test_dna_to_rna(self):
        self.assertEqual(to_rna("ACGTGGTCTTAA"), "UGCACCAGAAUU")
        self.assertEqual(to_rna("GGTCTTAA"), "CCAGAUU")
        self.assertEqual(to_rna("A"), "U")
        self.assertEqual(to_rna("T"), "A")
        self.assertEqual(to_rna("C"), "G")
        self.assertEqual(to_rna("G"), "C")

if __name__ == '__main__':
    unittest.main()