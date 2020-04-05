# Indonesia Food Price Forecasting


As project for Bangkit Google first machine learning assignment, trainee were asked to create ML project by using TensorFlow.<br/><br/>

This group task consisted of:<br/>
- Yola Kamalita;
- Rike Adelia; and
- Indah Tika Lestari.<br/><br/>

The problem chosen is to predict chili prices in Indonesia, with dataset from [Global Food Prices Database (WFP) provided by HDX](https://data.humdata.org/dataset/wfp-food-prices/resource/12d7c8e3-eff9-4db0-93b7-726825c4fe9a). Hereby is the first look of the dataset:<br/>
(image1)

Description for each column names[1]:<br/>
- adm0_id: country id
- adm0_name: country name
- adm1_id: locality id
- adm1_name: locality name
- mkt_id: market id
- mkt_name: market name
- cm_id: commodity purchase id
- cm_name: commodity purchased
- cur_id: currency id
- cur_name: name of currency
- pt_id: market type id
- pt_name: market type (Retail/Wholesale/Producer/Farm Gate)
- um_id: measurement id
- um_name: unit of goods measurement
- mp_month: month recorded
- mp_year: year recorded
- mp_price: price paid
- mp_commoditysource: Source supplying price information

There are 99 unique country names, with **Indonesia** is one of them; thus we chose to slice the dataset to get more focused view.<br/>
(image2)<br/>

The sectors available in the data are:<br/>
(image3)<br/>

In this forecasting, we tried to predict Chili sectors; **Chili Red** and **Chili Bird's Eye**. Each of us developed the model by following [TensorFlow Tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series#part_2_forecast_a_multivariate_time_series).<br/>
We did univariate analysis with **mp_month** (or month frame) and **mp_price** as features. We were trying to train the model using only red chili data and test it to bird's eye chili data. Because based on the data, both of them have high correlation.<br/><br/>

**Enjoy this project!**<br/>
Feedback is welcomed. :)

[1] [Kaggle Dataset-Global Food Prices](https://www.kaggle.com/jboysen/global-food-prices)
