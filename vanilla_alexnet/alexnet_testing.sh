GLOG_logtostderr=1 ../../build/tools/caffe test \
--model=./proto/alexnet_ind_finetuning_test.prototxt \
--weights=./snapshot/caffe_alexnet_finetuning_iter_20000.caffemodel \
--iterations=304 \
--gpu=1

