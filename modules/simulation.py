import progressbar
import matplotlib.pyplot as plt
import math
from settings.data import *
from modules.oneGame import *
import numpy as np
import time
from modules.Log import log


def runSimulation():
    """run multiple game simulations"""
    results = []

    if showProgressBar:
        widgets = [progressbar.Percentage(), progressbar.Bar(),
                   progressbar.ETA()]
        pbar = progressbar.ProgressBar(
            widgets=widgets, term_width=OUT_WIDTH, maxval=nSimulations)
        pbar.start()

    for i in range(nSimulations):

        if showProgressBar:
            pbar.update(i+1)

        log.write("="*10+" GAME "+str(i+1)+" "+"="*10+"\n")

        # remaining players - add to the results list
        results.append(oneGame())

        # write remaining players in a data log
        if writeData == "remainingPlayers":
            remPlayers = sum([1 for r in results[-1] if r > 0])
            log.write(str(remPlayers), data=True)

    if showProgressBar:
        pbar.finish()

    return results


def analyzeResults(results):
    """Analize results"""

    remainingPlayers = [0, ]*nPlayers
    for result in results:
        alive = 0
        for score in result:
            if score >= 0:
                alive += 1
        remainingPlayers[alive-1] += 1

    if showRemPlayers:
        print("Remaining:", remainingPlayers)


def analyzeData():

    if writeData == "losersNames" or writeData == "experiment" or writeData == "remainingPlayers":
        groups = {}
        with open("data.txt", "r") as fs:
            for line in fs:
                item = line.strip()
                if item in groups:
                    groups[item] += 1
                else:
                    groups[item] = 1
        experiment = 0
        control = 0
        for item in sorted(groups.keys()):
            count = groups[item]/nSimulations

            if writeData == "losersNames":
                count = 1-count
            if item == "exp":
                experiment = count
            else:
                control += count

            margin = 1.96 * math.sqrt(count*(1-count)/nSimulations)
            print("{}: {:.1%} +- {:.1%}".format(item, count, margin))

        if experiment != 0:
            print("Exp result: {:.1%}".format(experiment-control/(nPlayers-1)))

    if writeData == "netWorth":
        print("graph here")
        npdata = np.transpose(np.loadtxt(
            "data.txt", dtype=int, delimiter="\t"))
        x = np.arange(0, max([len(d) for d in npdata]))

        plt.ioff()
        fig, ax = plt.subplots()
        for i in range(nPlayers):
            ax.plot(x, npdata[i], label='1')
        plt.savefig("fig"+str(time.time())+".png")
