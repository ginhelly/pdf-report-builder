import unittest

from pdf_report_builder.structure.files.pages_subset import *

class TestPagesSubset(unittest.TestCase):
    chunk = SubsetChunk(1,2)
    chunk2 = SubsetChunk(3)
    subset = PagesSubset()
    subset_chunks = PagesSubset([chunk, chunk2])
    subset_from_string = PagesSubset.from_string('11-10,13')

    def test_subset_chunk(self):
        self.assertEqual(self.chunk.__str__(), '1-2')
    
    def test_subset_chunk_one_page(self):
        self.assertEqual(str(self.chunk2), '3')
    
    def test_subset(self):
        self.assertEqual(str(self.subset), '')
    
    def test_subset2(self):
        self.assertEqual(str(self.subset_chunks), '1-2,3')

    def test_subset3(self):
        s = '10-11,13'
        self.assertEqual(PagesSubset.from_string(s).__str__(), s)
    
    def test_add_chunk(self):
        subset4 = PagesSubset()
        subset4.add_chunk((10, 13))
        subset4.add_chunk((20, 23))
        self.assertEqual(str(subset4), '10-13,20-23')
    
    def test_range(self):
        chunk = SubsetChunk(1,4)
        self.assertListEqual(list(chunk.range), [1,2,3,4])
    
    def test_len(self):
        chunk = SubsetChunk(2,5)
        self.assertEqual(len(chunk), 4)
    
    def test_chunk_iter(self):
        chunk = SubsetChunk(2,5)
        self.assertListEqual(list(chunk), [2,3,4,5])
    
    def test_chunk_iter2(self):
        chunk = SubsetChunk(2)
        self.assertListEqual(list(chunk), [2])
    
    def test_subset_iter(self):
        subset = PagesSubset.from_string('23,27-28')
        self.assertListEqual(
            list(subset), 
            [23,27,28]
        )
    
    def test_wrong_subset(self):
        x = lambda: PagesSubset.from_string('0-0')
        self.assertRaises(ValueError, x)
    
    def test_max_page_num(self):
        x = lambda: PagesSubset.from_string('50-60', max_page_num=10)
        self.assertRaises(ValueError, x)

if __name__ == '__main__':
    unittest.main()