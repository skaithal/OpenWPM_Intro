from automation import CommandSequence, TaskManager
import pandas as pd

# Declare constants
NUM_BROWSERS = 3

# Load a pd dataframe using the given csv file
top100_df = pd.read_csv('top-1m.csv', header=None, nrows=100, usecols=[1])

# Load the default manager params and NUM_BROWSER copies of the default browser params
manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)

# Update browser configuration (use this for per-browser settings)
for i in range(NUM_BROWSERS):
    # Record HTTP Requests and Responses
    browser_params[i]['http_instrument'] = True
    # Record cookie changes
    browser_params[i]['cookie_instrument'] = True
    # Record JS Web API calls
    browser_params[i]['js_instrument'] = True

    # Set true for ad blocking mode. Set false for vanilla mode. 
    browser_params[i]['ublock-origin'] = False

    # Do not record the callstack of all WebRequests made
    browser_params[i]['callstack_instrument'] = False
    # Do not record Navigations
    browser_params[i]['navigation_instrument'] = False

    # Set the display quality to headful
    browser_params[i]['display mode'] = 'headful'


if (browser_params[0]['ublock-origin']):
    db_path = '/Users/sanjanaaithal/Desktop/Ad-Block'
else:
    db_path = '/Users/sanjanaaithal/Desktop/Vanilla'


# Update TaskManager configuration (use this for crawl-wide settings)
manager_params['data_directory'] = db_path
manager_params['log_directory'] = db_path

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params)

# Visit the sites
for numpy_object in top100_df.to_numpy():
    # Turn numpy object into a site string
    site = 'http://' +  str(numpy_object)[2:-2]


    # Parallelize sites over all number of browsers set above.
    command_sequence = CommandSequence.CommandSequence(
        site, reset=True,
        callback=lambda success, val=site:
        print("CommandSequence {} done".format(val)))

    # Start by visiting the page
    command_sequence.get(sleep=3, timeout=60)

    # Run commands across the three browsers (simple parallelization)
    manager.execute_command_sequence(command_sequence)


# Shuts down the browsers and waits for the data to finish logging
manager.close()
    




