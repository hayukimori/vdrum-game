import os, sys
from ursina import *
import configparser
#import vlc


parser = configparser.ConfigParser()
app = Ursina()

class Cardinal:
	def __init__(self):
		print("Cardinal started")


	def defineConsts():
		Cardinal.defineColors()
		Cardinal.defineVideo()
		Cardinal.defineSounds()
		Cardinal.defineTextures()
		Cardinal.defineKeys()
		Cardinal.defineVolume()
		Cardinal.defineAudio()

	def defineColors():
		global kickl_color
		global kickr_color
		global snare_color
		global tom1_color
		global tom2_color
		global tom3_color
		global crashm_color
		global crashl_color
		global crashr_color
		global ride_color
		global close_hh_color
		global open_hh_color
		global floortom_color


		kickl_color = color.rgb(192,192,192)
		kickr_color = color.rgb(192,192,192)
		snare_color = color.rgb(255,204,255)
		tom1_color = color.rgb(153,153,255)
		tom2_color = color.rgb(102,102,255)
		tom3_color = color.rgb(51,51,255)
		crashm_color = color.rgb(204,204,0)
		crashl_color = color.rgb(255,255,0)
		crashr_color = color.rgb(255,255,51)
		ride_color = color.rgb(255,255,153)
		close_hh_color = color.rgb(225,229,204)
		open_hh_color = color.rgb(255,204,153)
		floortom_color = color.rgb(0,0,255)
		


	def defineVideo():
		window.title = "I don't have any name to set"
		window.borderless = False
		window.fullscreen = False
		window.exit_button.visible = False
		window.fps_counter.enabled = True


	def defineSounds():

		global kickl_sound
		global kickr_sound
		global snare_sound
		global tom1_sound
		global tom2_sound
		global tom3_sound
		global crashm_sound
		global crashl_sound
		global crashr_sound
		global ride_sound
		global close_hh_sound
		global open_hh_sound
		global floortom_sound
		

		kickl_sound = drumkit + "kick.mp3"
		kickr_sound = drumkit + "kick.mp3"
		snare_sound = drumkit + "snare.mp3"
		tom1_sound = drumkit + "tom1.mp3"
		tom2_sound = drumkit + "tom2.mp3"
		tom3_sound = drumkit + "tom3.mp3"
		crashm_sound = drumkit + "crashm.mp3"
		crashl_sound = drumkit + "crashl.mp3"
		crashr_sound = drumkit + "crashr.mp3"
		ride_sound = drumkit + "ride.mp3"
		close_hh_sound = drumkit + "closehh.mp3"
		open_hh_sound = drumkit + "openhh.mp3"
		floortom_sound = drumkit + "floor.mp3"


	def defineTextures():
		## ==> Define texturas
		global bg_texture
		global kickl_texture
		global kickr_texture
		global snare_texture
		global tom1_texture
		global tom2_texture
		global tom3_texture
		global crashm_texture
		global crashl_texture
		global crashr_texture
		global ride_texture
		global closehhl_texture
		global openhhl_texture
		global floortom_texture

				


		## ==> Define texturas
		bg_texture = drumkit + "fundo"
		kickl_texture = drumkit + "kickl"
		kickr_texture = drumkit + "kickr"
		snare_texture = drumkit + "snare"
		tom1_texture = drumkit + "tom1"
		tom2_texture = drumkit + "tom2"
		tom3_texture = drumkit + "tom3"
		crashm_texture = drumkit + "crashm" 
		crashl_texture = drumkit + "crashl"
		crashr_texture = drumkit + "crashr"
		ride_texture = drumkit + "ride"
		closehhl_texture = drumkit + "closehhl"
		openhhl_texture = drumkit + "openhhl"
		floortom_texture = drumkit + "floorr"

		
	def defineKeys():
		global kickl_key
		global kickr_key
		global snare_key
		global close_hh_key
		global open_hh_key
		global crashl_key
		global crashm_key
		global crashr_key
		global ride_key
		global tom1_key
		global tom2_key
		global tom3_key
		global floortom_key

		kickl_key = parser.get('keys', 'kickl_key')
		kickr_key = parser.get('keys', 'kickr_key')
		snare_key = parser.get('keys', 'snare_key')
		close_hh_key = parser.get('keys', 'close_hh_key')
		open_hh_key = parser.get('keys', 'open_hh_key')
		crashl_key = parser.get('keys', 'crashl_key')
		crashm_key = parser.get('keys', 'crashm_key')
		crashr_key = parser.get('keys', 'crashr_key')
		ride_key = parser.get('keys', 'ride_key')
		tom1_key = parser.get('keys', 'tom1_key')
		tom2_key = parser.get('keys', 'tom2_key')
		tom3_key = parser.get('keys', 'tom3_key')
		floortom_key = parser.get('keys', 'floortom_key')


		snare_key = eval(snare_key)
		close_hh_key = eval(close_hh_key)
		open_hh_key = eval(open_hh_key)
		crashl_key = eval(crashl_key)
		crashm_key = eval(crashm_key)
		crashr_key = eval(crashr_key)
		ride_key = eval(ride_key)
		floortom_key = eval(floortom_key)


	def defineVolume():
		global kickr_volume
		global kickl_volume
		global snare_volume
		global close_hh_volume
		global open_hh_volume
		global crashl_volume
		global crashm_volume
		global crashr_volume
		global ride_volume
		global floortom_volume

		global tom1_volume
		global tom2_volume
		global tom3_volume


		kickr_volume = eval(parser.get('volume', 'kickr_vol'))
		kickl_volume = eval(parser.get('volume', 'kickl_vol'))
		snare_volume = eval(parser.get('volume', 'snare_vol'))
		close_hh_volume = eval(parser.get('volume', 'close_hh_vol'))
		open_hh_volume = eval(parser.get('volume', 'open_hh_vol'))
		crashl_volume = eval(parser.get('volume', 'crashl_vol'))
		crashm_volume = eval(parser.get('volume', 'crashm_vol'))
		crashr_volume = eval(parser.get('volume', 'crashr_vol'))
		ride_volume = eval(parser.get('volume', 'ride_vol'))
		floortom_volume = eval(parser.get('volume', 'floortom_vol'))
		tom1_volume = eval(parser.get('volume', 'tom1_vol'))
		tom2_volume = eval(parser.get('volume', 'tom2_vol'))
		tom3_volume = eval(parser.get('volume', 'tom3_vol'))


	def defineAudio():
		# DualKey
		global kick_audio
		global snare_audio
		global close_hh_audio
		global open_hh_audio
		global crashl_audio
		global crashm_audio
		global crashr_audio
		global ride_audio
		global floortom_audio

		global tom1_audio
		global tom2_audio
		global tom3_audio


		kick_audio = Audio(kickl_sound, volume=kickl_volume, autoplay=False)
		snare_audio = Audio(snare_sound, volume=snare_volume, autoplay=False)
		close_hh_audio = Audio(close_hh_sound, volume=close_hh_volume, autoplay=False)
		open_hh_audio = Audio(open_hh_sound, volume=open_hh_volume, autoplay=False)
		crashl_audio = Audio(crashl_sound, volume=crashl_volume, autoplay=False)
		crashm_audio = Audio(crashm_sound, volume=crashm_volume, autoplay=False)
		crashr_audio = Audio(crashr_sound, volume=crashr_volume, autoplay=False)
		ride_audio = Audio(ride_sound, volume=ride_volume, autoplay=False)
		floortom_audio = Audio(floortom_sound, volume=floortom_volume, autoplay=False)

		tom1_audio = Audio(tom1_sound, volume=tom1_volume, autoplay=False)
		tom2_audio = Audio(tom2_sound, volume=tom2_volume, autoplay=False)
		tom3_audio = Audio(tom3_sound, volume=tom3_volume, autoplay=False)





