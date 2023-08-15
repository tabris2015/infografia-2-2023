import arcade
from game_object import Player, Bullet

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Uso de Sprites"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        # sprite list para dibujar
        self.sprites = arcade.SpriteList()
        self.player = Player(
            "9.sprites/img/tank.gif", 
            1, 
            center_x=SCREEN_WIDTH / 2, 
            center_y=SCREEN_HEIGHT / 2
        )
        self.sprites.append(self.player)

        # lista para las balas
        self.bullets = arcade.SpriteList()
        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 2
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = -2

        if symbol == arcade.key.UP:
            self.player.speed = 5
        if symbol == arcade.key.DOWN:
            self.player.speed = -5

        if symbol == arcade.key.SPACE:
            bullet = Bullet(
                "9.sprites/img/bullet.png",
                0.1,
                20,
                self.player.angle + 90,
                self.player.center_x,
                self.player.center_y
            )

            self.bullets.append(bullet)
            self.sprites.append(bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_angle = 0

        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.speed = 0

    def on_update(self, delta_time: float):
        """Metodo para  actualizar objetos de la app"""
        self.sprites.update()
        self.update_bullets()
        print(len(self.bullets))

    def update_bullets(self):
        for b in self.bullets:
            if ((b.center_x > SCREEN_WIDTH or b.center_x < 0) 
                or (b.center_y > SCREEN_HEIGHT or b.center_y < 0)):
                b.remove_from_sprite_lists()


    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.sprites.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()
