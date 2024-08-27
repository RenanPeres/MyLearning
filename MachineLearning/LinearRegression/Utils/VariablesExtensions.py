from typing import Optional
import pandas as pd

class VariablesExtensions:
    _REGRESSION_AGGREGATOR_SYMBOL = ' + '
    
    @staticmethod
    def print_nominal_counts(dataFrame: pd.DataFrame,
                             indexes: list):
        for index in indexes:
            print(dataFrame[index].value_counts())

    @staticmethod
    def get_regression_command_string(dataFrame: pd.DataFrame,
                                      target_index: str,
                                      columns_to_remove: Optional[list] = []) -> str:
        variables = list(dataFrame.columns.values)
        variables.remove(target_index)

        for column in columns_to_remove:
            variables.remove(column)

        return target_index + ' ~ ' + VariablesExtensions._REGRESSION_AGGREGATOR_SYMBOL.join(variables)
