# MD_Global_Terrorism
University project. Data mining.

- Final Report Draft.odt:
File containing our final written report.

- Preprocessing:
Contains the scripts related to the preprocessing of our dataset.
  - BIUDS_raw_data.Rmd: markdown file with the basic statistical analysis and study of our dataset before preprocessing
  - BUDS_preprocessed_data.Rmd: markdown file with the basic statistical analysis and study of our dataset after preprocessing
  - Preprocessing.Rmd: markdown file with the explanation alongside the code of each step we've gone through during preprocessing

- bivariate_analysis:
  - SDA_Bivariate.Rmd: markdown file with the bivariate statistical analysis and study of our dataset after preprocessing

- PCA:
Contains the scripts related to the Principal Component Analysis of the project.
  - PCA.R
  - PCA.Rmd

- clusters:
  - clusters_script.Rmd: markdown file with the clustering and its analysis of our dataset
  
- profiling:
  - ??

- datasets:
Contains the different versions of the dataset we've been using.
  - .Rhistory
  - fips-codes-added.csv
  - fips_codes_state.csv
  - longitudeFixed.csv

- map:
Contains the python scripts used to generate the maps, and the maps themselves.
  - html_files: directory with the maps
      + map_points.html: map with all the incidents in our dataset, filterable by the ruling party
      + map_provs.html: map with all the incidents classified by the FIPS codes
      + map_states.html: map with all incidents classified by states
      + map_time.html: map with all the incidents classified by the month the took place in
  - insert_fips.py: script used to add the fips codes of each incident from another file to our dataset
  - map_points.py: script used to create map_points.html
  - map_states.py: script used to create map_states.html
  - map_time.py: script used to create map_time.html
  - maps_provs.py: script used to create maps_provs.html
