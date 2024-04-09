# Urdu Poetry Generation 
## Project Description:
This project aims to generate Urdu poetry using N-Grams based on a scrapped poetry dataset. The dataset contains a collection of Urdu poems from various **Urdu Poets**, serving as the foundation for training and generating new poetic verses. 
The project will explore the use of the following different N-Gram models:
1. **Unigram**
2. **Bigram** 
3. **Trigram**
4. **Backward Bigram**
5. **Bi-directional Bigram**
## Data Collection:
The dataset has been scrapped from the following website : https://www.rekhta.org/ . All poems of atleast 25 Urdu Poets have been scrapped from this website.
**Scrappy** has been used to achieve the web-scrapping task . Following is the link for **Scrappy** : https://scrapy.org/
The scrapped data has been saved in the **scrapped poems.csv**.
A spider has been used for this purpose . It is avaliable in the **I212705urdupoemsspider.py** file.

## Scrapped_Poems.csv:
The csv file contains the following 3 columns :
1. **Poem Line :** This is the verse in a particular poem.
2. **Nazm Name :** This is the name of the poem.
3. **Author Name :** This is the name of the author of the poem.

## I212705urdupoemsspider.py:
This is the spider that has been used to scrap the poems . 
Following are the steps to use the spider:
1. Create virtual environment in Visual Studio Code.
2. Install scrappy.
3. Create a scrappy project inside the virtual environment.
4. Either Copy Paste my spider in your spider or add my spider into your project in the spiders directory.
5. run the spider.
6. data will automatically be stored in a new file called **scrapped_poems.csv** in the same directory.
7. The spider code is modifiable . You can change as per your requirement.
8. This code can also serve as a base to scrap other websites but Knowledge of scrappy is a must.
## Conclusion: 
Through this project, I aim to showcase the versatility and creativity of N-Gram models in generating Urdu poetry while preserving the aesthetic and linguistic richness of the language. 
