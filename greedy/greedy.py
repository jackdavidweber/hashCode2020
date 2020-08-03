from setup import *

def greedy_approach(ds):
  req_list = request_list_builder(ds["request_ds"])
  lat_ds = ds["latency_ds"]
  cache_capacity_list = cache_capacity_list_builder(ds["capacity_cache_servers"], ds["num_cache_servers"])
  cache_contents = [ set() for _ in range(ds["num_cache_servers"])]
  
  for req in req_list:
    endpoint_id = req[1]
    for cache_id in lat_ds[endpoint_id]:
      video_id = req[0]
      video_size = ds["video_ds"][video_id]
      cache_remaining_space = cache_capacity_list[cache_id] - video_size
      if (cache_remaining_space >= 0):
        cache_capacity_list[cache_id] = cache_remaining_space
        cache_contents[cache_id].add(video_id)
        break
  
  return cache_contents