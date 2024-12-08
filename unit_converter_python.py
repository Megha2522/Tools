from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
# making main window
window = Tk() 
window.title("Unit Converter")
window.config(background="teal")
# widgets
topFrame=Frame(window)
topFrame.pack()
bottomFrame=Frame(window)
bottomFrame.pack()
heading=Label(topFrame,text="UNIT CONVERTER", background="black",foreground="white",font=("Arial Bold", 50))
heading.pack(fill=X)
################## EMPTY CELLS ########################
empty_1=Label(bottomFrame,text="            ") #empty cell
empty_1.grid(column=8,row=0)
empty_2=Label(bottomFrame,text="            ") #empty cell
empty_2.grid(column=7,row=0)
################## EMPTY CELLS ########################

# unit converter functioning start###############################################
def inject_units(event):
        uc_property=uc_properties.get()
        if uc_property=="Area":
        	uc_unit1['values']=("KmSq","Msq","FtSq")
        	uc_unit2['values']=("KmSq","Msq","FtSq")
        elif uc_property=="Length":
        	uc_unit1['values']=("Km","Meter","Mile","Foot")
        	uc_unit2['values']=("Km","Meter","Mile","Foot")
        elif uc_property=="Mass":
        	uc_unit1['values']=("Kg","Gram","Tonne")
        	uc_unit2['values']=("Kg","Gram","Tonne")
        elif uc_property=="Speed":
        	uc_unit1['values']=("M/s","Km/hr","Mile/hr")
        	uc_unit2['values']=("M/s","Km/hr","Mile/hr")
        elif uc_property=="Temprature":
        	uc_unit1['values']=("Celsius","Kelvin","Fahrenheit")
        	uc_unit2['values']=("Celsius","Kelvin","Fahrenheit")
        else:
        	uc_unit1['values']=("unit-1")
        	uc_unit2['values']=("unit-2")
        uc_unit1.current(0)
        uc_unit2.current(0)