#############################################
#	GET USER INPUT FUNCTION (FROM URSINA)   #
#############################################


class HitObject(Entity):
	def __init__(self, parent, color=color.random_color()):
		super().__init__()

		self.model='cube'
		self.scale_y = .2
		self.parent = parent
		self.collider = 'mesh'
		self.color = color
		self.rotation_x = 90


		self.destroy(delay=5)

	def update(self):
		self.y += 30 *time.dt


	def destroy(self, delay):
		destroy(self, delay=delay)


class Game(Entity):
	def __init__(self):
		super().__init__()

		self.rotation_x = 90
		self.y = -4
		self.z = 4
		self.scale = .5

		self.bar1 = Entity(
			model='cube',
			parent=self,
			x=8,
			y=100,
			scale_y=200,
			scale_x=.3,
			scale_z=.3
			)

		self.bar2 = Entity(
			model='cube',
			parent=self,
			x=-8,
			y=100,
			scale_y=200,
			scale_x=.3,
			scale_z=.3
			)


		self.hatsbar2 = Entity(
			model='cube',
			parent=self,
			x=-5,
			y=100,
			z=-4,
			scale_x=.1,
			scale_z=.1,
			scale_y=200
			)

		self.hatsbar = Entity(
			model='cube',
			parent=self,
			x=-1.3,
			y=100,
			z=-4,
			scale_x=.1,
			scale_z=.1,
			scale_y=200
			)

		self.hatsbar3 = Entity(
			model='cube',
			parent=self,
			x=2,
			y=100,
			z=-4,
			scale_x=.1,
			scale_z=.1,
			scale_y=200
			)

		self.hatsbar4 = Entity(
			model='cube',
			parent=self,
			x=5,
			y=100,
			z=-4,
			scale_x=.1,
			scale_z=.1,
			scale_y=200
			)



		self.kickl = Entity(
			model='cube',
			color=color.rgba(0,0,255,150),#texture=kickl_texture, 
			scale=1.2,
			y=0, 
			x=-1.7, 
			z=1,
			scale_z=.3,
			scale_x=3,
			parent=self
			)

		self.kickr = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=kickr_texture, 
			scale=1.2,
			y=0, 
			x=1.6, 
			z=1,
			scale_z=.3,
			scale_x=3,
			parent=self
			)

		self.snare = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=snare_texture, 
			scale=1.2,
			y=0, 
			x=0, 
			z=0,
			parent=self
			)

		self.tom1 = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=tom1_texture, 
			scale=1.2,
			y=0, 
			x=-2.2, 
			z=0,
			parent=self
			)

		self.tom2 = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=tom2_texture, 
			scale=1.2,
			y=0, 
			x=3, 
			z=0,
			parent=self
			)

		self.tom3 = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=tom3_texture, 
			scale=1.2,
			y=0, 
			x=4.6, 
			z=0,
			parent=self
			)

		self.crashm = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=crashm_texture, 
			scale=1.2,
			y=0, 
			x=self.hatsbar.x, 
			z=-4,
			parent=self
			)

		self.crashl = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=crashl_texture, 
			scale=1.2,
			y=0, 
			x=self.hatsbar2.x, 
			z=-4,
			parent=self
			)

		self.crashr = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=crashr_texture, 
			scale=1.2,
			y=0, 
			x=self.hatsbar3.x, 
			z=-4,
			parent=self
			)

		self.ride = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=ride_texture, 
			scale=1.2,
			y=0, 
			x=self.hatsbar4.x, 
			z=-4,
			parent=self
			)

		self.close_hh = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=closehhl_texture, 
			scale=1.2,
			y=0, 
			x=-4, 
			z=0,
			parent=self
			)

		self.open_hh = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=openhhl_texture, 
			scale=1.2,
			y=0, 
			x=-6,
			z=0,
			parent=self
			)

		self.floortom = Entity(
			model='cube', 
			color=color.rgba(0,0,255,150),#texture=floortom_texture, 
			scale=1.2,
			y=0, 
			x=6.4, 
			z=0,
			parent=self
			)




	def input(self, key):

		# Kick L + R Sound
		if key == kickl_key or key == kickr_key:
			_tmpObj = HitObject(parent=self.kickr, color=kickl_color)
			camera.shake(duration=.2, magnitude=.2, speed=.05, direction=(.5,.5))
			kick_audio.play()

		# Snare Sound
		if key == snare_key[0] or key == snare_key[1]:
			_tmpObj = HitObject(parent=self.snare, color=snare_color)
			camera.shake(duration=.5, magnitude=.1, speed=.3, direction=(1,1))
			snare_audio.play()

		# Tom 1 Sound
		if key == tom1_key:
			_tmpObj = HitObject(parent=self.tom1, color=tom1_color)
			tom1_audio.play()

		# Tom 2 Sound
		if key == tom2_key:
			_tmpObj = HitObject(parent=self.tom2, color=tom2_color)
			tom2_audio.play()

		# Tom 3 Sound
		if key == tom3_key:
			_tmpObj = HitObject(parent=self.tom3, color=tom3_color)
			tom3_audio.play()

		# CrashM Sound
		if key == crashm_key[0] or key == crashm_key[1]:
			_tmpObj = HitObject(parent=self.crashm, color=crashm_color)
			crashm_audio.play()

		# Crash R Sound
		if key == crashr_key[0] or key == crashr_key[1]:
			_tmpObj = HitObject(parent=self.crashr, color=crashr_color)
			crashr_audio.play()

		# Crash L Sound
		if key == crashl_key[0] or key == crashl_key[1]:
			_tmpObj = HitObject(parent=self.crashl, color=crashl_color)
			crashl_audio.play()

		# Ride Sound
		if key == ride_key[0] or key == ride_key[1]:
			_tmpObj = HitObject(parent=self.ride, color=ride_color)
			ride_audio.play()

		# Close HH Sound
		if key == close_hh_key[0] or key == close_hh_key[1]:
			_tmpObj = HitObject(parent=self.close_hh, color=close_hh_color)
			# Stop open hihat if is playing 
			if open_hh_audio.playing == True:
				open_hh_audio.stop()
			close_hh_audio.play()

		# Open HH Sound
		if key == open_hh_key[0] or key == open_hh_key[1]:
			_tmpObj = HitObject(parent=self.open_hh, color=open_hh_color)
			if open_hh_audio.playing:
			    new_audio = Audio(open_hh_sound)
			else:
			    open_hh_audio.play()
			

		# FloorTom Sound
		if key == floortom_key[0] or key == floortom_key[1]:
			_tmpObj = HitObject(parent=self.floortom, color=floortom_color)
			floortom_audio.play()
	


def input(key):
	if key == 'f1':
		game.enabled = not game.enabled


if __name__ == "__main__":

	try:
		parser.read("config.ini")
		drumkit = parser.get('general', 'drumkit') + "/"
		Cardinal.defineConsts()

	except configparser.NoSectionError:
		print("\n\n[ERROR]: Arquivo de configuração inválido\n\n")
		sys.exit(1)

	except Exception as e:
		print("Ocorreu um erro desconhecido ou arquivo 'config.ini' inexistente")
		print(f"\n\nTexto do erro: {str(e)}")
		sys.exit(1)


	camera.ortographic = True
	ec = EditorCamera()


	background	= Entity(
		model='quad', 
		#texture=bg_texture, 
		color=color.rgba(0,0,0,0),
		scale=(16*camera.aspect_ratio,9*camera.aspect_ratio),
		z=.3, 
		y=-.5
		)
	window.color = color.black

	#current_song = vlc.MediaPlayer()

	game = Game()
	game.enabled = 1


	app.run()
