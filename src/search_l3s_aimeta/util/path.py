import os
# import json

def get_dataset_path(dataset_name):
    dataset_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}")
    return dataset_path


def get_encode_path(encode_type, model_name, dataset_name):
    encode_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{encode_type}/{model_name}/{dataset_name}")
    return encode_path


def get_index_path(type_name, method_name, dataset_name):
    index_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{type_name}/{method_name}/{dataset_name}")
    return index_path