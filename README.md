Requirements:
- python 3.6
- lda
- pyvi
- demoji
(Demoji need to download a package to be able to perform. See the detail here https://pypi.org/project/demoji)
- scikit-learn
- seaborn
- pickle
- pandas
____________________________________________

### CRAWLING DATA

To crawl the data, run the bash files (test.sh to test4.sh).
You can change the parameters in those files to customize the crawling session.

Data will be crawled from the fanpage links in "link_fb" files.

____________________________________________

### PRE-PROCESSING

After crawling raw data, we need to pre-process it before process it with LDA.
Run the "pre-processing.py" to perform this stage.
Remember to change the file directions in the file to get the right dataset and stopwords file.

Run the "Pre_processing_IDF.ipynb" notebook to finish preprocessing

There are 4 output files of this stage:
- corpus.txt
- rating.txt
- source.txt
- done_processing.txt 

You can put them into the datasets folder to categorize them for each dataset.
____________________________________________

### LDA STAGE

Run the "lda_simple.py" to process the data.
Remember to change the file direction to get the right dataset folders. 
The LDA model will be saved in the "model" folder inside each dataset folder.


____________________________________________

### VISUALZIE 

Run the "Visualize.ipynb" notebook to visualize the results
