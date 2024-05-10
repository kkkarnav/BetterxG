### **CS-IS-3066-1: Applied Machine Learning in Football**

### Karnav Popat, Pranav Koka, Suyog Joshi

1_data_creation: This notebook uses the statsbombpy API to grab all events for all seasons of StatsBomb's open data. Note that this is a large volume of data - about 
5 GB, and running the notebook might therefore be difficult due to network speed and data transfer constraints on the API. It is advisable to use the downloaded csv
files available in the /data directory instead.

2_data_augmentation: This notebook uses the StatsBomb's open data. Note that this is a large volume of data - about 5 GB, and running the notebook might therefore be
difficult due to network speed and data transfer constraints on the API. It is advisable to use the downloaded csv files available in the /data directory instead. We 
have added a lot of features in this notebook which we have later used in the baseline models.

3_data_exploration: This notebook has some visualisations that we made along with an exploration of the dataset statistics and our line of thinking.

4_baseline_models: Based on the literature review that we did, we ran five models. We did no fine tuning, feature selection, or augmentation and because of this our
results are much worse than statsbomb's. 

5_hypotheses: Some hypothesis testing we did based on our earlier line of thinking.

6_augmented_models: We did the fine tuning, feature selection, and augmentation and our results are now equal to statsbomb's.

6_feature_selection: Some of the feature selection methods we used for data augmentation.

7_gam_models: Generalized additive model that we implemented to see if we could add interpretability. 

7_leagues_testing: We tested the performance of the model on out of distribution data by training and testing on separate leagues and comparing the performance when
training and testing within the same league.
