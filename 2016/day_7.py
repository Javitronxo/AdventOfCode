import re
from typing import List


class IPv7:
    def __init__(self, address: str):
        self.address_parts = re.split(r"[\[\]]", address.strip())
        self.tls_support = self._has_tls_support()
        self.ssl_support = self._has_ssl_support()

    def _has_tls_support(self) -> bool:
        tls_support = False
        for i in range(len(self.address_parts)):
            if i % 2 == 0 and self.has_abba(self.address_parts[i]):
                tls_support = True
            elif i % 2 == 1 and self.has_abba(self.address_parts[i]):
                tls_support = False
                break
        return tls_support

    @staticmethod
    def has_abba(chunk: str) -> bool:
        for i in range(len(chunk) - 3):
            if chunk[i] == chunk[i + 3] and chunk[i] != chunk[i + 1] and chunk[i + 1] == chunk[i + 2]:
                return True
        return False

    def _has_ssl_support(self) -> bool:
        aba_blocks = list()
        bab_blocks = list()

        for i in range(len(self.address_parts)):
            xyx_chunks = self.get_xyx_chunks(self.address_parts[i])
            if i % 2 == 0:
                aba_blocks.extend(xyx_chunks)
            elif i % 2 == 1:
                bab_blocks.extend(xyx_chunks)

        for aba_block in aba_blocks:
            bab_block = aba_block[1] + aba_block[0] + aba_block[1]
            if bab_block in bab_blocks:
                return True
        return False

    @staticmethod
    def get_xyx_chunks(chunk: str) -> List[str]:
        aba_chunks = list()
        for i in range(len(chunk) - 2):
            if chunk[i] == chunk[i + 2] and chunk[i] != chunk[i + 1]:
                aba_chunks.append(chunk[i] + chunk[i + 1] + chunk[i + 2])
        return aba_chunks


def main():
    addresses_tls_support = list()
    addresses_ssl_support = list()
    with open("day_7_input.txt") as f_in:
        for line in f_in.readlines():
            ipv7_address = IPv7(line)
            if ipv7_address.tls_support:
                addresses_tls_support.append(ipv7_address)
            if ipv7_address.ssl_support:
                addresses_ssl_support.append(ipv7_address)

    print(f"Part 1: We have {len(addresses_tls_support)} with TLS support")
    print(f"Part 2: We have {len(addresses_ssl_support)} with SSL support")


if __name__ == "__main__":
    main()
