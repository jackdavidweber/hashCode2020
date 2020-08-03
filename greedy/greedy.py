from setup import *

def greedy_approach(ds):
  req_list = request_list_builder(ds["request_ds"])
  lat_list = latency_list_builder(ds["latency_ds"])
  cache_capacity_list = cache_capacity_list_builder(ds["capacity_cache_servers"], ds["num_cache_servers"])
  cache_contents = [ [] for _ in range(ds["num_cache_servers"])]

  for req in req_list:
    for lat in lat_list:
      cache_endpoint_id = lat[0]
      req_endpoint_id = req[1]
      cache_id = lat[1]
      video_id = req[0]
      video_size = ds["video_ds"][video_id]
      cache_remaining_space = cache_capacity_list[cache_id] - video_size
      if (cache_remaining_space >= 0 and cache_endpoint_id == req_endpoint_id):
        # check to make sure video is not already stored in cache
        if (video_id not in cache_contents[cache_id]):
          cache_capacity_list[cache_id] = cache_remaining_space
          cache_contents[cache_id].append(video_id)
          break
  
  return cache_contents