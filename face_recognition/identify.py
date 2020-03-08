import face_recognition
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("arial.ttf", 50)


image_of_ankur = face_recognition.load_image_file(
    './img/face_models/ankur.jpg')
ankur_face_encoding = face_recognition.face_encodings(image_of_ankur)[0]

image_of_arpit = face_recognition.load_image_file(
    './img/face_models/arpit.jpg')
arpit_face_encoding = face_recognition.face_encodings(image_of_arpit)[0]

image_of_shubham = face_recognition.load_image_file(
    './img/face_models/shubham2.jpg')
shubham_face_encoding = face_recognition.face_encodings(image_of_shubham)[0]


image_of_ds = face_recognition.load_image_file('./img/face_models/ds.jpg')
ds_face_encoding = face_recognition.face_encodings(image_of_ds)[0]

#  Create array of encodings and names

known_face_encodings = [
    ankur_face_encoding,
    arpit_face_encoding,
    shubham_face_encoding,
    ds_face_encoding,

]

known_face_names = [
    "Ankur",
    "Arpit Sahu",
    "Shubham Ranjan",
    "Divyanshu Shekhar"
]


#  Load test image to find faces in

test_image = face_recognition.load_image_file('./img/asd.jpg')

#  Find Faces
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL Format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (t, r, b, l), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown Person"

    # IF MATCH
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    #  Draw Box
    draw.rectangle(((l, t), (r, b)), outline=(0, 255, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((l, b - text_height - 90), (r, b)),
                   fill=(0, 0, 0), outline=(0, 255, 0))
    draw.text((l+6, b-text_height-75), name, fill=(0, 255, 0), font=font)

del draw

# Display image
pil_image.show()
