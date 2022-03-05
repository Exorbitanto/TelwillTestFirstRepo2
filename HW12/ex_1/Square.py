from Rectangle import Rectangle
from my_library.numeric_tools import verify_if_value_is_positive


class Square(Rectangle):

    def __init__(self, inner_color=None, border_color=None, length=1, width=1):
        super().__init__(inner_color, border_color)
        if verify_if_value_is_positive(length) and verify_if_value_is_positive(width):
            self._length = length
            self._width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle) and not isinstance(other, Rectangle):
            raise Exception("You cannot compare objects from different classes.")
        elif self.area == other.area and self.border_color == other.border_color and self.inner_color == other.inner_color:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.inner_color} and {self.border_color} rectangle with the length of {self.length} the width of {self.width} and the are of {self.area}"

    def __add__(self, other):
        if not isinstance(other, Square):
            raise Exception("You cannot add objects from different classes.")
        return Square(self.inner_color, self.border_color, self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle) and not isinstance(other, Square):
            raise Exception("You cannot subtract objects from different classes.")
        if self.length < other.length:
            raise Exception("You cannot subtract a bigger object from a lesser one.")
        return Square(self.inner_color, self.border_color, self.length - other.length, self.width - other.width)

    @property
    def area(self):
        return self.width * self.length





