from PIL import Image, ImageDraw, ImageFont, ExifTags
from PIL.ExifTags import TAGS
from datetime import datetime

def insert_timestamp_from_filename_into_image(path_to_image:str, 
ignorable_string:str,
output_filename:str = "", 
distance_to_border:int = 5, 
color_of_timestamp:tuple = (0,0,0), 
size_of_timestamp:int = 20):
    
    image = Image.open(path_to_image)

    #Place the timestamp in the bottom left hand corner with a certain distance to the border
    pos_of_timestamp = (distance_to_border, image.height-size_of_timestamp-distance_to_border);

    #Only get the filename with its extension of the filepath
    filename_with_extension = path_to_image.split("/")[-1]

    filename = filename_with_extension
    #Filter out the file ending (.png, .jpeg ...)
    for i in range(len(filename)-1, 0, -1):
        if(filename[i]=="."):
            filename = filename[:i]

    #Filter out the ignorable part of the string to only get the timestamp
    timestamp = filename.replace(ignorable_string, "")

    #Get an object back that allows for drawing on an image
    drawable_image = ImageDraw.Draw(image)

    #Load the font file from the local directory and print the text on to the image
    font = ImageFont.truetype('arial.ttf',size_of_timestamp)
    drawable_image.text(pos_of_timestamp, timestamp, color_of_timestamp, font=font)

    #Either overwrite the image or save it as a new image
    if(output_filename==""):
        image.save(filename_with_extension)
    else:
        image.save(output_filename)

def insert_timestamp_into_image(path_to_image:str, 
output_filename:str = "", 
distance_to_border:int = 5, 
color_of_timestamp:tuple = (0,0,0), 
size_of_timestamp:int = 20):
    
    image = Image.open(path_to_image)

    #Place the timestamp in the bottom left hand corner with a certain distance to the border
    pos_of_timestamp = (distance_to_border, image.height-size_of_timestamp-distance_to_border);

    #Only get the filename with its extension of the filepath
    filename_with_extension = path_to_image.split("/")[-1]

    #Get the current timestamp
    timestamp = str(datetime.now());

    #Get an object back that allows for drawing on an image
    drawable_image = ImageDraw.Draw(image)

    #Load the font file from the local directory and print the text on to the image
    font = ImageFont.truetype('arial.ttf',size_of_timestamp)
    drawable_image.text(pos_of_timestamp, timestamp, color_of_timestamp, font=font)

    #Either overwrite the image or save it as a new image
    if(output_filename==""):
        image.save(filename_with_extension)
    else:
        image.save(output_filename)

def insert_timestamp_from_imagedata_into_image(path_to_image:str, 
output_filename:str = "", 
distance_to_border:int = 5, 
color_of_timestamp:tuple = (0,0,0), 
size_of_timestamp:int = 20):
    
    image = Image.open(path_to_image)

    #Place the timestamp in the bottom left hand corner with a certain distance to the border
    pos_of_timestamp = (distance_to_border, image.height-size_of_timestamp-distance_to_border);

    #Only get the filename with its extension of the filepath
    filename_with_extension = path_to_image.split("/")[-1]

    exifdata = image.getexif();
    tag_id = 0
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        if(tag == "DateTime"):
            break


    #Get the current timestamp
    timestamp = str(exifdata.get(tag_id))

    #Get an object back that allows for drawing on an image
    drawable_image = ImageDraw.Draw(image)

    #Load the font file from the local directory and print the text on to the image
    font = ImageFont.truetype('arial.ttf',size_of_timestamp)
    drawable_image.text(pos_of_timestamp, timestamp, color_of_timestamp, font=font)

    #Either overwrite the image or save it as a new image
    if(output_filename==""):
        image.save(filename_with_extension)
    else:
        image.save(output_filename)


if __name__=="__main__":
    #insert_timestamp_from_filename_into_image("Image_2021-09-09_09-00-00.png", "Image_")
    insert_timestamp_from_filename_into_image("Image_2021-09-09_09-00-00.JPG", "Image_", "NewImage.JPG", distance_to_border=5, color_of_timestamp=(255,0,0), size_of_timestamp=50)
    #insert_timestamp_into_image("Image_2021-01-01_20-00-00.png")
    insert_timestamp_into_image("Image_2021-09-09_09-00-00.JPG", "NewImage2.JPG", distance_to_border=5, color_of_timestamp=(255,0,0), size_of_timestamp=50)
    #insert_timestamp_from_imagedata_into_image("Image_2021-09-09_09-00-00.png")
    insert_timestamp_from_imagedata_into_image("Image_2021-09-09_09-00-00.JPG", "NewImage3.JPG", distance_to_border=5, color_of_timestamp=(255,0,0), size_of_timestamp=50)
