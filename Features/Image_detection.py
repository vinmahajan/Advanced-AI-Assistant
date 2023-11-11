from ..AI_Brains.Bard import Bard
import datetime
while True:
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename,'rb').read()
    # bard = BardCookies(cookie_dict=cookie_dict)
    results = Bard().ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "DataBase//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))