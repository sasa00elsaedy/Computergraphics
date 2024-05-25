from drawer_lib.drawer import *



def draw_cube(scale_factor=1):
    scaled_vertices = get_cube_vertices(scale_factor)
    edges = get_cube_edges()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(scaled_vertices[vertex])
    glEnd()

# sasa_drawer(draw_cube,caption="rotated cube", rotate=True)
# sasa_drawer(draw_cube,caption="cube", rotate=False)

def draw_sphere(x=0, y=0, z=0, radius=1.0, slices=30, stacks=30, color=(1, 1, 1)):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(color)
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluQuadricTexture(quad, GL_TRUE)
    gluSphere(quad, radius, slices, stacks)
    gluDeleteQuadric(quad)
    glPopMatrix()

# sasa_drawer(draw_sphere, caption="Sphere Drawer rotated", rotate=True)
# sasa_drawer(draw_sphere, caption="Sphere Drawer", rotate=False)

def draw_multiple_spheres():
    for _ in range(10):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-5, 5)
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        draw_sphere(x=x, y=y, z=z, color=color)

sasa_drawer(draw_multiple_spheres, caption="3d sphere")

def draw_dot_wrapper():
    glColor3f(10, 20 , 0.0) # YELLOW
    glPointSize(50.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()

# sasa_drawer(draw_dot_wrapper)
