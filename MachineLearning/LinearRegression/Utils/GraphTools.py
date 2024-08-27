import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional

class GraphTools:    
    @staticmethod
    def generate_graph(dataFrame: pd.DataFrame,
                       title: str,
                       annot: Optional[bool] = True,
                       square: Optional[bool] = True):
        sns.heatmap(
            data=dataFrame, 
            annot=annot,
            square=square,
            cmap = plt.cm.viridis,
            annot_kws={'size':8},fmt=".2f",linewidths=0.1)
        plt.tick_params(labelsize=6)
        plt.title(
            label=title,fontsize=10)
        plt.show()