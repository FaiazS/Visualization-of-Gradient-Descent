import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash.dependencies import ALL

# Define the quadratic function (U-shaped curve)
def quadratic(x):
    return x**2 + 2

# Gradient of the quadratic function
def gradient(x):
    return 2 * x

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Learning Rate Visualization", className="text-center mb-4"),
            html.P("This interactive visualization demonstrates how different learning rates affect gradient descent convergence on a simple quadratic function.", 
                  className="text-muted text-center mb-4"),
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='gradient-descent-plot'),
        ], width=12, md=8, className="mb-4"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Parameters", className="card-title"),
                    
                    html.Label("Initial X Position", className="mt-3"),
                    dcc.Slider(
                        id='initial-x',
                        min=-5,
                        max=5,
                        step=0.1,
                        value=4.5,
                        marks={i: str(i) for i in range(-5, 6)},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    
                    html.Label("Learning Rate", className="mt-4"),
                    dcc.Slider(
                        id='learning-rate',
                        min=0.01,
                        max=0.5,
                        step=0.01,
                        value=0.1,
                        marks={0.01: '0.01', 0.1: '0.1', 0.2: '0.2', 0.3: '0.3', 0.4: '0.4', 0.5: '0.5'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    
                    html.Label("Number of Iterations", className="mt-4"),
                    dcc.Slider(
                        id='iterations',
                        min=1,
                        max=50,
                        step=1,
                        value=10,
                        marks={1: '1', 10: '10', 20: '20', 30: '30', 40: '40', 50: '50'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                    
                    dbc.Button("Reset View", id="reset-view", color="secondary", className="mt-4 w-100")
                ])
            ])
        ], width=12, md=4)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4("How to Use"),
                html.Ul([
                    html.Li("Adjust the Initial X Position to set the starting point of gradient descent."),
                    html.Li("Modify the Learning Rate to see how it affects convergence."),
                    html.Li("Change the Number of Iterations to see more or fewer steps of the algorithm."),
                    html.Li("Hover over the plot to see coordinates and function values."),
                    html.Li("Use the toolbar in the top-right of the plot to zoom, pan, or download the plot.")
                ]),
                html.H4("Observations", className="mt-4"),
                html.Ul([
                    html.Li("A learning rate that's too small will converge very slowly."),
                    html.Li("A moderate learning rate will converge efficiently."),
                    html.Li("A learning rate that's too large may cause divergence or oscillation."),
                    html.Li("The optimal learning rate for this function is 0.5 (the maximum shown).")
                ])
            ], className="mt-4 p-3 bg-light rounded")
        ], width=12)
    ])
], fluid=True)

from dash.exceptions import PreventUpdate

@callback(
    Output('gradient-descent-plot', 'figure'),
    Input('initial-x', 'value'),
    Input('learning-rate', 'value'),
    Input('iterations', 'value'),
    Input('reset-view', 'n_clicks'),
    prevent_initial_call=True
)
def update_plot(initial_x, lr, n_iter, reset_click):
    # Get the callback context
    ctx = callback
    
    # Check which input triggered the callback
    if not ctx.triggered:
        raise PreventUpdate
        
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Generate x values for the plot
    x_vals = np.linspace(-5, 5, 400)
    y_vals = quadratic(x_vals)
    
    # Initialize figure
    fig = go.Figure()
    
    # Plot the quadratic function
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name='f(x) = x² + 2',
        line=dict(color='blue', width=2)
    ))
    
    # Only perform gradient descent if not just resetting the view
    if triggered_id != 'reset-view' or reset_click is None:
        # Perform gradient descent
        x = initial_x
        x_history = [x]
        y_history = [quadratic(x)]
        
        for _ in range(n_iter):
            grad = gradient(x)
            x = x - lr * grad
            x_history.append(x)
            y_history.append(quadratic(x))
        
        # Plot the gradient descent path
        fig.add_trace(go.Scatter(
            x=x_history,
            y=y_history,
            mode='lines+markers',
            name='Gradient Descent',
            line=dict(color='red', width=1, dash='dash'),
            marker=dict(size=8, color='red')
        ))
        
        # Add a marker for the starting point
        fig.add_trace(go.Scatter(
            x=[x_history[0]],
            y=[y_history[0]],
            mode='markers',
            name='Start',
            marker=dict(size=12, color='green')
        ))
        
        # Add a marker for the final point
        fig.add_trace(go.Scatter(
            x=[x_history[-1]],
            y=[y_history[-1]],
            mode='markers',
            name='End',
            marker=dict(size=12, color='purple')
        ))
        
        # Auto-scale y-axis to show the full path
        y_min = min(min(y_vals), min(y_history)) - 1
        y_max = max(max(y_vals), max(y_history)) + 1
        y_range = [y_min, y_max]
    else:
        # Default y-range when just resetting
        y_range = [0, 30]
    
    # Add a line showing the minimum
    fig.add_hline(y=2, line_dash="dash", line_color="green", opacity=0.5, annotation_text="Global Minimum (x=0, y=2)")
    
    # Update layout
    fig.update_layout(
        title=f'Gradient Descent with Learning Rate = {lr}',
        xaxis_title='x',
        yaxis_title='f(x)',
        showlegend=True,
        hovermode='closest',
        margin=dict(l=50, r=50, t=50, b=50),
        height=600,
        xaxis=dict(range=[-5, 5]),
        yaxis=dict(range=y_range)
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
