SUBJECT_ID_KEY = 'SubjectID'
ASSIGNMENT_ID_KEY = 'AssignmentID'
MID_SCORE_KEY = 'MID_Score'
INCREMENTAL_KEY = 'Incremental' # boolean key in df, <=2.5 Incremental, >2.5 Non-Incremental
ASSIGNMENT_SCORE_KEY = 'AssignmentScore'
FINAL_SCORE_KEY = 'FinalScore'
CLIENT_TIMESTAMP_KEY = 'ClientTimestamp'

DATE_TIME_KEY = 'DateTime'
NEXT_DATE_TIME_KEY = 'NextDateTime'
DIFF_KEY = 'Diff'
DAYS_DIFF_KEY = 'DaysDiff'
HOURS_DIFF_KEY = 'HoursDiff'
MINUTES_DIFF_KEY = 'MinutesDiff'
SECONDS_DIFF_KEY = 'SecondsDiff'
SESSION_ID_KEY = 'SessionID'
SESSION_TIME_KEY = 'SessionTotalTime' #Swapped from Ms -> S
TOTAL_ASSIGNMENT_TIME_KEY = 'TotalAssignmentTime'#Swapped from Ms -> S


EVENT_TIME_DIFF_KEY = 'EventTimeDiffSeconds' # This is done in seconds
SESSION_START_TIME_KEY = 'SessionStartTime'
SESSION_END_TIME_KEY = 'SessionEndTime'
SESSION_KEYSTROKES_KEY = 'SessionNumberEvents'
SESSION_AVG_KEYDIFF_TIME_KEY = 'SessionAvgEventDiffTime'

SESSION_COUNT_KEY = 'SessionCount'
FIRST_SESSION_START_KEY = 'FirstSessionStart'
LAST_SESSION_END_KEY = 'LastSessionEnd'
NUMBER_EVENTS_KEY = 'NumberEvents'
NUMBER_EVENTS_BEFORE_RUN_KEY = 'NumberEventsBeforeRun'
NUMBER_EVENTS_BEFORE_RUN_IN_SESSION_KEY = NUMBER_EVENTS_BEFORE_RUN_KEY + 'InSession'
NUMBER_EVENTS_AFTER_RUN_KEY = 'NumberEventsAfterRun'
NUMBER_EVENTS_AFTER_RUN_IN_SESSION_KEY = NUMBER_EVENTS_AFTER_RUN_KEY + 'InSession'

AVG_EVENTDIFF_TIME_KEY = 'AvgEventDiffTime'
AVG_TIME_BETWEEN_RUNS_KEY = 'AvgTimeBetweenRuns'
NUMBER_RUNS_KEY = 'NumRuns'
AVG_TIME_PER_RUN_KEY = 'AverageTimePerRun'
NUM_RUNS_PER_ASSIGNMENT_KEY = 'NumRunsPerAssignment'

INSESSION_RUNTIME_DIFF_KEY = 'TimeSinceLastRunInSession'
INSESSION_HAS_RAN_CODE_KEY = 'HasRanCodeInSession'
