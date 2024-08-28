import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional

class GraphTools:    
    
    @staticmethod
    def generate_pearson_correlation_graph( dataFrame: pd.DataFrame,
                                            title: str,
                                            annot: Optional[bool] = True,
                                            square: Optional[bool] = True):
        sns.heatmap(
            data=dataFrame, 
            annot=annot,
            square=square,
            cmap = plt.cm.Oranges,
            annot_kws={'size':8},fmt=".2f",linewidths=0.1)
        plt.tick_params(labelsize=6)
        plt.title(
            label=title,fontsize=10)
        plt.show()

    @staticmethod
    def generate_sample_fitted_analysis_graph(dataFrame: pd.DataFrame,
                                            target_index_name: str,
                                            fitted_index_name: str,
                                            title: str,
                                            x_axis_label : Optional[str] = 'Sample Values',
                                            y_axis_label : Optional[str] = 'Fitted Values'):        
        sns.regplot(
            data=dataFrame,
            x=target_index_name,
            y=fitted_index_name,
            marker='o', color='violet', scatter_kws={'s':0.50}, line_kws={'color':'green', 'lw':2})
        plt.title(
            label=title, fontsize=10)
        plt.xlabel(x_axis_label, fontsize=8)
        plt.ylabel(y_axis_label, fontsize=8)
        plt.tick_params(labelsize=4)
        plt.show()