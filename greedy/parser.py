
def in_file_to_ds(file_name):
  f = open(file_name, "r") # open file
  totals = f.readline().split()
  num_endpoints = int(totals[1])
  num_request_descs = int(totals[2])
  num_cache_servers = int(totals[3])
  capacity_cache_servers = int(totals[4])
  video_ds = {}
  latency_ds = {}
  request_ds = {}

  # build video ds
  video_ds = video_ds_builder(f.readline())

  # build latency ds
  for endpoint_id in range(0,num_endpoints):
    latency_ds[endpoint_id] = {}
    num_caches = int(f.readline().split()[1])
    for i in range(0, num_caches):
      latency_list = f.readline().split()
      cache_id = int(latency_list[0]) # cache_id
      latency_val = int(latency_list[1])
      latency_ds[endpoint_id][cache_id] = latency_val
  
  # build request ds
  for i in range(0, num_request_descs):
    desc_list = f.readline().split()
    request_id = (int(desc_list[0]), int(desc_list[1])) # (video_id, endpoint_id)
    num_requests = int(desc_list[2])
    request_ds[request_id] = num_requests

  f.close()
  
  return {
      "video_ds": video_ds,
      "latency_ds": latency_ds,
      "request_ds": request_ds,
      "num_cache_servers": num_cache_servers,
      "capacity_cache_servers": capacity_cache_servers
  }



def video_ds_builder(video_line):
  video_list = video_line.split()
  video_ds = {}
  for i in range(0, len(video_list)):
    video_ds[i]= int(video_list[i])

  return video_ds
  