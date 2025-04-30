
#問1-1

num = [1,3,5,7]
for i in num:
     ans = i ** 2
     print(ans)



#問1-2
for j in range(1,8,2):
     ans2 = j ** 2
     print(ans2)



#問2-1
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]
for place in all_place:
   if place in get_place:
      print(place + "のチケットが当選しました！")
   elif place in wait_place:
       print(place + "のチケットは結果待ち")
   else:
       print(place + "のチケットは落選しました")



#問2-2

get_place2 = get_place + wait_place
print(get_place2)
['横浜', '札幌', '大阪']
s = "{}と{}と{}のチケットが当選しました！"
result = s.format(*get_place2)
print(result)
