#!/bin/bash

geth --identity "miner1" \
--networkid 42 \
--datadir "~/Desktop/Github/Blockchain_dev/MyChains/miner1" \
--nodiscover \
--mine \
--minerthreads "1" \
--rpc --rpcport "8042" \
--port "30303" \
--allow-insecure-unlock \
--unlock 0 \
--password ~/Desktop/Github/Blockchain_dev/MyChains/miner1/password.sec \
--ipcpath "~/.ethereum/geth.ipc"
