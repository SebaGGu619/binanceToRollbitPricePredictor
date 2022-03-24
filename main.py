from binance.client import Client
from time import sleep
import os
import json
from websocket import create_connection

# wss://stream.binance.com:9443/ws/btcusdt@trade

global pretGlobal

ws = create_connection("wss://stream.binance.com:9443/ws/btcusdt@trade")
print(" -Logged In-\n---------------")

result = ws.recv()
result = json.loads(result)
pretGlobal = float(result["p"])

total = 0
tempPrev = pretGlobal
diff1 = pretGlobal - tempPrev
diffPrev = diff1
# tempPrev2 = pretGlobal
totalUP = 0
totalDOWN = 0

while True:
    # print(".")
    result = ws.recv()
    result = json.loads(result)
    pretGlobal = float(result["p"])

    diff1 = pretGlobal - tempPrev

    # diff2 = pretGlobal - tempPrev2

    # print(diff1 + diff2)

    averageDiff = (diff1 + diffPrev) / 2

    thresholdView = 1
    if averageDiff > thresholdView or averageDiff < -thresholdView:
        # print(averageDiff)
        total = total + averageDiff

    if total > 1:
        total = total - 1
        # print("UP " + str(total))
        totalUP = totalUP + 1
        totalDOWN = 0
    else:
        if total < -1:
            total = total + 1
            # print("DOWN " + str(total))
            totalDOWN = totalDOWN + 1
            totalUP = 0
        else:
            # print("EH " + str(total))
            totalUP = 0
            totalDOWN = 0

    if totalUP >= 5:
        print("UP")
    else:
        if totalDOWN >= 5:
            print("DOWN")
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # if diff1 <= -15:
    # os.system("xdotool click 1")
    # print("UP " + str(pretGlobal) + " " + str(pretGlobal + 35))
    # break
    # if diff1 >= 15:
    # print("DOWN " + str(pretGlobal) + " " + str(pretGlobal + 35))
    # tempPrev2 = tempPrev
    tempPrev = pretGlobal
    diffPrev = diff1
