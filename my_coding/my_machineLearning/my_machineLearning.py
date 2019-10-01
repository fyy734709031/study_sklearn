import seaborn as sns

from sklearn.linear_model import LinearRegression
data = sns.load_dataset("flights")
passengers = data.groupby("year")["passengers"].sum()
print(passengers)


from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit_transform()
ss.transform()