# Informal Response_1
## What is Machine Learning...

### According to Moroney, what is the difference between traditional programming and machine learning?

According to Moroney traditional programming is using specified rules and data to produce answers. The difference with machine learning is that the programmer gives the computer/machine lots of answers and data with the hope that the computer can figure out the rules on its own.


### With the first basic script that Maroney used to predict a value output from the model he estimated (he initially started with 10 that predicted ~31. Modify the predict function to produce the output for the value 7. Do this twice and provide both answers. Are they the same? Are they different? Why is this so?

For the value of 7 my two answers are 22.0024 and 22.002678. Stochastic means randomly determined; having a random probability distribution or pattern that may be analyzed statistically but may not be predicted precisely (Google). So whenever the machine is trained it learns a slightly different model because again decisions made during the learning process as it tries to figure out the rules of the data can vary randomly. It could also be because the dataset is extremely small.



### Using the script you produced to predict housing price, take the provided six houses from Mathews, Virginia and train a neural net model that estimates the relationship between them. Based on this model, which of the six homes present a good deal? Which one is the worst deal? Justify your answer.

According to my model the suggested prices for two, three, four, and five bedroom houses are $169441, $234615, $299789, and $364963 respectively.
All of the 3, 4, and 5 bedroom houses except the four bedroom house (church) provide good deals since according to the model they are underpriced. However the best deal is offered by the 3 bedroom house Hudgins with an approximate savings of $137615. The worst deal is the 4 bedroom house "church" retailing for $399,000 because according to the model it is overpriced by approximately $99,211.


| Number of Bedrooms     | Actual House Price  |	Predicted House Price |	Savings/(Overpayment) |
| -------------------    | --------------------| -----------------------| ----------------------|
|2_Bedroom(moon)	       |250000	             |169441	                |($80,559.00)           |
|<mark>3_Bedroom(hudgins) </mark>	     |<mark>97000 </mark>	               |<mark>234615 </mark>                  |<mark>	$137,615.00 </mark>           |
|3_Bedroom(newptcomfort) |229000               |	234615                |	$5,615.00             | 
|4_Bedroom(church)	     |399000               |	299789	              |($99,211.00)           |
|4_Bedroom(mobjack)      |	289000	           |299789	                |$10,789.00             |
|5_Bedroom(mathews)      |	347500             |	364963	              |$17,463.00             | 


