GLOG_logtostderr=1 ../../build/tools/caffe test \
--model=./proto/googlenet_test.prototxt \
--weights=./snapshot/caffe_googlenet_correct_iter_20000.caffemodel \
--iterations=304 \
--gpu=1

