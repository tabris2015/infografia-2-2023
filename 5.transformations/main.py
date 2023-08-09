import arcade
import numpy as np

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformacion"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        
    def on_draw(self):
        arcade.start_render()
        vertices = [(100, 100), (100, 200), (200, 200), (200, 100)]
        arcade.draw_polygon_outline(vertices, arcade.color.YELLOW, 5)
        new_vertices = self.translate2(vertices, 200, 200)
        arcade.draw_polygon_outline(new_vertices, arcade.color.CYBER_YELLOW, 5)

    def translate(self, vertices, dx, dy):
        new_vertices = [(v[0] + dx, v[1] + dy) for v in vertices]
        return new_vertices
    
    def translate2(self, vertices, dx, dy):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        v_array = np.array([[v[0], v[1], 1] for v in vertices])
        v_array = np.transpose(v_array)
        # aplicar transformacion
        new_vertices_array = np.dot(TM, v_array)
        new_vertices = np.transpose(new_vertices_array[0:2, :])
        new_vertices = new_vertices.tolist()
        print(new_vertices)
        return new_vertices


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()