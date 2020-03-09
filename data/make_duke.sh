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
