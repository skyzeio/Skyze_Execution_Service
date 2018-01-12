"""Created on 9 / 1 / 2018 @author: michaelnew"""


# Standard Libraries
import ccxt

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp

# Skyze libraries - Test Case Specific
from SkyzeExecutionService import *
from Skyze_Messaging_Service.SkyzeMessageBusService import *
from Skyze_Messaging_Service.Messages.MessageOrderMarket \
    import MessageOrderMarket


class SkyzeExecutionService_test(UnitTestSkyzeAbstract):
  """Test the SkyzeExecutionService Class"""

  _package_name = "Skyze_Execution_Service"
  _class_tested = "SkyzeExecutionService"

  def setUp(self):
    super().setUp()
    self.__message_bus = SkyzeMessageBusService()
    self.__execution_service = SkyzeExecutionService(self.__message_bus)

  def tearDown(self):
    super().tearDown()
    pass

  def receiveMessage(self, message_received):
    # Route to appropriate service
    message_type = message_received.getMessageType()
    if message_type == SkyzeMessageType.FILL:
      self.__order_market(message_received)

  #@unittest.skip("Working on new test")
  def test__XXXX(self):
    test_name = "__sendTweet"
    test_file = target_file = test_columns = "N/A"
    self.printTestHeader(self._package_name, test_name, test_file,
                         target_file, test_columns)

    # Test Parameters
    source_name = "Bitfinex"
    exchange_intervals = []
    error_list = []

    print("\tsource_name: " + source_name +
          "\texchange_intervals: " + str(exchange_intervals) +
          "\terror_list: " + str(error_list) + "\n\n")

    # Execute Test
    print("=== Test Execution: \n")
    order_msg = MessageOrderMarket()
    self.__execution_service.receiveMessage(order_msg)

    # Test Results
    # TODO Set up the infrastructure for receiving messages, in this case FILLS
    #      and asserting to the target results


if __name__ == '__main__':
  unittest.main()
