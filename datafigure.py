import pandas as pd
from matplotlib import pyplot as plt

def data_plot():
    
    df = pd.read_json('user_study.json')
    print(type(df))

    data = df.groupby('user_id').sum().head(100)

    fig = plt.figure()

    ax = fig.add_subplot(1,1,1)

    ax.set_xlabel('User Id')
    ax.set_ylabel('Study Time')
    ax.set_title('StudyData')

    ax.plot(data.index, data.minutes)

    plt.show()

    return ax

if __name__ == '__main__':
    data_plot()
