import pandas as pd
import plotly.figure_factory as ff

dataFrame = pd.read_csv('humanIndex.csv')
# print(dataFrame['Height(Inches)'])
# print('---------------------------------------------------')
# print(dataFrame['Height(Inches)'].tolist())

figure = ff.create_distplot([dataFrame['Weight(Pounds)'].tolist()], ['Weight'], show_hist = False)
figure.show()