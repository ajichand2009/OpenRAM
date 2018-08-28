#!/usr/bin/env python3
"""
Run regresion tests on a parameterized bitcell
"""

import unittest
from testutils import header,openram_test
import sys,os
sys.path.append(os.path.join(sys.path[0],".."))
import globals
from globals import OPTS
import debug

OPTS = globals.OPTS

@unittest.skip("SKIPPING 04_pbitcell_test")
class pbitcell_test(openram_test):

    def runTest(self):
        globals.init_openram("config_20_{0}".format(OPTS.tech_name))
        global verify
        import verify

        import pbitcell
        import tech

        debug.info(2, "Bitcell with 1 of each port: read/write, write, and read")
        tx = pbitcell.pbitcell(num_readwrite=1,num_write=1,num_read=1)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read/write ports")
        tx = pbitcell.pbitcell(num_readwrite=0,num_write=1,num_read=1)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 write ports")
        tx = pbitcell.pbitcell(num_readwrite=1,num_write=0,num_read=1)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read ports")
        tx = pbitcell.pbitcell(num_readwrite=1,num_write=1,num_read=0)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read ports and 0 write ports")
        tx = pbitcell.pbitcell(num_readwrite=1,num_write=0,num_read=0)
        self.local_check(tx)

        debug.info(2, "Bitcell with 2 of each port: read/write, write, and read")
        tx = pbitcell.pbitcell(num_readwrite=2,num_write=2,num_read=2)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read/write ports")
        tx = pbitcell.pbitcell(num_readwrite=0,num_write=2,num_read=2)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 write ports")
        tx = pbitcell.pbitcell(num_readwrite=2,num_write=0,num_read=2)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read ports")
        tx = pbitcell.pbitcell(num_readwrite=2,num_write=2,num_read=0)
        self.local_check(tx)
        
        debug.info(2, "Bitcell with 0 read ports and 0 write ports")
        tx = pbitcell.pbitcell(num_readwrite=2,num_write=0,num_read=0)
        self.local_check(tx)

        globals.end_openram()



# instantiate a copy of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()
