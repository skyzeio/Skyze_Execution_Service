"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageOrderMarket(MessageSkyzeAbstract):
  '''A Market Order to be executed on an exchange'''

  def __init__(self):
    """Constructor"""
    super().__init__(SkyzeMessageType.ORDER_MARKET)
    self.__message_content = "Order Market"

  def getMessageContent(self):
    """Getter"""
    return self.__message_content

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
