import threading
import unittest

import time


class BaseThreadingTest(unittest.TestCase):
    def test_snap_dict_size(self):
        caches = {'1.{}'.format(i): None for i in range(10000)}
        self._caches = dict(caches.items())
        self.t_cont = True
        self.t_delay = True

        def _change_dict():
            i = len(self._caches)
            while self.t_cont:
                while self.t_delay:
                    self._caches = caches
                    time.sleep(0.001)

                i += 1
                self._caches['1.{}'.format(i)] = 1
                time.sleep(0.001)

        t = threading.Thread(target=_change_dict)
        t.start()

        try:
            for _ in range(100):
                self.t_delay = False
                for _ in self._caches.values():
                    pass
                self.t_delay = True

        finally:
            self.t_cont = False

#
