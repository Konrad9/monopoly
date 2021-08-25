# Copyright (C) 2021 Games Computers Play <https://github.com/gamescomputersplay> and nopeless
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Monopoly Simulator
# Videos with some research using this simulator:
# https://www.youtube.com/watch?v=6EJrZeN0jNI
# https://www.youtube.com/watch?v=Dx1ofZHGUtI

import random
import time
from modules.Log import log
from modules.simulation import *

from settings.data import *

if __name__ == "__main__":

    print("="*OUT_WIDTH)

    t = time.time()
    if seed != "":
        random.seed(seed)
    else:
        random.seed()
    print("Players:", nPlayers, " Turns:", nMoves,
          " Games:", nSimulations, " Seed:", seed)
    results = runSimulation()
    analyzeResults(results)
    log.close()
    analyzeData()
    print("Done in {:.2f}s".format(time.time()-t))
