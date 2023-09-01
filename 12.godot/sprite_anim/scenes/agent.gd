extends CharacterBody2D

@export var movement_speed: float = 100
@export var target: Node2D

@onready var nav_agent = $NavigationAgent2D

func _ready():
	nav_agent.path_desired_distance = 4.0 
	nav_agent.target_desired_distance = 4.0
	
	target.connect("new_goal", _on_new_goal)
	
	call_deferred("actor_setup")
	
func actor_setup():
	await get_tree().physics_frame
	nav_agent.target_position = target.position 
	
func _physics_process(delta):
	if nav_agent.is_navigation_finished():
		return
	
	var current_position = global_position
	var next_path_position = nav_agent.get_next_path_position()
	
	var direction = next_path_position - current_position
	direction = direction.normalized()
	
	velocity = direction * movement_speed
	
	move_and_slide()


func _on_new_goal(target_position):
	print(name, "new goal: ", target_position)
	nav_agent.target_position = target_position
