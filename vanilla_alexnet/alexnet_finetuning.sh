GLOG_logtostderr=1 ../../build/tools/caffe train \
--solver=./proto/alexnet_ind_finetuning_solver.prototxt \
--weights=../../models/bvlc_alexnet/bvlc_alexnet.caffemodel
