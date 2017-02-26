mkdir -p output
rm -rf output/test
./extract_feature.sh # need update for model name and minibatch
python mdb_reader.py output/test
python videoerror2.py
