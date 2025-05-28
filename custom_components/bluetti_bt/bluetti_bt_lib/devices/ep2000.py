"""EP2000 fields."""

from typing import List

from ..field_enums import ChargingMode
from ..utils.commands import ReadHoldingRegisters
from ..base_devices.ProtocolV2Device import ProtocolV2Device

class EP2000(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "EP2000", sn)

        # Meins
        self.struct.add_uint_field("total_battery_percent_ep2000_py", 102)
        
        # Power IO
        #self.struct.add_uint_field('dc_output_power', 140)
        #self.struct.add_uint_field('ac_output_power', 142)
        #self.struct.add_uint_field('dc_input_power', 144)
        #self.struct.add_uint_field('ac_input_power', 146)

        
    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(102, 1),
            ]

    #@property
    #def writable_ranges(self) -> List[range]:
    #    return super().writable_ranges + [
    #        range(2000, 2022),
   #         range(2200, 2226)
        ]



####
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
