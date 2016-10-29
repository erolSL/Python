from datetime import datetime

logFile = "../log.txt"

def hataBas(errMessage):
    errFile = open(logFile, encoding='utf-8', mode='a')
    errFile.write("%s %s" % (datetime.now(), errMessage + "\n"))
    errFile.close()
