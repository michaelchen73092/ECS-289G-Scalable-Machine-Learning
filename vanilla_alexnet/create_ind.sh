#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs

EXAMPLE=/home/SSD3/ycjlin-data/20150928caffe/examples/vanilla_alexnet2
LIST=$EXAMPLE/list
TOOLS=/home/SSD3/ycjlin-data/20150928caffe/build/tools
DATA_ROOT=/home/SSD3/ycjlin-data/actrcg/video_sync/

# variables
#LMDBINPUT=train000.lst
#LMDBOUPUT=ind_sim_train_lmdb
LMDBINPUT=$1
LMDBOUPUT=$2

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
#RESIZE=false
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$DATA_ROOT" ]; then
  echo "Error: DATA_ROOT is not a path to a directory: $DATA_ROOT"
  echo "Set the DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $DATA_ROOT \
    $LIST/$LMDBINPUT \
    $EXAMPLE/$LMDBOUPUT

echo "Done."
