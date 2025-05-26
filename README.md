# Gradient Descent Learning Rate Visualizer

![Gradient Descent Visualization](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive visualization tool that demonstrates how different learning rates affect the convergence of gradient descent on a simple quadratic function.

## Features

- Interactive visualization of gradient descent on a U-shaped curve
- Adjustable learning rate, initial position, and number of iterations
- Real-time updates as you modify parameters
- Clear visualization of the optimization path
- Responsive design that works on different screen sizes

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/FaiazS/Visualization-of-Gradient-Descent.git
   cd Visualization-of-Gradient-Descent
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8050
   ```

3. Use the sliders to adjust:
   - **Initial X Position**: Set the starting point
   - **Learning Rate**: Control the step size
   - **Number of Iterations**: Set how many steps to take

## Understanding the Visualization

- **Blue Curve**: The quadratic function (f(x) = x² + 2)
- **Red Path**: The optimization path of gradient descent
- **Green Dot**: Starting position
- **Purple Dot**: Final position
- **Green Line**: Global minimum of the function

## Try These Examples

- **Slow Convergence**: Learning Rate = 0.01, Iterations = 50
- **Good Convergence**: Learning Rate = 0.1, Iterations = 10
- **Oscillation**: Learning Rate = 0.5, Iterations = 20
- **Divergence**: Learning Rate = 1.0, Iterations = 10

## Dependencies

- Python 3.7+
- Dash
- Plotly
- NumPy
- Dash Bootstrap Components

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Created using [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/)
- Inspired by machine learning education materials

---

Happy Learning! 🚀
