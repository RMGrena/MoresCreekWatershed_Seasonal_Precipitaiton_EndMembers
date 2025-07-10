#import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, date2num
import seaborn as sns
import scipy
from scipy.stats import linregress
import matplotlib.patches as mpatches
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.dates as mdates
import matplotlib.lines as mlines
from matplotlib import patheffects, cm, patheffects
import matplotlib.patches as mpatches
from pandas.core.groupby import groupby
import scipy.io as si
import statsmodels.api as sm
import statsmodels.formula.api as smf
from datetime import datetime, timedelta
from matplotlib.ticker import NullFormatter
from itertools import combinations
from matplotlib.colors import to_rgba
import matplotlib.colors as mcolors
import matplotlib.lines as mlines
import math
from matplotlib.ticker import FormatStrFormatter
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from scipy.optimize import curve_fit
from pathlib import Path
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from matplotlib.colors import ListedColormap
#import researchpy as rp
# %matplotlib inline # only in jupyer notebook