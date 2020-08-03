def request_list_builder(request_ds):
  """
  takes request ids and builds list of request id's sorted from
  largest num of requests to least
  """
  request_list = []
  for req_id in sorted(request_ds, key=request_ds.get, reverse=True):
    request_list.append(req_id)

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