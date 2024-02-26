from brian2 import *

# Define the SNN parameters
start_scope()

# Neuron group with a simple threshold
neuron_eqs = '''
dv/dt = (0.2 - v) / 10 : 1 (unless refractory)
'''

snn = NeuronGroup(2, neuron_eqs, threshold='v > 1', reset='v = 0', refractory=5*ms)

# Define Hebbian learning rule
alpha = 0.1  # learning rate

# Synaptic weights matrix
w = Synapses(snn, snn, model='''w : 1''', on_pre='v_post += w')
w.connect(i=0, j=1)  # Connect neuron 0 to neuron 1

# Hebbian learning rule
learning_rule = '''
            dw/dt = alpha * v_pre * v_post : 1 (event-driven)
'''

w_pre_post = Synapses(snn, snn, model=learning_rule, on_pre='w += dw')
w_pre_post.connect(i=0, j=1)

# Set initial synaptic weight
w.w = 0.5

# Run the simulation
snn_state = StateMonitor(snn, 'v', record=True)
w_state = StateMonitor(w, 'w', record=True)

run(100*ms)

# Plot the membrane potential and synaptic weights
"""figure(figsize=(12, 6))

subplot(2, 1, 1)
plot(snn_state.t/ms, snn_state.v[0], label='Neuron 0')
plot(snn_state.t/ms, snn_state.v[1], label='Neuron 1')
xlabel('Time (ms)')
ylabel('Membrane Potential')
legend()

subplot(2, 1, 2)
plot(w_state.t/ms, w_state.w[0], label='Synaptic Weight')
xlabel('Time (ms)')
ylabel('Weight')
legend()

show()"""
