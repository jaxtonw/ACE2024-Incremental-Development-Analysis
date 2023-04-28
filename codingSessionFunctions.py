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
        # We do not want any X-Attention or X-Keystroke events, or Editor Close Actions
          ~ (
              ( df.EventType == 'X-Attention' )
            | ( df.EventType == 'X-Keystroke' ) # X-Keystrokes are essentially duplicates of edits with some fickle-behaviors
            | ( ( df.EventType == 'X-Action' ) & (df['X-Metadata'] == 'Close Active Editor') )
          )
        )
        ].copy()

    assnSessionDf[DATE_TIME_KEY] = pd.to_datetime(assnSessionDf.ClientTimestamp, unit='ms') 
    assnSessionDf[SESSION_ID_KEY] = -1
    assnSessionDf[EVENT_TIME_DIFF_KEY] = np.NaN
    assnSessionDf[INSESSION_RUNTIME_DIFF_KEY] = np.NaN
    assnSessionDf[INSESSION_HAS_RAN_CODE_KEY] = 0

    # sort by timestamp
    assnSessionDf.sort_values(by=DATE_TIME_KEY, inplace=True)

    if assnSessionDf.size > 0:
        lastEventTime = assnSessionDf.head(1)[DATE_TIME_KEY].values[0]
        lastRunTime = lastEventTime

    # 5 minutes from last event, not start of the session
    sessionId = 0
    hasRanCodeInSession = 0

    for i, row in assnSessionDf.iterrows():
        diff = row[DATE_TIME_KEY] - lastEventTime
        minutes_diff = diff.total_seconds() / 60

        if minutes_diff > 5:
            sessionId += 1
            lastRunTime = row[DATE_TIME_KEY]
            hasRanCodeInSession = 0
            # assnSessionDf.at[i, EVENT_TIME_DIFF_KEY] = np.NaN
        else:
            # If this event is still part of the same coding session, we note the diff time
            # If it's not, leave it as NaN
            assnSessionDf.at[i, EVENT_TIME_DIFF_KEY] = diff.total_seconds()

        assnSessionDf.at[i, INSESSION_RUNTIME_DIFF_KEY] = (row[DATE_TIME_KEY] - lastRunTime).total_seconds()
        assnSessionDf.at[i, INSESSION_HAS_RAN_CODE_KEY] = hasRanCodeInSession
        if row.EventType == 'Run.Program' and row['X-Metadata'] == 'Start':
            hasRanCodeInSession = 1
            # Compute time since last run in this session
            lastRunTime = row[DATE_TIME_KEY]

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
    sessionAvgEventDiffTime = []
    sessionNumEventsBeforeRun = []
    sessionNumEventsAfterRun = []
    sessionNumRuns = []
    sessionAvgTimeBetweenRuns = []

    for sessionId in allSessionIds:
        # Reduce df down to just this session
        sessionDf = df[(df[SESSION_ID_KEY] == sessionId)].copy()
        # sort by dates just in case
        sessionDf.sort_values(by=DATE_TIME_KEY, inplace=True)

        startTime = sessionDf.head(1)[CLIENT_TIMESTAMP_KEY].values[0]
        endTime = sessionDf.tail(1)[CLIENT_TIMESTAMP_KEY].values[0]
        # subtract start session time and end session time to get total session time
        lengthTime = endTime - startTime


        # Get Only Run Events
        runEvents = sessionDf[(sessionDf.EventType == 'Run.Program') & (sessionDf['X-Metadata'] == 'Start')]
        avgTimeBetweenRuns = runEvents[INSESSION_RUNTIME_DIFF_KEY].mean()

        avgEventDiffTime = sessionDf[EVENT_TIME_DIFF_KEY].mean()

        eventsBeforeRun = sessionDf[sessionDf[INSESSION_HAS_RAN_CODE_KEY] == 0]
        eventsAfterRun = sessionDf[sessionDf[INSESSION_HAS_RAN_CODE_KEY] == 1]



        # Add all data for this session to a list
        sessionIdsColumn.append(sessionId)
        sessionStartTimes.append(startTime)
        sessionEndTimes.append(endTime)
        sessionLengths.append(lengthTime)
        sessionNumEvents.append(len(sessionDf))
        sessionNumEventsBeforeRun.append(len(eventsBeforeRun))
        sessionNumEventsAfterRun.append(len(eventsAfterRun))
        sessionAvgEventDiffTime.append(avgEventDiffTime)
        sessionNumRuns.append(len(runEvents))
        sessionAvgTimeBetweenRuns.append(avgTimeBetweenRuns)

    return pd.DataFrame(
        {
            SUBJECT_ID_KEY: studentSessionID,
            ASSIGNMENT_ID_KEY: assnSessionID,
            SESSION_ID_KEY: sessionIdsColumn,
            SESSION_START_TIME_KEY: sessionStartTimes,
            SESSION_END_TIME_KEY: sessionEndTimes,
            SESSION_TIME_KEY: sessionLengths,
            NUMBER_EVENTS_KEY: sessionNumEvents,
            NUMBER_EVENTS_BEFORE_RUN_KEY: sessionNumEventsBeforeRun,
            NUMBER_EVENTS_AFTER_RUN_KEY: sessionNumEventsAfterRun,
            AVG_EVENTDIFF_TIME_KEY: sessionAvgEventDiffTime,
            NUMBER_RUNS_KEY: sessionNumRuns,
            AVG_TIME_BETWEEN_RUNS_KEY: sessionAvgTimeBetweenRuns,
        }
    )


