#!/usr/bin/env python3
import re
import os
def def_credentials(chain):

    #TODO: add osx/windows support for ac_dir
    ac_dir = os.environ['HOME'] + '/.komodo'
    #chain = 'STAKEDW1'

    # define config file path
    if chain == 'KMD':
        coin_config_file = str(ac_dir + '/komodo.conf')
    else:
        coin_config_file = str(ac_dir + '/' + chain + '/' + chain + '.conf')
        print(coin_config_file)
    #define rpc creds
    with open(coin_config_file, 'r') as f:
        #print("Reading config file for credentials:", coin_config_file)
        for line in f:
            l = line.rstrip()
            if re.search('rpcuser', l):
                rpcuser = l.replace('rpcuser=', '')
            elif re.search('rpcpassword', l):
                rpcpassword = l.replace('rpcpassword=', '')
            elif re.search('rpcport', l):
                rpcport = l.replace('rpcport=', '')
    return('http://' + rpcuser + ':' + rpcpassword + '@127.0.0.1:' + rpcport)