def uc_convert():
	#messagebox.showinfo('Message title',uc_properties.get())
	ip_value,op_value=float(uc_input.get()),""
	u1_value=uc_unit1.get()
	u2_value=uc_unit2.get()
	if u1_value==u2_value: op_value=ip_value
	###################        AREA STARTS        ########################################
	elif u1_value=="KmSq" and u2_value=="Msq": op_value=ip_value*(10**6)
	elif u1_value=="KmSq" and u2_value=="FtSq": op_value=ip_value*(1.0764262648*(10**7))
	elif u1_value=="Msq" and u2_value=="KmSq": op_value=ip_value*(10**(-6))
	elif u1_value=="Msq" and u2_value=="FtSq": op_value=ip_value*(10.764)
	elif u1_value=="FtSq" and u2_value=="KmSq": op_value=ip_value*(9.290304*(10**(-6)))/100
	elif u1_value=="FtSq" and u2_value=="Msq": op_value=ip_value/10.764
	###################        AREA ENDS        ##########################################
	###################        LENGTH STARTS     ##########################################
	elif u1_value=="Km" and u2_value=="Meter": op_value=ip_value*1000
	elif u1_value=="Km" and u2_value=="Mile": op_value=ip_value/1.609
	elif u1_value=="Km" and u2_value=="Foot": op_value=ip_value*3280.84
	elif u1_value=="Meter" and u2_value=="Km": op_value=ip_value/1000
	elif u1_value=="Meter" and u2_value=="Mile": op_value=ip_value*1609.344
	elif u1_value=="Meter" and u2_value=="Foot": op_value=ip_value*3.28084
	elif u1_value=="Mile" and u2_value=="Km": op_value=ip_value*1.609
	elif u1_value=="Mile" and u2_value=="Meter": op_value=ip_value*1609.344
	elif u1_value=="Mile" and u2_value=="Foot": op_value=ip_value*5280
	elif u1_value=="Foot" and u2_value=="Km": op_value=ip_value/3280.84
	elif u1_value=="Foot" and u2_value=="Meter": op_value=ip_value/3.28084
	elif u1_value=="Foot" and u2_value=="Mile": op_value=ip_value/5280
	###################        LENGTH ENDS       ##########################################
	###################        MASS STARTS       ##########################################
	elif u1_value=="Kg" and u2_value=="Gram": op_value=ip_value*1000
	elif u1_value=="Kg" and u2_value=="Tonne": op_value=ip_value/1000
	elif u1_value=="Gram" and u2_value=="Kg": op_value=ip_value/1000
	elif u1_value=="Gram" and u2_value=="Tonne": op_value=ip_value/(10**6)
	elif u1_value=="Tonne" and u2_value=="Kg": op_value=ip_value*1000
	elif u1_value=="Tonne" and u2_value=="Gram": op_value=ip_value*(10**6)
	###################        MASS ENDS       ##########################################
	###################        SPEED STARTS       ########################################
	elif u1_value=="M/s" and u2_value=="Km/hr": op_value=ip_value*3.6
	elif u1_value=="M/s" and u2_value=="Mile/hr": op_value=ip_value*2.237
	elif u1_value=="Km/hr" and u2_value=="M/s": op_value=ip_value/3.6
	elif u1_value=="Km/hr" and u2_value=="Mile/hr": op_value=ip_value/1.609
	elif u1_value=="Mile/hr" and u2_value=="Km/hr": op_value=ip_value*1.609
	elif u1_value=="Mile/hr" and u2_value=="M/s": op_value=ip_value/2.237
	###################        SPEED ENDS       ##########################################
	###################        TEMPRATURE STARTS       ########################################
	elif u1_value=="Celsius" and u2_value=="Kelvin": op_value=ip_value+273.15
	elif u1_value=="Celsius" and u2_value=="Fahrenheit": op_value=(ip_value*1.8)+32
	elif u1_value=="Kelvin" and u2_value=="Celsius": op_value=ip_value-273.15
	elif u1_value=="Kelvin" and u2_value=="Fahrenheit": op_value=((ip_value-273.15)*1.8)+32
	elif u1_value=="Fahrenheit" and u2_value=="Celsius": op_value=(ip_value-32)*0.555555
	elif u1_value=="Fahrenheit" and u2_value=="Kelvin": op_value=((ip_value-32)*0.555555)+273.15
	###################        TEMPRATURE ENDS       ##########################################
	uc_output.configure(text= op_value)##### 
# unit converter functioning ends#################################################

# unit converter main body starts
uc_properties = Combobox(bottomFrame,width=25,font=("Arial Bold", 15))
uc_properties['values']= ("Select a Property...","Area","Length","Mass","Speed","Temprature")
uc_properties.current(0) #set default property to first element in list of values 
uc_properties.grid(column=6, row=1,columnspan=5,pady=10)
uc_properties.bind('<FocusIn>',inject_units)

uc_unit1=Combobox(bottomFrame,font=("Arial Bold", 12))
uc_unit1['values']=("unit-1")
uc_unit1.current(0)
uc_unit1.grid(column=6,row=2,columnspan=2,padx=20,pady=5)

uc_unit2=Combobox(bottomFrame,font=("Arial Bold", 12))
uc_unit2['values']=("unit-2")
uc_unit2.current(0)
uc_unit2.grid(column=8,row=2,columnspan=2,padx=20,pady=5)

uc_input=Entry(bottomFrame,width=22,font=("Arial Bold", 12))
uc_input.grid(column=6,row=3,columnspan=2,padx=20,pady=10)
uc_input.insert(0,"Input...")
uc_output=Label(bottomFrame,text="",width=22,background="white",font=("Arial Bold", 12))
uc_output.grid(column=8,row=3,columnspan=2,padx=20,pady=5)

convert_button=Button(bottomFrame,text="Convert",command=uc_convert,width=23)
convert_button.grid(column=6, row=4,columnspan=5,pady=10)
# unit converter main body ends

# mainloop
window.mainloop()
