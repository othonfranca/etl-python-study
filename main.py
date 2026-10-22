# Pandas para ler csv e transformar em dataframe
import pandas as pd

# Pandas Profiling
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file('output.html')