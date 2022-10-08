if __name__ == '__main__':
    u = set("abcdefghijklmnopqrstuvwxyz")
a={"a","b","h","j","l"}
b={"b","c","h","l","r","u"}
c={"j","k","n","t","z"}
d={"b","i","k","u","w"}

x=(a.union(b)).intersection(c)
print(f"x={x}")
#Дополнение множеств
an=u.difference(b)
bn=u.difference(a)
y=(an.intersection(bn)).difference(c.union(d))
print(f"y={y}")