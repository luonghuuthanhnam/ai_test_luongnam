import time
import pandas as pd
import json
import random
from source.preprocess_data import PreprocessData
from source.hierarchy_parser import HierarchyRetriever
import timeit

JSON_FILE = r"task1\data\bbox_labels_600_hierarchy.json"
CSV_FILE = r"task1\data\oidv6-class-descriptions.csv"
RANDOM_CHOICE_KEYWORD = "r"

s_time = timeit.default_timer()
preprocessed_data = PreprocessData(JSON_FILE, CSV_FILE)
hierarchy_retriever = HierarchyRetriever(preprocessed_data)
print("Total preprocessing time: ", timeit.default_timer() - s_time)


def get_random_class():
    print(
        "\n[WARNING] Your specification does not exist LabelName. Use random LabelName instead",
        end="\n\n",
    )
    random_label_id = random.choice(list(preprocessed_data.pair_dict_hierarchy.keys()))
    return random_label_id, hierarchy_retriever.get_name(random_label_id)


def is_exist_labelname(labelname):
    return labelname in preprocessed_data.pair_dict_hierarchy


if __name__ == "__main__":
    while True:
        print(
            "\n\n***************************************************NEW PAGE************************************************\n\n"
        )
        checking_id = input(
            "[INSTRUCTION] \n"
            "Type LabelName that you want to check (For example: /m/01_5g)\n"
            f"Press [{RANDOM_CHOICE_KEYWORD}] to randomly pick out of the existing labels \n"
            "Your input:  "
        ).strip()
        if checking_id == RANDOM_CHOICE_KEYWORD or not is_exist_labelname(checking_id):
            checking_id, checking_name = get_random_class()
        else:
            checking_name = hierarchy_retriever.get_name(checking_id)
        # LOOKUP DATA

        print(f"Checking [PARENTS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        parents = hierarchy_retriever.get_parent(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Parents: \n", hierarchy_retriever.get_name(parents))
        print("---------------------", end="\n\n")

        # Get Siblings
        print(f"Checking [SIBLINGS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        siblings = hierarchy_retriever.get_siblings(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Siblings: \n", hierarchy_retriever.get_name(siblings))
        print("---------------------", end="\n\n")

        # Get Ancestors
        print(f"Checking [ANCESTORS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        ancestors = hierarchy_retriever.get_ancestors(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Ancestors: \n", hierarchy_retriever.get_name(ancestors))
        print("---------------------", end="\n\n")

        checking_id_2 = input(
            "[INSTRUCTION] \n"
            "Type LabelName that you want to check mutual Ancestors with {checking_name} (For example: /m/01lsmm)\n"
            f"Press [{RANDOM_CHOICE_KEYWORD}] to randomly pick out of the existing labels \n"
            "Your input:  "
        ).strip()

        if checking_id_2 == RANDOM_CHOICE_KEYWORD or not is_exist_labelname(
            checking_id_2
        ):
            checking_id_2, checking_name_2 = get_random_class()
        else:
            checking_name_2 = hierarchy_retriever.get_name(checking_id_2)
        # Find if both class 1 and class 2 belong to the same ancestor class(es)
        print(
            f"Checking [{checking_name}] and [{checking_name_2}] belong to the same ancestor..."
        )
        s_time = timeit.default_timer()
        is_relative, mutual_ancestors = hierarchy_retriever.check_same_ancestors(
            checking_id, checking_id_2
        )
        print("runing time: ", timeit.default_timer() - s_time)
        print(
            f"Is Releative: {is_relative}\n"
            f"Mutual Ancestors: \n{hierarchy_retriever.get_name(mutual_ancestors)}"
            "---------------------",
            end="\n\n",
        )
