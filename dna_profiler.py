"""
Module: dna_profiler

A program to use short tandem repeats (STRs) to identify a person using their
DNA.

Authors:
    1) Ethan - ehaug@sandiego.edu
"""

from typing import Tuple, List, Dict


# Write your new functions below this point.
# Recall that all functions need type hints for all parameters and the return,
# AND must have docstrings in the correct format.
def read_dna_sequence(sequence_filename: str) -> str:
    """opens given file, and reads only the first line, strips it, and returns it as a string

        Args: sequence_filename - name of the file we want to read.

        Return: firstLine - the first line of the file. 

    >>> read_dna_sequence('alice.txt')
    'AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA'

    >>> read_dna_sequence('bob.txt')
    'AACCCTGCGCGCGCGCGATCTATCTATCTATCTATCCAGCATTAGCTAGCATCAAGATAGATAGATGAATTTCGAAATGAATGAATGAATGAATGAATGAATG'
    """
    with open(sequence_filename) as file:
        firstLine = file.readline().strip()
    return firstLine


def create_dna_profiles(profile_filename: str) -> tuple[list[str] and dict[str, list[int]]]:
    """Reading through the dna_database file, and organizing each individual's DNA information

        Args: profile_filename - the name of the file we are reading

        Return: dnaProfiles - a dictionary containing the names of the individuals as the keys, and a list of their necleotide patterns
                dnaPatterns - a list of the patterns we are looking out for


        >>> create_dna_profiles('dna_database.csv')
        ({'Alice': ['5', '2', '8'], 'Bob': ['3', '7', '4'], 'Charlie': ['6', '1', '5']}, ['name', 'AGAT', 'AATG', 'TATC'])


    """
    dnaProfiles = {}
    with open(profile_filename) as file:
        name = file.readline().strip()
        dnaPatterns = name.split(',')
        for line in file:
            line = line.strip()
            x = line.split(',')
            dnaProfiles[x[0]] = [x[1], x[2], x[3]]
    return dnaProfiles, dnaPatterns


def find_max_consecutive():

    # keep the following code at the END of your file, as per convention
    if __name__ == "__main__":
        pass
