import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#Graficos
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

#Procesado y modelado
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels as sms
#from sklearn.datasets import load_boston
from statsmodels.stats.outliers_influence import variance_inflation_factor # para calcular el VIF
# configuración de matplotlib
plt.rcParams['image.cmap']="bwr"
plt.rcParams['figure.dpi']="100"
plt.rcParams['savefig.bbox']="tight"
style.use('ggplot') or plt.style.use('ggplot')

# configuración de warnings
import warnings
warnings.filterwarnings('ignore')
# ===========================================================


# Cargamos la Base datos 
DataSet = pd.read_csv('tiempomodificada20162022.csv',sep=",")
print(DataSet.columns)
X_predictores = pd.DataFrame(data = DataSet, columns=['PRECIP','EVAP','TMAX','TMIN'])
print(X_predictores.head())

Y_prediccion = DataSet['HOJAS']
print(Y_prediccion.head())

## Separacion de datos 

X,X_test,y,y_test = train_test_split(X_predictores,Y_prediccion,random_state=90)
df = pd.concat([X,y],axis=1)
X.shape
X_test.shape
y.shape
y_test.shape
# analisis explolatorio 

print(sns.heatmap(df.corr(), annot=True))
print(sns.pairplot(df))
## modelo 
X_constant= sm.add_constant(X)
modelo = sm.OLS(y,X_constant).fit()
print(modelo.summary())