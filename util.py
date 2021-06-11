import math


# liczy odległość point1 i point2 w lini prostej używając pitagorasa
def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)


def collides_with(self, other_object):
    collision_distance = self.image.width / 2 + other_object.image.width / 2
    actual_distance = distance(self.position, other_object.position)

    return (actual_distance <= collision_distance)
