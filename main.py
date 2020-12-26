import pywhatkit

# config for getting secret phone no from env
import os
from dotenv import load_dotenv

load_dotenv()
# config ends

pywhatkit.sendwhatmsg(os.getenv("phone"), 'This is a message from a whatsapp bot', 20, 33)

# or you can

pywhatkit.sendwhatmsg('phone-no', 'message', 'hour', 'minutes')

# and that will work fellows