import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from scipy.stats import chi2


## Data points graphics
def display_graph_data(df, ellipse=False, title='', xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(8,6))

    for name, group in df.groupby("Groupe"):
        x, y = group["Distance"], group["Force"]
        ax.scatter(x, y, label=name, alpha=0.6)
        ax.scatter(x.mean(), y.mean(), color="black", marker="D", s=20)

        if ellipse:
            confidence_ellipse(x, y, ax, n_std=1)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.set_title(title)
    
## Display only confidence ellipse
def display_graph_ellipse(df, title='', xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(8,6))

    for name, group in df.groupby("Groupe"):
        x, y = group["Distance"], group["Force"]
        scatter = ax.scatter(x.mean(), y.mean(), marker="P", s=50, label=name)
        color = scatter.get_facecolor()[0]
        confidence_ellipse(x, y, ax, n_std=1, edgecolor=color)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.set_title(title)

## Confidence ellipse
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', edgecolor='black', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The Axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")
    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)
        
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, 
                        height=ell_radius_y * 2,
                      edgecolor=edgecolor, facecolor=facecolor, 
                      linestyle="--", **kwargs)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    ax.add_patch(ellipse)
    
    
    

# Flexion 3 points
## File parameters
col_data = 3
row_date = 1 
row_data_number = 2
row_group_number = 3
row_data_exp = 4

## Data parameters
first_data = 6
header_rows = 6
empty_rows = 4
dist_col = 8
force_col = 6
  
## 
def flexion_3points_dist_force(file_path):
    # Load XLSX file
    raw = pd.read_excel(file_path, sheet_name="donnees", header=None)
    group_number = int(raw.iloc[row_group_number-1, col_data-1])
    data_number = int(raw.iloc[row_data_number-1, col_data-1])
    
    print(f'Number of groups = {group_number}')
    
    data = []
    group_names = []
    for i in range(group_number):
        # Group name extraction
        inter_row = header_rows + empty_rows + data_number
        g_name = raw.iloc[inter_row*i+first_data-1, 0]
        print(g_name)
        group_names.append(g_name)
        
        # Data extraction
        for k in range(data_number):
            inter_row = header_rows + empty_rows + data_number
            force = raw.iloc[header_rows+(inter_row*i+first_data-1)+k, force_col-1]
            dist = raw.iloc[header_rows+(inter_row*i+first_data-1)+k, dist_col-1]
            data.append([g_name, dist, force])

    # DataFrame for data analyses
    df = pd.DataFrame(data, columns=["Groupe", "Distance", "Force"])
    return df
