import threading
import unittest

import time


class BaseThreadingTest(unittest.TestCase):
    def test_snap(self):
        self._caches = {'1.{}'.format(i): None for i in range(10000)}
        self.t_cont = True

        def _change_dict():
            while self.t_cont:
                self._caches['1.2'] = 1
                self._caches.pop('1.2')

        t = threading.Thread(target=_change_dict)
        t.start()

        for _ in range(10):
            for _ in self._caches.values():
                pass

        self.t_cont = False

#
