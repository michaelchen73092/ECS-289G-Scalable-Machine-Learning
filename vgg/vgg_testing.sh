GLOG_logtostderr=1 ../../build/tools/caffe test \
--model=./proto/vgg_test.prototxt \
--weights=./snapshot/caffe_vgg_iter_20000.caffemodel \
--iterations=304 \
--gpu=1

