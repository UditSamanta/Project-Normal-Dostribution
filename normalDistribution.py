import pandas as pd
import statistics
import plotly.figure_factory as ff

dataFrame = pd.read_csv('humanIndex.csv')
height_list = dataFrame['Height(Inches)'].to_list()
weight_list = dataFrame['Weight(Pounds)'].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_stdDeviation = statistics.stdev(height_list)
weight_stdDeviation = statistics.stdev(weight_list)

print('Mean, Median, Mode of the height is :{}, {}, {}'.format(height_mean, height_median, height_mode))
print('Mean, Median, Mode of the weight is :{}, {}, {}'.format(weight_mean, weight_median, weight_mode))
print('Standard Deviation of the weight is :{}'.format(weight_stdDeviation))
print('Standard Deviation of the height is :{}'.format(height_stdDeviation))

# figure = ff.create_distplot([dataFrame['Weight(Pounds)'].tolist()], ['Weight'], show_hist = False)
# figure.show()

height_1st_stdDev_start, height_1st_stdDev_end = height_mean - height_stdDeviation, height_mean + height_stdDeviation
height_2nd_stdDev_start, height_2nd_stdDev_end = height_mean - (height_stdDeviation*2), height_mean + (height_stdDeviation*2)
height_3rd_stdDev_start, height_3rd_stdDev_end = height_mean - (height_stdDeviation*3), height_mean + (height_stdDeviation*3)

height_listOfData_under1stStdDev = [result for result in height_list if result>height_1st_stdDev_start and result<height_1st_stdDev_end]
height_listOfData_under2ndStdDev = [result for result in height_list if result>height_2nd_stdDev_start and result<height_2nd_stdDev_end]
height_listOfData_under3rdStdDev = [result for result in height_list if result>height_3rd_stdDev_start and result<height_3rd_stdDev_end]

print('{}% of data for height lies within 1st standard deviation'.format(len(height_listOfData_under1stStdDev)*100/len(height_list)))
print('{}% of data for height lies within 2nd standard deviation'.format(len(height_listOfData_under2ndStdDev)*100/len(height_list)))
print('{}% of data for height lies within 3rd standard deviation'.format(len(height_listOfData_under3rdStdDev)*100/len(height_list)))
