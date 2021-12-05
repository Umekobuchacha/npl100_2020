# %%
# 00
str = "stressed"
print(str[::-1])

# %%
# 01
str = "パタトクカシーー"
print(str[::2])

# %%
# 02
str1 = "パトカー"
str2 = "タクシー"
str3 =""
for str1,str2 in zip(str1,str2):
    str3 += str1 + str2
print(str3)
# %%
