extends CharacterBody2D

@onready var state_machine = $AnimationTree.get("parameters/playback")
@onready var start_position = global_position
@onready var target_position = global_position
@onready var timer = $Timer

@export var movement_range: int = 500

var speed = 60
var accel = 130

func _physics_process(delta):
	# calcular la direccion
	var direction = global_position.direction_to(target_position).normalized()
	
	if direction.x < 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
	elif direction.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
		
	# calcular velocidad
	if global_position.distance_to(target_position) > 20:
		velocity = velocity.move_toward(direction * speed, accel * delta)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, accel * delta)
		state_machine.travel("idle")
	
	move_and_slide()


func _on_timer_timeout():
	target_position = Vector2(randf_range(0, movement_range), randf_range(0, movement_range))
	state_machine.travel("walk")
	print("moverse a: ", target_position)
	timer.start()
