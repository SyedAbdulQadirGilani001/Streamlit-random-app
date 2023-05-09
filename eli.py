# eli random generator
import random
import sys
import os
import time
import datetime
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import streamlit as st
import pandas as pd
random.seed(datetime.datetime.now())
df=pd.DataFrame(np.random.randn(100, 3),columns=['a','b','c'])
st.line_chart(df)
st.write('''
# Eli Random Generator
''')
st.write('''
## Random Number
''')
st.write(random.randint(0,100))
st.write('''
## Random Float
''')
st.write(random.random())
st.write('''
## Random Choice
''')