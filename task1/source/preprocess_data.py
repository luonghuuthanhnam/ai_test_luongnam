import pandas as pd
import json
import time


class PreprocessData:
    """
    Function:
        Process, restructure data structure to make it easier and faster to parse
        Transform data structure to Dictionary is the best way to get data directly
        Algorithm complexity of get Dictionary is 1, so the Algorithm complexity is O(1)
    """

    def __init__(self, json_file, csv_file):
        """
        Agrs:
            json_file (str): Class hierarchy Json file path
            csv_file (str): label name and display name csv file path
        """
        self.json_hierarchy = json.load(open(json_file))
        self.root_class = self.json_hierarchy["LabelName"]
        self.csv_df = pd.read_csv(csv_file)
        self.csv_df = self.csv_df.set_index("LabelName")
        self.csv_df = self.csv_df.append(
            pd.DataFrame(["Root Entity"], columns=["DisplayName"], index=["/m/0bl9f"])
        )
        self.dict_hierarchy = {}
        self.json2dict_hierarchy(
            self.json_hierarchy["Subcategory"], self.dict_hierarchy
        )
        self.first_classes = list(self.dict_hierarchy.keys())
        self.pair_dict_hierarchy = {}
        self.make_pair(
            self.dict_hierarchy,
            self.pair_dict_hierarchy,
            self.first_classes,
            self.root_class,
        )
        self.pair_dict_hierarchy = self.remove_duplicate_in_pair(
            self.pair_dict_hierarchy
        )

    def json2dict_hierarchy(self, json_hierarchy, dict_hierarchy):
        """
        Agrs:
            json_hierarchy (Json): Classes hierarchy Json Object
            dict_hierarchy (Dictionary): [output] Classes hierarchy Dictionary Object
        Function:
            Convert the Hierarchy from Json object to Dictionary Object.
            Replace the Key "Label_name", "Subcategory" and "Part" by using LabelName value as Key directly
            The values of each Key is subcategories LabelName
        """
        for iter in json_hierarchy:
            dict_hierarchy[iter["LabelName"]] = {}
            if "Subcategory" in list(iter.keys()):
                self.json2dict_hierarchy(
                    iter["Subcategory"], dict_hierarchy[iter["LabelName"]]
                )
            if "Part" in list(iter.keys()):
                self.json2dict_hierarchy(
                    iter["Part"], dict_hierarchy[iter["LabelName"]]
                )

    def make_pair(self, dict_hierarchy, pair_dict_hierarchy, first_classes, parent_key):
        """
        Agrs:
            dict_hierarchy (Dictionary): full or sub classes hierarchy dictionary object
            pair_dict_hierarchy (Dictionary): [output] Flatten Dictionary
            first_classes (List): List of the First level classes of the Hierarchy
            parent_key (Str): Current parent LabelName of child [dict_hierarchy]
        Function:
            Flatten the dict_hierarchy to become one-level dictionary
            Dataset have 601 classes so the output is a dictionary with lenght = 601
            Each pair [Key - Value] is represent to [Child(single value) - Parents(list)]
        """
        for key, val in dict_hierarchy.items():
            if key in first_classes and key not in list(pair_dict_hierarchy.keys()):
                pair_dict_hierarchy[key] = []
                pair_dict_hierarchy[key].append(parent_key)
                self.make_pair(val, pair_dict_hierarchy, first_classes, key)
            else:
                if len(val) == 0:
                    if key not in list(pair_dict_hierarchy.keys()):
                        pair_dict_hierarchy[key] = []
                    else:
                        pass
                    pair_dict_hierarchy[key].append(parent_key)
                else:
                    if key not in list(pair_dict_hierarchy.keys()):
                        pair_dict_hierarchy[key] = []
                    pair_dict_hierarchy[key].append(parent_key)
                    self.make_pair(val, pair_dict_hierarchy, first_classes, key)

    def remove_duplicate_in_pair(self, pair_dict_hierarchy):
        """
        Agrs:
            pair_dict_hierarchy (Dictionary): dict_hierarchy has been flatten
        Function:
            drop duplicated data point
        """
        temp_dict = pair_dict_hierarchy.copy()
        for key, val in temp_dict.items():
            temp_dict[key] = list(set(val))
        return temp_dict
