import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np

flat_data = pd.read_csv('data.csv')
coef = [-25.285041938862830,80.424586008651660]

flat_data = flat_data[flat_data["Voltage"] >= 120]
flat_data["Distance"] = flat_data["Voltage"] * .01 * coef[0] + coef[1]

flat_data["a"] = np.radians(flat_data["Tilt Angle"])
flat_data["b"] = np.radians(flat_data["Rotational Angle"])
flat_data['x'] = flat_data['Distance'] * np.cos(flat_data["a"]) * np.sin(flat_data["b"])
flat_data['y'] = flat_data['Distance'] * np.cos(flat_data["a"]) * np.cos(flat_data["b"])
flat_data['z'] = flat_data['Distance'] * np.sin(flat_data["a"])
flat_data = flat_data[flat_data['y'] > 35]
flat_data = flat_data[flat_data['z'] > -10]

data = go.Scatter3d(
    x=flat_data['x'],
    y=flat_data['y'],
    z=flat_data['z'],
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