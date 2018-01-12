"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageScreenerRun(MessageSkyzeAbstract):
  """Run a specific screener"""

  def __init__(self, screener_name):
    """Constructor"""
    message_content = f"{screener_name}"
    super().__init__(SkyzeMessageType.SCREENER_RUN, message_content)
    self.__screener_name = screener_name

  def getScreenerName(self):
    """Getter"""
    return self.__screener_name

  def getJSON(self):
    """Return object as JSON"""
    text = super().getJSON()
    text += f', "screener name": "{self.__screener_name}"'
    text += '}'
    return text
