import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np

#read data from csv
flat_data = pd.read_csv('data.csv')
#calibrated coefficients to convert from volts to cm
coef = [-25.285041938862830,80.424586008651660]

#remove low voltages corresponding to the air behind the test figure
flat_data = flat_data[flat_data["Voltage"] >= 120]

#convert distance to cm
flat_data["Distance"] = flat_data["Voltage"] * .01 * coef[0] + coef[1]

#convert angles to radians
flat_data["a"] = np.radians(flat_data["Tilt Angle"])
flat_data["b"] = np.radians(flat_data["Rotational Angle"])

#calculate coordinates
flat_data['x'] = flat_data['Distance'] * np.cos(flat_data["a"]) * np.sin(flat_data["b"])
flat_data['y'] = flat_data['Distance'] * np.cos(flat_data["a"]) * np.cos(flat_data["b"])
flat_data['z'] = flat_data['Distance'] * np.sin(flat_data["a"])

#remove points too close to the sensor to too far below sensor
flat_data = flat_data[flat_data['y'] > 35]
flat_data = flat_data[flat_data['z'] > -10]

fig = go.Figure()

#create 3d scatter plot
fig.add_trace(go.Scatter3d(
    x=flat_data['x'],
    y=flat_data['y'],
    z=flat_data['z'],
    mode='markers',
    marker={
        'size': 10,
        'opacity': 0.8,
    }
))

#label plot
fig.update_layout(
    title={
        'text': "Cleaned Point Cloud",
        'x': .5,
        'y': .9,
        'xanchor': 'center',
        'yanchor': 'top'},
    scene=dict(xaxis_title="X (cm)",
    yaxis_title="Y (cm)",
    zaxis_title="Z (cm)"),
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

#plot
fig.show()