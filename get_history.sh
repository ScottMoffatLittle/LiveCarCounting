#!/bin/bash

#python Vehicle_Counting.py "rtmp://s12.us-east-1.skyvdn.com:1935/rtplive/SalemI81MM140" --iscam --droi "0,150|0,240|160,240|220,90|110,80" --showdroi --tracker "csrt" --di 5 --mctf 30 --ID 1
python Vehicle_Counting.py "rtmp://s11.us-east-1.skyvdn.com:1935/rtplive/FairfaxCCTV335" --iscam --droi "80,200|240,200|240,100|160,80|20,80" --showdroi --tracker "csrt" --record --di 5 --mctf 30 --ID 2
#python Vehicle_Counting.py "rtmp://s11.us-east-1.skyvdn.com:1935/rtplive/FairfaxCCTV337" --iscam --droi "0,130|0,240|160,240|280,120|90,105" --showdroi --tracker "csrt" --di 5 --mctf 30 --ID 3
