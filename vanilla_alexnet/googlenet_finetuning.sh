GLOG_logtostderr=1 ../../build/tools/caffe train \
--solver=./proto/googlenet_solver.prototxt \
--weights=../../models/bvlc_googlenet/bvlc_googlenet.caffemodel
