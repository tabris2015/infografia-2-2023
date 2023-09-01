extends Marker2D

signal new_goal(target_position)

func _input(event):
	if event.is_action_pressed("clic"):
		global_position = get_global_mouse_position()
		emit_signal("new_goal", global_position)
