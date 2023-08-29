extends CharacterBody2D

const MAX_SPEED = 80
const FRICTION = 500

var hp = 5 # puntos de vitalidad
var is_attacking = false
var state_machine

var is_hit = false
var is_dead = false

func take_damage(damage):
	is_hit = true
	hp -= damage
	print("hp: ", hp)
	if hp <= 0:
		is_dead = true

func _ready():
	state_machine = $AnimationTree["parameters/playback"]

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	input_vector.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		# movimiento
		state_machine.travel("run")
	else:
		state_machine.travel("idle")
		
	if Input.is_action_just_pressed("attack"):
		state_machine.travel("attack")
	
	velocity = MAX_SPEED * input_vector
	
	if is_hit:
		state_machine.travel("hit")
		is_hit = false
	if is_dead:
		state_machine.travel("death")
		$Timer.stop()
		velocity = Vector2.ZERO
	
	#print(input_vector)
	
	# si mira a la izquierda o derecha
	if velocity.x < 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x) * -1
	elif velocity.x > 0:
		$Sprite2D.scale.x = abs($Sprite2D.scale.x)
	
	move_and_slide()

func _on_hurtbox_area_entered(area):
	take_damage(1)
	$Timer.start()
	$Timer.one_shot = false

func _on_timer_timeout():
	take_damage(1)
	print("in damage")


func _on_hurtbox_area_exited(area):
	$Timer.stop()
	$Timer.one_shot = true
