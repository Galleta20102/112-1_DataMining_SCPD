# 112-1_DataMining_SCPD

## Experiment Enviroment
To start, we prefer creating the environment using **conda** :

```
conda create --name SCPD python=3.8
conda activate SCPD
```
Then you need to install some necessary packages. <br>
Execute the following command to install the package using **conda**:
```
conda install numpy==1.22
conda install scipy
conda install matplotlib
conda install networkx
conda install sparse
conda install scikit-learn
```
After you have performed all experiments, don't forget to close the virtual environment using :
```
deactivate
```

## Getting the dataset
Dataset Links used by the author in the SCPD paper:
* MAG History dataset : [history_scpd](https://object-arbutus.cloud.computecanada.ca/tgb/history_scpd.zip)
* COVID flight dataset: [fight_scpd](https://object-arbutus.cloud.computecanada.ca/tgb/flight_scpd.zip)
* Stablecoin dataset: [stablecoin_scpd](https://object-arbutus.cloud.computecanada.ca/tgb/stablecoin_scpd.zip)

The additional data set we applied is the flight records of the United States from Kaggle :
* Kaggle Dataset: [USA Airport Dataset](https://www.kaggle.com/datasets/flashgordon/usa-airport-dataset)

## 如何運行程式碼