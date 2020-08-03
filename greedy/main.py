from parser import in_file_to_ds
from greedy import greedy_approach as approach

def non_empty_list_counter(lol):
    count = 0
    for l in lol:
        if len(l) != 0:
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
    file.write(str(non_empty_list_counter(lol)) + "\n")
    
    for i in range(0, len(lol)):
        video_list = lol[i]
        if len(video_list) > 0:
            file.write(str(i) + video_str_helper(video_list) + "\n")

    file.close()



def main():
    file_names = ["example", "learning_cooking_from_youtube", "me_working_from_home", "music_videos_of_2020", "vloggers_of_the_world"]
    for file in file_names:
        print(file)
        in_file = "in_files/" + file + ".in"
        out_file = "out_files/" + file + ".txt"

        ds = in_file_to_ds(in_file)
        cache_list = approach(ds)
        output_helper(cache_list, out_file)

main()