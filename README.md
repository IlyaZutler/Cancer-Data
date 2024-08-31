# Berlin Airbnb Ratings
https://www.kaggle.com/datasets/thedevastator/berlin-airbnb-ratings-how-hosts-measure-up
 
0. The dataframe contains 450k comments about 23.5k apartments and takes up 250 MB. Therefore, the dataframe is divided into two tables: Comments and Apartments, which take up 37 MB and 3.5 MB respectively.

1. The Polarity of comments was analyzed. Aggregated data on the Polarity of comments was added to the Apartments table. The quality of processing of comments, unfortunately, is very disappointing.

2. Data Protocol, Descriptive Statistics was created for Apartments. Visualization of missing data, numerical and categorical, was made. Cross-correlations, skewness for numerical data, ANOVA and t-test of price differences by city districts were calculated.

3. Spatial Autocorrelation was calculated for the 'Price' and 'Location Rating' data. Moran's I index and its p-value were calculated.
A rough calculation on the plain requires N^2 operations. To reduce the complexity of calculations, the city is pre-divided into a grid.

4. Visualization of word frequencies in comments. Data on 'Price' is plotted on the city map - more and less expensive areas for accommodation are visible.

5. Data on 'Location Rating' is plotted on the city map - places that tourists rated as more and less comfortable are visible.

6. Missing values ​​in 'Post Code' are filled. The value is filled with the closest known value. Using a grid search speeds up the process.
Rejected offers for long-term accommodation over 14 days and accommodation in Shared room.

    Outliers by 'Price' accepted offers with a price of less than 14 and more than 300 euros. Log transformation of the data was performed to calculate the boundaries.

    Feature Engineering included Log transformation for features with a distribution with heavy tails. A new feature was introduced - distance from the city center.
   
7. Were tested the following regression models in basic settings: Lasso, Random Forest, CatBoost, LightGBM, XGBoost for two types of encoding: One-Hot Encoding and Target Encoding (in fact, CatBoost and LightGBM do not require preprocessing of categorical features - they do Target Encoding themselves).
CatBoost has shown that it is the best out-of-the-box solution, shows good results without manual settings.

For each model and encoding method, feature importances were ranked (for One-Hot sums of the importances of derived features). And belt the correlation matrix of feature importance ranks. It is clear that Lasso ranks features differently from other models that give good results. In this case, Lasso is poorly suited for feature selection. Lasso is a linear regression model and gives poor results in the case of nonlinear dependencies.
   
9. Fine Tuning with Cross-Validation were made for CatBoost and XGBoost.
    Features were divided into three groups: location-related, apartment-related, and hospitality-related. Our models assigned importance to the features in these groups in completely different ways.



   
