import statistics as st
import pandas as pd
import random as rng
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv ("data.csv")
data = df ["temp"].tolist()
mean = st.mean(data)
std = st.stdev(data)

print (mean,std)
fig = ff.create_distplot ([data], ["temp"], show_hist = False)
#fig.show ()

dataset = []
for i in range (0,100):
    ri = rng.randint(0,len(data))
    value = data[ri]
    dataset.append(value)
pop_mean = st.mean(dataset)
std = st.stdev(dataset)
print("Population Mean : " , pop_mean)
print("Standard deviation : " , std)

def random_set_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        ri = rng.randint(0,len(data)-1)
        value = data[ri]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = ff.create_distplot ([df], ["temp"], show_hist = False)
    fig.show ()   

def setup():
    mean_list = []
    for i in range (0,1000):
        s = random_set_of_mean(100)
        mean_list.append(s)
    show_fig (mean_list)
    mean = st.mean(mean_list)
    std = st.stdev(mean_list)
    print("\nMean of sampling distribution :",mean )
    print("\nStd of sampling distribution:",std)

setup()