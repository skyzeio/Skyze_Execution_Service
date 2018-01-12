'''Created on 12/01/2018 @author: michaelnew'''

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageOrder import *


class MessageOrderEntryLimit(MessageOrder):
  '''A Stop Entry Order to be executed on an exchange'''

  def __init__(self):
    """Constructor"""
    message_content = "Order Entry Limit"
    super().__init__(SkyzeMessageType.ORDER_ENTRY_LIMIT, messsage_content)

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
