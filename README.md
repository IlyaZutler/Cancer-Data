# Data
https://www.kaggle.com/datasets/thedevastator/berlin-airbnb-ratings-how-hosts-measure-up

The Berlin Airbnb Ratings dataframe is analyzed. 

The dataframe contains 450k comments about 23.5k apartments.

0. The original dataframe takes up 250 MB. Therefore, the dataframe is divided into two tables: Comments and Apartments, which take up 37 MB and 3.5 MB, respectively.

1. The Polarity of comments was analyzed. Aggregated data on the Polarity of comments was added to the Apartments table.

2. Data Protocol, Descriptive Statistics was created for Apartments. Visualization of missing data, numerical and categorical, was made. Cross-correlations, skewness for numerical data, and a t-test for price differences by city districts were calculated.

3. Spatial Autocorrelation was calculated for Price and Location Rating data. Moran's I index and its p-value were calculated.
       A rough calculation on the plain requires N^2 operations. To reduce the complexity of calculations, the city is pre-divided into a grid.

3. Visualization of word frequencies in comments. Price data is plotted on the city map - more and less expensive areas for accommodation are visible.
4. Location Rating data is plotted on the city map - places that tourists rate as more and less comfortable are visible.

5. Missing values ​​in Post Code are filled. The value is filled with the closest known value. Using grid search speeds up the process.

Long-term accommodation offers for more than 14 days are rejected. Offers for accommodation in Apartment and Condominium and not Shared room are left.

Outliers by Price accepted offers with accommodation prices less than 14 and more than 300 euros. Log data transformation was performed to calculate the boundaries.
