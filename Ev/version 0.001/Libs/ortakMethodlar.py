from datetime import datetime

def hataBas(errMessage):
    errFile = open("../log.txt", encoding='utf-8', mode='a')
    errFile.write("%s %s" % (datetime.now(), errMessage + "\n"))
    errFile.close()
