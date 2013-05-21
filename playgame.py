from game import Game

options = {
	"title" : "So You Think You Know Greek Mythology, eh?",
	"size" : [700, 500],
	"bg_music_file" : 'music/bg_music.mp3',
	"bg_img_file" : 'img/bg_img.jpg',
	"correct_img_file" : 'img/correct.png',
	"incorrect_img_file" : 'img/incorrect.png',
	"correct_sound_file" : 'music/correct.ogg',
	"incorrect_sound_file" : 'music/incorrect.ogg',
	"font" : 'font/adonais.ttf',
	"fps" : 20,
	"menu_container_colour" : (142,160,135,200),
	"q_json_file" : 'questions.json'
}

if __name__ == "__main__":
	game = Game(options)
	game.run()