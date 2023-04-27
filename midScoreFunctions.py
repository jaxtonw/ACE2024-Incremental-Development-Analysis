from projectConstants import *
import pandas as pd

from measure_incremental_development.compute import calculate_mid, classify_snapshots


def remove_empty_at_start(file_states):
    '''
    Function to remove empty strings at beginning of list

    file_states: list of file states

    returns a clean list
    '''
    index = -1
    for i in range(len(file_states)):
        if file_states[i] != '':
            index = i
            break
    if index > -1:
        return file_states[index:]
    return file_states


def get_scores(student, assignment, student_df):
    '''
    Get the score the student got on the specified student

    student: a string representing the SubjectID
    assignment: a string representing the Assignment
    student_df: a df containing the students grades

    Returns: a dictionary of the student's score for the specified assignment, 
    and final score
    None if there is no 
    '''
    # TODO Maybe we want to add more scores, we can do that here
    scores = dict()
    if student in student_df[SUBJECT_ID_KEY].unique():
        row_loc = student_df.loc[student_df[SUBJECT_ID_KEY] == student]
        if assignment in row_loc:
            scores[ASSIGNMENT_SCORE_KEY] = row_loc[assignment].values[0]
            scores[FINAL_SCORE_KEY] = row_loc[FINAL_SCORE_KEY].values[0]
    return scores


def get_mid_score_row(student, assignment, mid_score, student_df):
    '''
    Get a dictionary containing necessary information to build a row
    in the student dataframe with MID score
    
    student - a string representing the SubjectID to filter by
    assignment - a strinng representing the filename to filter by
    file - the name of the file in assignment
    
    Returns: A dictionary containing student, assignment, file, mid score
    and whether or not the returned score is incremental or not
    '''
    scores = get_scores(student, assignment, student_df)
    return {
        SUBJECT_ID_KEY: student,
        ASSIGNMENT_ID_KEY: assignment,
        MID_SCORE_KEY: mid_score,
        ASSIGNMENT_SCORE_KEY: scores[ASSIGNMENT_SCORE_KEY],
        FINAL_SCORE_KEY: scores[FINAL_SCORE_KEY],
        INCREMENTAL_KEY: 0 if mid_score > 2.5 else 1
    }


def get_mid_score_all(final_data, student_df):
    '''
    Creates a dataframe for a student, assignment, mid score, final score, 
    assignment score and the incremental information

    final_data - multiple tuples containing a single student, for a single assignment, 
        and file states.

    student_df - a dataframe containing student grade data and demographics information 

    Returns: A dataframe for all specified student containing the mid score
    and whether or not the student used incremental development
    '''
    mid_score_df = pd.DataFrame()
    for student, assignment, file_states in final_data:
        new_file_states = {}
        for file_name in file_states:
            # Filtering out 'bad' filenames
            if not file_name.endswith('.py') or '.txt' in file_name.lower() or 'plan' in file_name.lower() or 'main' in file_name.lower():
                print(f"filtering out file {file_name}")
                continue
            new_file_states[file_name] = file_states[file_name]
        file_states = new_file_states

        if len(file_states) == 0:
            continue
        all_file_states = []
        for _, state in file_states.items():
            clean_state = remove_empty_at_start(state)
            all_file_states += clean_state
        try:
            mid_score = calculate_mid(all_file_states)
            row = pd.DataFrame(get_mid_score_row(student, assignment, mid_score, student_df), index=[0])
            mid_score_df = pd.concat([mid_score_df, row], ignore_index=True)
        except Exception as e:
            print("Failed for student. Error:", e)
            print(len(all_file_states))
    return mid_score_df
