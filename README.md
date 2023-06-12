# ORCHID

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

Following this, your data is ready to be used. In order to use the data, you need to get all the patches into a single folder, and create two json files with the following mapping. The first json file is for differentiating between Normal, OSCC, and OSMF. And the second json is for differentiating between WDOSCC, MDOSCC, and PDOSCC:
```
{
    "image_name": "label"
}
```
In order to do so, you can use the following script:
```
python3 ./tools/data_preprocess.py
```

After this process is complete, it is time to train the model. In order to run the model that classifies Normal, OSMF, or OSCC, you can run the following command:
```
python3 ./training/train-classify-normal-oscc-osmf.py
```
