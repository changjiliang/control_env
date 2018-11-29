import pyglet
from pyglet.window import key
from pyglet.window import mouse


window = pyglet.window.Window(1920, 1080)

main_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

filename1 = '111.jpg'
filename2 = '1.jpg'
image = pyglet.image.load(filename1).get_texture(rectangle=True)
image.anchor_x = image.width//2
image.anchor_y = image.height//2
image_s = pyglet.image.load(filename2)

background = pyglet.sprite.Sprite(img=image, x=image.anchor_x,y=image.anchor_y,batch=main_batch, group=background)

S = pyglet.sprite.Sprite(img=image_s, x=400,y=450, batch=main_batch, group= foreground)

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()
    #image.blit(window.width//2, window.height//2, 0)


def on_mouse_press(x,y,button,modif):
    if button == mouse.LEFT:
        print('mouse left was pressed!')

    elif button == mouse.RIGHT:
        print('mouse right was pressed!')
    print(x)
    print(y)


def update(dt):
    if keys[key.LEFT]:
        S.x -= 0.5
    elif keys[key.RIGHT]:
        S.x += 0.5
    elif keys[key.UP]:
        S.y += 0.5
    elif keys[key.DOWN]:
        S.y -= 0.5
    if S.y > 1080:
        S.y = 1080
    elif S.y < 0:
        S.y = 0

    if S.x > 1920:
        S.x = 1920
    elif S.x < 0:
        S.x = 0


pyglet.clock.schedule_interval(update, 1/144.0)
pyglet.app.run()


