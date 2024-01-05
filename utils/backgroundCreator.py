from PIL import Image, ImageDraw

WIDTH = 1384
HEIGHT = 763
CIRCLE_RADIUS = 54
M = 4

COORDINATES = [
    [692, 284.5],       # START
    [1003.5, 109],      # Y
    [1024.5, 229.5],    # X
    [917.5, 302],       # B
    [910, 570.5],       # A
    [104.5, 260],       # L
    [896.5, 180.5],     # R
    [1150.5, 220.5],    # Z
    [1277.5, 271],      # UP
    [353, 217.5],       # DOWN
    [460, 291.5],       # RIGHT
    [226.5, 208.5],     # LEFT
    [441.5, 573.5],     # MX
    [528.5, 661],       # MY
    [787, 535.5],       # C LEFT
    [997.5, 485.5],     # C RIGHT
    [874.5, 448.5],     # C UP
    [823, 657],         # C DOWN
    [1129.5, 100],      # LS
    [1257.5, 149.5],    # MS
    [373.5, 102.5]      # UP2
]

def createImagesWithSolidColor(bgColor, activeColor):
    drawButtonBackground(bgColor)
    drawIndividualButtons(activeColor)

def createImagesWithSinglePicture(picture, activeColor):
    drawButtonBackgroundWithImage(picture)
    drawIndividualButtons(activeColor)

def createImagesWithTwoPictures(bgPicture, activePicture):
    drawButtonBackgroundWithImage(bgPicture)
    drawIndividualButtonsWithPicture(activePicture)


def drawButtonBackground(color):
    # Create a transparent canvas
    canvas_size = (WIDTH*M, HEIGHT*M)
    canvas_color = (0, 0, 0, 0)  # RGBA (red, green, blue, alpha)
    canvas = Image.new("RGBA", canvas_size, canvas_color)

    # Create a drawing object
    draw = ImageDraw.Draw(canvas)

    # Draw all the circles from the coordinates
    for coordinate in COORDINATES:
        radius = CIRCLE_RADIUS * M
        circle_center = (coordinate[0] * M, coordinate[1] * M) 

        draw.ellipse(
            [
                circle_center[0] - radius,
                circle_center[1] - radius,
                circle_center[0] + radius,
                circle_center[1] + radius,
            ],
            fill=color
        )

    # Reize to use antialiasing and save it as PNG
    canvas = canvas.resize((WIDTH, HEIGHT), resample=Image.LANCZOS)
    canvas.save("buttons.png", "PNG")

def drawIndividualButtons(color):
    i = 1;
    # Draw all the circles from the coordinates
    for coordinate in COORDINATES:

        # Create a transparent canvas
        canvas_size = (WIDTH*M, HEIGHT*M)
        canvas_color = (0, 0, 0, 0)  # RGBA (red, green, blue, alpha)
        canvas = Image.new("RGBA", canvas_size, canvas_color)

        # Create a drawing object
        draw = ImageDraw.Draw(canvas)

        radius = CIRCLE_RADIUS * M
        circle_center = (coordinate[0] * M, coordinate[1] * M) 

        draw.ellipse(
            [
                circle_center[0] - radius,
                circle_center[1] - radius,
                circle_center[0] + radius,
                circle_center[1] + radius,
            ],
            fill=color
        )

        # Reize to use antialiasing and save it as PNG
        canvas = canvas.resize((WIDTH, HEIGHT), resample=Image.LANCZOS)
        canvas.save(str(i) + ".png", "PNG")
        i = i + 1


def drawButtonBackgroundWithImage(image_path):
    SQUARE = CIRCLE_RADIUS * M * 2

    # Load the image
    original_image = Image.open(image_path)

    # Resize the image to a square
    size = min(original_image.size)
    square_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    square_image.paste(original_image, ((size - original_image.width) // 2, (size - original_image.height) // 2))

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the circular mask
    circular_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    circular_image.paste(square_image, mask=mask)
    circular_image.thumbnail((SQUARE, SQUARE))

    #Resize the image to button size
    buttonImage = Image.new("RGBA", (SQUARE, SQUARE), (0, 0, 0, 0))
    buttonImage.paste(circular_image)

    # Create a transparent canvas
    canvas_size = (WIDTH*M, HEIGHT*M)
    canvas_color = (0, 0, 0, 0)  # RGBA (red, green, blue, alpha)
    canvas = Image.new("RGBA", canvas_size, canvas_color)

    # Paste the image in all of the coordinates
    for coordinate in COORDINATES:
        canvas.paste(buttonImage, (int(coordinate[0] * M) - SQUARE // 2, int(coordinate[1] * M) - SQUARE // 2))

    # Reize to use antialiasing and save it as PNG
    canvas = canvas.resize((WIDTH, HEIGHT), resample=Image.LANCZOS)
    canvas.save("buttons.png", "PNG")



def drawIndividualButtonsWithPicture(image_path):
    SQUARE = CIRCLE_RADIUS * M * 2

    # Load the image
    original_image = Image.open(image_path)

    # Resize the image to a square and scale it if it is too small
    size = min(original_image.size)
    square_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    square_image.paste(original_image, ((size - original_image.width) // 2, (size - original_image.height) // 2))

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the circular mask
    circular_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    circular_image.paste(square_image, mask=mask)
    circular_image.thumbnail((SQUARE, SQUARE))

    #Resize the image to button size
    buttonImage = Image.new("RGBA", (SQUARE, SQUARE), (0, 0, 0, 0))
    buttonImage.paste(circular_image)

    i = 1;
    for coordinate in COORDINATES:

        # Create a transparent canvas
        canvas_size = (WIDTH*M, HEIGHT*M)
        canvas_color = (0, 0, 0, 0)  # RGBA (red, green, blue, alpha)
        canvas = Image.new("RGBA", canvas_size, canvas_color)

        canvas.paste(buttonImage, (int(coordinate[0] * M) - SQUARE // 2, int(coordinate[1] * M) - SQUARE // 2))

        # Reize to use antialiasing and save it as PNG
        canvas = canvas.resize((WIDTH, HEIGHT), resample=Image.LANCZOS)
        canvas.save(str(i) + ".png", "PNG")
        i = i + 1

#createImagesWithSolidColor((0, 0, 0), (255, 255, 255))
#createImagesWithSinglePicture("test.png", (255, 255, 255))
createImagesWithTwoPictures("test1.png", "test2.png")