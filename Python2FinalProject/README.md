# Github Jobs API Analysis
---
This final project used the api on [this website](https://jobs.github.com/api). Specifications I used for the URL were , as well as the .json feature. 
## Requirements
* URL Specifics: 
	* 'description=python' 
	* 'full_time=true'
	* Use .json


## Python File
* [Python2_FinalProject.py](https://github.com/eric-wisniewski/cit129_ccac/blob/master/Python2FinalProject/Python2_FinalProject.py)

## My Analysis

With information given from [Python2_FinalProject.py](https://github.com/eric-wisniewski/cit129_ccac/blob/master/Python2FinalProject/Python2_FinalProject.py), it wil find:
* The total number of jobs with the paramters in the search bar. With most of my searches, I found the average number to be 550 jobs.
* The difference, in percentages, of the jobs that are full time and part time. On most calls from the URL, 95% are full time and 5% are part time. Recently, the jobs have been split 50/50 between full and part time.
* The total count of 3 words in all titles. The words I selected were 'Engineer', 'Developer', and 'Senior'. In my most recent search, as of May 13 2020, 'Engineer' appears in 264 titles, 'Developer' shows up in 165 titles, and 'Senior' is in 121 titles.
* With some minor tweaks to my code, one would get a wide array of results. For example:
	* One could select different descriptions such as 'python', 'java', 'HTML', etc. The descripton term is aliased to search, therefore you can use other terms not listed to find a specific type of jobs.
	* One could also search for a location either by city name, zip code, or lattitude and longitude. No location with lattitude and longitude. 
	* One would be able to limit results of full time positions.
	* Finally, someone may also search for different words in job titles by changing the Regex.

## Output File:
* The last part of this project outputs a .dat file for later use if one would like the data from a previous date. You can see how I saved the file in my code using Pickle. To use this file later, one would simply use ln[1] f=open('githubJobs.dat') ln[2] d2=load(f) ln[3] f.close(). And boom, there is your list of Job dictionaries ready to be used later. 

# Hope You Enjoyed