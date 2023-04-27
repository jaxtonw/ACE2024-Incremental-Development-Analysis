from projectConstants import *
import pandas as pd
import numpy as np

from timeBetweenRuns import *


def markEventsByCodingSessions(df, student, assignment):
    '''
    For a specific (student, assignment) pair, make a new dataframe that marks all these events with a coding session

    Coding sessions end if there's more than 5 minutes from last event
    '''
    assnSessionDf = df[
        (df.SubjectID == student) & (df.AssignmentID == assignment)
        & (
        # We do not want any X-Attention events or Editor Close Actions
          ~ (
              ( df.EventType == 'X-Attention' )
            | ( ( df.EventType == 'X-Action' ) & (df['X-Metadata'] == 'Close Active Editor')
            )
          )
        )
        ].copy()

    assnSessionDf[DATE_TIME_KEY] = pd.to_datetime(assnSessionDf.ClientTimestamp, unit='ms') 
    assnSessionDf[SESSION_ID_KEY] = -1
    assnSessionDf[EVENT_TIME_DIFF_KEY] = np.NaN

    # sort by timestamp
    assnSessionDf.sort_values(by=DATE_TIME_KEY, inplace=True)

    if assnSessionDf.size > 0:
        lastEventTime = assnSessionDf.head(1)[DATE_TIME_KEY].values[0]
    # 5 minutes from last event, not start of the session
    sessionId = 0
    for i, row in assnSessionDf.iterrows():
        diff = row[DATE_TIME_KEY] - lastEventTime
        minutes_diff = diff.total_seconds() / 60

        if minutes_diff > 5:
            sessionId += 1
            # assnSessionDf.at[i, EVENT_TIME_DIFF_KEY] = np.NaN
        else:
            # If this event is still part of the same coding session, we note the diff time
            # If it's not, leave it as NaN
            assnSessionDf.at[i, EVENT_TIME_DIFF_KEY] = diff.total_seconds()

        assnSessionDf.at[i,SESSION_ID_KEY] = sessionId
        lastEventTime = row[DATE_TIME_KEY]

    return assnSessionDf


def getIndividualSessionInfo(df):
    '''
    Get information for each coding sesssion for a given (Student,Assignment)

    df should contain keystroke/event data for a given student/assignment with session numbers and time-diffs between sessions marked
        (See markEventsByCodingSessions)
    
    '''
    if df.size == 0:
        return None

    # The given dataframe should only be for one (Student,Assignment)

    allSessionIds = df[SESSION_ID_KEY].unique()
    student = df.head(1)[SUBJECT_ID_KEY].values[0]
    assn = df.head(1)[ASSIGNMENT_ID_KEY].values[0]

    studentSessionID = [student] * len(allSessionIds)
    assnSessionID = [assn] * len(allSessionIds)

    sessionIdsColumn = []
    sessionStartTimes = []
    sessionEndTimes = []
    sessionLengths = []
    sessionNumEvents = []
    sessionAvgKeyDiffTime = []

    for sessionId in allSessionIds:
        # Reduce df down to just this session
        sessionDf = df[(df[SESSION_ID_KEY] == sessionId)].copy()
        # sort by dates just in case
        sessionDf.sort_values(by=DATE_TIME_KEY, inplace=True)

        startTime = sessionDf.head(1)[CLIENT_TIMESTAMP_KEY].values[0]
        endTime = sessionDf.tail(1)[CLIENT_TIMESTAMP_KEY].values[0]
        # subtract start session time and end session time to get total session time
        lengthTime = endTime - startTime

        avgKeyDiffTime = sessionDf[EVENT_TIME_DIFF_KEY].mean()

        # Add all data for this session to a list
        sessionIdsColumn.append(sessionId)
        sessionStartTimes.append(startTime)
        sessionEndTimes.append(endTime)
        sessionLengths.append(lengthTime)
        sessionNumEvents.append(len(sessionDf))
        sessionAvgKeyDiffTime.append(avgKeyDiffTime)

    return pd.DataFrame(
        {
            SUBJECT_ID_KEY: studentSessionID,
            ASSIGNMENT_ID_KEY: assnSessionID,
            SESSION_ID_KEY: sessionIdsColumn,
            SESSION_START_TIME_KEY: sessionStartTimes,
            SESSION_END_TIME_KEY: sessionEndTimes,
            SESSION_TIME_KEY: sessionLengths,
            SESSION_KEYSTROKES_KEY: sessionNumEvents,
            SESSION_AVG_KEYDIFF_TIME_KEY: sessionAvgKeyDiffTime
        }
    )

def getCodingSessionsDf(keystroke_df, final_data):
    '''
    Get coding session for each student and assignment, where coding session is events within 5 minutes
    
    Returns a dataframe containing an entry for each unique coding session
    '''

    codingSessionDf = pd.DataFrame()
    for student, assignment, _ in final_data:

        # Get a dataframe with keystroke info for this (student,assignment), marked by coding sessions
        codingSessionAssignmentDf = markEventsByCodingSessions(keystroke_df, student, assignment)

        # Compute info for each coding session
        oneCodingSessionInfoDf = getIndividualSessionInfo(codingSessionAssignmentDf)

        if oneCodingSessionInfoDf is None:
            continue

        codingSessionDf = pd.concat([codingSessionDf, oneCodingSessionInfoDf], ignore_index=True)

    return codingSessionDf


def sessionInfoToAssignmentInfo(session_info_df):
    '''
    Convert a dataframe containing individual session info into a dataframe containing info for all sessions on an assignment
    '''

    return session_info_df.groupby(
        by=[SUBJECT_ID_KEY, ASSIGNMENT_ID_KEY]
        ).agg({
            SESSION_ID_KEY: 'count',
            SESSION_TIME_KEY: 'sum',
            SESSION_START_TIME_KEY: 'first',
            SESSION_END_TIME_KEY: 'last',
            SESSION_KEYSTROKES_KEY: 'sum',
            SESSION_AVG_KEYDIFF_TIME_KEY: 'mean',
        }).rename(
            columns={
                SESSION_ID_KEY: SESSION_COUNT_KEY,
                SESSION_START_TIME_KEY: FIRST_SESSION_START_KEY,
                SESSION_END_TIME_KEY: LAST_SESSION_END_KEY,
                SESSION_TIME_KEY: TOTAL_ASSIGNMENT_TIME_KEY,
                SESSION_KEYSTROKES_KEY: NUMBER_KEYSTROKES_KEY,
                SESSION_AVG_KEYDIFF_TIME_KEY: AVG_KEYDIFF_TIME_KEY
            }).reset_index()
