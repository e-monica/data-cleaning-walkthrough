# Provided by Dataquest.io coursework
#
# At many points in your career, you'll need to be able to build complete, end-to-end data science projects on your own. Data science projects usually consist of one of two things:

# An exploration and analysis of a set of data. One example might involve analyzing donors to political campaigns, creating a plot, and then sharing an analysis of the plot with others.
# An operational system that generates predictions based on data that updates continually. An algorithm that pulls in daily stock ticker data and predicts which stock prices will rise and fall would be one example.
# You'll find the ability to create data science projects useful in several different contexts:

# Projects will help you build a portfolio, which is critical to finding a job as a data analyst or scientist.
# Working on projects will help you learn new skills and reinforce existing concepts.
# Most "real-world" data science and analysis work consists of developing internal projects.
# Projects allow you to investigate interesting phenomena and satisfy your curiosity.
# Whether you aim to become a data scientist or analyst or you're just curious about the world, building projects can be immensely rewarding.

# Here's an example of a finished project.

# In this mission, we'll walk through the first part of a complete data science project, including how to acquire the raw data. The project will focus on exploring and analyzing a data set. We'll develop our data cleaning and storytelling skills, which will enable us to build complete projects on our own.

# We'll focus primarily on data exploration in this mission. We'll also combine several messy data sets into a single clean one to make analysis easier. Over the next few missions, we'll work through the rest of our project and perform the actual analysis.

# The first step in creating a project is to decide on a topic. You want the topic to be something you're interested in and motivated to explore. It's very obvious when people are making projects just to make them, rather than out of a genuine interest in the topic.

# Here are two ways to go about finding a good topic:

# Think about what sectors or angles you're really interested in, then find data sets relating to those sectors.
# Review several data sets, and find one that seems interesting enough to explore.
# Whichever approach you take, you can start your search at these sites:

# Data.gov - A directory of government data downloads
# /r/datasets - A subreddit that has hundreds of interesting data sets
# Awesome datasets - A list of data sets hosted on GitHub
# rs.io - A great blog post with hundreds of interesting data sets
# In real-world data science, you may not find an ideal data set. You might have to aggregate disparate data sources instead, or do a good amount of data cleaning.

# For the purposes of this project, we'll be using data about New York City public schools, which can be found here.

#################################################################################################################################


# Once you've chosen a topic, you'll want to pick an angle to investigate. It's important to choose an angle that has enough depth to analyze, but isn't so complicated that it's difficult to get started. You want to finish the project, and you want your results to be interesting to others.

# One of the most controversial issues in the U.S. educational system is the efficacy of standardized tests, and whether they're unfair to certain groups. Given our prior knowledge of this topic, investigating the correlations between SAT scores and demographics might be an interesting angle to take. We could correlate SAT scores with factors like race, gender, income, and more.

# The SAT, or Scholastic Aptitude Test, is an exam that U.S. high school students take before applying to college. Colleges take the test scores into account when deciding who to admit, so it's fairly important to perform well on it.

# The test consists of three sections, each of which has 800 possible points. The combined score is out of 2,400 possible points (while this number has changed a few times, the data set for our project is based on 2,400 total points). Organizations often rank high schools by their average SAT scores. The scores are also considered a measure of overall school district quality.

# New York City makes its data on high school SAT scores available online, as well as the demographics for each high school. The first few rows of the SAT data look like this:

# SAT

# Unfortunately, combining both of the data sets won't give us all of the demographic information we want to use. We'll need to supplement our data with other sources to do our full analysis.

# The same website has several related data sets covering demographic information and test scores. Here are the links to all of the data sets we'll be using:

# SAT scores by school - SAT scores for each high school in New York City
# School attendance - Attendance information for each school in New York City
# Class size - Information on class size for each school
# AP test results - Advanced Placement (AP) exam results for each high school (passing an optional AP exam in a particular subject can earn a student college credit in that subject)
# Graduation outcomes - The percentage of students who graduated, and other outcome information
# Demographics - Demographic information for each school
# School survey - Surveys of parents, teachers, and students at each school
# All of these data sets are interrelated. We'll need to combine them into a single data set before we can find correlations.

########################################################################################################################################

