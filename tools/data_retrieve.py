import os 
import sys
import tarfile

def unzip(filename, path):
    tar = tarfile.open(filename)
    tar.extractall(path)
    tar.close()

if __name__ == "__main__":
    data_path = "./ORCHID_data.tar.gz"
    if not os.path.exists(data_path):
        print("Data file not found. Please download and put it in the parent directory of this repository.")
        sys.exit()
    unzip(data_path, "./") #you get the main folder
    os.remove(data_path)
    data_path = "./ORCHID_data"
    for filename in os.listdir(data_path):
        if ".DS_Store" in filename:
            continue
        if filename.endswith(".tar.gz"):
            unzip(os.path.join(data_path, filename), data_path) # normal.tar.gz => normal, OSCC.tar.gz => OSCC, OSMF.tar.gz => OSMF
            level_class = os.path.join(data_path, filename.split(".")[0])
            for level_class_filename in os.listdir(level_class):
                if ".DS_Store" in level_class_filename:
                    continue
                if level_class_filename.endswith(".tar.gz"):
                    unzip(os.path.join(level_class, level_class_filename), level_class) 
                    # normal_patient.tar.gz => normal_patient, OSMF_patient.tar.gz => OSMF_patient, 
                    # wdoscc.tar.gz => wdoscc, pdoscc.tar.gz => pdoscc, mdoscc.tar.gz => mdoscc
                    level_class_2 = os.path.join(level_class, level_class_filename.split(".")[0])
                    for level_class_filename_2 in os.listdir(level_class_2):
                        if ".DS_Store" in level_class_filename_2:
                            continue
                        if level_class_filename_2.endswith(".tar.gz"):
                            unzip(os.path.join(level_class_2, level_class_filename_2), level_class_2) 
                            # normal_patient_100x.tar.gz => normal_patient_100x, normal_patient_patches.tar.gz => normal_patient_patches
                            # OSMF_patient_100x.tar.gz => OSMF_patient_100x, OSMF_patient_patches.tar.gz => OSMF_patient_patches
                            # wdoscc_patient.tar.gz => wdoscc_patient, wdoscc_patient_patches.tar.gz => wdoscc_patient_patches
                            # pdoscc_patient.tar.gz => pdoscc_patient, pdoscc_patient_patches.tar.gz => pdoscc_patient_patches
                            # mdoscc_patient.tar.gz => mdoscc_patient, mdoscc_patient_patches.tar.gz => mdoscc_patient_patches
                            level_class_3 = os.path.join(level_class_2, level_class_filename_2.split(".")[0])
                            if "OSCC" in level_class_3:
                                for level_class_filename_3 in os.listdir(level_class_3):
                                    if ".DS_Store" in level_class_filename_3:
                                        continue
                                    if level_class_filename_3.endswith(".tar.gz"):
                                        unzip(os.path.join(level_class_3, level_class_filename_3), level_class_3)
                                        os.remove(os.path.join(level_class_3, level_class_filename_3))
                            os.remove(os.path.join(level_class_2, level_class_filename_2))
                    os.remove(os.path.join(level_class, level_class_filename))
            os.remove(os.path.join(data_path, filename))