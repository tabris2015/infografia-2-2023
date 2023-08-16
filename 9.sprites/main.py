import math
import random

import arcade
from game_object import Player, Bullet

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"
SCALING = 0.5
SPEED = 5
BULLET_SPEED = 15


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.sprites = arcade.SpriteList()
        self.player = Player("9.sprites/img/tank.gif", SCALING, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.sprites.append(self.player)
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.score = 0
        arcade.schedule(self.add_enemy, random.randint(1, 4))

    def on_key_press(self, symbol: int, modifiers: int):
        """Metodo para detectar teclas que han sido presionada
        El punto se movera con las teclas de direccion.
        Argumentos:
            symbol: tecla presionada
            modifiers: modificadores presionados
        """
        if symbol == arcade.key.UP:
            self.player.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.player.speed = -SPEED

        if symbol == arcade.key.LEFT:
            self.player.change_angle = 5
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = -5

        if symbol == arcade.key.SPACE:
            bullet = Bullet(
                "9.sprites/img/bullet.png",
                0.1,
                20,
                angle=self.player.angle + 90,
                center_x=self.player.center_x,
                center_y=self.player.center_y
            )
            
            self.bullets.append(bullet)
            self.sprites.append(bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.speed = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_angle = 0

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        self.update_bullets()
        self.update_enemies()
        self.sprites.update()

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.sprites.draw()
        arcade.draw_text(
            f"Score: {self.score}",
            700,
            35,
            arcade.color.YELLOW,
            15,
            width=SCREEN_WIDTH,
            align="left"
        )

    def update_bullets(self):
        for b in self.bullets:
            if b.top > SCREEN_HEIGHT or b.bottom < 0 or b.left < 0 or b.right > SCREEN_WIDTH:
                b.remove_from_sprite_lists()

    def update_enemies(self):
        for e in self.enemies:
            if e.collides_with_list(self.bullets):
                e.remove_from_sprite_lists()
                self.score += 1

    def add_enemy(self, delta_time: float):
        print(delta_time)
        enemy = arcade.SpriteSolidColor(30, 30, arcade.color.RED)
        enemy.left = random.randint(10, SCREEN_WIDTH - 10)
        enemy.top = random.randint(10, SCREEN_HEIGHT - 10)
        self.enemies.append(enemy)
        self.sprites.append(enemy)


if __name__ == "__main__":
    app = App()
    arcade.run()
