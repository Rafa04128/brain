import numpy as np

# Physical constants
g = 9.8
L = 2
mu = 0.1
# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

# Solution to the differential equation
def theta(t, THETA_0, THETA_DOT_0):
    # Initialize changing values
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    return theta
# Example usage
THETA_0 = 0.1
THETA_DOT_0 = 0.0
result = theta(10, THETA_0, THETA_DOT_0)
print(result)

#basically this calculates that change of a pendulum with respect to time.