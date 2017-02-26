#Automatic Run following files
#For alexnet
rm -rf ./output/test
sh extract_feature.sh
python mdb_reader.py ./output/test
python videoerror2.py
