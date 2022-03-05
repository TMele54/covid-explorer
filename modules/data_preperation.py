import json
from modules.data_definitions import countries
from modules.data_definitions import meta
from modules.data_definitions import metrics

data_pth = "data/source/owid-covid-data.json"
_data_pth = "data/prepped/covid-data.json"

countries = countries()
meta = meta()
metrics = metrics()

# include these countries, meta, and metrics (always include data in meta)
includes = {
    "countries": [k for k, v in countries.items() if v == True],
    "meta": [k for k, v in meta.items() if v == True],
    "metrics":  [k for k, v in metrics.items() if v == True],
}

def open_data(file_name):
    file = open(file_name)
    data = json.load(file)
    file.close()

    return data
def filter_data(includes, input_data):
    data=dict()
    output=list()

    # Filter Countries
    records = {k: v for k, v in input_data.items() if k in includes["countries"]}

    # Filter Meta
    for ct in records.keys():
        data[ct] = {k: v for k, v in records[ct].items() if k in includes["meta"]}

    # Filter Metrics
    for ct in data:
        _data=dict()
        _data['country'] = ct

        for meta in data[ct].keys():
            if meta == 'data':
                _data[meta] = list()
            else:
                _data[meta] = data[ct][meta]

        for these in data[ct]["data"]:
            _data["data"].append({k: v for k, v in these.items() if k in includes["metrics"]})

        output.append(_data)

    return output
def save_data(data, file_name):
    f = open(file_name, "w")
    json.dump(data, f)
    f.close()
    return True

print("Opening Data")
data = open_data(data_pth)

print("Filter Data")
filtered_data = filter_data(includes=includes, input_data=data)

print("Save Data")
confirma = save_data(data=filtered_data, file_name=_data_pth)

print(confirma)