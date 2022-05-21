import pandas as pd
import plotly.express as px
df=pd.read_csv('./csv files/line_chart.csv')
df1=pd.read_csv('./csv files/data.csv')
#fig=px.line(df, x='Year', y='Per capita income', color='Country', title='Per capita income')
#fig=px.bar(df1, x='Country', y='InternetUsers')
fig=px.scatter(df1, x='Population', y='Per capita', size='Percentage', color='Country', size_max=60)
fig.show()