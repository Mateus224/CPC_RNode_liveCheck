# CPC_RNode_liveCheck
This Script send you an Email if your RNode has died. 


# HowTo
- First you have stop your RNode.
- Then Restart your RNode with: 
```console
foo@bar:~$ ./cpchain-linux-amd64 run --datadir ./datadir     --unlock yourRNodeAddress     --rpcaddr 127.0.0.1:8501 --port 30311 --mine     --rpcapi personal,eth,cpc,admission,net,web3,db,txpool,miner --linenumber &  echo $!> pid.txt
```
Here we start the RNode but we put it in the background and we store the PID in the pid.txt file. Now we can can put the RNode again in the foreground with:
```console
foo@bar:~$ fg
```
We have the PID of our CPC program stored in the file. Before we can start the python file you need repleace in the RNodeLiveCheck.py your email andress and your password for accessing your email account. If you use gmail it should works otherwise you have to change line 60 to the domain of your Email Provider too. After that we can start the python script (which has be in the same folder like the cpchain program):
```console
foo@bar:~$ python3 RNodeLiveCheck.py
```
If verything is fine the program just terminates. If you will kill your RNode the program will send you an Email.

# Crontab
To run the script in a loop you need to call the python script every X Minutes which will check if the Node is alive. For that you can use for example Crontab.

If you have installed Crontab then write into the console:

```console
foo@bar:~$ crontab -e
```
choose an editor and add on the end of the file this line:
```console
5 * * * * /usr/bin/python3 /path/to/the/python/script.py
```
the 5 means that every 5 min the script will check if your RNode is alive.

If you like the script you can give me a STAR ;p 

