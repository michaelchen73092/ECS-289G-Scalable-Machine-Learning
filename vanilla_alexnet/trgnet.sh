rm -f traingnet.log
#sh ind2core_finetuning.sh 2>&1 | tee -a train.log
sh googlenet_finetuning.sh 2>&1 | tee -a traingnet.log

