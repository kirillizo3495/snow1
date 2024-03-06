from PIL import Image, ImageDraw


im = Image.new('RGB',(1920,1080),(230,230,230))
draw = ImageDraw.Draw(im)

draw.ellipse((200,640,500,910), fill='white',outline=(0,0,0))
draw.ellipse((230,484,470,700), fill='white',outline=(0,0,0))
draw.ellipse((260,374,440,534), fill='white',outline=(0,0,0))

draw.ellipse((320,427,330,437), fill='black',outline=(0,0,0))
draw.ellipse((320,427,330,437), fill='black',outline=(0,0,0))
draw.ellipse((370,427,380,437), fill='black',outline=(0,0,0))
draw.ellipse((320,487,330,497), fill='black',outline=(0,0,0))
draw.ellipse((370,487,380,497), fill='black',outline=(0,0,0))
draw.ellipse((360,502,370,512), fill='black',outline=(0,0,0))
draw.ellipse((330,502,340,512), fill='black',outline=(0,0,0))
draw.ellipse((345,507,355,517), fill='black',outline=(0,0,0))

draw.ellipse((1050,750,1100,800), fill='black',outline=(0,0,0))


draw.polygon(
    xy=(
        (350,450),
        (410,457),
        (350,464)
    ), fill='orange',outline=(0,0,0)
)

draw.polygon(
    xy=(
        (1000,800),
        (1300,450),
        (1600,800)
    ), fill='green',outline=(0,0,0)
)
draw.polygon(
    xy=(
        (1060,634),
        (1300,335),
        (1540,634)
    ), fill='green',outline=(0,0,0)
)
draw.polygon(
    xy=(
        (1120,480),
        (1300,250),
        (1480,480)
    ), fill='green',outline=(0,0,0)
)
draw.polygon(
    xy=(
        (1180,330),
        (1300,150),
        (1420,330)
    ), fill='green',outline=(0,0,0)
)

draw.ellipse((1050,740,1100,790), fill='red',outline=(0,0,0))
draw.ellipse((1150,650,1200,700), fill='blue',outline=(0,0,0))
draw.ellipse((1250,720,1300,770), fill='orange',outline=(0,0,0))
draw.ellipse((1350,685,1400,735), fill='red',outline=(0,0,0))
draw.ellipse((1450,735,1500,785), fill='purple',outline=(0,0,0))
draw.ellipse((1350,685,1400,735), fill='blue',outline=(0,0,0))
draw.ellipse((1100,580,1150,630), fill='purple',outline=(0,0,0))
draw.ellipse((1200,520,1250,570), fill='red',outline=(0,0,0))
draw.ellipse((1300,550,1350,600), fill='orange',outline=(0,0,0))
draw.ellipse((1400,540,1450,590), fill='blue',outline=(0,0,0))
draw.ellipse((1180,420,1230,470), fill='red',outline=(0,0,0))
draw.ellipse((1280,380,1330,430), fill='blue',outline=(0,0,0))
draw.ellipse((1370,400,1420,450), fill='orange',outline=(0,0,0))
draw.ellipse((1230,240,1280,290), fill='purple',outline=(0,0,0))
draw.ellipse((1305,220,1355,270), fill='blue',outline=(0,0,0))
draw.rectangle((1250,800,1350,910), fill='brown',outline=(0,0,0))
draw.rectangle((0,910,1920,1080), fill='white',outline=(0,0,0))
draw.polygon(
    xy=(
        (1300,180),
        (1365,230),
        (1330,160)
    ),fill='gold',outline=(0,0,0)
)
draw.polygon(
    xy=(
        (1300,180),
        (1235,230),
        (1270,160)
    ),fill='gold',outline=(0,0,0)
)

draw.polygon(
    xy=(
        (1300,180),
        (1220,140),
        (1380,140)
    ),fill='gold',outline=(0,0,0)
)
draw.polygon(
    xy=(
        (1280,140),
        (1300,90),
        (1320,140)
    ),fill='gold',outline=(0,0,0)
)


im.show()