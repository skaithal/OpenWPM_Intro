import sqlite3
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt 
import tldextract
from collections import Counter
import seaborn as sns
from collections import defaultdict

# Set seaborn state
sns.set()

# Instantiate pathnames to databases
VANILLA_DB_PATH = '/Users/sanjanaaithal/Desktop/Vanilla/crawl-data.sqlite'
ADBLOCK_DB_PATH = '/Users/sanjanaaithal/Desktop/Ad-Block/crawl-data.sqlite'


# SQL query
js_query = 'SELECT script_url, visit_id FROM javascript'

def df_toDictionary(df):

    # Convert a pandas df to a dictionary
    sample_dict = {}
    for i in range(len(df)):
        sample_dict[i+1] = str(df[i])[2:-2]
    return sample_dict

def isThirdParty(url, top_level_url):

    # Extract from both the urls
    ext_url = tldextract.extract(url)
    ext_top_level_url = tldextract.extract(top_level_url)

    # If extracts are equal, not a third party
    if ext_url == ext_top_level_url:
        return False
    return True


def getQueryResult(database_path, query):

    # Establish database connection and cursor
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Execute the sqlite3 query, get query results
    cursor.execute(query)
    query_result = cursor.fetchall()
    
    # Close the connection and cursor
    cursor.close(), connection.close()

    # Return query results
    return query_result


def updateDictionary(site, dictionary_param):

    # If item is not in dictionary, set default as 1. Else, increment value.
    if (site not in dictionary_param): 
        dictionary_param.setdefault(site, 1)
    else:
        dictionary_param[site] += 1


def findThirdParty(query_result, website_dict, tparty_dict, csv_dict):

    # Traverse through the query results
    for row in query_result:
        host = row[0]
        visit_id = row[1]

        # Check to see if it is third-party
        if(isThirdParty(host, csv_dict[visit_id])):

            # If third party, append site to dictionaries
            ext = tldextract.extract(host)
            third_party_domain = '.'.join(ext[1:])

            updateDictionary(third_party_domain, tparty_dict)
            updateDictionary(csv_dict[visit_id], website_dict)



if __name__ == "__main__":

    # Create dictionary containers
    vanilla_websites = {}
    vanilla_tparty_websites = {}

    adblock_websites = {}
    adblock_tparty_websites = {}

    # Load a pd dataframe using the given csv file, create dictionary of csv entries
    top100_df = pd.read_csv('top-1m.csv', header=None, nrows=100, usecols=[1]).to_numpy()
    top100_dict = df_toDictionary(top100_df)

    # Get the vanilla SQL query results, turn it into a numpy array for better space and time complexity
    vanilla_result = getQueryResult(VANILLA_DB_PATH, js_query)
    df_vanilla = DataFrame(vanilla_result).to_numpy()
    
    # Get the adblock SQL query results, turn it into a numpy array for better space and time complexity
    adblock_result = getQueryResult(ADBLOCK_DB_PATH, js_query)
    df_adblock = DataFrame(adblock_result).to_numpy()

    # Find third party websites
    findThirdParty(vanilla_result, vanilla_websites, vanilla_tparty_websites, top100_dict)
    findThirdParty(adblock_result, adblock_websites, adblock_tparty_websites, top100_dict)

    # Sort and return the 10 most common
    sorted_vanilla_10 = sorted(vanilla_tparty_websites.items(), key=lambda x: x[1], reverse=True)[:10]
    sorted_adblock_10 = sorted(adblock_tparty_websites.items(), key=lambda x: x[1], reverse=True)[:10]

    #Print output
    print('Top 10 Third Parties(Vanilla Mode)\n')
    for i in range(len(sorted_vanilla_10)):
        print(str(sorted_vanilla_10[i][0]) + ': ' + str(sorted_vanilla_10[i][1]))

    print('Top 10 Third Parties(Ad-block Mode)\n')
    for i in range(len(sorted_adblock_10)):
        print(str(sorted_adblock_10[i][0]) + ': ' + str(sorted_adblock_10[i][1]))

    # Plot values
    vanilla_count = list(Counter(vanilla_websites).values())
    adblock_count = list(Counter(adblock_websites).values())

    plt.title("Distribution of Third-Party Javascript Requests")
    plt.xlabel("Top 100 Websites")
    plt.ylabel("Number of Third-Party Javascript Requests")
    plt.plot(vanilla_count, label="Vanilla Mode")
    plt.plot(adblock_count, label="Ad-Block Mode")
    plt.legend()
    # plt.show()
    plt.savefig('js.png')
