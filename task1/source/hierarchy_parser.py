class HierarchyRetriever:
    """
    Function:
        Retrieve expected data by using preprocessed data
        Combine retrieve dictionary method and recursion to get the expected data
    """

    def __init__(self, preprocessed_data):
        """
        Args:
            preprocessed_data (PreprocessData): object of PreprocessData class
        """
        self.preprocessed_data = preprocessed_data

    def get_name(self, label_id):
        """
        Args:
            label_id (Str): LabelName of a class
        Return:
            Display Name (Str)
        """
        return self.preprocessed_data.csv_df.loc[label_id, "DisplayName"]

    def get_parent(self, label_id):
        """
        Args:
            label_id (Str): LabelName of a class
        Return:
            Parents LabelName (List)
        """
        return self.preprocessed_data.pair_dict_hierarchy[label_id].copy()

    def ancestors_recursion(self, child_class, ancestors):
        """
        Args:
            child_class (Str): LabelName of ancestors checked class
            ancestors (List): [output] ancestors LabelName save to this list
        """
        parent_ids = self.get_parent(child_class)
        for parent_id in parent_ids:
            if parent_id != "/m/0bl9f":
                ancestors.append(parent_id)
                self.ancestors_recursion(parent_id, ancestors)
            else:
                pass

    def get_ancestors(self, child_class):
        """
        Args:
            child_class (Str): LabelName of ancestors checked class
        Return:
            ancestors (List): List of all ancestors LabelName
        """
        ancestors = []
        self.ancestors_recursion(child_class, ancestors)
        return list(set(ancestors))

    def get_siblings(self, child_class):
        """
        Args:
            child_class (Str): LabelName of ancestors checked class
        Return:
            siblings (List): List of all siblings LabelName
        """
        siblings = []
        parents = self.get_parent(child_class)
        print(parents)
        if "/m/0bl9f" in parents:
            parents.remove("/m/0bl9f")
        parents_as_set = set(parents)
        for key, val in self.preprocessed_data.pair_dict_hierarchy.items():
            intersection = parents_as_set.intersection(val)
            list_intersection = list(intersection)
            if list_intersection != []:
                siblings.append(key)
        return siblings

    def check_same_ancestors(self, child_1, child_2):
        child_1_path = self.get_ancestors(child_1)
        child_2_path = self.get_ancestors(child_2)
        ancestors1_as_set = set(child_1_path)
        intersection = ancestors1_as_set.intersection(child_2_path)
        list_intersection = list(intersection)
        if list_intersection != []:
            return True, list_intersection
        else:
            return False, []
