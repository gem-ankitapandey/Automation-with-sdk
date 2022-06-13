from gempyp.pyprest.keyCheck import KeyCheck
from gempyp.pyprest import utils
from copy import deepcopy
import logging as logger
from gempyp.pyprest.variableReplacement import VariableReplacement as var_replacement
from gempyp.pyprest.preVariables import PreVariables



class PostVariables:
    def __init__(self, pyprest_obj):
        self.pyprest_obj = pyprest_obj
        # get variable written in data["POST_VARIABLE"]
        # postdefined func
        # remove $[#]
        # assign_values and append to a dict
        # different dicts for loal and suite variables


    def postVariables(self):
        logger.info("****************************** INSIDE POST VARIABLES  ******************************")
        post_variables_str = self.pyprest_obj.post_variables
        if post_variables_str:

            # separate by ;
            variable_list = post_variables_str.split(";")
            for each in variable_list:
                each_item = each.split("=")
                scope = "local"
                # checking for syntax
                if "SET" in each_item[0].upper() and '$[#' in each_item[0]:
                    # key = each_item[0].strip("set $[#").strip("Set $[#").strip("SET $[#").strip("]")
                    key = each_item[0].split("#")[1].strip("]")

                    # find suite variables
                    if "SUITE." in key.upper():
                        scope = "suite"
                        key = key.replace(".", "_")
                    
                    # check for postdefined functions and response variables
                    if "$[#" in each_item[1].strip(" "):
                        # check for predefined function
                        self.pyprest_obj.variables[scope][key] = PreVariables(self.pyprest_obj).getFunctionValues(each_item[1])
                        
                        # if not found in predefined functions, check in response
                        response_key = each_item[1].strip("$[#").strip("]")
                        # find key in response  
                        # call keycheck
                        response_key_partition = response_key.split(".")
                        response_json = utils.formatRespBody(self.pyprest_obj.res_obj.response_body)
                        result = KeyCheck(self.pyprest_obj).findKeys(response_json, deepcopy(response_key_partition), deepcopy(response_key_partition))
                        # if result is not "FOUND" then can't set value
                        if result.upper() != "FOUND":
                            logger.info("====== Key Not Found in response =======")
                            logger.info("'" + key + "' is not found")

                            # check predefined functions
                            self.pyprest_obj.variables[scope][key] = PreVariables(self.pyprest_obj).getFunctionValues(each_item[1])
                        else:
                            new_list = utils.fetchValueOfKey(response_json, response_key_partition, result)
                            self.pyprest_obj.variables[scope][key] = new_list[response_key]

                    # key not found in response, checking pre variables and pre variables
                    if "$[#" in each_item[1].strip(" "):
                        var_replacement(self.pyprest_obj).variableReplacement()
            logger.info(f"variables dict after setting POST VARIABLES: -------- {str(self.pyprest_obj.variables)} ")