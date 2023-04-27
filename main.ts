input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    shoot = game.createSprite(player.get(LedSpriteProperty.X), player.get(LedSpriteProperty.Y))
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 1266, 255, 0, 40, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    for (let index = 0; index < 4; index++) {
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(10)
        if (_01.isDeleted()) {
        	
        } else if (_01.isTouching(shoot)) {
            _01.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_02.isDeleted()) {
        	
        } else if (_02.isTouching(shoot)) {
            _02.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_03.isDeleted()) {
        	
        } else if (_03.isTouching(shoot)) {
            _03.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_04.isDeleted()) {
        	
        } else if (_04.isTouching(shoot)) {
            _04.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_05.isDeleted()) {
        	
        } else if (_05.isTouching(shoot)) {
            _05.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_06.isDeleted()) {
        	
        } else if (_06.isTouching(shoot)) {
            _06.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_07.isDeleted()) {
        	
        } else if (_07.isTouching(shoot)) {
            _07.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
        if (_08.isDeleted()) {
        	
        } else if (_08.isTouching(shoot)) {
            _08.delete()
            music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 3808, 1356, 255, 0, 100, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
            game.addScore(1)
            shoot.delete()
        }
    }
    basic.pause(50)
    shoot.delete()
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
})
let shoot: game.LedSprite = null
let _08: game.LedSprite = null
let _07: game.LedSprite = null
let _06: game.LedSprite = null
let _05: game.LedSprite = null
let _04: game.LedSprite = null
let _03: game.LedSprite = null
let _02: game.LedSprite = null
let _01: game.LedSprite = null
let player: game.LedSprite = null
player = game.createSprite(2, 4)
_01 = game.createSprite(1, 1)
_02 = game.createSprite(2, 1)
_03 = game.createSprite(3, 1)
_04 = game.createSprite(4, 1)
_05 = game.createSprite(1, 0)
_06 = game.createSprite(2, 0)
_07 = game.createSprite(3, 0)
_08 = game.createSprite(4, 0)
basic.forever(function () {
    if (_01.isDeleted()) {
    	
    } else if (_01.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_02.isDeleted()) {
    	
    } else if (_02.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_03.isDeleted()) {
    	
    } else if (_03.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_04.isDeleted()) {
    	
    } else if (_04.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_05.isDeleted()) {
    	
    } else if (_05.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_06.isDeleted()) {
    	
    } else if (_06.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_08.isDeleted()) {
    	
    } else if (_08.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_07.isDeleted()) {
    	
    } else if (_07.isTouching(player)) {
        player.delete()
        music.startMelody(music.builtInMelody(Melodies.Baddy), MelodyOptions.Once)
        game.gameOver()
    }
})
basic.forever(function () {
    if (_01.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _01.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _01.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_02.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _02.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _02.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_03.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _03.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _03.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_04.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _04.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _04.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_05.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _05.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _05.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_06.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _06.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _06.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_07.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _07.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _07.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    if (_08.isDeleted()) {
        basic.pause(9999999999)
    } else {
        for (let index = 0; index < 1; index++) {
            _08.change(LedSpriteProperty.X, -1)
            basic.pause(500)
        }
        for (let index = 0; index < 1; index++) {
            _08.change(LedSpriteProperty.X, 1)
            basic.pause(500)
        }
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_07.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _07.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_01.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _01.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_02.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _02.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_08.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _08.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_03.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _03.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_04.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _04.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_05.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _05.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(3500)
    if (_06.isDeleted()) {
        basic.pause(9999999999)
    } else {
        _06.change(LedSpriteProperty.Y, 1)
    }
})
basic.forever(function () {
    basic.pause(14000)
    game.gameOver()
})
basic.forever(function () {
    if (_01.isDeleted() && (_02.isDeleted() && (_03.isDeleted() && (_04.isDeleted() && (_05.isDeleted() && (_06.isDeleted() && (_07.isDeleted() && _08.isDeleted()))))))) {
        basic.showString("YOU WIN!      KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY! KUBAJEGAY!")
    }
})