# Before we move into coding, we'll need to do some background research. A thorough understanding of the data will help us avoid costly mistakes, such as thinking that a column represents something other than what it does. Background research will also give us a better understanding of how to combine and analyze the data.

# In this case, we'll want to research:

# New York City
# The SAT
# Schools in New York City
# Our data
# We can learn a few different things from these resources. For example:

# Only high school students take the SAT, so we'll want to focus on high schools.
# New York City is made up of five boroughs, which are essentially distinct regions.
# New York City schools fall within several different school districts, each of which can contains dozens of schools.
# Our data sets include several different types of schools. We'll need to clean them so that we can focus on high schools only.
# Each school in New York City has a unique code called a DBN, or district borough number.
# Aggregating data by district will allow us to use the district mapping data to plot district-by-district differences.

#########################################################################################################################################

# Once we've done our background research, we're ready to read in the data. For your convenience, we've placed all the data into the schools folder. Here are all of the files in the folder:

# ap_2010.csv - Data on AP test results
# class_size.csv - Data on class size
# demographics.csv - Data on demographics
# graduation.csv - Data on graduation outcomes
# hs_directory.csv - A directory of high schools
# sat_results.csv - Data on SAT scores
# survey_all.txt - Data on surveys from all schools
# survey_d75.txt - Data on surveys from New York City district 75
# survey_all.txt and survey_d75.txt are in more complicated formats than the other files. For now, we'll focus on reading in the CSV files only, and then explore them.

# We'll read each file into a pandas dataframe, and then store all of the dataframes in a dictionary. This will give us a convenient way to store them, and a quick way to reference them later on.

# Instructions

# Read each of the files in the list data_files into a pandas dataframe using the pandas.read_csv() function.
# Recall that all of the data sets are in the schools folder. That means the path to ap_2010.csv is schools/ap_2010.csv.
# Add each of the dataframes to the dictionary data, using the base of the filename as the key. For example, you'd enter ap_2010 for the file ap_2010.csv.
# Afterwards, data should have the following keys:
# ap_2010
# class_size
# demographics
# graduation
# hs_directory
# sat_results
# In addition, each key in data should have the corresponding dataframe as its value.

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    #note the schools string combo with the bracketed zero
    #format(f) takes an arbitrary number of positional and keyword arguments: "The story of {0}, {1}, and {c}".format(a, b, c=d)
    key_name = f.replace(".csv", "")
    data[key_name] = d
    
#####################################################################################################################################


# What we're mainly interested in is the SAT data set, which corresponds to the dictionary key sat_results. This data set contains the SAT scores for each high school in New York City. We eventually want to correlate selected information from this data set with information in the other data sets.

# Let's explore sat_results to see what we can discover. Exploring the dataframe will help us understand the structure of the data, and make it easier for us to analyze it.

# Instructions

# Display the first five rows of the SAT scores data.
# Use the key sat_results to access the SAT scores dataframe stored in the dictionary data.
# Use the pandas.DataFrame.head() method along with the print() function to display the first five rows of the dataframe.

print(data["sat_results"].head())  #refer to page 4 for context


########################################################################################################################################


# When we printed the first five rows of the SAT data, the output looked like this:

# DBN                                    SCHOOL NAME  \
# 0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
# 1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
# 2  01M450                     EAST SIDE COMMUNITY SCHOOL
# 3  01M458                      FORSYTH SATELLITE ACADEMY
# 4  01M509                        MARTA VALLE HIGH SCHOOL
# ​
#   Num of SAT Test Takers SAT Critical Reading Avg. Score SAT Math Avg. Score  \
# 0                     29                             355                 404
# 1                     91                             383                 423
# 2                     70                             377                 402
# 3                      7                             414                 401
# 4                     44                             390                 433
# ​
#   SAT Writing Avg. Score
# 0                    363
# 1                    366
# 2                    370
# 3                    359
# 4                    384
# We can make a few observations based on this output:

# The DBN appears to be a unique ID for each school.
# We can tell from the first few rows of names that we only have data about high schools.
# There's only a single row for each high school, so each DBN is unique in the SAT data.
# We may eventually want to combine the three columns that contain SAT scores -- SAT Critical Reading Avg., Score SAT Math Avg. Score, and SAT Writing Avg. Score -- into a single column to make the scores easier to analyze.
# Given these observations, let's explore the other data sets to see if we can gain any insight into how to combine them.

