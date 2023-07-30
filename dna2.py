import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/FILENAME.csv sequences/FILENAME.txt")

    # TODO: Read database file into a variable

    filename = sys.argv[1]
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # TODO: Read DNA sequence file into a variable
    filename2 = sys.argv[2]
    dna = []
    with open(filename2, 'r') as file2:
        for line in file2:
            dna.append(line.strip())

    # TODO: Find longest match of each STR in DNA sequence
    longest_matches = {}
    for dictionary in data:
        for key, value in dictionary.items():
            if key != 'name':
                str_length = longest_match(dna, value)
                longest_matches[key] = str_length


    # TODO: Check database for matching profiles
    check_matching_profiles(data, longest_matches)

    return longest_matches


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

def check_matching_profiles(data, longest_matches):
    # Iterate through each profile in the database
    for profile in data:
        match = True # Flag to track if the profile matches the DNA sequence

        # Iterate through each STR and its longest match in the DNA sequence
        for str_name, longest in longest_matches.items():
            # Check if the longest match in the DNA sequence matches the profile's value
            if int(profile[str_name]) != longest:
                match = False
                break

        # If all STR matches, print the profile's name as a match
        if match:
            print(profile['name'])


if __name__ == '__main__':
    main()
