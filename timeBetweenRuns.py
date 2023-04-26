from projectConstants import *
import pandas as pd


def getTimestampRow(row):
    '''Get a dictionary containing information for date time'''
    return {
        SUBJECT_ID_KEY: row[SUBJECT_ID_KEY],
        ASSIGNMENT_ID_KEY: row[ASSIGNMENT_ID_KEY],
        CLIENT_TIMESTAMP_KEY: row[CLIENT_TIMESTAMP_KEY],
        DATE_TIME_KEY: pd.to_datetime(row.ClientTimestamp, unit='ms')       
    }


def getFilteredRunEvents(df):
    '''
    Get run events with execution action and start events only
    '''
    runDf = pd.DataFrame()
    
    for _, row in df.iterrows():
        if row.EventType == 'Run.Program':
            if row['X-Metadata'] != 'Start':
                continue
            timeRow = pd.DataFrame(getTimestampRow(row), index=[0])
            runDf = pd.concat([runDf, timeRow], ignore_index=True)
    return runDf


def getTimeBetweenRuns(df, student, assignment):
    '''Get time between runs for a student and assignment'''
    studentRunsDf = df[(df.SubjectID == student)&(df.AssignmentID == assignment)]
    studentRunsDf.sort_values(by=DATE_TIME_KEY, inplace=True)
    studentRunsDf[NEXT_DATE_TIME_KEY] = studentRunsDf[DATE_TIME_KEY].shift(-1)
    studentRunsDf[DIFF_KEY] = studentRunsDf[NEXT_DATE_TIME_KEY] - studentRunsDf[DATE_TIME_KEY]
    studentRunsDf[DAYS_DIFF_KEY] = round((studentRunsDf[NEXT_DATE_TIME_KEY] - studentRunsDf[DATE_TIME_KEY]).dt.days)
    studentRunsDf[HOURS_DIFF_KEY] = round((studentRunsDf[NEXT_DATE_TIME_KEY] - studentRunsDf[DATE_TIME_KEY]).dt.seconds / 3600.0, 2)
    studentRunsDf[MINUTES_DIFF_KEY] = round((studentRunsDf[NEXT_DATE_TIME_KEY] - studentRunsDf[DATE_TIME_KEY]).dt.seconds / 60.0, 2)
    studentRunsDf[SECONDS_DIFF_KEY] = round((studentRunsDf[NEXT_DATE_TIME_KEY] - studentRunsDf[DATE_TIME_KEY]).dt.seconds, 2)
    return studentRunsDf


def getTimeBetweenRunsDf(keystroke_df, final_data):
    '''Get time between runs for each student'''
    runEvents = getFilteredRunEvents(keystroke_df)
    timeDifferenceDf = pd.DataFrame()
    for student, assignment, _ in final_data:
        studentDf = getTimeBetweenRuns(runEvents, student, assignment)
        timeDifferenceDf = pd.concat([timeDifferenceDf, studentDf], ignore_index=True)
    return timeDifferenceDf
