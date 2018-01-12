'''Created on 10/01/2018 @author: michaelnew'''

# Third Party Imports
from datetime import datetime


# Skyze Imports
import settings_skyze
from Skyze_Standard_Library.SkyzeServiceAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp

# Skyze Messages
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *
from Skyze_Messaging_Service.Messages.MessageOrderMarket \
    import MessageOrderMarket
from Skyze_Messaging_Service.Messages.MessageOrderEntryStop \
    import MessageOrderEntryStop
from Skyze_Messaging_Service.Messages.MessageOrderEntryLimit \
    import MessageOrderEntryLimit
from Skyze_Messaging_Service.Messages.MessageOrderExitStopLoss \
    import MessageOrderExitStopLoss
from Skyze_Messaging_Service.Messages.MessageOrderExitTakeProfit \
    import MessageOrderExitTakeProfit
from Skyze_Messaging_Service.Messages.MessageOrderExitTrailingStop \
    import MessageOrderExitTrailingStop
from Skyze_Messaging_Service.Messages.MessageOrderCancel \
    import MessageOrderCancel


class SkyzeExecutionService(SkyzeServiceAbstract):
  '''Skyze inter-service message logger'''

  def __init__(self, message_bus):
    '''Constructor'''
    path_to_service = ""
    super().__init__(message_bus=message_bus, log_path=path_to_service)

  def __order_market(self, message_received):
    print("\n\nEXCEPTION NOT YET IMPLIMENTED - ORDER MARKET")
    # raise "EXCEPTION NOT YET IMPLIMENTED - ORDER MARKET"

  def receiveMessage(self, message_received):
    '''Gets the mssage from the bus and routes internally'''
    # Parent class processing
    super().receiveMessage(message_received)
    # Route to appropriate service
    message_type = message_received.getMessageType()
    if message_type == SkyzeMessageType.ORDER_MARKET:
      self.__order_market(message_received)
    elif message_type == SkyzeMessageType.ORDER_ENTRY_STOP:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    elif message_type == SkyzeMessageType.ORDER_ENTRY_LIMIT:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    elif message_type == SkyzeMessageType.ORDER_EXIT_STOP_LOSS:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    elif message_type == SkyzeMessageType.ORDER_EXIT_TAKE_PROFIT:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    elif message_type == SkyzeMessageType.ORDER_EXIT_TRAILING_STOP:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    elif message_type == SkyzeMessageType.ORDER_CANCEL:
      print("\n\nNOT YET IMPLIMENTED - SkyzeExecutionService::ReceiveMessage")
    else:
      self._unknownMessageTypeError(message_received)
