import pandas as pd

RECONSRUCTION_FAILURES_FILE = 'data/reconstructionFailures.csv'

def getFileReconstructionDF():
    return pd.read_csv(RECONSRUCTION_FAILURES_FILE)


def getProjectReconstructionDF():
    '''
    Get the reconstruction failures, by project
    '''

    failed_reconstruction_df = pd.read_csv(RECONSRUCTION_FAILURES_FILE)
    failed_reconstruction_df = failed_reconstruction_df.groupby(
        ['Student', 'Assignment']
        ).agg({
                'ReconstructionFailure': 'max'
            }).reset_index()
    return failed_reconstruction_df


def getOnlyBadFileReconstructionsDF():
    '''
    Get a dataframe with only the failed file reconstructions

    Return a df containing only the failed reconstructions
    '''

    df = getFileReconstructionDF()
    return df[df.ReconstructionFailure == 1]


def getOnlyBadProjectReconstructionsDF(df=None):
    '''
    Get a dataframe with only the failed project reconstructions

    Return a df containing only the failed reconstructions
    '''

    df = getProjectReconstructionDF()
    return df[df.ReconstructionFailure == 1]


def mergeKeystrokesWithFileReconstructions(keystroke_df):
    '''
    Join the keystrokes dataframe with the file reconstruction dataframe

    The result is a keystrokes dataframe with a new column titled 'ReconstructionFailure'
        If this column contains a 0, that means the file reconstructed correctly
        If this column contains a 1, that means the file reconstrcuted *incorrectly*
        If this column contains a NaN, that means this keystroke was associated with either:
            1. a file that never got reconstructed
            2. a non-file related event
    
    Returns a new dataframe with this extra column
    '''
    reconstruction_df = getFileReconstructionDF()
    reconstruction_df = reconstruction_df.rename(columns={'Student': 'SubjectID', 'Assignment': 'AssignmentID', 'FileName': 'CodeStateSection'})

    return keystroke_df.merge(
        reconstruction_df,
        on=['SubjectID', 'AssignmentID', 'CodeStateSection'],
        how='left'
        ).reset_index()


def mergeKeystrokesWithProjectReconstructions(keystroke_df):
    '''
    Join the keystrokes dataframe with the project reconstruction dataframe

    The result is a keystrokes dataframe with a new column titled 'ReconstructionFailure'
        If this column contains a 0, that means the project reconstructed correctly
        If this column contains a 1, that means the project reconstrcuted *incorrectly*
        If this column contains a NaN, that means this keystroke was associated with a project that never got reconstructed

    Returns a new dataframe with this extra column
    '''

    reconstruction_df = getProjectReconstructionDF()
    reconstruction_df = reconstruction_df.rename(columns={'Student': 'SubjectID', 'Assignment': 'AssignmentID'})

    return keystroke_df.merge(
        reconstruction_df,
        on=['SubjectID', 'AssignmentID'],
        how='left'
        ).reset_index()

def getKeystrokesDFWithoutBadFileReconstructions(keystroke_df):
    '''
    Return a keystrokes dataframe without data for files that were unable to reconstruct correctly

    NOTE: The returned dataframe does NOT have the extra 'ReconstructionFailure' column
    '''

    df = mergeKeystrokesWithFileReconstructions(keystroke_df)

    return df[df.ReconstructionFailure != 1].drop(columns=['ReconstructionFailure'])

def getKeystrokesDFWithoutBadProjectReconstructions(keystroke_df):
    '''
    Return a keystrokes dataframe without data for projects that were unable to reconstruct correctly

    NOTE: The returned dataframe does NOT have the extra 'ReconstructionFailure' column
    '''

    df = mergeKeystrokesWithProjectReconstructions(keystroke_df)

    return df[df.ReconstructionFailure != 1].drop(columns=['ReconstructionFailure'])
