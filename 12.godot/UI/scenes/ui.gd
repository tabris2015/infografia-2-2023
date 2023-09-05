extends Control


# Called when the node enters the scene tree for the first time.
func _ready():
	$MarginContainer/VBoxContainer/HBoxContainer2/Button.connect("button_down", _on_button1_down)
	$MarginContainer/VBoxContainer/HBoxContainer2/Button2.connect("button_down", _on_button2_down)
	$MarginContainer/VBoxContainer/HBoxContainer2/Button3.connect("button_down", _on_button3_down)
	$MarginContainer/VBoxContainer/HBoxContainer2/Button4.connect("button_down", _on_button4_down)

func _on_button1_down():
	print("button1")

func _on_button2_down():
	print("button2")

func _on_button3_down():
	print("button3")

func _on_button4_down():
	print("button4")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
