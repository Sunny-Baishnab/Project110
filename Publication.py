import csv 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics as st

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

population_mean = st.mean(data)
population_stdev = st.stdev(data)

print('the mean of the publication is',population_mean)
print('the standard deviation of the publication is',population_stdev)

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = st.mean(mean_list)
    print('the mean for the sample is',mean)
    fig = ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'mean'))
    fig.show()

def main():
    mean_list = []
    for i in range(0,100):
        setOfMean = randomSetOfMeans(30)
        mean_list.append(setOfMean)
    show_fig(mean_list)

main()