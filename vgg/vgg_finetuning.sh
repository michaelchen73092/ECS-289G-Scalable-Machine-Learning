GLOG_logtostderr=1 ../../build/tools/caffe train \
--solver=./proto/vgg_solver.prototxt \
--weights=../../models/VGG/VGG_ILSVRC_19_layers.caffemodel
