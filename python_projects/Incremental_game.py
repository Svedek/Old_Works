# Future Note:
# The game is a fairly rudementary and stright forward
# incremental/idle game.
# Original Link: https://py2.codeskulptor.org/#user45_8V04TCNqVdiJRpy.py


#Samuel Walsh
import simplegui
import math

mon=0;

monBase=1;
monMod=1;
baseCost=10;
baseModCost=25;

autoT1=0;
autoT1mod=0;
T1cost=100;
T1modCost=250;
T1monPframe=0;

autoT2=0;
autoT2mod=0
T2cost=500;
T2modCost=1250;
T2monPframe=0;

autoT3=0;
autoT3mod=0;
T3cost=2500;
T3modCost=6250;
T3monPframe=0;

totMonPframe=0;

def test():
    global mon,monBase,monMod;
    mon=1000000000;
    
def c():
    global mon,monBase,monMod;
    mon+=monBase*monMod;
    
def cu():
    global monBase, baseCost, mon;
    if(mon>=baseCost):
        mon-=baseCost;
        baseCost=math.trunc(baseCost*1.125);
        monBase+=1;

def cm():
    global monMod, baseModCost, mon;
    if(mon>=baseModCost):
        mon-=baseModCost;
        baseModCost=math.trunc(baseModCost*1.875);
        monMod+=1;
        
def ac():
    global autoT1, T1cost, mon, T1monPframe, totMonPframe;
    if(mon>=T1cost):
        mon-=T1cost;
        T1cost=math.trunc(T1cost*1.175);
        autoT1+=1;
        T1monPframe=autoT1*0.01*autoT1mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;
        
def acm():
    global autoT1mod, T1modCost, mon, T1monPframe, totMonPframe;
    if(mon>=T1modCost):
        mon-=T1modCost;
        T1modCost=math.trunc(T1modCost*2.125);
        autoT1mod+=1;
        T1monPframe=autoT1*0.01*autoT1mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;
        
def mc():
    global autoT2, T2cost, mon, T2monPframe, totMonPframe;
    if(mon>=T2cost):
        mon-=T2cost;
        T2cost=math.trunc(T2cost*1.25);
        autoT2+=1;
        T2monPframe=autoT2*0.075*autoT2mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;
        
def mcm():
    global autoT2mod, T2modCost, mon, T2monPframe, totMonPframe;
    if(mon>=T2modCost):
        mon-=T2modCost;
        T2modCost=math.trunc(T2modCost*2.325);
        autoT2mod+=1;
        T2monPframe=autoT2*0.075*autoT2mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;
        
def uc():
    global autoT3, T3cost, mon, T3monPframe, totMonPframe;
    if(mon>=T3cost):
        mon-=T3cost;
        T3cost=math.trunc(T3cost*1.325);
        autoT3+=1;
        T3monPframe=autoT3*0.45*autoT3mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;
        
def ucm():
    global autoT3mod, T3modCost, mon, T3monPframe, totMonPframe;
    if(mon>=T3modCost):
        mon-=T3modCost;
        T3modCost=math.trunc(T3modCost*2.625);
        autoT3mod+=1;
        T3monPframe=autoT3*0.45*autoT3mod;
        totMonPframe=T1monPframe+T2monPframe+T3monPframe;

# Handler to draw on canvas
def draw(canvas):
    global mon
    canvas.draw_text("muns", [450,80], 20, "Red")
    canvas.draw_text(str(mon), [425,100], 20, "Red")
    canvas.draw_text(str(monBase*monMod)+" mun per click", [10,18], 22, "Blue")
    canvas.draw_text("Cost: "+str(baseCost)+" mons - "+str(monBase)+" click upgrades", [10,38], 18, "Blue")
    canvas.draw_text("Cost: "+str(baseModCost)+" mons - "+str(monMod)+"x click multiplyer", [10,56], 18, "Blue")
    canvas.draw_text(str(T1monPframe)+" mun per frame from Auto clickers", [10,72], 16, "Green")
    canvas.draw_text("Cost: "+str(T1cost)+" mons - "+str(autoT1)+" Auto clickers", [10,86], 16, "Green")
    canvas.draw_text("Cost: "+str(T1modCost)+" mons - "+str(autoT1mod)+"x Auto clicker multiplyer", [10,100], 16, "Green")
    canvas.draw_text(str(T2monPframe)+" mun per frame from Mega clickers", [10,116], 16, "Yellow")
    canvas.draw_text("Cost: "+str(T2cost)+" mons - "+str(autoT2)+" Mega clickers", [10,130], 16, "Yellow")
    canvas.draw_text("Cost: "+str(T2modCost)+" mons - "+str(autoT2mod)+"x Mega clicker multiplyer", [10,144], 16, "Yellow")
    canvas.draw_text(str(T3monPframe)+" mun per frame from Ultra clickers", [10,160], 16, "Red")
    canvas.draw_text("Cost: "+str(T3cost)+" mons - "+str(autoT3)+" Ultra clickers", [10,174], 16, "Red")
    canvas.draw_text("Cost: "+str(T3modCost)+" mons - "+str(autoT3mod)+"x Ultra clicker multiplyer", [10,188], 16, "Red")
    #auto mon generation
    mon+=totMonPframe;
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 300)
frame.add_button("Click", c)
frame.add_button("Click Upgrade", cu)
frame.add_button("Click Multiplier", cm)
frame.add_button("Auto Clicker", ac)
frame.add_button("Auto Clicker Multiplier", acm)
frame.add_button("Mega Clicker", mc)
frame.add_button("Mega Clicker Multiplier", mcm)
frame.add_button("Ultra Clicker", uc)
frame.add_button("Ultra Clicker Multiplier", ucm)
frame.add_button("Test", test)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
