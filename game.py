import matplotlib.pyplot as plt
import numpy as np
from inverse_k import inverse_k2dof as ik
from matplotlib.widgets import Slider
import math
from datetime import datetime



#  lengths
L1 = 12.5
L2 = 12.5


end_effector_x = -21
end_effector_y = 0





"""
def update(val):
    global theta1, theta2
    theta1 = slider_theta1.val
    theta2 = slider_theta2.val
    update_simulation()
"""

def update_simulation():
    joint2_x = L1 * np.cos(theta1)
    joint2_y = L1 * np.sin(theta1)
    end_effector_x_sim = joint2_x + L2 * np.cos(theta1 + theta2)
    end_effector_y_sim = joint2_y + L2 * np.sin(theta1 + theta2)

  
    ax.clear()
    ax.plot([0, joint2_x], [0, joint2_y], 'r-')
    ax.plot([joint2_x, end_effector_x_sim], [joint2_y, end_effector_y_sim], 'b-')
    ax.plot(0, 0, 'ro')  
    ax.plot(joint2_x, joint2_y, 'ro')  
    ax.plot(end_effector_x_sim, end_effector_y_sim, 'bo')  
    ax.set_xlim([-30, 30])
    ax.set_ylim([-30, 30])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('2-DOF Robotic Arm Simulation')
    ax.grid(True)
    plt.draw()
def sim_inverse_k(end_effector_x,end_effector_y):

    p,initial_theta1, initial_theta2 = ik(end_effector_x, end_effector_y, L1, L2)
    global theta1,theta2,ax
    theta1 =  math.radians(initial_theta1*-1)
    theta2 =  math.radians(initial_theta2*-1)
    print(f"{theta1} and {theta2}")

    fig, ax = plt.subplots()
    update_simulation()

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    axcolor = 'lightgoldenrodyellow'
    plt.savefig(f'logs/sim-{formatted_time}.png')

    return initial_theta1, initial_theta2
"""
ax_theta1 = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor=axcolor)

slider_theta1 = Slider(ax_theta1, 'Theta1', -np.pi, np.pi, valinit=initial_theta1, valfmt='%1.2f rad')
slider_theta2 = Slider(ax_theta2, 'Theta2', -np.pi, np.pi, valinit=initial_theta2, valfmt='%1.2f rad')

d
slider_theta1.on_changed(update)
slider_theta2.on_changed(update)
"""
    
