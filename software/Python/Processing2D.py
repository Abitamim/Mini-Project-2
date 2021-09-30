import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np

flat_data = pd.read_csv('data_2d.csv')
coef = [-25.285041938862830,80.424586008651660]

flat_data["Distance"] = flat_data["Voltage"] * .01 * coef[0] + coef[1]

flat_data["theta"] = np.radians(flat_data["Rotational Angle"])
flat_data['x'] = flat_data['Distance'] * np.sin(flat_data["theta"])
flat_data['y'] = flat_data['Distance'] * np.cos(flat_data["theta"])

data = go.Scatter3d(
    x=flat_data['x'],
    y=flat_data['y'],
    mode='markers',
    marker={
        'size': 10,
        'opacity': 0.8,
    }
)

layout = go.Layout(
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
)

plot_figure = go.Figure(data=data, layout=layout)

plotly.offline.iplot(plot_figure)