# Instructions

# Loop through each key in data. For each key:
# Display the first five rows of the dataframe associated with the key.

for key in data:
    print(data[key].head(5))


#######################################################################################################################################

# In the last step, we saw a group of dataframes that looked like this:

# CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
# 0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
# 1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
# 2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
# 3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
# 4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED
# We can make some observations based on the first few rows of each one.

# Each data set appears to either have a DBN column, or the information we need to create one. That means we can use a DBN column to combine the data sets. First we'll pinpoint matching rows from different data sets by looking for identical DBNs, then group all of their columns together in a single data set.
# Some fields look interesting for mapping -- particularly Location 1, which contains coordinates inside a larger string.
# Some of the data sets appear to contain multiple rows for each school (because the rows have duplicate DBN values). That means we’ll have to do some preprocessing to ensure that each DBN is unique within each data set. If we don't do this, we'll run into problems when we combine the data sets, because we might be merging two rows in one data set with one row in another data set.
# Before we proceed with the merge, we should make sure we have all of the data we want to unify. We mentioned the survey data earlier (survey_all.txt and survey_d75.txt), but we didn't read those files in because they're in a slightly more complex format.

# Each survey text file looks like this:


# dbn bn  schoolname  d75 studentssurveyed    highschool  schooltype  rr_s
# "01M015"    "M015"  "P.S. 015 Roberto Clemente" 0   "No"    0   "Elementary School"     88
# The files are tab delimited and encoded with Windows-1252 encoding. An encoding defines how a computer stores the contents of a file in binary. The most common encodings are UTF-8 and ASCII. Windows-1252 is rarely used, and can cause errors if we read such a file in without specifying the encoding. If you'd like to read more about encodings, here's a good primer.

# We'll need to specify the encoding and delimiter to the pandas pandas.read_csv() function to ensure it reads the surveys in properly.

# After we read in the survey data, we'll want to combine it into a single dataframe. We can do this by calling the pandas.concat() function:


# z = pd.concat([x,y], axis=0)
# The code above will combine dataframes x and y by essentially appending y to the end of x. The combined dataframe z will have the number of rows in x plus the number of rows in y.

#########################################################################################################################################

# Read in survey_all.txt.
# Use the pandas.read_csv() function to read survey_all.txt into the variable all_survey. Recall that this file is located in the schools folder.
# Specify the keyword argument delimiter="\t".
# Specify the keyword argument encoding="windows-1252".
# Read in survey_d75.txt.
# Use the pandas.read_csv() function to read schools/survey_d75.txt into the variable d75_survey. Recall that this file is located in the schools folder.
# Specify the keyword argument delimiter="\t".
# Specify the keyword argument encoding="windows-1252".
# Combine d75_survey and all_survey into a single dataframe.
# Use the pandas concat() function with the keyword argument axis=0 to combine d75_survey and all_survey into the dataframe survey.
# Pass in all_survey first, then d75_survey when calling the pandas.concat() function.
# Display the first five rows of survey using the pandas.DataFrame.head() function.


#pandas not schools as the reference point for read_csv
#note how to route the direction of going within the folder 
#schools is done within a string-ed context
all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")
survey = pd.concat([all_survey, d75_survey], axis=0)

print(survey.head(5))


##########################################################################################################################################'

# In the last step, the expected output was:
# N_p  N_s  N_t  aca_p_11  aca_s_11  aca_t_11  aca_tot_11    bn  com_p_11  \
# 0   90  NaN   22       7.8       NaN       7.9         7.9  M015       7.6   
# 1  161  NaN   34       7.8       NaN       9.1         8.4  M019       7.6
# There are two immediate facts that we can see in the data:

# There are over 2000 columns, nearly all of which we don't need. We'll have to filter the data to remove the unnecessary ones. Working with fewer columns will make it easier to print the dataframe out and find correlations within it.
# The survey data has a dbn column that we'll want to convert to uppercase (DBN). The conversion will make the column name consistent with the other data sets.
# First, we'll need filter the columns to remove the ones we don't need. Luckily, there's a data dictionary at the original data download location. The dictionary tells us what each column represents. Based on our knowledge of the problem and the analysis we're trying to do, we can use the data dictionary to determine which columns to use.

