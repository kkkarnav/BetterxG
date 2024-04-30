### **Literature Review - Expected Goals 1968-2024**<a id="literature-review---expected-goals-1968-2024"></a>

Karnav Popat, Pranav Koka, Suyog Joshi

\



### **History (Before 2012)**<a id="history-before-2012"></a>

Data analytics in football is a field almost as old as the sport itself. The first football analysts are considered to be [Charles Reep and Bernard Benjamin](https://thesefootballtimes.co/2020/04/08/the-roots-of-expected-goals-xg-and-its-journey-from-nerd-nonsense-to-the-mainstream/) all the way back in the 1960s, who watched hundreds of matches to manually analyze which types of shots and positions most often resulted in goals. Their collaborator, Charles Hughes, created the first football metric: **Position of Maximum Opportunity**. This simplistic metric measured the likelihood of a goal purely from the position on the pitch that the shot was taken from.<a id="data-analytics-in-football-is-a-field-almost-as-old-as-the-sport-itself-the-first-football-analysts-are-considered-to-be-charles-reep-and-bernard-benjamin-all-the-way-back-in-the-1960s-who-watched-hundreds-of-matches-to-manually-analyze-which-types-of-shots-and-positions-most-often-resulted-in-goals-their-collaborator-charles-hughes-created-the-first-football-metric-position-of-maximum-opportunity-this-simplistic-metric-measured-the-likelihood-of-a-goal-purely-from-the-position-on-the-pitch-that-the-shot-was-taken-from"></a>

As the Premier League globalized football and scouts and analysts started playing a greater role in team strategy, football analytics grew much more sophisticated, though still informal. The first use of the phrase “expected goals”, though not in modern context, was in Vic Barnett and Sarah Hilditch’s 1993 paper “[The Effect of an Artificial Pitch Surface on Home Team Performance in Football (Soccer)](https://www.jstor.org/stable/2982859?origin=crossref\&seq=5)”, which performed a regression analysis of the impact of artificial pitches on goals. Meanwhile, scouts had begun identifying lists of factors that influence the likelihood of a goal, including angle, pressure, and form.

\



### **Analyses before xG**<a id="analyses-before-xg"></a>

**2003** [**Analysis of Sports Data by Using Bivariate Poisson Models**](https://www.jstor.org/stable/4128211) **- Karlis, Ntzoufras**<a id="2003-analysis-of-sports-data-by-using-bivariate-poisson-models---karlis-ntzoufras"></a>

Proposes the use of bivariate Poisson models and their extensions to account for the correlation between the scores of two competing teams, such as in football and water polo. They discuss the limitations of Poisson distributions and demonstrate how bivariate Poisson models can improve predictions and model fit, especially for the number of draws in football games.


**2004** [**Possession as a performance indicator in soccer**](https://www.researchgate.net/publication/233491176_Possession_as_a_Performance_Indicator_in_Soccer) **- Jones et al.**<a id="2004-possession-as-a-performance-indicator-in-soccer---jones-et-al"></a>

This paper investigates the relationship between ball possession and team success in English PL football, analyzing 24 matches from the 2001-02 season. It found that successful teams have longer possessions than unsuccessful teams, regardless of match status, and that both types of teams increase possession duration when losing. The paper suggests that possession is linked to success due to individual player skill rather than team strategy.


**2010** [**Soccer: is Scoring Goals a Predictable Poissonian Process?**](https://arxiv.org/pdf/1002.0797.pdf) **- Heuer et al.**<a id="2010-soccer-is-scoring-goals-a-predictable-poissonian-process---heuer-et-al"></a>

Investigates the predictability of soccer match outcomes using a team fitness model, with fitness being defined as the average goal difference per match. It challenges the belief that scoring goals is influenced by self-affirmative effects, instead proposing that goals can be modeled as independent Poissonian processes with predetermined expectation values. The study utilizes data from the German Bundesliga to quantify the limits of predictability in soccer matches and suggests that the outcome is largely determined by team fitness variations and random effects, rather than systematic or match-specific factors.

\



### **Adding Nuances to xG (2012-2019)**<a id="adding-nuances-to-xg-2012-2019"></a>

Expected Goals as a formal metric for football performance came into existence in 2012, during a time of increased interest in statistical measurement of football due to the proliferation of blog posts as a [popular forum for sports analysts](https://thepowerofgoals.blogspot.com/2012/05/scoring-efficiency-and-current-score.html). Sam Green, an analyst at OptaPro, [first described the xG metric in April 2012](https://www.statsperform.com/resource/assessing-the-performance-of-premier-league-goalscorers/), which revolutionized the football analytics industry. Since then, xG has developed in two ways: **adding nuances to the calculation of the xG metric, and adding new metrics such as xT and xGChain which model parts of the game other than goals.**

A large part of the developments in xG from 2012 to 2019 focused on refining the expected goals model to better predict shot outcomes. These added nuances involved selection of features and statistical distribution, modeling factors which were previously invisible in the data, and adding complexities to the representation of ball and pitch to better represent the game. 


**2013** [**Beating the bookie: A look at statistical models for prediction of football matches.**](https://folk.idi.ntnu.no/helgel/papers/LangsethSCAI14.pdf) **- Langseth**<a id="2013-beating-the-bookie-a-look-at-statistical-models-for-prediction-of-football-matches---langseth"></a>

This paper investigates some classical methods of predicting the outcome of football matches by evaluating them against various moneymaking (betting) techniques. The study finds that models which incorporate more of the available information describing the games perform better than those with fewer data points. They do not use event data at the level current xG models use, instead opting for shots on target and total shots.


**2014**[ **A Bayesian network model for forecasting Association Football match outcomes**](https://www.researchgate.net/publication/236944355_pi-football_A_Bayesian_network_model_for_forecasting_Association_Football_match_outcomes_Knowledge-Based_Systems_36_322-339/link/5aed93480f7e9b01d3e1793e/download?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIn19) **- Constantinou et al.**<a id="2014-a-bayesian-network-model-for-forecasting-association-football-match-outcomes---constantinou-et-al"></a>

Proposes a Bayesian network model to predict match outcomes. The dataset is Premier League match outcomes, with the names of teams replaced with a ranked number representing the strength of that team for a particular season. Along with this, the study uses form, fatigue, and psychology as additional features. The model is able to match a bookmaker in predicting the outcome of a game, and is able to choose bets that make more money than the bookmaker.


**2015** [**“Quality vs Quantity”: Improved Shot Prediction in Soccer using Strategic Features from Spatiotemporal Data**](https://espace.library.uq.edu.au/view/UQ:b1c69d7) **- Lucey et al**<a id="2015-quality-vs-quantity-improved-shot-prediction-in-soccer-using-strategic-features-from-spatiotemporal-data---lucey-et-al"></a>

Utilizes player and ball tracking data to analyze approximately 10,000 shots to identify features that influence scoring chances. These features include game phase, defender proximity, player interactions, speed of play, and shot location. It also explores team efficiency ratings and individual game analysis, offering insights into the effectiveness of various strategies in different types of match contexts.


**2016** [**Master’s Thesis (“Expected Goals in Soccer: Explaining Match Results using Predictive Analytics)**](https://pure.tue.nl/ws/portalfiles/portal/46945853/855660-1.pdf) **- Eggels**<a id="2016-masters-thesis-expected-goals-in-soccer-explaining-match-results-using-predictive-analytics---eggels"></a>

Presents a method for determining the expected winner of a football match by analyzing goal scoring opportunities. It introduces a predictive analytics approach that assigns quality scores to individual shots. Spatiotemporal and player quality (from FIFA) data is used to train various classification models. These quality scores represent the probability of the shot resulting in a goal. These scores are aggregated to predict match outcomes, with a 50% success rate in predicting the winner of a match.


**2021** [**A Goal Scoring Probability Model for Shots Based on Synchronized Positional and Event Data in Football**](https://www.frontiersin.org/articles/10.3389/fspor.2021.624475/full#T2) **- Anzer and Bauer**<a id="2021-a-goal-scoring-probability-model-for-shots-based-on-synchronized-positional-and-event-data-in-football---anzer-and-bauer"></a>

This paper proposes the use of both positional and event data for xG prediction. Event data does not paint a full picture of the match situation, so positional data is added to the feature set in order to improve  New features are calculated using data which comprises the location of all 11 players and the ball, updated at 25Hz. This data is synchronized with event data (when the shot was taken) to calculate xG using a gradient-boosted tree. The new features include the speed of the player taking the shot, pressure on the shooter, goalkeeper position, and the number of defenders in line of the shot. 


**2023** [**Bayes-xG: Player and Position Correction on Expected Goals (xG) using Bayesian Hierarchical Approach**](https://arxiv.org/pdf/2311.13707.pdf) **- Scholtes and Karakus**<a id="2023-bayes-xg-player-and-position-correction-on-expected-goals-xg-using-bayesian-hierarchical-approach---scholtes-and-karakus"></a>

This study uses Bayesian hierarchical logistic regression to investigate the influence of player and positional factors on xG. The findings reveal positional effects in a basic model that includes only distance to goal and shot angle as predictors, highlighting that strikers and attacking midfielders exhibit a higher likelihood of scoring. However, these effects diminish when more informative predictors are introduced. Notably, even with additional predictors, player-level effects persist, indicating that certain players possess notable positive or negative xG adjustments.


**2023** [**A machine learning approach for player and position adjusted expected goals in football (soccer)**](https://www.sciencedirect.com/science/article/pii/S2773186323000282?ref=pdf_download\&fr=RR-2\&rr=85bfdd79bd339633) **- Hewitt and Karakus**<a id="2023-a-machine-learning-approach-for-player-and-position-adjusted-expected-goals-in-football-soccer---hewitt-and-karakus"></a>

### Uses a logistic regression approach to calculate Position-adjusted xG and Player-adjusted xG for prediction and forecasting purposes at the individual action level. Studies the impact of the shot-taker on the shot, a data point which is usually ignored in xG calculations for generalization purposes.<a id="uses-a-logistic-regression-approach-to-calculate-position-adjusted-xg-and-player-adjusted-xg-for-prediction-and-forecasting-purposes-at-the-individual-action-level-studies-the-impact-of-the-shot-taker-on-the-shot-a-data-point-which-is-usually-ignored-in-xg-calculations-for-generalization-purposes"></a>

\



### **Adding New Metrics (2019-2024)**<a id="adding-new-metrics-2019-2024"></a>

Post 2019, much of the focus of the industry has been on developing metrics similar to xG which can model actions other than shots. The larger goal is to develop a statistical model for the intuitive understanding of [“who is dominating”](https://www.americansocceranalysis.com/home/2018/8/28/expected-possession-goals-part-1) that fans can grasp. These metrics primarily try to measure passing and possession values. 

Three key developments have primarily affected innovation in football analytics since 2019. The first is the increasing commercialization of football data, and the resulting switch to closed-source research by industry giants such as OptaPro and StatsBomb. Post-2014, with the establishment of analytics departments in many Premier League football clubs, many of the sources of information on football statistics via blog posts and research papers have ried up. Today there is a dearth of information on the advancement of core xG and xT since a lot of this knowledge is considered proprietary by analytics firms. 

The other developments in analytics relate to the increasing sophistication of modeling. One of them has been the introduction of [measuring spatial influence “projection”](https://trainingground.guru/articles/william-spearman-how-liverpool-create-pitch-control) of players using objects such as Gaussian surfaces. Gradient boosted trees have become the dominant way of modeling football statistics, because of the effectiveness of decision trees and the additional value of using spatial gradient representations of players. StatsBomb and related companies have developed [metrics such as “Packing”](https://statsbomb.com/articles/soccer/unpacking-ball-progression/) (number of players bypassed by a pass) and[ “pitch control”](https://soccermatics.readthedocs.io/en/latest/lesson6/PitchControl.html) which effectively model the influence of each player on a play or shot. This has led to an additional focus on modeling “tactics” and team setups to identify the different types of possession processes and their influence on shot and goal types.

The final development has been the resurgence of interest in time-sequential analysis. These primarily involve analyzing the possession values and passes leading up to a goal (xGChain and xPG) and [pitch control over time](https://trainingground.guru/articles/william-spearman-how-liverpool-create-pitch-control). This has also led to an emerging field of analyzing changes in team metrics over a season or a range of matches to account for changes in tactics and external factors, which is the area we want to work on.

\



### **Different Metrics**<a id="different-metrics"></a>

**2019** [**Introducing Expected Threat (xT)**](https://karun.in/blog/expected-threat.html) **- Karun Singh**<a id="2019-introducing-expected-threat-xt---karun-singh"></a>

Introduces a framework for quantifying individual contributions to a team’s offensive play, using a new metric called Expected Threat. xT operates on event data and rewards player actions that contribute to creating scoring opportunities, regardless of the final outcome of the possession.


**2019** [**Actions Speak Louder than Goals: Valuing Player Actions in Soccer**](https://arxiv.org/pdf/1802.07127.pdf) **- Decroos et al. (VAEP)**<a id="2019-actions-speak-louder-than-goals-valuing-player-actions-in-soccer---decroos-et-al-vaep"></a>

This paper introduces a model to value _all_ player actions, including passes and shots. It uses direct event data as well as features calculated from the data to train probabilistic models including CatBoost, logistic regression, and random forest. They find that their feature set shows improved prediction performance compared to datasets including only locations, actions, or locations + actions.


**2019** [**Interpretable Prediction of Goals in Soccer**](https://tomdecroos.github.io/reports/interpret_vaep.pdf) **- Decroos, Davis**<a id="2019-interpretable-prediction-of-goals-in-soccer---decroos-davis"></a>

Argues that current xG models sacrifice interpretability for performance, meaning the models often yield no insight into why a given game state has a higher or lower probability of resulting in a goal. To combat this, the study replaces the the complicated non-interpretable gradient boosting tree model using 151 features from the original VAEP paper (Decroos et al. 2019) with a Generalized Additive Model (GAM) using only 10 features. The GAM can get close to the performance of XGBoost while remaining interpretable. Given how crucial the interpretability of models can be in soccer analytics, GAMs may be a better choice than XGBoost to build predictive models with, even if their performance is slightly worse.


**2022** [**“Estimated Player Impact” (EPI): Quantifying the effects of individual players on football (soccer) actions using hierarchical statistical models**](https://statsbomb.com/wp-content/uploads/2022/09/Tahmeed-Tureen-and-Sigrid-Olthof-%E2%80%93-Estimated-Player-Impact-EPI-Quantifying-The-Effects-Of-Individual-Players-On-Football-Actions-Using-Hierarchical-Statistical-Models.pdf) **- Tureen and Olthoff**<a id="2022-estimated-player-impact-epi-quantifying-the-effects-of-individual-players-on-football-soccer-actions-using-hierarchical-statistical-models---tureen-and-olthoff"></a>

This paper studies the development of a model to quantify individual players’ effects on football actions using hierarchical statistical models. It incorporates player-specific effects, leading to more personalized xG values. Generalized Linear Mixed Models are utilized to account for the hierarchical nature of football data. It shows that certain players can have either a positive or a negative effect on xG for a shot taken from the same location.

**2022** [**xG Chain: the most important thing is to participate**](https://www.driblab.com/analysis-player/xg-chain/) **- DribLab**

This introduces the xGChain metric, which measures a player’s involvement in xG generated by propagating any xG generated by a shot down the chain of passes. Every player involved in the play that led to a shot is attributed the xG of the shot. This aims to answer the question “which players most often generate opportunities via their actions on the pitch?”

**2023** [**Expected Pass (xPass) and Pass Clustering**](https://statsbomb.com/articles/soccer/statsbomb-release-new-models-expected-pass-xp-and-pass-clustering/) **- StatsBomb**

This introduces the xPass metric, which is very similar to xG but instead of measuring the likelihood of a goal being scored, it measures the likelihood of a shot being completed. It also introduces the technique of pass clustering which takes all passes completed in a series and uses a clustering algorithm to categorize them by their characteristics.

\



### **Spatial Projection Papers**<a id="spatial-projection-papers"></a>

**2017** [**Visual analysis of pressure in football**](https://link.springer.com/article/10.1007/s10618-017-0513-2) **- Andrienko et al.**

Introduces a technique to measure how a player’s positioning and movement exerts defensive pressure on the other team. It does so by analyzing a series of spatio-temporal attributes of the defensive team and measuring their impact on the xG vs G statistics of the offensive team.

**2021** [**A framework for the fine-grained evaluation of the instantaneous expected value of soccer possessions**](https://www.researchgate.net/publication/351834743_A_framework_for_the_fine-grained_evaluation_of_the_instantaneous_expected_value_of_soccer_possessions) **- Fernandez et al**

Develops a metric called “Expected Possession Value” which analyzes the likelihood of a goal resulting from any particular possession situation of a team. It accomplishes this by representing game states as probability surfaces based on the position of players in a given range of time.

**2023:** [**Beyond the Surface: Deep Learning Framework for Measuring Football’s Expected Possession Value**](https://medium.com/@marin11amf11/beyond-the-surface-deep-learning-framework-for-measuring-footballs-expected-possession-value-7c087f979502) **- Alex Marin Felices**

Blog post talking about the methodology behind the Expected Possession Value framework, and how it measured instantaneous value based on analysis of possession sequences.

\


### **Sequential Analysis Papers**

**2013** [**A Framework for Tactical Analysis and Individual Offensive Production Assessment in Soccer Using Markov Chains** ](https://nessis.org/nessis11/rudd.pdf)**- Sarah Rudd**

This is foundational research from the pre-xG era that applied Markov Chain to measure game states of a possession sequence and analyze players’ offensive output based on these goal-sequences. This is some of the earliest research that looks at goals as the termination of time-sequences.

**2022** [**Pitch control metrics to improve the predictions of moments leading to goals in football**](https://staff.fnwi.uva.nl/a.visser/education/masterProjects/Thesis_Ramon_Dop_MsDS.pdf)**- Ramon Dop**

Creates a physics-based pitch control model to analyze off-ball actions. It evaluates the likelihood of a team continuing to be in possession of a ball at a certain point on the pitch at a certain point of the passing sequence. This allows for the off-ball actions of offensive and defensive players to be factored into xG calculations.


**2023** [**Expected goals in football: Improving model performance and demonstrating value**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10075453/) **- Mead et al.**<a id="2023-expected-goals-in-football-improving-model-performance-and-demonstrating-value---mead-et-al"></a>

This study advances the xG model by incorporating novel features such as player and team abilities, as well as psychological factors, which were previously untested in this context. These new features include the team’s current and previous season league position, match attendance, PlayeRank (a score rating the player’s ability), match importance, team form, Elo rating, and player transfer value. These additional features significantly enhance the predictive ability of xG.

**2023** [**Measuring the pitch control of professional football players using spatiotemporal tracking data**](https://iopscience.iop.org/article/10.1088/2632-072X/acb67d) **- Higgins et al.**

Correlates variation of pitch control statistics over a season to variation in expected goals metrics. Similarly it quantifies home advantage to find its impact on expected goals across a season.
