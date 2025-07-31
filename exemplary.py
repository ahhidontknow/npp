import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. Globale Systemparameter ---
# Diese Werte definieren unser physikalisches System.
# Ändere sie, um zu sehen, wie sich das Verhalten des Pendels ändert!
G = 9.81  # Erdbeschleunigung (m/s^2)
L1 = 1.0  # Länge des ersten Pendelarms (m)
L2 = 1.0  # Länge des zweiten Pendelarms (m)
M1 = 1.0  # Masse des ersten Pendelkörpers (kg)
M2 = 1.0  # Masse des zweiten Pendelkörpers (kg)

# --- 2. Anfangsbedingungen ---
# Der Zustand des Systems wird durch vier Werte beschrieben:
# theta1: Winkel des ersten Pendels (relativ zur Vertikalen)
# omega1: Winkelgeschwindigkeit des ersten Pendels
# theta2: Winkel des zweiten Pendels (relativ zum ersten Pendel)
# omega2: Winkelgeschwindigkeit des zweiten Pendels
#
# Hier starten wir beide Pendel aus einer leicht ausgelenkten Position ohne Anfangsgeschwindigkeit.
# Selbst kleine Änderungen hier führen zu drastisch anderem Verhalten (Chaos!).
theta1_start = np.pi / 2
omega1_start = 0.0
theta2_start = np.pi / 2
omega2_start = 0.0

# Packen der Anfangsbedingungen in einen Vektor
y0 = [theta1_start, omega1_start, theta2_start, omega2_start]

# --- 3. Die Bewegungsgleichungen (System von Differentialgleichungen) ---
# Diese Funktion beschreibt die Physik des Doppelpendels.
# Sie nimmt den aktuellen Zustand (y) und die Zeit (t) entgegen und gibt die
# zeitliche Ableitung des Zustands zurück (also die Geschwindigkeiten und Beschleunigungen).
def double_pendulum_ode(t, y):
    """
    Definiert das System von gewöhnlichen Differentialgleichungen für das Doppelpendel.
    y ist ein Vektor [theta1, omega1, theta2, omega2].
    Gibt [d(theta1)/dt, d(omega1)/dt, d(theta2)/dt, d(omega2)/dt] zurück.
    """
    theta1, omega1, theta2, omega2 = y

    # Diese komplexen Formeln ergeben sich aus der Lagrange-Mechanik.
    # Sie berechnen die Winkelbeschleunigungen d(omega1)/dt und d(omega2)/dt.
    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    d_omega1 = (M2 * G * np.sin(theta2) * c - M2 * s * (L1 * omega1**2 * c + L2 * omega2**2) -
               (M1 + M2) * G * np.sin(theta1)) / L1 / (M1 + M2 * s**2)

    d_omega2 = ((M1 + M2) * (L1 * omega1**2 * s - G * np.sin(theta2) + G * np.sin(theta1) * c) +
               M2 * L2 * omega2**2 * s * c) / L2 / (M1 + M2 * s**2)

    return [omega1, d_omega1, omega2, d_omega2]

# --- 4. Numerische Lösung der Differentialgleichungen ---
# Wir definieren den Zeitraum, für den wir die Simulation laufen lassen wollen.
t_max = 40.0  # Simulationsdauer in Sekunden
dt = 0.02     # Zeitschritt für die Ausgabe

# Erzeugt die Zeitpunkte, an denen die Lösung berechnet werden soll.
t_eval = np.arange(0, t_max, dt)

# Der Kern der Simulation: solve_ivp von SciPy löst das ODE-System.
# 'Radau' ist eine gute Methode für steife Differentialgleichungen wie diese.
sol = solve_ivp(
    fun=double_pendulum_ode,
    t_span=[0, t_max],
    y0=y0,
    t_eval=t_eval,
    method='Radau'
)

# Extrahieren der Winkel aus der Lösung
theta1, theta2 = sol.y[0, :], sol.y[2, :]

# --- 5. Umrechnung in kartesische Koordinaten für die Visualisierung ---
# Die Positionen der Massen werden aus den Winkeln und Längen berechnet.
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# --- 6. Erstellung der Animation ---
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-L1-L2-0.5, L1+L2+0.5), ylim=(-L1-L2-0.5, L1+L2+0.5))
ax.set_aspect('equal')
ax.grid()
ax.set_title("Doppelpendel-Simulation")
ax.get_xaxis().set_ticks([]) # Achsenbeschriftung ausblenden
ax.get_yaxis().set_ticks([])

# Initialisieren der Zeichenelemente
line, = ax.plot([], [], 'o-', lw=2, color='#3498db', markersize=8, markerfacecolor='#e74c3c', markeredgecolor='black')
trace, = ax.plot([], [], ',-', lw=1, color='#e67e22', alpha=0.7) # Spur des zweiten Pendels
time_template = 'Zeit = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# Initialisierungsfunktion für die Animation
def init():
    line.set_data([], [])
    trace.set_data([], [])
    time_text.set_text('')
    return line, trace, time_text

# Animationsfunktion, die für jeden Frame aufgerufen wird
def animate(i):
    # Positionen für den aktuellen Frame i
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    # Aktualisieren der Pendelarme und Massen
    line.set_data(thisx, thisy)

    # Aktualisieren der Spur (nur die ersten i Punkte)
    trace.set_data(x2[:i], y2[:i])

    # Aktualisieren der Zeitanzeige
    time_text.set_text(time_template % (i * dt))
    return line, trace, time_text

# Erstellen der Animation
# frames: Anzahl der Bilder in der Animation
# interval: Zeit zwischen den Bildern in Millisekunden
# blit=True: Optimierung, die nur die geänderten Teile neu zeichnet
ani = animation.FuncAnimation(fig, animate, frames=len(t_eval),
                              interval=dt*1000, blit=True, init_func=init)

# Zeigt die Animation an.
# Um die Animation als Video zu speichern, kann man ani.save() verwenden.
# Beispiel: ani.save('doppelpendel.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
