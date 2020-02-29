# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Gburowaty Wieśniak")

define n = Character("Niemir")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene wioska

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    image wioska = im.Scale("wioska.jpg", 1920, 1080)
    image wiesniak = im.Scale("wiesniak.png", 1500, 900)

    show wiesniak

    # These display lines of dialogue.

    w "Czołem, panie bracie! Niech będzie pochwalony Jezus Chrystus! Co was sprowadza do naszej skromnej osady?"

    n "Pochwalony, panie bracie! Pragnę mówić z waszym rządcą."

    w "A wy kto żeście, że z panem wójtem pragniecie prawić?"

    n "Jam jest Niemir, wasz przyjaciel. Jakimż tonem wy gadacie?"

    w "Ton nie ważny, proszę ja was, mam zagadkę - podam zaraz."

    w "Patrzcież ludy! Anteprener chce pokazać nam swą cenę! Jest zagadka na tym słupie a na razie mam was w dupie!"


    # This ends the game.

    return
