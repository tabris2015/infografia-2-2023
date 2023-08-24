extends Node2D

signal touch()

@export var amplitude = 100
@export var speed = 1.0
var accum_time = 0.0
var next_x_pos
var offset = Vector2(200, 100)
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	accum_time += delta
	next_x_pos = amplitude * sin(speed * accum_time)
	if next_x_pos > 400:
		print("player emittin signal touch")
		touch.emit()
	position.x = next_x_pos + offset.x
	position.y = offset.y
	

func _on_button_button_down():
	amplitude += 50
