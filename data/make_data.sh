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

python download.py 1jjE85dRCMOgRtvJ5RQV9-Afs-2_5dY3O duke.zip
python download.py 1QzORs_vSUCnqI5QuzLSq9snt0prB9-Hx duke-style.zip
unzip duke.zip
unzip duke-style.zip
mv DukeMTMC-reID duke
mv bounding_box_train_camstyle duke/bounding_box_train_camstyle
rm duke.zip
rm duke-style.zip
rm -rf __MACOSX
rm duke/CITATION.txt
rm duke/LICENSE_DukeMTMC-reID.txt
rm duke/LICENSE_DukeMTMC.txt
rm duke/README.md
