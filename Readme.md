### **CS-IS-3066-1: Applied Machine Learning in Football**

### Karnav Popat, Pranav Koka, Suyog Joshi

This repository represents the entire pipeline needed to setup our replication of STatsBomb's xG models, including our own calculated features, data exploration, and hypothesis testing.

Note that some of the datasets we've used are too large to upload, however, they can be created by running the first two notebooks.

To get started, create the main data we'll be using, augmented_data.csv:

1_data_creation: This notebook uses the statsbombpy API to grab all events for all seasons of StatsBomb's open data. Note that this is a large volume of data - about 5 GB, and running the notebook might therefore be difficult due to network speed and data transfer constraints on the API.

2_data_augmentation: This notebook uses the StatsBomb's open data to calculate our main dataset. We have added a lot of features in this notebook which we have later used in the baseline models. The output of this is stored in the ./data directory.

Once you've set up, you can proceed to explore the data and establish baseline results:

3_data_exploration: This notebook has some visualisations that we made along with an exploration of the dataset statistics and our line of thinking.

4_baseline_models: Based on the literature review that we did, we ran five models. We did no fine tuning, feature selection, or augmentation, and yielded the basic results.

Once we've established a baseline, we can use our calculated features and finetuning to obtain the best results we can:

5_hypotheses: Some hypothesis testing we did based on our earlier line of thinking.

6_augmented_models: This notebook contains our final results, as well as the techniques we applied and features we used to achieve them.

Finally, if you're interested in some of the work we did to get to our final results, check out:

7_feature_selection: Some of the feature selection methods we considered for data augmentation and used to test our model's out-of-distribution prediction.

8_leagues_testing: We tested the performance of the model on out of distribution data by training and testing on separate leagues and comparing the performance when training and testing within the same league. We also established our hypothesis that different leagues have different playstyles.
