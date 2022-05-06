import re


class pre_variables:
    def __init__(self, pirest_obj):
        self.pirest_obj = pirest_obj
        # get variable written in data["PRE_VARIABLE"]
        # predefined func
        # remove $[#]
        # assign_values and append to a dict
        # different dicts for loal and suite variables


    def pre_variable(self):
        self.pirest_obj.variables["local"] = {}
        self.pirest_obj.variables["suite"] = {}
        pre_variables_str = self.pirest_obj.pre_variables

        # separate by ;
        variable_list = pre_variables_str.split(";")
        for each in variable_list:
            each_item = each.split("=")
            if "$[#" in each_item[0].strip(" "):  #in re.search(r'$[#', str(each_item[0].strip())):
                key = each_item[0].strip("set $[#").strip("Set $[#").strip("]")

                # find suite variables
                if "SUITE." in str(each_item[0].strip()):
                    key = "SUITE_" + each_item[0].strip().strip("SUITE.").upper()
                    self.pirest_obj.variables["suite"][key] = each_item[1].strip()
                else:
                    self.pirest_obj.variables["local"][key] = each_item[1].strip()
                # check for predefined functions
        print("Setting pre variables: -------- ", self.pirest_obj.variables)