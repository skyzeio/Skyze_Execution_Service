"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageMarketDataUpdaterRunAll(MessageSkyzeAbstract):
  """Data has been fully loaded and ready for use"""

  def __init__(self, exchange):
    """Constructor"""
    message_content = f"{exchange}:ALL PAIRS AND INTERVALS"
    super().__init__(SkyzeMessageType.MARKET_DATA_UPDATER_RUN_ALL,
                     message_content)
    self.__exchange = exchange

  def getExchange(self):
    """Getter"""
    return self.__exchange

  def getJSON(self):
    """Return object as JSON"""
    return super().getJSON() + "}"
