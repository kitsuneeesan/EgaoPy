from PIL import Image, ImageFont, ImageDraw
from werkzeug.utils import secure_filename
from datetime import datetime
import random
import base64
import text
import io

class Egao():

    def _get_random_text(self):
        if self.is_rin_birthday:
            return text.happy_birthday
        else:
            n = random.randint(0,len(text.kotoba)-1)
            return text.kotoba[n]

    def _editor(self):
        # Load Fonts
        Consola16 = ImageFont.truetype("static/font/CONSOLA.TTF", 16)
        JakobsHandwriting28 = ImageFont.truetype("static/font/Jakob's-Handwriting.ttf", 28)
        JakobsHandwriting40 = ImageFont.truetype("static/font/Jakob's-Handwriting.ttf", 40)
        SanafonMugi18 = ImageFont.truetype("static/font/SNsanafonMugiV260.ttf", 18)
        SanafonMugi28 = ImageFont.truetype("static/font/SNsanafonMugiV260.ttf", 28)

        # Create Background
        bg_widht, bg_height = (600, 745)
        img = Image.new("RGB", (bg_widht, bg_height), (255, 255, 255))

        img_2 = Image.open(io.BytesIO(self.raw_photo))
        width, height = img_2.size

        if height >= width:
            x = height - width
            left = 0
            top = x/2
            right = width
            bottom = x/2+width
        else:
            x = width - height
            left = x/2
            top = 0
            right = x/2+height
            bottom = height
        
        img_2 = img_2.crop((left, top, right, bottom))
        img_2 = img_2.resize((556,556))

        # Merge Image
        img.paste(img_2, (22,58))

        # Texting Image
        draw = ImageDraw.Draw(img)
        draw.text((395, 30), "egao-py.herokuapp.com", (41, 41, 41), font=Consola16)
        draw.text((20, 11), self.date.strftime("%A %d %B %Y"), (41, 41, 41), font=JakobsHandwriting28)
        draw.text((506, 9), "その笑顔", (41, 41, 41), font=SanafonMugi18)
        
        # Random Text
        msg = self._get_random_text()
        text_w, text_h = SanafonMugi28.getsize(msg)
        text_y = bg_height - (bg_height - (text_h + 614))
        draw.text(((bg_widht-text_w)/2, text_y), msg, (71, 71, 71), font=SanafonMugi28)
        
        data = io.BytesIO()

        img.save(data, "PNG")
        return base64.b64encode(data.getvalue()) 

    def __init__(self, raw_photo, date):
        self.raw_photo = raw_photo
        self.date = datetime.strptime(date, '%m/%d/%Y, %H:%M:%S %p')
        rin_birthday = datetime.strptime(f'6/25/{self.date.year}', '%m/%d/%Y')
        self.is_rin_birthday = True if self.date.date() == rin_birthday.date() else False