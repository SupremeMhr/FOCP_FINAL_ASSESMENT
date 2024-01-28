import sys
# This function displays the analysis results
def show_analysis_results(their_cat_count, our_cat_count, total_minute, longest_visit_time, shortest_visit_time):
    """
    Display the analysis results based on cat visits and total time stayed.

    Args:
        their_cat_count (int): Count of visits by other cats.
        our_cat_count (int): Count of visits by our cat.
        total_minute (int): Total time spent by our cat in minutes.
        longest_visit_time (int): Duration of the longest visit in minutes.
        shortest_visit_time (int): Duration of the shortest visit in minutes.
    """
    print("\nLog File Analysis")
    print("===================")
    print(f"\nCat Visits: {our_cat_count}")
    print(f"Other Cats: {their_cat_count}")
    print(f"\nTotal Time in House: {total_minute // 60} Hours, {total_minute % 60} Minutes")
    print(f"\nAverage Visit Length: \t{total_minute // our_cat_count} Minutes")
    print(f"Longest Visit:\t\t{longest_visit_time} Minutes")
    print(f"Shortest Visit:\t\t{shortest_visit_time} Minutes")
    
def main():#main function
    their_cat_count = 0
    our_cat_count = 0
    total_minute = 0
    longest_visit_time = 0
    shortest_visit_time = float('inf')
    try:
        log_file = sys.argv[1]
        with open(log_file, "r") as log_file:
            data = log_file.readlines()
            for line in data:
                word = line.strip().split(',')
                if word[0] == 'THEIRS':
                    their_cat_count += 1
                elif word[0] == 'OURS':
                    our_cat_count += 1
                    time_stayed = int(word[2]) - int(word[1])
                    total_minute += time_stayed

                    if time_stayed > longest_visit_time:
                        longest_visit_time = time_stayed
                    if time_stayed < shortest_visit_time:
                        shortest_visit_time = time_stayed
    
        show_analysis_results(their_cat_count, our_cat_count, total_minute, longest_visit_time, shortest_visit_time)#calling the function
    # This Handles exceptions
    except IndexError:
        print("Missing command line argument!")
    except FileNotFoundError:
        print(f"Cannot open '{log_file}'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#calls the main function
if __name__ == '__main__':
    main()

