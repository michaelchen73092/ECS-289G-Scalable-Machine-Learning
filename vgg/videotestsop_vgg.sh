#Automatic Run following files
#for var in 6 7 8 9 10 11 12 13 14 15 16
#do
#    find extract_feature_googlenet.sh| xargs -i sed -i 's/iter_'"$var"'/iter_'"$(($var+1))"'/g' {} 
rm -rf ./output/test
sh extract_feature_vgg.sh
python mdb_reader_vgg.py ./output/test
echo "##################################" | tee -a videotestsop_vgg.log
echo "####### iter_20k.caffemodel ######" | tee -a videotestsop_vgg.log
python videoerror2.py | tee -a videotestsop_vgg.log
#done