def condenseCodingSessions(session_info_df, allCodingSessionsDf):
    '''
    Convert a dataframe containing individual session info into a dataframe containing info for all sessions on an assignment
    '''

    allCodingSessionsDf[SUBJECT_ID_KEY].append(
        session_info_df[SUBJECT_ID_KEY].head(1).values[0]
    )
    allCodingSessionsDf[ASSIGNMENT_ID_KEY].append(
        session_info_df[ASSIGNMENT_ID_KEY].head(1).values[0]
    )
    allCodingSessionsDf[SESSION_COUNT_KEY].append(
        session_info_df[SESSION_ID_KEY].count()
    )
    allCodingSessionsDf[TOTAL_ASSIGNMENT_TIME_KEY].append(
        session_info_df[SESSION_TIME_KEY].sum()
    )
    allCodingSessionsDf[NUMBER_EVENTS_KEY].append(
        session_info_df[NUMBER_EVENTS_KEY].sum()
    )
    allCodingSessionsDf[NUMBER_EVENTS_BEFORE_RUN_IN_SESSION_KEY].append(
        session_info_df[NUMBER_EVENTS_BEFORE_RUN_KEY].sum()
    )
    allCodingSessionsDf[NUMBER_EVENTS_AFTER_RUN_IN_SESSION_KEY].append(
        session_info_df[NUMBER_EVENTS_AFTER_RUN_KEY].sum()
    )
    allCodingSessionsDf[NUMBER_RUNS_KEY].append(
        session_info_df[NUMBER_RUNS_KEY].sum()
    )
    allCodingSessionsDf[FIRST_SESSION_START_KEY].append( 
        session_info_df.head(1)[SESSION_START_TIME_KEY].values[0]
    )
    allCodingSessionsDf[LAST_SESSION_END_KEY].append(
        session_info_df.tail(1)[SESSION_END_TIME_KEY].values[0]
    )
    allCodingSessionsDf[AVG_EVENTDIFF_TIME_KEY].append(
        session_info_df[AVG_EVENTDIFF_TIME_KEY].mean()
    )
    allCodingSessionsDf[AVG_TIME_BETWEEN_RUNS_KEY].append(
        session_info_df[AVG_TIME_BETWEEN_RUNS_KEY].mean()
    )


def getCodingSessionsDf(keystroke_df, final_data):
    '''
    Get coding session for each student and assignment, where coding session is events within 5 minutes
    
    Returns a dataframe containing an entry for each unique coding session
    '''

    individualCodingSessionDf = pd.DataFrame()
    allCodingSessionsDf = {
        SUBJECT_ID_KEY: [],
        ASSIGNMENT_ID_KEY: [],
        SESSION_COUNT_KEY : [],
        TOTAL_ASSIGNMENT_TIME_KEY: [],
        NUMBER_EVENTS_KEY: [],
        NUMBER_EVENTS_BEFORE_RUN_IN_SESSION_KEY: [],
        NUMBER_EVENTS_AFTER_RUN_IN_SESSION_KEY: [],
        NUMBER_RUNS_KEY: [],
        FIRST_SESSION_START_KEY: [],
        LAST_SESSION_END_KEY: [],
        AVG_EVENTDIFF_TIME_KEY: [],
        AVG_TIME_BETWEEN_RUNS_KEY: [],
    }



    for student, assignment, _ in final_data:

        # Get a dataframe with keystroke info for this (student,assignment), marked by coding sessions
        codingSessionAssignmentDf = markEventsByCodingSessions(keystroke_df, student, assignment)

        # Compute info for each coding session
        oneCodingSessionInfoDf = getIndividualSessionInfo(codingSessionAssignmentDf)

        if oneCodingSessionInfoDf is None:
            continue


        individualCodingSessionDf = pd.concat([individualCodingSessionDf, oneCodingSessionInfoDf], ignore_index=True)
        condenseCodingSessions(oneCodingSessionInfoDf, allCodingSessionsDf)

    return individualCodingSessionDf, pd.DataFrame(allCodingSessionsDf)