# Here's a preview of the data dictionary:
# Based on the dictionary, it looks like these are the relevant columns:

# ["dbn", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
# These columns will give us aggregate survey data about how parents, teachers, and students feel about school safety, academic performance, and more. It will also give us the DBN, which allows us to uniquely identify the school.

# Before we filter columns out, we'll want to copy the data from the dbn column into a new column called DBN. We can copy columns like this:

# survey["new_column"] = survey["old_column"]
# Instructions

# Copy the data from the dbn column of survey into a new column in survey called DBN.
# Filter survey so it only contains the columns we listed above. You can do this using pandas.DataFrame.loc[].
# Remember that we renamed dbn to DBN; be sure to change the list of columns we want to keep accordingly.
# Assign the dataframe survey to the key survey in the dictionary data.
# When you're finished, the value in data["survey"] should be a dataframe with 23 columns and 1702 rows.

survey['DBN'] = survey['dbn']

columns = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey = survey.loc[:,columns]
#loc utilizes rows:columns
#filtered survey is the new reassigned survey variable
data['survey'] = survey
print(survey.head())

######################################################################################################################################

# When we explored all of the data sets, we noticed that some of them, like class_size and hs_directory, don't have a DBN column. hs_directory does have a dbn column, though, so we can just rename it.

# However, class_size doesn't appear to have the column at all. Here are the first few rows of the data set:

# CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
# 0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
# 1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
# 2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
# 3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
# 4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED
# Here are the first few rows of the sat_results data, which does have a DBN column:

# DBN                                    SCHOOL NAME  \
# 0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
# 1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
# 2  01M450                     EAST SIDE COMMUNITY SCHOOL
# 3  01M458                      FORSYTH SATELLITE ACADEMY
# 4  01M509                        MARTA VALLE HIGH SCHOOL
# From looking at these rows, we can tell that the DBN in the sat_results data is just a combination of the CSD and SCHOOL CODE columns in the class_size data. The main difference is that the DBN is padded, so that the CSD portion of it always consists of two digits. That means we'll need to add a leading 0 to the CSD if the CSD is less than two digits long. Here's a diagram illustrating what we need to do:

# As you can see, whenever the CSD is less than two digits long, we need to add a leading 0. We can accomplish this using the pandas.Series.apply() method, along with a custom function that:

# Takes in a number.
# Converts the number to a string using the str() function.
# Check the length of the string using the len() function.
# If the string is two digits long, returns the string.
# If the string is one digit long, adds a 0 to the front of the string, then returns it.
# You can use the string method zfill() to do this.
# Once we've padded the CSD, we can use the addition operator (+) to combine the values in the CSD and SCHOOL CODE columns. Here's an example of how we would do this:

# dataframe["new_column"] = dataframe["column_one"] + dataframe["column_two"]
# And here's a diagram illustrating the basic concept:

# Copy the dbn column in hs_directory into a new column called DBN.
# Create a new column called padded_csd in the class_size data set.
# Use the pandas.Series.apply() method along with a custom function to generate this column.
# Make sure to apply the function along the data["class_size"]["CSD"] column.
# Use the addition operator (+) along with the padded_csd and SCHOOL CODE columns of class_size, then assign the result to the DBN column of class_size.
# Display the first few rows of class_size to double check the DBN column.

#hs_directory["DBN"] = hs_directory["dbn"]
#pandas.DataFrame.apply()
#    class_size['padded_csd'] = padded_csd

#def function(number):
#    if 2 == len(str(number)):
#        return str(number)
#    if 1 == len(str(number)):
#        return '0'.join(str(number))
#zfill()

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return string_representation.zfill(2)
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())

#########################################################################################################################################

# Now we're almost ready to combine our data sets. Before we do, let's take some time to calculate variables that will be useful in our analysis. We've already discussed one such variable -- a column that totals up the SAT scores for the different sections of the exam. This will make it much easier to correlate scores with demographic factors because we'll be working with a single number, rather than three different ones.
# Before we can generate this column, we'll need to convert the SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score columns in the sat_results data set from the object (string) data type to a numeric data type. We can use the pandas.to_numeric() method for the conversion. If we don't convert the values, we won't be able to add the columns together.
# It's important to pass the keyword argument errors="coerce" when we call pandas.to_numeric(), so that pandas treats any invalid strings it can't convert to numbers as missing values instead.
# After we perform the conversion, we can use the addition operator (+) to add all three columns together.

