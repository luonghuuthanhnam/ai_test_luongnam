import time
import pandas as pd
import json
import random
from source.preprocess_data import PreprocessData
from source.hierarchy_parser import HierarchyRetriever
import timeit

json_file = r"task1\data\bbox_labels_600_hierarchy.json"
csv_file = r"task1\data\oidv6-class-descriptions.csv"
s_time = timeit.default_timer()
preprocessed_data = PreprocessData(json_file, csv_file)
hierarchy_retriever = HierarchyRetriever(preprocessed_data)
print("Total preprocessing time: ", timeit.default_timer() - s_time)


def get_random_class():
    rand_i = random.randint(0, len(preprocessed_data.pair_dict_hierarchy) - 1)
    randome_label_id = list(preprocessed_data.pair_dict_hierarchy.keys())[rand_i]
    return randome_label_id, hierarchy_retriever.get_name(randome_label_id)


def is_exist_labelname(labelname):
    if labelname in list(preprocessed_data.pair_dict_hierarchy.keys()):
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        print(
            "\n\n***************************************************NEWPAGE************************************************\n\n"
        )
        print("hint: type [r] to get a random class LabelName")
        print("Type LabelName you want to check: ...")
        print("exp: /m/01_5g")
        checking_id = str(input())
        if checking_id == "r":
            checking_id, checking_name = get_random_class()
        elif not is_exist_labelname(checking_id):
            print("not exist LabelName, using random LabelName instead")
            checking_id, checking_name = get_random_class()
        else:
            checking_name = hierarchy_retriever.get_name(checking_id)
        # LOOKUP DATA
        # hierarchy_retriever.get_parent("/m/01_5g")

        print(f"Checking [PARENTS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        parents = hierarchy_retriever.get_parent(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Parents: \n", hierarchy_retriever.get_name(parents))
        print("---------------------")
        print()

        # Get Siblings
        print(f"Checking [SIBLINGS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        siblings = hierarchy_retriever.get_siblings(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Siblings: \n", hierarchy_retriever.get_name(siblings))
        print("---------------------")
        print()

        # Get Ancestors
        print(f"Checking [ANCESTORS] of [{checking_name}]...")
        s_time = timeit.default_timer()
        ancestors = hierarchy_retriever.get_ancestors(checking_id)
        print("runing time: ", timeit.default_timer() - s_time)
        print("Ancestors: \n", hierarchy_retriever.get_name(ancestors))
        print("---------------------")
        print()

        print("hint: type [r] to get a random class LabelName")
        print(
            f"Type LabelName you want to check mutual Ancestors with {checking_name}:..."
        )
        print("exp: /m/01lsmm")
        checking_id_2 = str(input())
        if checking_id_2 == "r":
            checking_id_2, checking_name_2 = get_random_class()
        elif not is_exist_labelname(checking_id_2):
            print("not exist LabelName, using random LabelName instead")
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
        print(f"Is Relative: {is_relative}")
        print(f"Mutual Ancestors: \n{hierarchy_retriever.get_name(mutual_ancestors)}")
        print("---------------------")
        print()
