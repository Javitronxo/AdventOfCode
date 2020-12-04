import re


class Passport:
    EXPECTED_FIELDS = {
        "byr": 1,  # (Birth Year)
        "iyr": 1,  # (Issue Year)
        "eyr": 1,  # (Expiration Year)
        "hgt": 1,  # (Height)
        "hcl": 1,  # (Hair Color)
        "ecl": 1,  # (Eye Color)
        "pid": 1,  # (Passport ID)
        "cid": 0,  # (Country ID) - OPTIONAL
    }
    EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def __init__(self, passport_str: str):
        self.fields = {field.split(":")[0]: field.split(":")[1] for field in passport_str.split()}

    def has_required_info(self) -> bool:
        present_keys_set = list(self.fields.keys())
        return all(field in present_keys_set for field, value in self.EXPECTED_FIELDS.items() if value)

    def has_valid_info(self) -> bool:
        if not self.has_required_info():
            return False
        if (
            (1920 <= int(self.fields["byr"]) <= 2020)
            and (2010 <= int(self.fields["iyr"]) <= 2020)
            and (2020 <= int(self.fields["eyr"]) <= 2030)
            and (self.fields["ecl"] in self.EYE_COLORS)
            and (len(self.fields["pid"]) == 9 and self.fields["pid"].isdigit())
            and re.match(r"#[a-f0-9]{6}", self.fields["hcl"])
        ):
            if (self.fields["hgt"].endswith("cm") and ("150cm" <= self.fields["hgt"] <= "193cm")) or (
                self.fields["hgt"].endswith("in") and ("59in" <= self.fields["hgt"] <= "76in")
            ):
                return True
        return False


def main():
    passports = list()
    with open("day_4_input.txt") as f:
        passport_str = ""
        for line in f.readlines():
            if len(line.strip()):
                passport_str += line.strip() + " "
            else:
                passports.append(Passport(passport_str))
                passport_str = ""

    part_1_passports = len([passport for passport in passports if passport.has_required_info()])
    print(f"Part 1: We have {part_1_passports} valid passports")

    part_2_passports = len([passport for passport in passports if passport.has_valid_info()])
    print(f"Part 2: We have {part_2_passports} valid passports")


if __name__ == "__main__":
    main()
