from __future__ import division
from javax.swing import JFrame,JButton,JLabel,JTextField
from java.awt import Font
from java.lang import StringBuilder
from java.lang import String
from java.lang import Integer
from java.lang import Float
frame = JFrame("Student Detail")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setSize(400,520)
frame.setLocation(300,100)
frame.setLayout(None)
frame.setVisible(True)

sb= StringBuilder() # in jython if we have to use the java class then we have to import it and make object of it and then call the method of java


def clickBtnPlus(event):
    sb.append("+")
    tf.setText(sb.toString())
    
def clickBtnSubtract(event):
    sb.append("-")
    tf.setText(sb.toString())    
    
def clickBtnMultiply(event):
    sb.append("*")
    tf.setText(sb.toString())    

def clickBtnDivide(event):
    sb.append("/")
    tf.setText(sb.toString())

def clickBtn1(event):
    sb.append("1")
    tf.setText(sb.toString())
    
def clickBtn2(event):
    sb.append("2")
    tf.setText(sb.toString())
    
def clickBtn3(event):
    sb.append("3")
    tf.setText(sb.toString())    

def clickBtn4(event):
    sb.append("4")
    tf.setText(sb.toString())

def clickBtn5(event):
    sb.append("5")
    tf.setText(sb.toString())

def clickBtn6(event):
    sb.append("6")
    tf.setText(sb.toString())
    
def clickBtn7(event):
    sb.append("7")
    tf.setText(sb.toString())    
    
def clickBtn8(event):
    sb.append("8")
    tf.setText(sb.toString())    

def clickBtn9(event):
    sb.append("9") # no need to decclare the global variable
    tf.setText(sb.toString())

def clickBtn0(event):
    sb.append("0")
    tf.setText(sb.toString())

def clickBtnDot(event):
    sb.append(".")
    tf.setText(sb.toString())
    
def clickBtnDel(event):
    global sb
    l=sb.length()
    if(l==0):
        return
    else:
        st = sb.substring(0,l-1)
        tf.setText(st) #show on text field
        sbNew =StringBuilder(st) # now we have to convert the string into StringBuilder sowe pass the String into StringBuilder
        sb=sbNew # again update in sb
def clickBtnEqual(event):
    global sb
    st=sb.toString() # return as String
    ch =''
    i=0
    
    for c in st:
        i=i+1
        if(c== '+' or c=='-' or c=='*' or c=='/'):
            ch=c
            break
    str = String(st)   # if we have to call the java String class method then we have st as string but we have to tell that it is String so we make the object of string and
    #pass the string then str is work as String object and we easily call the method of java string class
    s1=str.substring(0,i-1) # if i=4 and + is at index 3 then we have to pass the 0 as starting  and 3 as second argument b/z it is excuding
    s2=str.substring(i)
    v1=Float.valueOf(s1) # we know that the vi value is Integer type value b/z we convert from string to Integer but in python we cann't assign the vtype of variable
    v2 =Float.valueOf(s2)
    if (ch == '+'):
        result=v1+v2
        #tf.setText(.toString(result))
    elif(ch=='-'):
        result=v1-v2
       # tf.setText(Integer.toString(result))
    elif(ch=='*'):
        result=v1*v2
        #tf.setText(Integer.toString(result))
    elif(ch=='/'):
        result=v1/v2 
        
        # we want the result in float so we import the __future__ in starting
    
    # now we have to set the text in textField as string and we have the value as Integer or float type
    #tf.setText()
    tf.setText(Float.toString(result))
    sb.delete(0,sb.length())    
    sb.insert(0,tf.getText())

btnDot=JButton(".",actionPerformed=clickBtnDot)
btnDot.setBounds(0,401,100,100)
btn0=JButton("0",actionPerformed=clickBtn0)
btn0.setBounds(101,401,100,100)
btnDel=JButton("DEL",actionPerformed=clickBtnDel)
btnDel.setBounds(201,401,100,100)
btn1=JButton("1",actionPerformed=clickBtn1)
btn1.setBounds(0,301,100,100)
btn2=JButton("2",actionPerformed=clickBtn2)
btn2.setBounds(101,301,100,100)
btn3=JButton("3",actionPerformed=clickBtn3)
btn3.setBounds(201,301,100,100)
btn4=JButton("4",actionPerformed=clickBtn4)
btn4.setBounds(0,201,100,100)
btn5=JButton("5",actionPerformed=clickBtn5)
btn5.setBounds(101,201,100,100)
btn6=JButton("6",actionPerformed=clickBtn6)
btn6.setBounds(201,201,100,100)
btn7=JButton("7",actionPerformed=clickBtn7)
btn7.setBounds(0,101,100,100)
btn8=JButton("8",actionPerformed=clickBtn8)
btn8.setBounds(101,101,100,100)
btn9=JButton("9",actionPerformed=clickBtn9)
btn9.setBounds(201,101,100,100)
btnDivide=JButton("/",actionPerformed=clickBtnDivide)
btnDivide.setBounds(301,101,100,80)
btnMultiply=JButton("*",actionPerformed=clickBtnMultiply)
btnMultiply.setBounds(301,181,100,80)
btnSubtract=JButton("-",actionPerformed=clickBtnSubtract)
btnSubtract.setBounds(301,261,100,80)
btnPlus=JButton("+",actionPerformed=clickBtnPlus)
btnPlus.setBounds(301,341,100,80)
btnEqual=JButton("=",actionPerformed=clickBtnEqual)
btnEqual.setBounds(301,421,100,80)

tf = JTextField("")
tf.setBounds(0,0,400,100)
tf.setHorizontalAlignment(JTextField.RIGHT)
font =  Font("Courier",Font.BOLD,30)		
tf.setFont(font)

    
     
    
frame.add(btnDot)
frame.add(btnDel)
frame.add(btn0)
frame.add(btnEqual)
frame.add(btn1)
frame.add(btn2)
frame.add(btn3)
frame.add(btn4)
frame.add(btn5)
frame.add(btn6)
frame.add(btn7)
frame.add(btn8)
frame.add(btn9)
frame.add(btnPlus)
frame.add(btnSubtract)
frame.add(btnMultiply)
frame.add(btnDivide)
frame.add(tf)


