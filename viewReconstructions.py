import pandas as pd

def viewFinalReconstructedProject(reconstructedFiles):
    '''
    View the final file states that get reconstructed

    reconstructedFiles : A dictionary containing filenames as keys and a list
        of said file at various states

    Returns nothing, prints to the console
    '''

    for fileName in sorted(reconstructedFiles.keys()):
        print(40*"=")
        print(f"file = {fileName}")
        print(40*"=")
        print(reconstructedFiles[fileName][-1])


def viewReconstructedProjectStates(reconstructedFiles):
    '''
    View the project at all the different run states that get reconstructed

    reconstructedFiles : A dictionary containing filenames as keys and a list
        of said file at various states

    Returns nothing, prints to the console
    '''
    numberOfStates = len(reconstructedFiles[reconstructedFiles.keys()[0]])

    for stateNo in range(numberOfStates):
        print("v" * 40)
        print(f"Project State : {stateNo if stateNo != numberOfStates - 1 else 'FINAL'}")
        print("^" * 40)
        for fileName in sorted(reconstructedFiles.keys()):
            print(40*"=")
            print(f"file = {fileName}")
            print(40*"=")
            print(reconstructedFiles[fileName][stateNo])
