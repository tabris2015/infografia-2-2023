import arcade

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Uso de Sprites"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player = arcade.Sprite("img/mario.png", 1, center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player.center_x += 5
        if symbol == arcade.key.RIGHT:
            self.player.center_x -= 5

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        self.player.update()

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.player.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()
