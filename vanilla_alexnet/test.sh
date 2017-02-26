rm -f test.log
sh alexnet_testing.sh 2>&1 | tee -a test.log
