#!/usr/bin/env bash

SUBMISSIONS_DIRECTORY=reconstructed_submissions

# If you need to overwrite the Python command, change this value
PYTHON_CMD=python

SUCCESS_CODE=0
INDENT_OR_SYNTAX_CODE=1
IMPORT_ERROR_CODE=2
OTHER_ERROR_CODE=3

HEADER="Student,Assignment,FileName,ExecutionState"

echo $HEADER

for STUDENT in $SUBMISSIONS_DIRECTORY/*; do
    
    # Ensure the directory exists
    if [[ ! -d $STUDENT ]]; then
        continue
    fi
    # Get *just* the student name
    STUDENT_ID=${STUDENT/#$SUBMISSIONS_DIRECTORY\/}


    for ASSIGN in $STUDENT/*; do
        # Ensure the directory exists
        if [[ ! -d $ASSIGN ]]; then
            continue
        fi
        # Get *just* the assignment name
        ASSIGN_ID=${ASSIGN/#$STUDENT\/}

        for FILE in $ASSIGN/*; do
            # Ensure the file exists
            if [[ ! -f $FILE ]]; then
                continue
            fi
            # Get *just* the file name
            FILE_ID=${FILE/#$ASSIGN\/}
            
            FILE_EXECUTION_STATE=
            STUDENT_EXECUTION_OUTPUT=$(timeout 1.5 $PYTHON_CMD $FILE 2>&1 > /dev/null)
            SUCCESS=$?

            [[ -n $DEBUG ]] && echo "SUCCESS=$SUCCESS" >&2 && printf "EXECUTION_OUTPUT : \n$STUDENT_EXECUTION_OUTPUT\n" >&2

            # If the file executes and returns 0
            if [[ $SUCCESS == 0 ]]; then
                FILE_EXECUTION_STATE=$SUCCESS_CODE
            elif [[ $SUCCESS == 124 ]]; then
                # Success == 124 indicates that the timeout program quit the program
                FILE_EXECUTION_STATE=$SUCCESS_CODE
            else
                printf "$STUDENT_EXECUTION_OUTPUT\n" | grep -qE '^SyntaxError'
                SYNTAX_ERR=$?
                printf "$STUDENT_EXECUTION_OUTPUT\n" | grep -qE '^IndentationError'
                INDENT_ERR=$?
                printf "$STUDENT_EXECUTION_OUTPUT\n" | grep -qE '^ModuleNotFoundError'
                IMPORT_ERR=$?

                [[ -n $DEBUG ]] && echo "SYNTAX_ERR=$SYNTAX_ERR" >&2
                [[ -n $DEBUG ]] && echo "INDENT_ERR=$INDENT_ERR" >&2
                [[ -n $DEBUG ]] && echo "IMPORT_ERR=$IMPORT_ERR" >&2

                if [[ $SYNTAX_ERR == 0 || $INDENT_ERR == 0 ]]; then
                    FILE_EXECUTION_STATE=$INDENT_OR_SYNTAX_CODE
                elif [[ $IMPORT_ERR == 0 ]]; then
                    FILE_EXECUTION_STATE=$IMPORT_ERROR_CODE
                else
                    FILE_EXECUTION_STATE=$OTHER_ERROR_CODE
                fi
            fi

            printf "$STUDENT_ID,$ASSIGN_ID,$FILE_ID,$FILE_EXECUTION_STATE\n"
        done
    done
done
