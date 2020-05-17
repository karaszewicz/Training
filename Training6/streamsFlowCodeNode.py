# Preinstalled Python packages can be viewed from the Settings pane.
# In the Settings pane you can also install additional Python packages.

import sys
import time
import logging
import pandas as pd

# Use this logger for tracing or debugging your code:
logger = logging.getLogger(__name__)
# Example:
#     logger.info('Got to step 2...')

# init() function will be called once on flow initialization
# @state a Python dictionary object for keeping state. The state object is passed to the produce function
def init(state):
    # do something once on flow initialization and save in the state object
    pass
# produce() function will be called when the job starts to run.
# It is called on a background thread, and it will typically invoke the 'submit()' callback
# whenever a tuple of data is ready to be emitted from this operator.
# This allows for using asynchronous data services as well as synchronous data generation or retrieval.
# @submit a Python callback function that takes one argument: a dictionary representing a single tuple.
# @state a Python dictionary object for keeping state
# You must declare all output attributes in the Edit Schema window.
def produce(submit, state):
    df = pd.read_csv('https://raw.githubusercontent.com/pmservice/drug-selection/master/data/drug_batch_data.csv',
              sep=',')
    while True:
         for i, AGE in enumerate(df.AGE):
             event = {"Age": df.AGE.iloc[i],
                    "Sex": df.SEX.iloc[i],
                    "BP": df.BP.iloc[i],
                    "Cholesterol": df.CHOLESTEROL.iloc[i],
                    "Na":df.Na.iloc[i],
                    "K":df.K.iloc[i]}
             submit(event)
             time.sleep(0.5)  # Simulates a delay of 0.5 seconds between emitted events
# produce() function will be called when the job starts to run.
# It is called on a background thread, and it will typically invoke the 'submit()' callback
# whenever a tuple of data is ready to be emitted from this operator.
# This allows for using asynchronous data services as well as synchronous data generation or retrieval.
# @submit a Python callback function that takes one argument: a dictionary representing a single tuple.
# @state a Python dictionary object for keeping state
# You must declare all output attributes in the Edit Schema window.
def produce(submit, state):
    df = pd.read_csv('https://raw.githubusercontent.com/pmservice/drug-selection/master/data/drug_batch_data.csv',
              sep=',')
    while True:
        for i, AGE in enumerate(df.AGE):
            event = {"Age": df.AGE.iloc[i],
                    "Sex": df.SEX.iloc[i],
                    "BP": df.BP.iloc[i],
                    "Cholesterol": df.CHOLESTEROL.iloc[i],
                    "Na": df.NA.iloc[i],
                    "K":df.K.iloc[i]}
            submit(event)
            time.sleep(0.5) # Simulates a delay of 0.5 seconds between emitted events