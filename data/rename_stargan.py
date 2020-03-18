import os 
import argparse

# 0002_c1s1_000451_03_fake_1to2.jpg <-- 0002_c1s1_000451_03_fake_2.jpg
def main(args):  
    for filename in os.listdir(args.folder_name + "/bounding_box_train_camstyle_stargan"): 
        cam_type = filename[6]
        if args.folder_name == 'market':
            dst = filename[:25] + cam_type + "to" + filename[25:]
        elif args.folder_name == 'duke':
            dst = filename[:22] + cam_type + "to" + filename[22:]    
        os.rename(args.folder_name + "/bounding_box_train_camstyle_stargan/" + filename, args.folder_name + "/bounding_box_train_camstyle_stargan/" + dst) 
  

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder_name', type=str, required=True)
    args = parser.parse_args()
    main(args) 