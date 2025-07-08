import pygame
import math

WIDTH, HEIGHT = 800, 800
FPS = 60

G = 1
DT = 0.005
STEPS_PER_FRAME = 5

SCALE = 200
CENTER = WIDTH // 2, HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three-Body Problem - Figure-8 Orbit (RK4)")
clock = pygame.time.Clock()

class Body:
    def __init__(self, x, y, vx, vy, mass, color):
        self.mass = mass
        self.color = color
        self.pos = [x, y]   
        self.vel = [vx, vy] 

    def draw(self, surface):
        draw_x = int(self.pos[0] * SCALE + CENTER[0])
        draw_y = int(self.pos[1] * SCALE + CENTER[1])
        pygame.draw.circle(surface, self.color, (draw_x, draw_y), 4)

def compute_acceleration(bodies, target_index):
    ax, ay = 0.0, 0.0
    target = bodies[target_index]
    for i, other in enumerate(bodies):
        if i != target_index:
            dx = other.pos[0] - target.pos[0]
            dy = other.pos[1] - target.pos[1]
            dist_sq = dx**2 + dy**2 + 1e-8  
            dist = math.sqrt(dist_sq)
            force = G * other.mass / dist_sq
            ax += force * dx / dist
            ay += force * dy / dist
    return [ax, ay]

def rk4_step(bodies):
    n = len(bodies)

    # Save original state
    pos0 = [b.pos[:] for b in bodies]
    vel0 = [b.vel[:] for b in bodies]

    # k1 / l1
    a1 = [compute_acceleration(bodies, i) for i in range(n)]
    k1 = vel0
    l1 = a1

    # k2 / l2
    temp_pos = [[pos0[i][0] + 0.5 * DT * k1[i][0],
                 pos0[i][1] + 0.5 * DT * k1[i][1]] for i in range(n)]
    temp_vel = [[vel0[i][0] + 0.5 * DT * l1[i][0],
                 vel0[i][1] + 0.5 * DT * l1[i][1]] for i in range(n)]
    for i in range(n):
        bodies[i].pos = temp_pos[i]
        bodies[i].vel = temp_vel[i]
    a2 = [compute_acceleration(bodies, i) for i in range(n)]
    k2 = temp_vel
    l2 = a2

    # k3 / l3
    temp_pos = [[pos0[i][0] + 0.5 * DT * k2[i][0],
                 pos0[i][1] + 0.5 * DT * k2[i][1]] for i in range(n)]
    temp_vel = [[vel0[i][0] + 0.5 * DT * l2[i][0],
                 vel0[i][1] + 0.5 * DT * l2[i][1]] for i in range(n)]
    for i in range(n):
        bodies[i].pos = temp_pos[i]
        bodies[i].vel = temp_vel[i]
    a3 = [compute_acceleration(bodies, i) for i in range(n)]
    k3 = temp_vel
    l3 = a3

    # k4 / l4
    temp_pos = [[pos0[i][0] + DT * k3[i][0],
                 pos0[i][1] + DT * k3[i][1]] for i in range(n)]
    temp_vel = [[vel0[i][0] + DT * l3[i][0],
                 vel0[i][1] + DT * l3[i][1]] for i in range(n)]
    for i in range(n):
        bodies[i].pos = temp_pos[i]
        bodies[i].vel = temp_vel[i]
    a4 = [compute_acceleration(bodies, i) for i in range(n)]
    k4 = temp_vel
    l4 = a4

    # Final RK4 update
    for i in range(n):
        bodies[i].pos = [
            pos0[i][0] + DT / 6 * (k1[i][0] + 2*k2[i][0] + 2*k3[i][0] + k4[i][0]),
            pos0[i][1] + DT / 6 * (k1[i][1] + 2*k2[i][1] + 2*k3[i][1] + k4[i][1])
        ]
        bodies[i].vel = [
            vel0[i][0] + DT / 6 * (l1[i][0] + 2*l2[i][0] + 2*l3[i][0] + l4[i][0]),
            vel0[i][1] + DT / 6 * (l1[i][1] + 2*l2[i][1] + 2*l3[i][1] + l4[i][1])
        ]


vx = 0.3471128135672417
vy = 0.532726851767674

bodies = [
    Body(-1.0,  0.0,  vx,  vy, 1.0, (255, 0, 0)),
    Body( 1.0,  0.0,  vx,  vy, 1.0, (0, 255, 0)),
    Body( 0.0,  0.0, -2*vx, -2*vy, 1.0, (0, 0, 255)),
]

trails = [[] for _ in bodies]

####################### Main loop 
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(STEPS_PER_FRAME):
        rk4_step(bodies)

    for i, body in enumerate(bodies):
        screen_pos = (int(body.pos[0] * SCALE + CENTER[0]), int(body.pos[1] * SCALE + CENTER[1]))
        trails[i].append(screen_pos)
        if len(trails[i]) > 1000:
            trails[i].pop(0)
        for point in trails[i]:
            pygame.draw.circle(screen, body.color, point, 1)

    for body in bodies:
        body.draw(screen)

    pygame.display.flip()

pygame.quit()
