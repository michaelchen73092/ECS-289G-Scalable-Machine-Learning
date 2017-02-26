rm -f trainvgg.log
#sh ind2core_finetuning.sh 2>&1 | tee -a train.log
sh vgg_finetuning.sh 2>&1 | tee -a trainvgg.log

