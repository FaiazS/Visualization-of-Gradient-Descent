# Gradient Descent Learning Rate Visualizer

An interactive visualization tool that demonstrates how different learning rates affect the convergence of gradient descent on a simple quadratic function.

---
## Features

- Interactive visualization of gradient descent on a U-shaped curve
  
- Adjustable learning rate, initial position, and number of iterations
  
- Real-time updates as you modify parameters
  
- Clear visualization of the optimization path
  
- Responsive design that works on different screen sizes

---

Use the sliders to adjust:

-Initial X Position: Set the starting point.

-Learning Rate: Control the step size.

-Number of Iterations: Set how many steps to take.

---

# Understanding the Visualization

Blue Curve: The quadratic function (f(x) = x² + 2)

Red Path: The optimization path of gradient descent

Green Dot: Starting position

Purple Dot: Final position

Green Line: Global minimum of the function

Try These Examples

1.Slow Convergence: Learning Rate = 0.01, Iterations = 50 

2.Good Convergence: Learning Rate = 0.1, Iterations = 10

3.Oscillation: Learning Rate = 0.5, Iterations = 20

4.Divergence: Learning Rate = 1.0, Iterations = 10

---
# Dependencies

-Python 3.7+

-Dash

-Plotly

-NumPy

-Dash Bootstrap Components

---
# Acknowledgments

Created using Dash and Plotly

Inspired by machine learning education materials
