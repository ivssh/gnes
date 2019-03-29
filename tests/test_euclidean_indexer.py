import ctypes
import os
import unittest

import numpy as np

from gnes.indexer import EuclideanIndexer


class TestEUIndexer(unittest.TestCase):
    def setUp(self):
        self.toy_query = np.random.random([1000, 20]).astype(np.float32)
        self.toy_label = np.random.randint(0, 1e9, [1000]).tolist()
        self.add_query = np.random.random([1000, 20]).astype(np.float32)
        self.add_label = np.random.randint(0, 1e9, [1000]).tolist()

        self.sub_query = self.toy_query[:10]
        self.dump_path = './test_eu_indexer'

    def tearDown(self):
        if os.path.exists(self.dump_path):
            os.remove(self.dump_path)

    def test_add(self):
        fd = EuclideanIndexer()
        fd.add(self.toy_query, self.toy_label)
        self.assertEqual(fd._count, self.toy_query.shape[0])
        fd.add(self.add_query, self.add_label)
        self.assertEqual(fd._count,
                         self.toy_query.shape[0]+self.add_query.shape[0])

    def test_query(self):
        fd = EuclideanIndexer()
        fd.add(self.toy_query, self.toy_label)
        ret = fd.query(self.sub_query, top_k=5)
        self.assertEqual(len(ret), self.sub_query.shape[0])
        self.assertEqual(len(ret[0]), 5)

    def test_dump_load(self):
        tmp = EuclideanIndexer()
        tmp.add(self.toy_query, self.toy_label)
        tmp.dump(self.dump_path)

        fd = EuclideanIndexer.load(self.dump_path)
        ret = fd.query(self.sub_query, top_k=2)
        self.assertEqual(len(ret), self.sub_query.shape[0])
        self.assertEqual(len(ret[0]), 2)