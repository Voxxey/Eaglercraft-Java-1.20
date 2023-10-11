from tkinter import *
from time import sleep


root = Tk()
root.title('Eaglercraft 1.20')
root.geometry('800x600')
root.resizable(False, False)

def extract_png_asset(asset_name):
    return PhotoImage(file='assets/' + asset_name + '.png')


a_normal_black_photo = extract_png_asset('font/normal-black/a')
b_normal_black_photo = extract_png_asset('font/normal-black/b')
c_normal_black_photo = extract_png_asset('font/normal-black/c')
d_normal_black_photo = extract_png_asset('font/normal-black/d')
e_normal_black_photo = extract_png_asset('font/normal-black/e')
f_normal_black_photo = extract_png_asset('font/normal-black/f')
g_normal_black_photo = extract_png_asset('font/normal-black/g')
h_normal_black_photo = extract_png_asset('font/normal-black/h')
i_normal_black_photo = extract_png_asset('font/normal-black/i')
j_normal_black_photo = extract_png_asset('font/normal-black/j')
k_normal_black_photo = extract_png_asset('font/normal-black/k')
l_normal_black_photo = extract_png_asset('font/normal-black/l')
m_normal_black_photo = extract_png_asset('font/normal-black/m')
n_normal_black_photo = extract_png_asset('font/normal-black/n')
o_normal_black_photo = extract_png_asset('font/normal-black/o')
p_normal_black_photo = extract_png_asset('font/normal-black/p')
q_normal_black_photo = extract_png_asset('font/normal-black/q')
r_normal_black_photo = extract_png_asset('font/normal-black/r')
s_normal_black_photo = extract_png_asset('font/normal-black/s')
t_normal_black_photo = extract_png_asset('font/normal-black/t')
u_normal_black_photo = extract_png_asset('font/normal-black/u')
v_normal_black_photo = extract_png_asset('font/normal-black/v')
w_normal_black_photo = extract_png_asset('font/normal-black/w')
x_normal_black_photo = extract_png_asset('font/normal-black/x')
y_normal_black_photo = extract_png_asset('font/normal-black/y')
z_normal_black_photo = extract_png_asset('font/normal-black/z')

a_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_a')
b_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_b')
c_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_c')
d_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_d')
e_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_e')
f_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_f')
g_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_g')
h_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_h')
i_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_i')
j_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_j')
k_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_k')
l_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_l')
m_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_m')
n_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_n')
o_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_o')
p_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_p')
q_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_q')
r_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_r')
s_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_s')
t_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_t')
u_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_u')
v_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_v')
w_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_w')
x_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_x')
y_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_y')
z_capital_normal_black_photo = extract_png_asset('font/normal-black/capital_z')

add_normal_black_photo = extract_png_asset('font/normal-black/add')
subtract_normal_black_photo = extract_png_asset('font/normal-black/subtract')

and_normal_black_photo = extract_png_asset('font/normal-black/and')

arrow_point_up_black_photo = extract_png_asset('font/normal-black/arrow_point_up')

arrow_left_black_photo = extract_png_asset('font/normal-black/arrow_left')
arrow_right_black_photo = extract_png_asset('font/normal-black/arrow_right')

at_normal_black_photo = extract_png_asset('font/normal-black/at')

backtick_normal_black_photo = extract_png_asset('font/normal-black/backtick')

backslash_normal_black_photo = extract_png_asset('font/normal-black/backslash')
frontslash_normal_black_photo = extract_png_asset('font/normal-black/frontslash')

colon_normal_black_photo = extract_png_asset('font/normal-black/colon')
semi_colon_normal_black_photo = extract_png_asset('font/normal-black/semi_colon')

period_normal_black_photo = extract_png_asset('font/normal-black/period')
comma_normal_black_photo = extract_png_asset('font/normal-black/comma')

percent_normal_black_photo = extract_png_asset('font/normal-black/percent')

copyright_normal_black_photo = extract_png_asset('font/normal-black/copyright')

money_normal_black_photo = extract_png_asset('font/normal-black/money')

UNKNOWN_normal_black_photo = extract_png_asset('font/normal-black/unknown_char')

pound_normal_black_photo = extract_png_asset('font/normal-black/pound')

underscore_normal_black_photo = extract_png_asset('font/normal-black/underscore')

straight_thing_normal_black_photo = extract_png_asset('font/normal-black/straight_thing')

single_quote_normal_black_photo = extract_png_asset('font/normal-black/single_quote')
double_quote_normal_black_photo = extract_png_asset('font/normal-black/double_quote')

