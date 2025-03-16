import pandas as pd
import Data_load as load
import numpy as np
import matplotlib.pyplot as plt
# Download latest version

df = load.dataset_load("abcsds/pokemon")


#Amplitude

df_speed = df[['Speed']]


plt.plot(df.index,df_speed)
plt.xlabel('index')
plt.ylabel('speed')
plt.show()