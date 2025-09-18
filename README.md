# football_transfermarkt

The dataset is taken from Kaggle ([link here](https://www.kaggle.com/datasets/davidcariboo/player-scores/data)).

There are many files available. I have loaded *transfers.csv* and *clubs.csv* so far. For more information about data see the README in the data folder.

The main file is *eda.py*, which contains the flow of an explorative data analysis of the dataset *transfers.csv*. Auxiliary functions and packages import are in *utils.py*. In *test_utils.py* there are simple tests for functions of *utils.py*. 

The *results* folder contains written results, progressively obtained during the analysis. More specifically, the main summaries of the analysis are written in a file called *other/EDA.txt*, while plots are automatically saved in the *figures* subfolder.

There is also the file *ask_llama.py*, which contains a query addressed to Llama, aiming to get some analysis suggestions we could perform on our dataset. The result of the query is in the file *results/other/llama_suggestions.txt*.
