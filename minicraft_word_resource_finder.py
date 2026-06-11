import random

print("[-_-] MINI-CRAFT WORD RESOURCE FINDER [-_-]")
print("Welcome to Minicraft!")
print("(It is not like the original game)")
print("\n")
print("You are about to enter a strange world..")
print("\n")
print("Whooooooosh")
print("THUD!")
print("\n")
print("Hope the landing wasn't too hard..")
print("\n")
print(" *Something drops at your feet* ")
print("\n")
print("Oh? You got equipped with a tool already?")
print("\n")
print("Use it to mine and unravel these mysterious blocks. You never know you may find something rare.")
print("Happy Mining.")

common = ["DIRT", "SAND", "WOOD", "GRAVEL", "CLAY", "SNOW",]
uncommon = ["IRON","COPPER", "REDSTONE", "NETHER QUARTZ"]
rare = ["GOLD", "DIAMOND" , "EMERALD" , "OBSIDIAN"]


block = input("Enter a block to mine: ")

print("Let's mine it..")

word_length = len(block)
if word_length > 5:
    print("It seems to be a big one")
else:
    print("Oh, that was easy!")
print("Now, we'll look at what you got.")
print("\n")

l_block = block.lower()
def vowel_check():
    vowel_crystals = 0
    for i in l_block:
        if i in "aeiou":
            vowel_crystals +=1
    return vowel_crystals

def consonants_check():
    consonant_fragments= 0
    for j in l_block:
        if j.isalpha() and j not in "aeiou":
            consonant_fragments +=1
    return consonant_fragments


def info_collect():
    frequency_info={}
    for u in l_block:
        if u in frequency_info:
            frequency_info[u] += 1
        else:
            frequency_info[u] = 1
    return frequency_info

def uniqueness():
    frequency_info = info_collect()
    unique = 0
    for l in frequency_info:
        if frequency_info[l] == 1:
            unique +=1

    return unique

unique = uniqueness()
if unique > 5:
        print("★ RARITY : RARE ★")
        print("\n")
        
elif unique >= 3:
        print(" ★ RARITY : UNCOMMON ★")
        print("\n")
        
else:
        print("★ RARITY : COMMON ★")
        print("\n")


def resource_gen():
    unique  = uniqueness()
    if unique > 5:
        rarity = random.choice(rare)
    elif unique <5 and unique >= 3:
        rarity = random.choice(uncommon)
    else:
        rarity = random.choice(common)

    return rarity

print("\n⛏ Mining Complete...")
print("Analyzing Resources...\n")

print("RESOURCE INFO ⛏")   
print(" ◈━◈━◈━◈━◈━◈━◈ ")  
print("\n")
print(f"▪ Block mined: {block}")
print("▪ Length:", word_length)
print("▪ Vowel Crystals:", vowel_check())
print("▪ Consonant Fragments:", consonants_check())
print("▪ Frequency:", info_collect())
print("▪ Unique Letters:", uniqueness())
print("▪ Resource Found:", resource_gen())
print("\n")
print(" ◈━◈━◈━◈━◈━◈━◈ ") 



