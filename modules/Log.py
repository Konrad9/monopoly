from settings.data import *


class Log:

    def __init__(self):
        for n in ['log.txt', 'data.txt']:
            with open(n, "w") as f:
                f.write("")
        # Use explicit form of append logging
        self.datafs = open("data.txt", "ab", 0)
        self.fs = open("log.txt", "ab", 0)

    def close(self):
        self.datafs.close()
        self.fs.close()

    def write(self, text, level=0, data=False):
        if data and writeData:
            self.datafs.write(bytes(text+"\n", "utf-8"))
            return
        if writeLog:
            if level < 2:
                self.fs.write(bytes("\n"*(2-level), "utf-8"))
            self.fs.write(bytes("\t"*level+text+"\n", "utf-8"))


log = Log()
