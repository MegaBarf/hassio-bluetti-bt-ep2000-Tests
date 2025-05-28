"""EP2000 fields."""

from ..base_devices.ProtocolV2Device import ProtocolV2Device


class EP2000(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "EP2000", sn)
