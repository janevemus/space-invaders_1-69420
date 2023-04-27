def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(player.get(LedSpriteProperty.X),
        player.get(LedSpriteProperty.Y))
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            1266,
            255,
            0,
            40,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(10)
        if _01.is_deleted():
            pass
        elif _01.is_touching(shoot):
            _01.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _02.is_deleted():
            pass
        elif _02.is_touching(shoot):
            _02.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _03.is_deleted():
            pass
        elif _03.is_touching(shoot):
            _03.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _04.is_deleted():
            pass
        elif _04.is_touching(shoot):
            _04.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _05.is_deleted():
            pass
        elif _05.is_touching(shoot):
            _05.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _06.is_deleted():
            pass
        elif _06.is_touching(shoot):
            _06.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _07.is_deleted():
            pass
        elif _07.is_touching(shoot):
            _07.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
        if _08.is_deleted():
            pass
        elif _08.is_touching(shoot):
            _08.delete()
            music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                    3808,
                    1356,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
            game.add_score(1)
            shoot.delete()
    basic.pause(50)
    shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

shoot: game.LedSprite = None
_08: game.LedSprite = None
_07: game.LedSprite = None
_06: game.LedSprite = None
_05: game.LedSprite = None
_04: game.LedSprite = None
_03: game.LedSprite = None
_02: game.LedSprite = None
_01: game.LedSprite = None
player: game.LedSprite = None
player = game.create_sprite(2, 4)
_01 = game.create_sprite(1, 1)
_02 = game.create_sprite(2, 1)
_03 = game.create_sprite(3, 1)
_04 = game.create_sprite(4, 1)
_05 = game.create_sprite(1, 0)
_06 = game.create_sprite(2, 0)
_07 = game.create_sprite(3, 0)
_08 = game.create_sprite(4, 0)

def on_forever():
    if _01.is_deleted():
        pass
    elif _01.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever)

def on_forever2():
    if _02.is_deleted():
        pass
    elif _02.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever2)

def on_forever3():
    if _03.is_deleted():
        pass
    elif _03.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever3)

def on_forever4():
    if _04.is_deleted():
        pass
    elif _04.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever4)

def on_forever5():
    if _05.is_deleted():
        pass
    elif _05.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever5)

def on_forever6():
    if _06.is_deleted():
        pass
    elif _06.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever6)

def on_forever7():
    if _08.is_deleted():
        pass
    elif _08.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever7)

def on_forever8():
    if _07.is_deleted():
        pass
    elif _07.is_touching(player):
        player.delete()
        music.start_melody(music.built_in_melody(Melodies.BADDY), MelodyOptions.ONCE)
        game.game_over()
basic.forever(on_forever8)

def on_forever9():
    music.start_melody(music.built_in_melody(Melodies.WEDDING), MelodyOptions.ONCE)
basic.forever(on_forever9)

def on_forever10():
    if _01.is_deleted():
        basic.pause(9999999999)
    else:
        for index2 in range(1):
            _01.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index3 in range(1):
            _01.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever10)

def on_forever11():
    if _02.is_deleted():
        basic.pause(9999999999)
    else:
        for index4 in range(1):
            _02.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index5 in range(1):
            _02.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever11)

def on_forever12():
    if _03.is_deleted():
        basic.pause(9999999999)
    else:
        for index6 in range(1):
            _03.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index7 in range(1):
            _03.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever12)

def on_forever13():
    if _04.is_deleted():
        basic.pause(9999999999)
    else:
        for index8 in range(1):
            _04.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index9 in range(1):
            _04.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever13)

def on_forever14():
    if _05.is_deleted():
        basic.pause(9999999999)
    else:
        for index10 in range(1):
            _05.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index11 in range(1):
            _05.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever14)

def on_forever15():
    if _06.is_deleted():
        basic.pause(9999999999)
    else:
        for index12 in range(1):
            _06.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index13 in range(1):
            _06.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever15)

def on_forever16():
    if _07.is_deleted():
        basic.pause(9999999999)
    else:
        for index14 in range(1):
            _07.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index15 in range(1):
            _07.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever16)

def on_forever17():
    if _08.is_deleted():
        basic.pause(9999999999)
    else:
        for index16 in range(1):
            _08.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        for index17 in range(1):
            _08.change(LedSpriteProperty.X, 1)
            basic.pause(500)
basic.forever(on_forever17)

def on_forever18():
    basic.pause(3500)
    if _01.is_deleted():
        basic.pause(9999999999)
    else:
        _01.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever18)

def on_forever19():
    basic.pause(3500)
    if _02.is_deleted():
        basic.pause(9999999999)
    else:
        _02.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever19)

def on_forever20():
    basic.pause(3500)
    if _08.is_deleted():
        basic.pause(9999999999)
    else:
        _08.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever20)

def on_forever21():
    basic.pause(3500)
    if _03.is_deleted():
        basic.pause(9999999999)
    else:
        _03.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever21)

def on_forever22():
    basic.pause(3500)
    if _04.is_deleted():
        basic.pause(9999999999)
    else:
        _04.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever22)

def on_forever23():
    basic.pause(3500)
    if _05.is_deleted():
        basic.pause(9999999999)
    else:
        _05.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever23)

def on_forever24():
    basic.pause(3500)
    if _06.is_deleted():
        basic.pause(9999999999)
    else:
        _06.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever24)

def on_forever25():
    basic.pause(3500)
    if _07.is_deleted():
        basic.pause(9999999999)
    else:
        _07.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever25)

def on_forever26():
    if _01.is_deleted() and (_02.is_deleted() and (_03.is_deleted() and (_04.is_deleted() and (_05.is_deleted() and (_06.is_deleted() and (_07.is_deleted() and _08.is_deleted())))))):
        basic.show_string("YOU WIN!      KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY!")
basic.forever(on_forever26)

def on_forever27():
    basic.pause(14000)
    game.game_over()
basic.forever(on_forever27)
