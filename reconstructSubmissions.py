import pandas as pd

def reconstructSingleFileDebugger(df):
    '''
    See a submission as it gets reconstructed, ignoring the Run events

    This is used primarily for debugging
    '''

    s = ''

    fileStateCount = 0
    for _,row in df[df.EventType=='File.Edit'].iterrows():
        i = int(row.SourceLocation)
        fileLengthRn = len(s)
        if i > fileLengthRn:
            print("DEBUG: Woah buddy, your cursor is out of bounds")


        insert = '' if pd.isna(row.InsertText) else row.InsertText
        delete = '' if pd.isna(row.DeleteText) else row.DeleteText
        s = s[:i] + insert + s[i+len(delete):]

        print(f"""\
================
StateNo : {fileStateCount}
{i=}
{insert=}
{delete=}
{row.EventID=}
================
{s}
""")
        fileStateCount += 1

    return s


def reconstructFinalFile(df):
    '''
    Reconstruct a single file

    df - A dataframe containing a single student, for a single assignment, 
            and a single file of that assignment

    Returns: A string representing the final state of the file
    '''

    s = ''

    for _,row in df[df.EventType=='File.Edit'].iterrows():
        i = int(row.SourceLocation)

        insert = '' if pd.isna(row.InsertText) else row.InsertText
        delete = '' if pd.isna(row.DeleteText) else row.DeleteText
        s = s[:i] + insert + s[i+len(delete):]
    
    return s


def reconstructFileAtRunEvents(df):
    '''
    Reconstruct a single file and save it's state at different run events

    df - A dataframe containing a single student, for a single assignment, 
            and a single file of that assignment. Must have edit events and run events

    Returns: A list containing strings representing the various states of the file at different run events
    '''

    fileStateAtRuns = []

    s = ''

    for _,row in df.iterrows():
        if row.EventType == 'File.Edit':
            i = int(row.SourceLocation)

            insert = '' if pd.isna(row.InsertText) else row.InsertText
            delete = '' if pd.isna(row.DeleteText) else row.DeleteText
            s = s[:i] + insert + s[i+len(delete):]
        elif row.EventType == 'Run.Program':
            fileStateAtRuns.append(s)

    fileStateAtRuns.append(s)

    return fileStateAtRuns


def reconstructProjectAtRunEvents(df):
    '''
    Reconstruct a whole project and save it's state at different run events

    df - A dataframe containing a single student, for a single assignment, 
            and one+ files. Must have edit events and run events

    Returns: A dictionary containing keys for each file name, with values that are a list
                of strings, representing each file state at different run events

    NOTE: Some files may always be empty in their states. This happens when students make meaningful 
            edits to files, but delete it's contents before running their code
    '''

    # Remove NaN edit events to ensure that only meaningful edits are logged
    df = df[
          ( df.EventType != 'File.Edit' )
          | ( ( df.EventType == 'File.Edit' )
            & ~ ( ( pd.isna(df.InsertText) ) 
                & ( pd.isna(df.DeleteText) ) 
                )
              )
        ]

    allFileNames = df.CodeStateSection.unique()
    
    fileStates = dict()
    currentFileContents = dict()
    # Setup the fileStates dictionary for every file and the currentFileContents for each file
    for fileName in allFileNames:
        fileStates[fileName] = []
        currentFileContents[fileName] = ''

    for _,row in df.iterrows():
        if row.EventType == 'File.Edit':
            # Get the name of the file that was just edited
            thisFileName = row.CodeStateSection

            # Get edit information
            i = int(row.SourceLocation)
            insert = '' if pd.isna(row.InsertText) else row.InsertText
            delete = '' if pd.isna(row.DeleteText) else row.DeleteText

            # Make the edit and save the current state of the file
            s = currentFileContents[thisFileName]
            s = s[:i] + insert + s[i+len(delete):]
            currentFileContents[thisFileName] = s
            
        elif row.EventType == 'Run.Program':
            # Save all files at their current states

            # We only want to save when a run is started
            if row['X-Metadata'] != 'Start': continue

            for fileName in allFileNames:
                # Adding this extra newline causes the calculate_mid function to not crash
                #   Adding a single newline shouldn't affect the midscore significantly, but it does seem to have a notable affect
                fileStates[fileName].append(currentFileContents[fileName] + "\n")

    # Save all files at their final states
    for fileName in allFileNames:
        fileStates[fileName].append(currentFileContents[fileName])

    return fileStates
