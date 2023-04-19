import pandas as pd

def getFileInStudentSubmission(df, student, assignment, fileName):
    '''
    Returns a dataframe that shows all submission data for a single file on a given assignment, for a given student

    df - a dataframe of keystroke data
    student - a string representing the SubjectID to filter by
    assignment - a strinng representing the filename to filter by
    fileName - the name of the file to filter by

    Returns a COPY of the dataframe, containing only the selected student, assignment, and file
    '''
    f = df[
          (df.SubjectID == student)
        & (df.AssignmentID == assignment)
        & (df.CodeStateSection == fileName)
        ].copy()
    return f


def getStudentSubmission(df, student, assignment):
    '''
    Returns a dataframe that shows all submission data for all files on a given assignment, for a given student

    df - a dataframe of keystroke data
    student - a string representing the SubjectID to filter by
    assignment - a string representing the filename to filter by
    
    Returns a COPY of the dataframe, containing only the selected student and assignment
    '''
    f = df[
          (df.SubjectID == student)
        & (df.AssignmentID == assignment)
        ].copy()

    return f


def filterDownToRunAndEdits(df):
    '''
    Filter down a dataframe to just have Edit and Run events

    df must be a dataframe of keystroke data. Usually, this dataframe will 
        already be filtered down to be representing a single students 
        submission

    Return a view of a dataframe with just the run and edit events
    '''

    return df[(
            (df.EventType == 'File.Edit')
          | (df.EventType == 'Run.Program')
          )]


def filterDownToRunAndEditsAndPastes(df):
    '''
    Filter down a dataframe to just have Edit, Run, and Paste events

    df must be a dataframe of keystroke data. Usually, this dataframe will 
        already be filtered down to be representing a single students 
        submission

    Return a view of a dataframe with just the run, edit, and paste events
    '''

    return df[(
            (df.EventType == 'File.Edit')
          | (df.EventType == 'Run.Program')
          | (df.EventType == 'X-Paste')
          )]


def getStudentSubmissionRunsAndEdits(df, student, assignment):
    '''
    Returns a dataframe that shows all submission data for a given assignment, for a given student, with only run and edit events

    df - a dataframe of keystroke data
    student - a string representing the SubjectID to filter by
    assignment - a strinng representing the filename to filter by
    '''
    return filterDownToRunAndEdits(getStudentSubmission(df, student, assignment))


def getFileInStudentSubmissionRunsAndEdits(df, student, assignment, fileName):
    '''
    Returns a dataframe that shows all submission data for a single file on a given assignment, for a given student, with only run and edit events

    df - a dataframe of keystroke data
    student - a string representing the SubjectID to filter by
    assignment - a strinng representing the filename to filter by
    fileName - the name of the file to filter by
    '''

    return filterDownToRunAndEdits(getFileInStudentSubmission(df, student, assignment, fileName))
