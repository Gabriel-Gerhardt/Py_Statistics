import pandas as pd
import Data_load as load
import numpy as np
import matplotlib.pyplot as plt
# Download latest version

df = load.dataset_load("abcsds/pokemon")


#Amplitude

df_speed = df[['Speed']]
print(df_speed.head())
amplitude_speed= np.ptp(df_speed)
valorMin = np.min(df_speed)
valorMax = np.max(df_speed)
print("A amplitude da velocidade é "+ str(amplitude_speed) + " com o menor valor sendo "+ str(valorMin) + " e o maior sendo "+ str(valorMax))
#----------------------------------------------------------------------------------------------------------------------------------------------------



#Variancia amostral

var_speed = np.var(df_speed)
print("A variancia amostral da velocidade é "+ str(var_speed))
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Desvio padrao

dp_speed = np.sqrt(var_speed)
print("O desvio padrao é "+ str(dp_speed))
#----------------------------------------------------------------------------------------------------------------------------------------------------


#Coeficiente de variacao
media_speed = np.mean(df_speed)
gx_speed = dp_speed / media_speed
print("O coeficiente de variacao é: "+str(round(gx_speed,2)))
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Amplitude Interquartilica

iqr = np.quantile(df_speed, 0.75)- np.quantile(df_speed, 0.25)
print("A Amplitude Interquartilica é: "+ str(iqr))
#----------------------------------------------------------------------------------------------------------------------------------------------------

#Desvio Absoluto em Mediano

mad = 1.4826 *np.median(np.abs(df_speed- np.median(df_speed)))
print("O Desvio Absoluto Mediano é: "+ str(mad))
#----------------------------------------------------------------------------------------------------------------------------------------------------


