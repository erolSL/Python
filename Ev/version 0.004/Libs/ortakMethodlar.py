#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

logFile = "../log.txt"

def hataBas(errMessage):
    errFile = open(logFile, encoding='utf-8', mode='a')
    errFile.write("%s %s" % (datetime.now(), errMessage) + "\n")
    errFile.close()

def extract(text, marker):
    endSymbol = '\n'
    return [item.split(endSymbol)[0]
        for item in text.split(marker + ":")[1:]][0]