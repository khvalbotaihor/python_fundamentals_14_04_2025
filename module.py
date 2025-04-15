# import functions as f

# f.greeting_10("Alice")
# f.greeting_9()
# f.user_guessing_game("50", "stop")

from my_module.functions import greeting_9 as gr, greeting_10, user_guessing_game
from my_module.functions import name, Test

greeting_10("Alice")
gr()
user_guessing_game("50", "stop")
print(name)
print(Test.a)