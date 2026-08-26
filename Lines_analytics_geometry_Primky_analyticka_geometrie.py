# analytics geometry
# plot all lines in 2 graphs - 2D and 3D

import numpy as np
import matplotlib.pyplot as plt

start = -5
to = 5
t = np.linspace(start, to, 130)

# 1) 2D parametric (p: A + t * u)

A = np.array([-2, 0]) # point
u = np.array([3, 4]) # direction vector

# param
x_par = A[0] + t * u[0]
y_par = A[1] + t * u[1]

# legend
sign_x = "+" if u[0] >= 0 else ""
sign_y = "+" if u[1] >= 0 else ""

#label
label_par = (
    r"Parametric: {"
    + f"[{A[0]}{sign_x}{u[0]}t, {A[1]}{sign_y}{u[1]}t]"
    + rf", t $\in$ [{start}, {to}]}}"
    )

label_point = (rf'Base Point A [{A[0]},{A[1]}] (parametric form)')

# =====================================================
# 2) general form  (ax + by + c = 0) => y = (-ax-c)/b

v = np.array([1, 3]) # normal vector
c = 2 # constant

x_gen = t
y_gen = (-v[0]* x_gen - c)/ v[1]

y0 = y_gen[0]

sign_b = "+" if v[1] >= 0 else ""
sign_c = "+" if c >= 0 else ""

label_gen = rf'General: {v[0]}x {sign_b} {v[1]}y {sign_c} {c} = 0'

# ======================================================
# 3) slope-intercept form (y = k*x + q)
k_slope = 2 # slope
q_slope = 3 # y-intercept

x_slope = t
y_slope = k_slope * x_slope + q_slope

sign_q = "+" if q_slope >= 0 else ""

label_slope = (rf'Slope: $y = {k_slope}x {sign_q} {q_slope}$')

# =======================================================
# 4) intercept form (x/p + y/q = 1) => y = q * (1 - x/p)
p_int = 2 # x-intercept
q_int = 4 # y-intercept

x_int = t
y_int = q_int * (1 - x_int / p_int)

label_int = rf'Intercept: x/{p_int} + y/{q_int} = 1'
# =======================================================
# 5) 3D dimension - parametric
A3 = np.array([1, 4, 5])
u3 = np.array([3, 4, 1])

x_par3 = A3[0] + t * u3[0]
y_par3 = A3[1] + t * u3[1]
z_par3 = A3[2] + t * u3[2]

# legend
sign_x3 = "+" if u3[0] >= 0 else ""
sign_y3 = "+" if u3[1] >= 0 else ""
sign_z3 = "+" if u3[2] >= 0 else ""


#label
label_par3d = (
    r"Parametric in 3D: {"
    + f"[{A3[0]}{sign_x3}{u3[0]}t, {A3[1]}{sign_y3}{u3[1]}t, {A3[2]}{sign_z3}{u3[2]}t]"
    + rf", t $\in$ [{start}, {to}]}}"
    )

label_point3d = (rf'Base Point A [{A3[0]},{A3[1]}, {A3[2]}]'
    )
# =========================================================
# 6) graphs
fig = plt.figure(figsize = (14, 6))

# a) 2D graphs
ax1 = fig.add_subplot(1, 2, 1)

ax1.scatter(A[0], A[1], color="black", s=50, label=label_point)
ax1.plot(x_par, y_par, label=label_par, lw = 2)
ax1.quiver(A[0], A[1], u[0], u[1], 
           color='orange', angles="xy", scale_units="xy", scale=1,zorder=3, label=rf'Direction vector, $u = ({u[0]}, {u[1]})$',)

ax1.plot(x_gen, y_gen, label=label_gen, color = 'Green', lw=2, linestyle="--")
ax1.quiver(0, -c/v[1], v[0], v[1], 
           color='Darkred', angles="xy", scale_units="xy", scale=1,zorder=3, label=rf'Normal vector, $v = ({v[0]}, {v[1]})$',)

ax1.plot(x_slope, y_slope, label=label_slope, lw=2, linestyle=":")
ax1.plot(x_int, y_int, label=label_int, color = 'crimson', lw=2, linestyle="-.")

ax1.set_title("2D Lines - Analytical Geometry Forms", fontsize=12, fontweight="bold")
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")

ax1.set_xlim(-5, 5)
ax1.set_ylim(-5, 5)

ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.axvline(0, color="black", linewidth=0.8, linestyle="--")

ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(loc="upper left")
#ax1.axis("equal")

# b) 3D graph
ax2 = fig.add_subplot(1, 2, 2, projection="3d")

ax2.plot(x_par3, y_par3, z_par3, label=label_par3d, color="crimson", lw=2)
ax2.scatter(A3[0], A3[1], A3[2], color="black", s=50, label=label_point3d)
ax2.quiver(A3[0], A3[1], A3[2], u3[0], u3[1], u3[2],
           color='darkgreen', length=1.0, normalize=False, linewidth=2, zorder=3, label=rf'Direction vector, $u = ({u3[0]}, {u3[1]}, {u3[2]})$',)

ax2.set_title("3D Space Line", fontsize=12, fontweight="bold")
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y Axis")
ax2.set_zlabel("Z Axis")

ax2.scatter(0, 0, 0, color="Navy", s=30, label ='Point [0,0,0]')

ax2.legend()

plt.tight_layout()
plt.show()