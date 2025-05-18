# This repo is to extract data from sam.gov programatically.

## Steps to extract information manually for fieldpay
1) Go to https://sam.gov/search/?index=opp
2) Switch to 'Any words' 
3) Apply these filters:

| Filter                                | What to choose                                                                                                                                  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Notice Type**                       | **Award Notice** (this is code **a** in the URL)                                                                                                |
| **Date Range**                        | “Last 30 days” or custom window                                                                                                                 |
| **NAICS / Keywords**                  | Type **236220** (commercial GC), **237310** (highway/road), **238210** (electrical), etc.  Press **Enter** after each code so it becomes a tag. |
| *(Optional)* **Place of Performance** | Your state or a specific county to keep it local                                                                                                |


## To run
1) source venv/bin/activate
2) pip3 install requests
3) python3 awards_to_csv.py
