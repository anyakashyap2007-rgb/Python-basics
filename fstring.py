name = "John"
age = 20
Language = "python"
hours = 3

# old way of doing

print(name,"is",age,"years old.He studies",hours,"hours a day.")

# f string
print(f"{name} is {age} years old.He studies {Language} {hours} hours a day.")

sub1=78
sub2=87
sub3=83

print(f"{name} scored {sub1+sub2+sub3} marks in total.")
percent = (sub1+sub2+sub3)/3
print(f"{name} scored {percent}%.")