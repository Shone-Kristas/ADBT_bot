import bson
import datetime
from collections import defaultdict


def search_data_by_time(data_search, time_format):
    file_path = 'sampleDB/sample_collection.bson'
    with open(file_path, 'rb') as file:
        data = bson.decode_all(file.read())

    min_time = datetime.datetime.strptime(data_search["dt_from"], "%Y-%m-%dT%H:%M:%S")
    max_time = datetime.datetime.strptime(data_search["dt_upto"], "%Y-%m-%dT%H:%M:%S")
    time_values = defaultdict(int)

    current_time = min_time
    if time_format != "%Y-%m":
        while current_time <= max_time:
            time_label = current_time.strftime(time_format)
            time_values[time_label] = 0
            if time_format == "%Y-%m-%d":
                current_time += datetime.timedelta(days=1)
            elif time_format == "%Y-%m-%dT%H":
                current_time += datetime.timedelta(hours=1)

    for document in data:
        document_time = document["dt"]
        if min_time <= document_time <= max_time:
            time_label = document_time.strftime(time_format)
            time_values[time_label] += document["value"]

    response = {
        "dataset": list(time_values.values()),
        "labels": [datetime.datetime.strptime(label, time_format).isoformat() for label in sorted(time_values.keys())]
    }
    return response


def search_per_month(data_search):
    return search_data_by_time(data_search, "%Y-%m")


def search_per_day(data_search):
    return search_data_by_time(data_search, "%Y-%m-%d")


def search_per_hour(data_search):
    return search_data_by_time(data_search, "%Y-%m-%dT%H")



def aggregation(data_search):
    if data_search["group_type"] == "month":
        return search_per_month(data_search)
    elif data_search["group_type"] == "day":
        return search_per_day(data_search)
    elif data_search["group_type"] == "hour":
        return search_per_hour(data_search)