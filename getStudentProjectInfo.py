import pandas as pd
from reconstructSubmissions import *
from getSubmissionDataframes import *


# Get all students and project list
def getStudentProjectList(students, df):
    '''
    Get lists containing dataframes of all student submissions

    Returns a tuple of length 3, containing: 
        index 0 - A list containing dataframes representing the given student's submission
        index 1 - A list containing dictionaries representing a reconstructed project at each run event 
        index 2 - A list containing tuples with the following information:
                    tuple[0] : The student name
                    tuple[1] : The assignment
                    tuple[2] : The dictionary representing that reconstructed project

    The index of each returned list corresponds with each other, representing the same student and submission

    More often than not, you will only want the last index of the tuple that is returned
    '''

    eachProject = []
    runEvents = []
    allData = []
    for _,row in students.iterrows():
        for i in students.columns[2:10]:
            # print(row[1], i)
            # arr.append((row[1],i))
            temp = getStudentSubmission(df, row[1], i)
            # print(temp)
            eachProject.append(temp)
            test = reconstructProjectAtRunEvents(temp)
            runEvents.append(test)
            # print(test)
            allData.append((row[1], i, test))
    return eachProject, runEvents, allData