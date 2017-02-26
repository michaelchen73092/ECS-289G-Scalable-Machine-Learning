import leveldb
import binascii
import numpy as np
import caffe
import sys
from caffe.proto import caffe_pb2

## parse input argument
dbName = sys.argv[1]

# open leveldb files

db = leveldb.LevelDB(dbName)

# get db iterator

it = db.RangeIter()

f1=open('./mdb_reader2.txt','w+')
for key,value in it:
    # convert string to datum
    datum = caffe_pb2.Datum.FromString(db.Get(key))
    
    # convert datum to numpy string
    f1.write('key:' + str(key) + '\n')
    arr = caffe.io.datum_to_array(datum)
    
    i = 0
    # convert to svm format

    for i in range(0, len(arr)):
        f1.write(str(i) + ':' +str(arr[i].tolist()[0]) + '\n')

f1.close()
