import numpy as np
import matplotlib.pyplot as plt

def reactor_point_model(N_0, reactivity, beta, lambda_decay, dt, T_sim):
    # Einfaches Punktmodell für die Neutronenkinetik
    # N_0: Anfangsneutronendichte
    # reactivity: Reaktivität (rho)
    # beta: Anteil der verzögerten Neutronen
    # lambda_decay: Zerfallskonstante der Vorläufer
    # dt: Zeitschritt
    # T_sim: Simulationszeit


    time = np.arange(0, T_sim, dt)
    neutron_density = np.zeros_like(time)
    precursor_density = np.zeros_like(time)

    neutron_density[0] = N_0
    precursor_density[0] = N_0 * beta / lambda_decay # Gleichgewicht

    for i in range(1, len(time)):
        dN_dt = (reactivity - beta) * neutron_density[i-1] + lambda_decay * precursor_density[i-1]
        dC_dt = beta * neutron_density[i-1] - lambda_decay * precursor_density[i-1]

        neutron_density[i] = neutron_density[i-1] + dN_dt * dt
        precursor_density[i] = precursor_density[i-1] + dC_dt * dt

    return time, neutron_density

# Beispielnutzung
time, neutrons = reactor_point_model(N_0=1e10, reactivity=0.005, beta=0.0065, lambda_decay=0.08, dt=0.01, T_sim=10)
plt.plot(time, neutrons)
plt.xlabel("Zeit (s)")
plt.ylabel("Neutronendichte")
plt.title("Neutronenkinetik im Punktmodell")
plt.grid(True)
plt.show()