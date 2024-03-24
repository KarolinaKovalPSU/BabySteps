#hair growth calculator
from tkinter import *

# creating a gui window
window = Tk()
window.geometry('800x800')
window.title('Hair growth calculator')
window.config(bg ='#88cffa')

hair = StringVar()
time = StringVar()
output = StringVar()

# defining a hair calculator function
def hair_calc():
        try:
                hair_growthrate = float(hair.get()) * 0.2 # let's say hair grows at a rate of 20% a year. First, we calculate how much is that in cm
                new_hair = float(hair_growthrate) * float(time.get()) # then we multiply that value by the number of years in question
                result = float(new_hair) + float(hair.get()) # finally, we add the total length of new hair to an initial hair length
        except Exception as ex:
                print(ex)
                result = 'error'
        output.set(result)

# asking about the hair length now
Label(window, text = 'Your hair length now (cm): ', font='arial 18', bg = '#88cffa').grid(row=0, column=0)
Entry(window, font = 'arial 18', textvariable = hair , bg = 'antiquewhite2').grid(row=0, column=1)

# asking about the period of time over which the hair will grow
Label(window, text = 'Type the period of time (years): ', font='arial 18', bg = '#88cffa').grid(row=1, column=0)
Entry(window, font = 'arial 18', textvariable = time , bg = 'antiquewhite2').grid(row=1, column=1)

# displaying the result
Label(window, text = 'Result (cm): ', font='arial 18', bg = '#88cffa').grid(row=2, column=0)
Entry(window, font = 'arial 18', textvariable = output , bg = 'antiquewhite2').grid(row=2, column=1)
button = Button(window, text="Calculate", command = hair_calc)
button.grid(row=3, column=1)

window.mainloop()






