# CPC_RNode_liveCheck
This Script send you an Email if your RNode has died. 


# HowTo
- First you have stop your RNode.
- Then Restart your RNode with: 
```console
foo@bar:~$ ./cpchain-linux-amd64 run --datadir ./datadir     --unlock YOUR_ADRES     --rpcaddr 127.0.0.1:8501 --port 30311      --rpcapi personal,eth,cpc,admission,net,web3,db,txpool --linenumber &  echo $!> pid.txt
```
Here we start the RNode but we put it in the background and we store the PID in the pid.txt file. Now we can can put the RNode again in the foreground with:
```console
foo@bar:~$ fg
```
We have the PID of our CPC program stored in the file so we can start the python script (which has be in the same folder like the cpchain program) to check if its work:
```console
foo@bar:~$ python3 RNodeLiveCheck.py
```
If verything is fine the program just terminates. If you will kill your RNode the program will send you an Email.

# Crontab
To run the script in a loop you need to call the python script every X Minutes which will check if the Node is alive. For that you can use for example Crontab.


