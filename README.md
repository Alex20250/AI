# DC To Edge 

### Datasets 
#### VMMR Dataset
The Vehicle Make and Model Recognition dataset (VMMRdb) is large in scale and diversity, containing 9,170 classes consisting of 291,752 images, covering models manufactured between 1950 and 2016. VMMRdb dataset contains images that were taken by different users, different imaging devices, and multiple view angles, ensuring a wide range of variations to account for various scenarios that could be encountered in a real-life scenario. The cars are not well aligned, and some images contain irrelevant background. The data covers vehicles from 712 areas covering all 412 sub-domains corresponding to US metro areas. Our dataset can be used as a baseline for training a robust model in several real-life scenarios for traffic surveillance.  
#### Download
A subset of the full VMMRdb dataset is now included with the repo

### Car Theft
Utilizing the dataset we're going to look at exploration classification of the top 10 most stolen cars according to the National Insurance Crime Bureau.  We gathered a basic list [here](https://www.forbes.com/sites/jimgorzelany/2018/09/18/hottest-wheels-the-most-stolen-new-and-used-cars-in-the-u-s/#720ecbc55258).

### Data Exploration
We will explore the distribution of classes within each brand and make. 

### Topology 
We currently have notebooks that test the classification of 10 classes using the InceptionV3, MobileNet and VGG16 Topologies.

### Software
We're utilizing Intel Optimized Tensorflow as a backend to Keras.  

Included is an environment.yml file.  This can help create the correct environment by issuing the following command on a system that has Anaconda installed.

```
conda env create -f environment.yml
python -m ipykernel install --user --name tf_training --display-name "tf_training"
```
### Citation for using the datasets
```
A Large and Diverse Dataset for Improved Vehicle Make and Model Recognition
F. Tafazzoli, K. Nishiyama and H. Frigui
In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops 2017. 
```
