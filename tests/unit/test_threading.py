import threading
import unittest

import time


class BaseThreadingTest(unittest.TestCase):
    def test_snap(self):
        self._caches = {'1.{}'.format(i): None for i in range(100)}
        self.t_cont = True

        def _change_dict():
            i = len(self._caches)
            while self.t_cont:
                i += 1
                self._caches['1.{}'.format(i)] = 1

        t = threading.Thread(target=_change_dict)
        t.start()

        try:
            for _ in range(100):
                for _ in self._caches.values():
                    pass
        finally:
            self.t_cont = False

#
