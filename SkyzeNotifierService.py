"""Created on 13/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime


# Skyze Imports
from Skyze_Execution_Service import settings
from Skyze_Standard_Library.SkyzeServiceAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp

# Skyze Messages
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *
from Skyze_Messaging_Service.Messages.MessageOrder \
    import MessageOrder


class SkyzeNotifierService(SkyzeServiceAbstract):
  """Skyze inter-service message logger"""

  def __init__(self, message_bus):
    """Constructor"""
    path_to_service = "Skyze_Execution_Service"
    super().__init__(message_bus=message_bus, log_path=path_to_service)

  def receiveMessage(self, message_received):
    """Gets the mssage from the bus and routes internally"""
    # Parent class processing
    super().receiveMessage(message_received)
    # Route to appropriate service
    message_type = message_received.getMessageType()
    if message_type == SkyzeMessageType.ORDER:
      pass
    elif message_type == SkyzeMessageType.CANCEL_ORDER:
      pass
    else:
      self._unknownMessageTypeError(message_received)
