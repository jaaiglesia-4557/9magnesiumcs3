def main():
    birth_year = get_birth_year()
    if birth_year is None:
        return
    print(f"You were born in {birth_year}")
    zodiac = return_chinese_zodiac_sign(birth_year)
    print(f"Your Chinese zodiac sign is: {zodiac}")

def get_birth_year():
    user_input = input("Enter your birth year(Input must be a valid year, and not earlier than 1900): ")
   
    try:
        year = int(user_input)
        if year < 0:
            print("Error: Year cannot be negative!")
            return None
        elif year < 1900:
            print("Error: It should not be earlier than 1900")
            return None
        elif year > 2026:
            print("Error: Invalid year, you haven't been born yet!")
            return None
        else:
            print(f"Valid birth year: {year}")
            return year
    except ValueError:
        print("Error: Please enter numbers only.")
        return None




def return_chinese_zodiac_sign(birth_year):
    remainder = birth_year % 12
    match remainder:
        case 0:
            return "Monkey (猴 / Hóu)"
        case 1:
            return "Rooster (鸡 / Jī)"
        case 2:
            return "Dog (狗 / Gǒu)"
        case 3:
            return "Pig (猪 / Zhū)"
        case 4:
            return "Rat (鼠 / Shǔ)"
        case 5:
            return "Ox (牛 / Niú)"
        case 6:
            return "Tiger (虎 / Hǔ)"
        case 7:
            return "Rabbit (兔 / Tù)"
        case 8:
            return "Dragon (龙 / Lóng)"
        case 9:
            return "Snake (蛇 / Shé)"
        case 10:
            return "Horse (马 / Mǎ)"
        case 11:
            return "Goat (羊 / Yáng)"




if __name__ == "__main__":
    main()

