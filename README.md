# The Three-Body Problem: _How do three masses move under their mutual gravitational pull?_
Unlike two bodies (which follow neat ellipses), three bodies create complex, often chaotic orbits; except for some rare solutions.

## The Problem:
- The two-body problem can be solved using Kepler's laws and results in closed-form equations for position and velocity as a function of time, but the 3-body problem generally lacks such a solution.
- This means there isn't a single formula that can directly calculate the future positions and velocities of the bodies for all initial conditions.
- The complexity arises from the non-linear nature of the gravitational forces and the interconnectedness of the bodies' motions. 

## The Physics:

Newton’s law of gravitation: to determine the gravitational forces between two bodies

$$
F = G \frac{m_1 m_2}{r^2}
$$

$$
F_{ij} = G \frac{m_i m_j}{r_{ij}^2} \hat{r}_{ij}
$$

- $G$: the gravitaional constant
- $m_i m_j$: the masses of the bodies
- $r_{ij}$: the distance between body $i$ and $j$
- $\hat{r}_{ij}$: the unit vector pointing from $i$ to $j$ :

$$
\hat{r}_{ij} = \frac{r_2​−r_1​​} {∣r2​−r1​∣}
$$

Newton’s second law: to determine how the force moves the bodies

$$
F = ma
$$

since,

$$
v = \frac{dr} {dt}
$$

$$
a = \frac{dv} {dt}
$$

$$
a = \frac{d} {dt} . \frac{dr} {dt}
$$

therefore,

$$
F = m . \frac{d^2r} {dt^2} 
$$

Calculating the acceleration $a_i$ : to determine the velocity $v_i$ and then the position $r_i$

The acceleration on body $i$ caused by the gravitational pull from others is,

$$
\frac{d^2r_i} {dt^2} = ∑_{j≠i}G \frac{m_j} {|r_j - r_i|^2} \hat{r}_{ij}
$$

e.g.: the acceleration on body 1,

$$
F_{12} = G . \frac{m_1m_2 . (r_2 - r_1)} {|r_2 - r_1|^3}
$$

$$
a_1 = \frac{F_{12} + F_{13}} {m_1}
$$

$$
a_1 = G . m_2 . \frac{r_2 - r_1} {|r_2 - r_1|^3} + G . m_3 . \frac{r_3 - r_1} {|r_3 - r_1|^3}
$$

since,

$$
v_{new} = v_{old} + a . Δt
$$

then,

$$
r_{new} = r_{old} + v_{new} . Δt
$$

## The Figure-8 Solution:
Constraints:
- Total momentum = 0
- Total angular momentum = 0
- Center of mass stays fixed

The initial velocities of body 1: $v_x = 0.3471128135672417$, $v_y = 0.532726851767674$ (based on research)

The initial velocities and positions of bodies 2 and 3 can be calculated to meet the constraints:

$$
r_1 = [1, 0]
$$

$$
r_2 = [-0.5, math.sqrt(3)/2] (120° around the origin)
$$

$$
r_3 = [-0.5, -math.sqrt(3)/2] (240° around the origin)
$$

$$
v_1 = [v_x, v_y]
$$

$$
v_2 = [-v_x, v_y]
$$

$$
[v_x, v_y] + [-v_x, v_y] + v_3 = 0
$$
$$
v_3 = [0, -2 * vy]
$$


https://github.com/user-attachments/assets/b747622c-a0c4-45cb-a87c-9c735ca8a84a



