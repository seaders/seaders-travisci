import threading
import unittest

import time


class BaseThreadingTest(unittest.TestCase):
    def test_snap_dict_size(self):
        caches = {'1.{}'.format(i): None for i in range(10000)}
        self._caches = dict(caches.items())
        self.t_cont = True

        def _change_dict():
            i = len(self._caches)
            while self.t_cont:
                i += 1
                self._caches['1.{}'.format(i)] = 1
                time.sleep(0.001)

        t = threading.Thread(target=_change_dict)
        t.start()

        try:
            for _ in self._caches.values():
                pass

        finally:
            self.t_cont = False
            
        self.t_cont = False

#
