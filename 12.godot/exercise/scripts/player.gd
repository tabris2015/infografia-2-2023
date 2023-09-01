extends CharacterBody2D

@export var speed: int = 35

func handle_input():
	var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	velocity = direction * speed
	
func _physics_process(delta):
	handle_input()
	move_and_slide()
