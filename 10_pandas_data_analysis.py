import pandas as pd



def get_max_exchange_usd_per_year(**kwargs):
    df = pd.read_csv(kwargs["file_path"])
    df_crisis = df[['exch_usd','country', 'banking_crisis','year']][(df['banking_crisis']=='crisis') & (df['year']>=1900)].groupby(['country','banking_crisis']).agg('max')
    pivoted_dict = df_crisis.reset_index().pivot(index='country',columns='banking_crisis', values=['exch_usd','year']).to_dict()
    flattened_dict = flatten_dict(pivoted_dict)
    result_list = [f"{k} had {v}" for k,v in flattened_dict.items() if k.lower() in kwargs["countries"]]
    return result_list


def flatten_dict(pivoted_dict):
    exch_usd = pivoted_dict[('exch_usd', 'crisis')]
    year = pivoted_dict[('year', 'crisis')]
    result_dict = {}
    for (k, v), (k1, v1) in zip(exch_usd.items(), year.items()):
        if k == k1:
            result_dict.update({k: f"exch_usd {v} in crisis year {v1}"})
    return result_dict

print(get_max_exchange_usd_per_year(file_path='african_crises.csv', countries=['south africa','nigeria']))



