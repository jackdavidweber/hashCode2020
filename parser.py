def in_file_to_ds(filename):

    file_input = uploaded["example.in"].decode("utf-8")

    profit_list = []
    weight_list = []
    video_list = []
    capacity_list = []

    pos = 0
    for line in file_input.split('\n'):
    # capacity list
    if pos == 0:
        line_one = line.split(' ')
        capacity = line_one[len(line_one) - 1] 
        num_caches = line_one[len(line_one) - 1]
        for i in num_caches:
        capacity_list.append(int(capacity))

    # weights of videos
    if pos == 1:
        for size in line.split(' '):
        video_list.append(int(size))
    pos += 1
    
    # file in profits and weights
    if len(line.split(' ')) == 3:
        request = line.split(' ')
        video = request[0]
        # add weight of request and profit of request
        weight_list.append(video_list[int(video)])
        profit_list.append(int(request[2]))

    return {
        "weight_list": weight_list,
        "profit_list": profit_list,
        "capacity_list": capacity_list
    }