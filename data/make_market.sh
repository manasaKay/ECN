python download.py 0B8-rUzbwVRk0c054eEozWG9COHM market.zip
python download.py 1h2bLngZmRLhkHGhBr8kUfRkRdZYlUzea market-style.zip
unzip market.zip
unzip market-style.zip
mv Market-1501-v15.09.15 market
mv bounding_box_train_camstyle market/bounding_box_train_camstyle
rm market.zip
rm market-style.zip
rm -rf market/gt_bbox
rm -rf market/gt_query
rm market/readme.txt
