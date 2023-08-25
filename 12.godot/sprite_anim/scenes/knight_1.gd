extends CharacterBody2D

const MAX_SPEED = 80
const FRICTION = 500

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	input_vector.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		# movimiento
		$AnimationPlayer.play("run")
	else:
		$AnimationPlayer.play("idle2")

	print(input_vector)
	velocity = MAX_SPEED * input_vector
	# si mira a la izquierda o derecha
	if velocity.x < 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
	elif velocity.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	
	move_and_slide()
