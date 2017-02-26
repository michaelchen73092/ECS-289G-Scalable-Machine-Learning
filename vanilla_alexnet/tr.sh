rm -f train.log
#sh ind2core_finetuning.sh 2>&1 | tee -a train.log
sh alexnet_finetuning.sh 2>&1 | tee -a train.log

