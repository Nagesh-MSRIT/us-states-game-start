#just commenting

# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image =r"C:\Users\Nagesh\Downloads\us-states-game-start (1)\us-states-game-start\blank_states_img.gif"
# screen.addshape(image) 
# turtle.shape(image)

# # def get_mouse_click_coor(x, y):
# #     print(x, y)

# # turtle.onscreenclick(get_mouse_click_coor)

# # turtle.mainloop()
# data_states=pandas.read_csv(r"C:\Users\Nagesh\Downloads\us-states-game-start (1)\us-states-game-start\50_states.csv")
# all_states=data_states["state"].to_list()
# guess_state=[]

# while len(guess_state)<50:
#     answer_state=screen.textinput(title=f"{len(guess_state)}/50 Statues Correct",prompt="what is another states name?").title()
#     print(answer_state)

#     if answer_state in all_states:
#         guess_state.append(answer_state)
#         t=turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_date=data_states[data_states.state==answer_state]
#         t.goto(int(state_date.x),int(state_date.y))
#         t.write(answer_state)


    





# screen.exitonclick()


import turtle,pandas

screen=turtle.Screen()
screen.title="India Map Game"
india_image=r"C:\Users\Nagesh\Downloads\us-states-game-start (1)\us-states-game-start\india.gif"
screen.addshape(india_image)
turtle.shape(india_image)
guess_data=[]

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
india_data=pandas.read_csv(r"C:\Users\Nagesh\Downloads\us-states-game-start (1)\us-states-game-start\50_states.csv")
all_states=india_data["state"].to_list()
print(all_states)
while len(guess_data)<50:
    guess_answer=screen.textinput(title="States of India",prompt="what is another state name?").title()
    print(guess_answer)
    if guess_answer=="Exit":
        missing_state=[state for state in all_states if state not in guess_data]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn")

        break

    if guess_answer in all_states:
        guess_data.append(guess_answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=india_data[india_data.state==guess_answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(guess_answer)

