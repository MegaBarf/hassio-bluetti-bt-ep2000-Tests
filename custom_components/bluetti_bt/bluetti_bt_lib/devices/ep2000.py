"""EP2000 fields."""

from ..base_devices.ProtocolV2Device import ProtocolV2Device


class EP2000(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "EP2000", sn)

        # Details
       # self.struct.add_uint_field("battery_range_start", 2022) ##bsp. aus der EO600.py
        self.struct.add_uint_field("total_battery_percent_ep2000_py", 102)






#    @property
#    def polling_commands(self) -> List[ReadHoldingRegisters]:
#        return self.struct.get_read_holding_registers()
