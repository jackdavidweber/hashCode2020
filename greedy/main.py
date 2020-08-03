from parser import in_file_to_ds
from greedy import greedy_approach as approach

def empty_list_counter(lol):
    count = 0
    for l in lol:
        if len(l) == 0:
            count += 1

    return count

def video_str_helper(video_list):
    video_str = ""
    for vid in video_list:
        video_str += " " + str(vid)
    return video_str

def output_helper(lol, filename):
    """
    Takes a list of lists and returns text file with correct output
    """
    file = open(filename, "w")
    file.write(str(empty_list_counter(lol)) + "\n")
    
    for i in range(0, len(lol)):
        file.write(str(i) + video_str_helper(lol[i]) + "\n")

    file.close()



def main():
    ds = in_file_to_ds("in_files/example.in")
    cache_list = approach(ds)
    output_helper(cache_list, "out/example.txt")

main()