# only library that the new process need
from src.tools.generate_music import generator
import pathlib

PATH = pathlib.Path(__file__).parent

if __name__=="__main__":
    gn = generator(PATH / "assets" / "music" / "Halloween LOOP.wav")
    gn.start()

    import src.tools.tools as tl
    tl.MixeurAudio.gn = gn
    tl.MixeurAudio.music_factor = gn.sound_factor

    # import the game
    import src.pygame_edit
    from src.game import Game as game
    
    try:
        game.run()
    except SystemExit:
        gn.p.terminate()
        print("bye !")