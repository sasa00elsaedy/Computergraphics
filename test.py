from drawer_lib.drawer import *
import random

def draw_cube(scale_factor=1):
    scaled_vertices = get_cube_vertices(scale_factor)
    edges = get_cube_edges()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(scaled_vertices[vertex])
    glEnd()

# draw(draw_cube,caption="rotated cube", rotate=True)
# draw(draw_cube,caption="cube", rotate=False)

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

# draw(draw_sphere, caption="Sphere Drawer rotated", rotate=True)
# draw(draw_sphere, caption="Sphere Drawer", rotate=False)

def draw_multiple_spheres():
    for _ in range(10):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-5, 5)
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        draw_sphere(x=x, y=y, z=z, color=color)

# draw(draw_multiple_spheres, caption="3d sphere")

def draw_dot_wrapper():
    glColor3f(10, 20 , 0.0) # YELLOW
    glPointSize(50.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glEnd()
    
# draw(draw_dot_wrapper)


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  # green color (red, green, blue)
    for vertex in get_triangle_vertices(1):
        glVertex3f(*vertex)
    glEnd()

# draw(draw_function=draw_triangle)
draw(draw_function=draw_triangle,rotate=True)



def contourslice(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    image = cv2.resize(image,(512,512))
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,threshold = cv2.threshold(gray,10,255,0)
    # Find contours
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(str(len(contours)))

    cv2.imshow("Original Image before", image)

    # Draw contours on the black background image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3) # you can replace -1 with index of contour.

    # Display 
    cv2.imshow("Original Image after contour", image)
    cv2.imshow("gray image", gray)
    cv2.imshow("threshold", threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# contourslice("path_of_your_image")
