# Data
https://www.kaggle.com/datasets/thedevastator/berlin-airbnb-ratings-how-hosts-measure-up

The Berlin Airbnb Ratings dataframe is analyzed. 

The dataframe contains 450k comments about 23.5k apartments.

0. The original dataframe takes up 250 MB. Therefore, the dataframe is divided into two tables: Comments and Apartments, which take up 37 MB and 3.5 MB respectively.

1. The Polarity of comments was analyzed. Aggregated data on the Polarity of comments was added to the Apartments table.

2. Data Protocol, Descriptive Statistics was created for Apartments. Visualization of missing data, numerical and categorical, was made. Cross-correlations, skewness for numerical data, ANOVA and t-test of price differences by city districts were calculated.

3. Spatial Autocorrelation was calculated for the 'Price' and 'Location Rating' data. Moran's I index and its p-value were calculated.
A rough calculation on the plain requires N^2 operations. To reduce the complexity of calculations, the city is pre-divided into a grid.

4. Visualization of word frequencies in comments.

    Data on 'Price' is plotted on the city map - more and less expensive areas for accommodation are visible.

5. Data on 'Location Rating' is plotted on the city map - places that tourists rated as more and less comfortable are visible.

6. Missing values ​​in 'Post Code' are filled. The value is filled with the closest known value. Using a grid search speeds up the process.
Rejected offers for long-term accommodation over 14 days. Retained offers for accommodation in Apartment and Condominium and not Shared room.

    Outliers by 'Price' accepted offers with a price of less than 14 and more than 300 euros. Log transformation of the data was performed to calculate the boundaries.

    Feature Engineering included Log transformation for features with a distribution with heavy tails. A new feature was introduced - distance from the city center. One-Hot Encoding was made for the 'Neighborhood Group' feature. The more detailed 'neighbourhood' feature was not changed. Target Encoding will be used for it.