weird_thing_normal_black_photo = extract_png_asset('font/normal-black/weird_thing')

worm_normal_black_photo = extract_png_asset('font/normal-black/worm')

exclamation_normal_black_photo = extract_png_asset('font/normal-black/exclamation')
question_normal_black_photo = extract_png_asset('font/normal-black/question')

equal_normal_black_photo = extract_png_asset('font/normal-black/equal')

star_normal_black_photo = extract_png_asset('font/normal-black/star')

left_p_normal_black_photo = extract_png_asset('font/normal-black/left_p')
right_p_normal_black_photo = extract_png_asset('font/normal-black/right_p')

left_b_normal_black_photo = extract_png_asset('font/normal-black/left_b')
right_b_normal_black_photo = extract_png_asset('font/normal-black/right_b')

left_b2_normal_black_photo = extract_png_asset('font/normal-black/left_b2')
right_b2_normal_black_photo = extract_png_asset('font/normal-black/right_b2')


zero_normal_black_photo = extract_png_asset('font/normal-black/0')
one_normal_black_photo = extract_png_asset('font/normal-black/1')
two_normal_black_photo = extract_png_asset('font/normal-black/2')
three_normal_black_photo = extract_png_asset('font/normal-black/3')
four_normal_black_photo = extract_png_asset('font/normal-black/4')
five_normal_black_photo = extract_png_asset('font/normal-black/5')
six_normal_black_photo = extract_png_asset('font/normal-black/6')
seven_normal_black_photo = extract_png_asset('font/normal-black/7')
eight_normal_black_photo = extract_png_asset('font/normal-black/8')
nine_normal_black_photo = extract_png_asset('font/normal-black/9')



a_normal_white_photo = extract_png_asset('font/normal-white/a')
b_normal_white_photo = extract_png_asset('font/normal-white/b')
c_normal_white_photo = extract_png_asset('font/normal-white/c')
d_normal_white_photo = extract_png_asset('font/normal-white/d')
e_normal_white_photo = extract_png_asset('font/normal-white/e')
f_normal_white_photo = extract_png_asset('font/normal-white/f')
g_normal_white_photo = extract_png_asset('font/normal-white/g')
h_normal_white_photo = extract_png_asset('font/normal-white/h')
i_normal_white_photo = extract_png_asset('font/normal-white/i')
j_normal_white_photo = extract_png_asset('font/normal-white/j')
k_normal_white_photo = extract_png_asset('font/normal-white/k')
l_normal_white_photo = extract_png_asset('font/normal-white/l')
m_normal_white_photo = extract_png_asset('font/normal-white/m')
n_normal_white_photo = extract_png_asset('font/normal-white/n')
o_normal_white_photo = extract_png_asset('font/normal-white/o')
p_normal_white_photo = extract_png_asset('font/normal-white/p')
q_normal_white_photo = extract_png_asset('font/normal-white/q')
r_normal_white_photo = extract_png_asset('font/normal-white/r')
s_normal_white_photo = extract_png_asset('font/normal-white/s')
t_normal_white_photo = extract_png_asset('font/normal-white/t')
u_normal_white_photo = extract_png_asset('font/normal-white/u')
v_normal_white_photo = extract_png_asset('font/normal-white/v')
w_normal_white_photo = extract_png_asset('font/normal-white/w')
x_normal_white_photo = extract_png_asset('font/normal-white/x')
y_normal_white_photo = extract_png_asset('font/normal-white/y')
z_normal_white_photo = extract_png_asset('font/normal-white/z')

a_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_a')
b_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_b')
c_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_c')
d_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_d')
e_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_e')
f_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_f')
g_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_g')
h_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_h')
i_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_i')
j_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_j')
k_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_k')
l_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_l')
m_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_m')
n_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_n')
o_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_o')
p_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_p')
q_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_q')
r_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_r')
s_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_s')
t_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_t')
u_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_u')
v_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_v')
w_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_w')
x_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_x')
y_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_y')
z_capital_normal_white_photo = extract_png_asset('font/normal-white/capital_z')


add_normal_white_photo = extract_png_asset('font/normal-white/add')
subtract_normal_white_photo = extract_png_asset('font/normal-white/subtract')

and_normal_white_photo = extract_png_asset('font/normal-white/and')

arrow_point_up_white_photo = extract_png_asset('font/normal-white/arrow_point_up')

arrow_left_white_photo = extract_png_asset('font/normal-white/arrow_left')
arrow_right_white_photo = extract_png_asset('font/normal-white/arrow_right')

