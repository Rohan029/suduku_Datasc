# -*- coding: utf-8 -*-
"""suduku

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AZYbrbMJ4H6Sc6TL0TzO0K5X-6_ISzco
"""

import numpy as np
import pandas as pd

df=np.load('/content/sudoku_game.npy')
df

flatten_df = df.flatten()
flatten_df

reshape_df = flatten_df.reshape((9,8))
reshape_df

df

df[2,4]

df[:,3]

df[0:4,0:4]

df[3:6:2, 3:6:2]

np.sort(df)

np.sort(df,axis=1)

np.sort(df,axis=0)

