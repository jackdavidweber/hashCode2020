def request_list_builder(request_ds, lat_ds, endpoint_from_datacenter):
  """
  takes request ids and builds list of request id's sorted from
  largest num of requests to least
  """
  avg_dif = {}

  for endpoint, caches in lat_ds.items():
    min_latency = 10000000000000
    num_caches = 0
    for cache, latency in caches.items():
      if latency < min_latency:
        min_latency = latency
      num_caches += 1
    if num_caches > 0:
      avg_dif[endpoint] = endpoint_from_datacenter[endpoint] - min_latency
    else:
      avg_dif[endpoint] = endpoint_from_datacenter[endpoint]

  sorted_avg_dif = sorted(avg_dif.items(), key=lambda x: x[1], reverse=True)
  sorted_request_ds = sorted(request_ds.items(), key=lambda x: x[1], reverse=True)
  request_list = []
  for pair in sorted_avg_dif:
    requests = [key[0] for key in sorted_request_ds if key[0][1]== pair[0]]
    for elem in requests:
      request_list.append(elem)

  #for req_id in sorted(request_ds, key=request_ds.get, reverse=True):
  #  request_list.append(req_id)
  return request_list


def latency_list_builder(latency_ds):
  """
  takes latency ids and builds list of latency id's sorted from
  lowest to highest latency
  """
  latency_list = []
  for lat_id in sorted(latency_ds, key=latency_ds.get, reverse=False):
    latency_list.append(lat_id)

  return latency_list


def cache_capacity_list_builder(capacity_cache_server, num_cache_servers):
  cache_capacity_list = []
  for i in range(0, num_cache_servers):
    cache_capacity_list.append(capacity_cache_server)

  return cache_capacity_list