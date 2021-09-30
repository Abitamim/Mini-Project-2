import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np

#read data from csv
flat_data = pd.read_csv('data_2d.csv')
#calibrated coefficients to convert from volts to cm
coef = [-25.285041938862830,80.424586008651660]

#convert distance to cm
flat_data["Distance"] = flat_data["Voltage"] * .01 * coef[0] + coef[1]

#convert angle to radians
flat_data["theta"] = np.radians(flat_data["Rotational Angle"])

#calculate x and y coordinates
flat_data['x'] = flat_data['Distance'] * np.sin(flat_data["theta"])
flat_data['y'] = flat_data['Distance'] * np.cos(flat_data["theta"])

fig = go.Figure()

#create scatter plot
fig.add_trace(go.Scatter(
    x=flat_data['x'],
    y=flat_data['y'],
    mode='markers',
    marker={
        'size': 10,
        'opacity': 0.8,
    }
))

#label plot
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

#plot
fig.show()