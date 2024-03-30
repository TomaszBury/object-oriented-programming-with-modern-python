from visual import *


scene = display(title="Earth's Orbit", width=500, height=500, range=3.e11)
#
scene.autoscale = 0              # Turn off auto scaling of display.
#
# Define the Sun and the Earth objects.
#
sun = sphere(color=color.yellow)
earth = sphere(color=color.blue)
venus = sphere(color=color.red)

# Gravitational constant (Nm**2/kg**2)
G = 6.67 * 10 ** -11
sun.pos = vector(0, 0, 0)         # Initial Sun position (m)
earth.pos = vector(0, 149.6 * 10 ** 9, 0)       # Initial Earth position (m)
venus.pos = vector(0, 1.0820948 * 10 ** 11, 0)  # initial venus position

rhat = -norm(earth.pos)
sun.mass = 2 * 10 ** 30                  # Mass of the Sun   (kg)
earth.mass = 6 * 10 ** 24                   # Mass of the Earth (kg)
venus.mass = 4.867 * 10 ** 24
# Initial velocity of the Earth (m/s)
earth.velocity = vector(30 * 10 ** 3, 0, 0)
venus.velocity = vector(35.02 * 10 ** 3)
#
# time increment in seconds (choose a sensible value)
dt = 86000
#
total = 0                       # initialize the total elapsed time
#
# Scale factors to control how big the Earth and Sun are drawn in the display.
#
sun.scale = 1e1
earth.scale = 5e2
venus.scale = earth.scale
#
sun.radius = 7.e8 * sun.scale
earth.radius = 6.4e6 * earth.scale
venus.radius = 6.052e6 * venus.scale
#
# Initialize the momentum and path of the Earth.
#
earth.momentum = earth.mass * earth.velocity       # momentum of the earth
venus.momentum = venus.mass * venus.velocity # momentum of venus
earth.trail = curve(color=earth.color)           # define the Earth's path
# set initial position of the Earth
earth.trail.append(pos=earth.pos)
#
# Define an arrow that points from the origin to the Earth.
#
rearrow = arrow(pos=(0, 0, 0), axis=earth.pos,
                color=earth.color, shaftwidth=1e6)
momentumArrow = arrow(pos=earth.pos, axis=earth.momentum,
                      color=earth.color, shaftwidth=1e6)
#
tmax = 3600 * 24 * 365.25                          # number of seconds in a year
#
# Start of the loop.
#
while (True):
    #
    rate(100)         # limit the loop to a maximum of 100 times per second.
#
# Fill in the next 3 lines with the correct expressions

    earthToSun = -norm(earth.pos)
    venusToSun = -norm(venus.pos)
    earthToVenus = -norm(earth.pos - venus.pos)
    # compute the force that the Sun exerts on the Earth and added venus's influence
    earth.force = ((G * earth.mass * sun.mass) / (mag(earth.pos)) ** 2 * rhat
                    + G * venus.mass * earth.mass / mag(earth.pos-venus.pos) ** 2 * earthToVenus)
    earth.momentum = earth.momentum + earth.force * \
        dt      # update the Earth's momentum

    # update the Earth's position
    earth.pos = earth.pos + (earth.momentum / earth.mass) * dt


    forceEarth = (G * earth.mass * venus.mass) / (mag(earth.pos-venus.pos)) ** 2 * earthToVenus
    forceSun = G * venus.mass * sun.mass / (mag(venus.pos)) ** 2 * venusToSun
    venus.force = forceEarth + forceSun
    venus.momentum += venus.force * dt

    venus.pos += (venus.momentum / venus.mass) * dt



    momentumArrow.pos = earth.pos
    momentumArrow.axis = earth.momentum * 10 ** -18
    earth.trail.append(pos=earth.pos)  # update the Earth's trail
    rearrow.axis = earth.pos             # move the Earth's position arrow
#
    total = total + dt                   # increment the timeu
#
# print this when the loop is done.
#






print earth.pos
#print ('All done.')
