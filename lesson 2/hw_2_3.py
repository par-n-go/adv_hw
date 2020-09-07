class Dot():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, value):
        self.x = value
        return self.x

    def set_y(self, value):
        self.y = value
        return self.y

    def set_z(self, value):
        self.z = value
        return self.z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Dot(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Dot(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Dot(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Dot(x, y, z)

    def __neg__(self):
        x = -self.x
        y = -self.y
        z = -self.z
        return Dot(x, y, z)

dot1 = Dot(1, 2, 3)
dot2 = Dot(1, 2, 3)
print(dot1 * dot2)

dot1 = -Dot(1, 2, 3)
print (dot1)