# Instructions

# Convert the SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score columns in the sat_results data set from the object (string) data type to a numeric data type.
# Use the pandas.to_numeric() function on each of the columns, and assign the result back to the same column.
# Pass in the keyword argument errors="coerce".
# Create a column called sat_score in sat_results that holds the combined SAT score for each student.
# Add up SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score, and assign the total to the sat_score column of sat_results.
# Display the first few rows of the sat_score column of sat_results to verify that everything went okay.

#sat_results = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score columns']
#sat_results.to_numeric()

cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]
print(data['sat_results']['sat_score'].head())

###########################################################################################################################################

# Next, we'll want to parse the latitude and longitude coordinates for each school. This will enable us to map the schools and uncover any geographic patterns in the data. The coordinates are currently in the text field Location 1 in the hs_directory data set.

# Let's take a look at the first few rows:

# 0    883 Classon Avenue\nBrooklyn, NY 11225\n(40.67...
# 1    1110 Boston Road\nBronx, NY 10456\n(40.8276026...
# 2    1501 Jerome Avenue\nBronx, NY 10452\n(40.84241...
# 3    411 Pearl Street\nNew York, NY 10038\n(40.7106...
# 4    160-20 Goethals Avenue\nJamaica, NY 11432\n(40...
# As you can see, this field contains a lot of information we don't need. We want to extract the coordinates, which are in parentheses at the end of the field. Here's an example:

# 1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)
# We want to extract the latitude, 40.8276026690005, and the longitude, -73.90447525699966. Taken together, latitude and longitude make up a pair of coordinates that allows us to pinpoint any location on Earth.

# We can do the extraction with a regular expression. The following expression will pull out everything inside the parentheses:

# import re
# re.findall("\(.+\)", "1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)")
# This command will return [(40.8276026690005, -73.90447525699966)]. We'll need to process this result further using the string methods split() and replace() methods to extract each coordinate.

# Instructions

# Write a function that:
# Takes in a string
# Uses the regular expression above to extract the coordinates
# Uses string manipulation functions to pull out the latitude
# Returns the latitude
# Use the Series.apply() method to apply the function across the Location 1 column of hs_directory. Assign the result to the lat column of hs_directory.
# Display the first few rows of hs_directory to verify the results.

import re
def find_lat(loc):
    coords = re.findall("\(.+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)

print(data["hs_directory"].head())

##########################################################################################################################################

# On the last screen, we parsed the latitude from the Location 1 column. Now we'll just need to do the same for the longitude.
# Once we have both coordinates, we'll need to convert them to numeric values. We can use the pandas.to_numeric() function to convert them from strings to numbers.

# Instructions

# Write a function that:
# Takes in a string.
# Uses the regular expression above to extract the coordinates.
# Uses string manipulation functions to pull out the longitude.
# Returns the longitude.
# Use the Series.apply() method to apply the function across the Location 1 column of hs_directory. Assign the result to the lon column of hs_directory.
# Use the to_numeric() function to convert the lat and lon columns of hs_directory to numbers.
# Specify the errors="coerce" keyword argument to handle missing values properly.
# Display the first few rows of hs_directory to verify the results.

import re
def find_lon(loc):
    coords = re.findall("\(.+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

print(data["hs_directory"].head())

###########################################################################################################################################

# We're almost ready to combine our data sets! We've come a long way in this mission -- we've gone from choosing a topic for a project to acquiring the data to having clean data that we're almost ready to combine.

# Along the way, we've learned how to:

# Handle files with different formats and columns
# Prepare to merge multiple files
# Use text processing to extract coordinates from a string
# Convert columns from strings to numbers
# You'll always learn something new while working on a real-world data science project. Each project is unique, and there will always be quirks you don't quite know how to handle. The key is to be willing to try different approaches, and to have a general framework in your head for how to move from Step A to Step B.

# In the next mission, we'll finish cleaning the data sets, then combine them so we can start our analysis.

