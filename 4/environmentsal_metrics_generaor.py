import itertools

def metric_generator(data_stream):
    for data in data_stream:
        yield {"metric": data * 2, "status": "normal" if data < 50 else "alert"}


stream1 = [20, 30]
stream2 = [50, 60]

combined_streams = itertools.chain(metric_generator(stream1), metric_generator(stream2))

for metric in combined_streams:
    print(metric)
