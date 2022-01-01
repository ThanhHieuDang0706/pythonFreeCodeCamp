class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""

        for i in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        selfArea = self.get_area()
        passedArea = shape.get_area()

        if passedArea != 0:
            return selfArea // passedArea

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, side):
        self.width = self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.height = self.width = height
