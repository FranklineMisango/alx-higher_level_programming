#!/usr/bin/python3

"""
This module introduces the class Base
"""
import json
import turtle


class Base:
    """
    Implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """list to json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @staticmethod
    def from_json_string(json_string):
        """transform a JSON string representation `json_string` to a list"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new object from dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))

        return object_created

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        filename = cls.__name__ + ".csv"
        content = ""
        text = []
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                content += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw the figure
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
