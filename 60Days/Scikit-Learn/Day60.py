from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
df = pd.read_csv("Student_Marks.csv")
x = df.iloc[:,:-1]
y = df.iloc[:,-1]