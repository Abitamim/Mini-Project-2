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

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=flat_data['x'],
    y=flat_data['y'],
    mode='markers',
    marker={
        'size': 10,
        'opacity': 0.8,
    }
))

fig.update_layout(
    title={
        'text': "Points with Rotational Servo Only",
        'x': .5,
        'y': .9,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="X (mm)",
    yaxis_title="Y (mm)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

layout = go.Layout(
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
)

fig.show()