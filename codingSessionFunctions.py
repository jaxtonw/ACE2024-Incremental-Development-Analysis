from projectConstants import *
import pandas as pd

from timeBetweenRuns import *

# use complete keystroke data
# student, assignment, number of coding sessions
def getCodingSessionsForAssignment(df, student, assignment):
    '''coding sessions end after more than 5 minutes from last event'''
    studentAssignmentDf = df[(df.SubjectID == student)&(df.AssignmentID == assignment)].copy()
    # studentAssignmentDf = studentAssignmentDf[SUBJECT_ID_KEY, ASSIGNMENT_ID_KEY, CLIENT_TIMESTAMP_KEY]
    # convert client timestamp to date time
    studentAssignmentDf[DATE_TIME_KEY] = pd.to_datetime(studentAssignmentDf.ClientTimestamp, unit='ms') 
    studentAssignmentDf[SESSION_ID_KEY] = -1
    # sort by timestamp
    studentAssignmentDf.sort_values(by=DATE_TIME_KEY, inplace=True)
    # give session number , if within 5 minutes, keep that session number numbers
    if studentAssignmentDf.size > 0: 
        lastEventTime = studentAssignmentDf.head(1)[DATE_TIME_KEY].values[0]
    # 5 minutes from last event, not start of the session
    sessionId = 0
    for i, row in studentAssignmentDf.iterrows():
        diff = row[DATE_TIME_KEY] - lastEventTime
        minutes_diff = diff.total_seconds() / 60
        if minutes_diff > 5:
            sessionId += 1
        studentAssignmentDf.at[i,SESSION_ID_KEY] = sessionId
        lastEventTime = row[DATE_TIME_KEY]
    return studentAssignmentDf 


def getTimeSpentPerSession(df):
    '''Get total time spent per session'''
    codingSessionDf = pd.DataFrame()
    sessionIds = df[SESSION_ID_KEY].unique()
    for sessionId in sessionIds:
        sessionDf = df[(df[SESSION_ID_KEY] == sessionId)].copy()
        # sort by dates just in case
        sessionDf.sort_values(by=DATE_TIME_KEY, inplace=True)
        # subtract start session time and end session time to get total session time
        startTime = sessionDf.head(1)[CLIENT_TIMESTAMP_KEY].values[0]
        endTime = sessionDf.tail(1)[CLIENT_TIMESTAMP_KEY].values[0]
        sessionTime = endTime - startTime
        sessionDf[SESSION_TIME_KEY] = sessionTime
        codingSessionDf = pd.concat([codingSessionDf, sessionDf], ignore_index=True)
    return codingSessionDf

def getTimeSpentPerAssignment(df):
    '''get total time spent per assignment using coding session time'''
    assignmentTimeDf = pd.DataFrame()
    assignments = df[ASSIGNMENT_ID_KEY].unique()
    for assignment in assignments:
        assignmentDf = df[(df[ASSIGNMENT_ID_KEY] == assignment)]
        # get unique session times
        sessionTimes = assignmentDf[SESSION_TIME_KEY].unique()
        # add all times in list
        totalAssignmentTime = sum(sessionTimes)
        assignmentDf[TOTAL_ASSIGNMENT_TIME_KEY] = totalAssignmentTime
        assignmentTimeDf = pd.concat([assignmentTimeDf, assignmentDf], ignore_index=True)
    return assignmentTimeDf

def getCodingSessionsDf(keystroke_df, final_data):
    '''Get coding session for each student and assignment, where coding session is within 5 minutes'''
    runEvents = getFilteredRunEvents(keystroke_df)
    codingSessionDf = pd.DataFrame()
    for student, assignment, _ in final_data:
        codingSessionAssignmentDf = getCodingSessionsForAssignment(runEvents, student, assignment)
        # get time on assignment
        # time spent per session
        codingSessionTimeDf = getTimeSpentPerSession(codingSessionAssignmentDf)
        # total time spent per assignment
        if codingSessionTimeDf.size > 0:
            codingSessionTimeTotalDf = getTimeSpentPerAssignment(codingSessionTimeDf)
            codingSessionDf = pd.concat([codingSessionDf, codingSessionTimeTotalDf], ignore_index=True)
    return codingSessionDf
