'''Created on 12/01/2018 @author: michaelnew'''

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageOrder(MessageSkyzeAbstract):
  '''A Stop Entry Order to be executed on an exchange'''

  def __init__(self, message_type, messsage_content):
    """Constructor"""
    super().__init__(message_type, messsage_content)

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
