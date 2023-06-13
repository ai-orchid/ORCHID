<div align="center">
 
## Oral Cancer Histology Image Dataset (ORCHID)

<!-- [![Demo](http://img.shields.io/badge/Demo-9acbff.svg)]() -->
<!-- [![Conference](http://img.shields.io/badge/CVPR-2022-4b44ce.svg)](#) -->
[![Project](http://img.shields.io/badge/Project%20Page-3d3d8f.svg)]()
[![Paper](https://img.shields.io/badge/paper-link%20to%20paper-green.svg)](#)

</div>

This repository is associated with the Oral Cancer Histology Image Datasat (ORCHID) and contains all the code files associated with the technical validation of the dataset. 
## Running the code
First, you must create a conda environment for the project, and install the dependencies. This can be done by running the following commands:
```
conda create -name orchid python=3.9
conda activate orchid
pip install -r requirements-ORCHID.txt
```

This process will ensure that you have all requirements adequately setup before you run the code. After this, the next step would be to place to zip-folder with all the data in the main repository directory. After you do so, the folder should look like this:
```
/ORCHID/ORCHID_data.tar.gz
```
The data, as mentioned previously, consists of nested folders, with compression applied to each folder. In order to retreive the data to its original form, you must run the following script:
```
./data_retrieve.sh
```

Following this, your data is ready to be used. In order to use the data, you need to get all the patches into a single folder, and create two datafram (CSV) files with the following mapping. The first datafram (CSV) file is for differentiating between Normal, OSCC, and OSMF. And the second datafram (CSV) is for differentiating between WDOSCC, MDOSCC, and PDOSCC. Both dataframes will contain filenames with their respective labels.

In order to do so, you can use the following script:
```
python3 ./tools/data_preprocess.py
```

After this process is complete, it is time to train the model. In order to run the model that classifies Normal, OSMF, or OSCC, you can run the following command:
```
python3 ./training/train-classify-normal-oscc-osmf.py
```
And in order to run the model that classifies WDOSCC, MDOSCC, or PDOSCC, you can run the following command:
```
python3 ./training/train-classify-wdoscc-mdoscc-pdoscc.py
```

Note: This code has been adapted for public release from the original codebase. As such, the code is error free and runs directly if the above instructions are followed. However, there may be some unforseen errors due to various reasons. If you encounter any such errors, please feel free to raise an issue on the repository, and we will try to address it as soon as possible. If you have a resolution to any issue please feel free to raise a pull request.