at_normal_white_photo = extract_png_asset('font/normal-white/at')

backtick_normal_white_photo = extract_png_asset('font/normal-white/backtick')

backslash_normal_white_photo = extract_png_asset('font/normal-white/backslash')
frontslash_normal_white_photo = extract_png_asset('font/normal-white/frontslash')

colon_normal_white_photo = extract_png_asset('font/normal-white/colon')
semi_colon_normal_white_photo = extract_png_asset('font/normal-white/semi_colon')

period_normal_white_photo = extract_png_asset('font/normal-white/period')
comma_normal_white_photo = extract_png_asset('font/normal-white/comma')

percent_normal_white_photo = extract_png_asset('font/normal-white/percent')

copyright_normal_white_photo = extract_png_asset('font/normal-white/copyright')

money_normal_white_photo = extract_png_asset('font/normal-white/money')

UNKNOWN_normal_white_photo = extract_png_asset('font/normal-white/unknown_char')

pound_normal_white_photo = extract_png_asset('font/normal-white/pound')

underscore_normal_white_photo = extract_png_asset('font/normal-white/underscore')

straight_thing_normal_white_photo = extract_png_asset('font/normal-white/straight_thing')

single_quote_normal_white_photo = extract_png_asset('font/normal-white/single_quote')
double_quote_normal_white_photo = extract_png_asset('font/normal-white/double_quote')

weird_thing_normal_white_photo = extract_png_asset('font/normal-white/weird_thing')

worm_normal_white_photo = extract_png_asset('font/normal-white/worm')

exclamation_normal_white_photo = extract_png_asset('font/normal-white/exclamation')
question_normal_white_photo = extract_png_asset('font/normal-white/question')

equal_normal_white_photo = extract_png_asset('font/normal-white/equal')

star_normal_white_photo = extract_png_asset('font/normal-white/star')

left_p_normal_white_photo = extract_png_asset('font/normal-white/left_p')
right_p_normal_white_photo = extract_png_asset('font/normal-white/right_p')

left_b_normal_white_photo = extract_png_asset('font/normal-white/left_b')
right_b_normal_white_photo = extract_png_asset('font/normal-white/right_b')

left_b2_normal_white_photo = extract_png_asset('font/normal-white/left_b2')
right_b2_normal_white_photo = extract_png_asset('font/normal-white/right_b2')


zero_normal_white_photo = extract_png_asset('font/normal-white/0')
one_normal_white_photo = extract_png_asset('font/normal-white/1')
two_normal_white_photo = extract_png_asset('font/normal-white/2')
three_normal_white_photo = extract_png_asset('font/normal-white/3')
four_normal_white_photo = extract_png_asset('font/normal-white/4')
five_normal_white_photo = extract_png_asset('font/normal-white/5')
six_normal_white_photo = extract_png_asset('font/normal-white/6')
seven_normal_white_photo = extract_png_asset('font/normal-white/7')
eight_normal_white_photo = extract_png_asset('font/normal-white/8')
nine_normal_white_photo = extract_png_asset('font/normal-white/9')





titlescreen_top_photo = extract_png_asset('titlescreen_top')
login_photo = extract_png_asset('login')
download_terrian_photo = extract_png_asset('download_terrain')
original_server_photo = extract_png_asset('original_server')
titlescreen_bg_photo = extract_png_asset('titlescreen_bg')
timed_out_photo = extract_png_asset('timed_out')
back_2_titlescreen_photo = extract_png_asset('buttons/back_2_titlescreen')
cancel_photo = extract_png_asset('buttons/cancel')
done_photo = extract_png_asset('buttons/done')
multiplayer_photo = extract_png_asset('buttons/multiplayer')
new_world_photo = extract_png_asset('buttons/new_world')
options_photo = extract_png_asset('buttons/options')
realms_photo = extract_png_asset('buttons/realms')
singleplayer_photo = extract_png_asset('buttons/singleplayer')
entry_bar_photo = extract_png_asset('entry_bar')


login_label = Label(image=login_photo)
login_label.pack()

class EntryBar:
    def __init__(self, x, y):
        pass

class Text:
    def __init__(self, msg, x, y):
        for char in msg:
            if char == 'a':
                Label(image=a_normal_black_photo).place(x=x, y=y)
                x += 15
            elif char == 'b':
                Label(image=b_normal_black_photo).place(x=x, y=y)
                x += 15
            elif char == 'c':
                Label(image=c_normal_black_photo).place(x=x, y=y)
                x += 15



Text('abc', 0, 0)


root.mainloop()
