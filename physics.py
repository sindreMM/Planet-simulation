import numpy as np


class Body:
    bodies = []

    def __init__(self, mass, starting_speed, starting_position):
        self.mass = mass

        self.position = None
        self.speed = None
        self.acceleration = [0, 0]

        # the old properties are always used when calculating. The resulting values are saved onto the normal properties
        # We use this differentiation between normal and old movement to calculate movement from the same time_step
        self.old_position = starting_position
        self.old_speed = starting_speed
        self.old_acceleration = [0, 0]

        self.distance = None
        self.__class__.bodies.append(self)

    def get_distance(self, other): # Calculates distance from self to target object
        s_x, s_y = self.old_position
        o_x, o_y = other.old_position
        self.distance = np.sqrt(np.power(s_x - o_x, 2) + np.power(s_y
            - o_y, 2))

    def calculate_movement(self, bodies, time_step): # Calculates new movement
        accelerations = []
        self.acceleration = [0, 0]
        for body in bodies:
            if body == self:
                continue
            else:
                self.get_distance(body)
                b_x, b_y = body.old_position
                s_x, s_y = self.old_position

                acc = [(body.mass / self.distance) * (b_x - s_x) / self.distance,
                    (body.mass / self.distance) * (b_y - s_y) / self.distance]
                accelerations.append(acc)

        if len(accelerations) > 0:
            for n in accelerations: # The acceleration is calculated by using the sum of the forces between all objects
                self.acceleration = np.add(self.acceleration, n)

        # Speed is calculated from the old speed, and the new acceleration
        self.speed = [self.old_speed[0] + self.acceleration[0] * time_step, self.old_speed[1] + self.acceleration[1] * time_step]

        # Position is calculated from the old position, as well as the new speed and acceleration
        self.position = [self.old_position[0] + self.speed[0] * time_step + self.acceleration[0] * np.power(time_step, 2),
                         self.old_position[1] + self.speed[1] * time_step + self.acceleration[1] * np.power(time_step, 2)]

        # the time_step variable is the time_step between each instance where the movement is calculated

    def update_body(self): # Updates the properties
        self.old_position = self.position
        self.old_speed = self.speed
        self.old_acceleration = self.acceleration

    @classmethod
    def update_bodies(cls):
        for body in cls.bodies:
            body.update_body()

    @classmethod
    def update_simulation(cls, time_step):
        for body in cls.bodies:
            body.calculate_movement(cls.bodies, time_step)

