import sqlite3
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt 
import tldextract
from collections import Counter
import seaborn as sns

# Set seaborn state
sns.set()

# Instantiate pathnames to databases
VANILLA_DB_PATH = '/Users/sanjanaaithal/Desktop/Vanilla/crawl-data.sqlite'
ADBLOCK_DB_PATH = '/Users/sanjanaaithal/Desktop/Ad-Block/crawl-data.sqlite'


# SQL query
http_query = 'SELECT url, top_level_url FROM http_requests'


def isThirdParty(url, top_level_url):

    # Extract from both the urls
    ext_url = tldextract.extract(url)
    ext_top_level_url = tldextract.extract(top_level_url)

    # If extracts are equal, not a third party
    if ext_url == ext_top_level_url:
        return False
    return True


def getQueryResult(database_path, http_query):

    # Establish database connection and cursor
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Execute the sqlite3 query, get query results
    cursor.execute(http_query)
    query_result = cursor.fetchall()
    
    # Close the connection and cursor
    cursor.close()
    connection.close()

    # Return query results
    return query_result


def updateDictionary(site, dictionary_param):
    # If item is not in dictionary, set default as 1. Else, increment value.
    if (site not in dictionary_param): 
        dictionary_param.setdefault(site, 1)
    else:
        dictionary_param[site] += 1


def findThirdParty(query_result, website_dict, tparty_dict):
    # Traverse through the query results
    for row in query_result:
        url = row[0]
        top_level_url = row[1]

        # Check to see if it is third-party
        if(isThirdParty(url, top_level_url)):
            # If third party, append site to dictionaries
            ext = tldextract.extract(url)
            third_party_domain = 'https://' + '.'.join(ext[1:])

            updateDictionary(third_party_domain, tparty_dict)
            updateDictionary(top_level_url, website_dict)



if __name__ == "__main__":

    # Create dictionary containers
    vanilla_websites = {}
    vanilla_tparty_websites = {}

    adblock_websites = {}
    adblock_tparty_websites = {}


    # Get the vanilla SQL query results, turn it into a numpy array for better space and time complexity
    vanilla_result = getQueryResult(VANILLA_DB_PATH, http_query)
    df_vanilla = DataFrame(vanilla_result).to_numpy()
    
    # Get the adblock SQL query results, turn it into a numpy array for better space and time complexity
    adblock_result = getQueryResult(ADBLOCK_DB_PATH, http_query)
    df_adblock = DataFrame(adblock_result).to_numpy()

    # Find third party websites
    findThirdParty(vanilla_result, vanilla_websites, vanilla_tparty_websites)
    findThirdParty(adblock_result, adblock_websites, adblock_tparty_websites)

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
    vanilla_y = list(Counter(vanilla_websites).values())
    adblock_y = list(Counter(adblock_websites).values())

    plt.title("Distribution of Third-Party HTTP Requests")
    plt.xlabel("Top 100 Websites")
    plt.ylabel("Number of Third-Party HTTP Requests")
    plt.plot(vanilla_y, label="Vanilla Mode")
    plt.plot(adblock_y, label="Ad-Block Mode")
    plt.legend()
    # plt.show()
    plt.savefig('http.png')