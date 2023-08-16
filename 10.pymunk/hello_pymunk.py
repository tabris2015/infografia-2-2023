import pymunk
# crear space
space = pymunk.Space()
space.gravity = (0, -981)
# crear un body
body = pymunk.Body()
body.position = (50, 100)
# crear shape y acoplar al body
poly = pymunk.Poly.create_box(body)
poly.mass = 10
# agregar objetos al space
space.add(body, poly)
print_options = pymunk.SpaceDebugDrawOptions()
# correr simulacion por 100 pasos
for _ in range(100):
    space.step(0.02)    # 50 fps
    space.debug_draw(print_options)

