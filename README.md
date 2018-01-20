# Demographics_data

## Steps

1. Download [Alabama through Missouri](https://www2.census.gov/programs-surveys/popest/datasets/2010/modified-race-data-2010/stco-mr2010_al_mo.csv) and [Montana through Wyoming](https://www2.census.gov/programs-surveys/popest/datasets/2010/modified-race-data-2010/stco-mr2010-1.csv)
2. Run parse_csvs.py
3. If Districts is empty, run download_files.py - Delete the error section in Districts/Kentucky.txt if you do
4. Run parse_district_txt.py
5. Run flip_counties.json
6. Run determine_party.py
7. party_counts.py is what is desired