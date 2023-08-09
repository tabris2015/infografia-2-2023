import arcade

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



if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()