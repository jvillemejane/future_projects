import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from scipy.stats import chi2
import data_analysis as da

## 
file_path = "copie.xlsx"

# Flexion 3 points / Force vs Distance
df = da.flexion_3points_dist_force(file_path)
da.display_graph_data(df, ellipse=True, title="Force vs Distance à la rupture avec ellipses de confiance", xlabel='Distance à la rupture (mm)', ylabel='Force à la rupture (N)')
da.display_graph_ellipse(df, title="Force vs Distance à la rupture avec ellipses de confiance", xlabel='Distance à la rupture (mm)', ylabel='Force à la rupture (N)')

plt.show()
