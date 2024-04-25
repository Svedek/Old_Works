# Future Note:
# This is the project I remember most fondly from this time,
# it was essentially my final for my computer science course.
# I actually still think of the way I did the turns here and,
# although it was undoubtably not intentional, I think the idea
# was cool. That certain abilities (although not well explained)
# take up a partail turn or stop the enemy from taking their turn.
# Similar things can be seen a lot in similar games with things like
# status effects and more refined mechanics lol.
# Original Link: https://py2.codeskulptor.org/#user44_Cy7bwVedjskuEVX.py


#Samuel Walsh

import simplegui
import random

action = 0 #different value for each different action so different animation for each different action
ani = 0
anibuf = 0
eani = 0
eanibuf = 0
hid = 16
stbf = 0
dy = 1
dead = 0
stage = 0; # 0 = start, 1 = character sheet, 2 = store, 3 = map, 4 = combat
substage = 0; #0=near start 1=Eforest 2=Lforest 3=path 4=Edungeon 5=Ldungeon 6=Bdungeon -store- 7=Ekingdom 8=Lkingdom 9=Bkingdom 10=Castle 11=EndBoss
progress = 0 #0-5, after 5 new substage
gold = 35;
unspec = 6;
vita = 2;
stre = 2;
dext = 2;
agil = 2;
inti = 2;
luck = 2;
bandage = 0;
mpot = 0;
arrow = 0;
sword = 0;
sword2 = 0;
bow = 0;
bow2 = 0;
enemy = 0;
ehp = 0;
ehpmax = 0;
php = 6;
phpmax = 6;
pmp = 6;
pmpmax = 6;
pxp = 0;
level = 1;
pxpr = 12;
pxpl = 0;
edmg = 0;
xpg = 0;
gpg = 0;
collected = 0;
amp = 0;    # 1 = active, 0 = inactive
strike = 0; # 1 = active, 0 = inactive
ice = 0;    # 1 = active, 0 = inactive
prot = 0;
subturn = 0;
shock = 0;

# Handler for mouse click
def button_click(position):
    global stage, collected, subturn, gold, mpot, bandage, arrow, sword, bow, phpmax, pmpmax, php, pmp, ehp, amp
    global unspec, vita, stre, dext, agil, inti, luck, strike, ice, bownum, pxpr, pxp, phpmax, pmpmax, enemy, bow2
    global shock, prot, gpg, xpg, edmg, pxpl, sword2, dead, substage, progress, action
    if stage == 0:### Start Screen
        #start button
        if (position[0] >= 330 and position[0] <= 470) and (position[1] >= 530 and position[1] <= 575):
            stage = 1
    
    elif stage == 1:### Character Creation Screen
        #positive buttons
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 25 and position[1] <= 63):
            if unspec > 0:
                vita = vita + 1
                unspec = unspec - 1
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 75 and position[1] <= 113):
            if unspec > 0:
                stre = stre + 1
                unspec = unspec - 1
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 125 and position[1] <= 163):   
            if unspec > 0:
                dext = dext + 1
                unspec = unspec - 1
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 175 and position[1] <= 213): 
            if unspec > 0:
                agil = agil + 1
                unspec = unspec - 1
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 225 and position[1] <= 263):
            if unspec > 0:
                inti = inti + 1
                unspec = unspec - 1
        if (position[0] >= 380 and position[0] <= 418) and (position[1] >= 275 and position[1] <= 313):
            if unspec > 0:
                luck = luck + 1
                unspec = unspec - 1
        
        #negetive buttons
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 25 and position[1] <= 63):
            if vita > 1:
                vita = vita - 1
                unspec = unspec + 1
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 75 and position[1] <= 113):
            if stre > 1:
                stre = stre - 1
                unspec = unspec + 1
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 125 and position[1] <= 163):   
            if dext > 1:
                dext = dext - 1
                unspec = unspec + 1
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 175 and position[1] <= 213): 
            if agil > 1:
                agil = agil - 1
                unspec = unspec + 1
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 225 and position[1] <= 263):
            if inti > 1:
                inti = inti - 1
                unspec = unspec + 1
        if (position[0] >= 430 and position[0] <= 468) and (position[1] >= 275 and position[1] <= 313):
            if luck > 1:
                luck = luck - 1
                unspec = unspec + 1
                
        #continue button
        if unspec == 0:
            if (position[0] >= 310 and position[0] <= 495) and (position[1] >= 530 and position[1] <= 575):
                stage = 2
                phpmax = (vita * 4) + 5
                php = phpmax
                pmpmax = (inti * 3) + 4
                pmp = pmpmax
                
    elif stage == 2:### Store
        #Buying
        if (position[0] >= 350 and position[0] <= 500) and (position[1] >= 50 and position[1] <= 100):
            if gold >= 15:
                gold = gold - 15
                bow = bow + 1
                
        if (position[0] >= 350 and position[0] <= 500) and (position[1] >= 120 and position[1] <= 170):
            if gold >= 2:
                gold = gold - 2
                arrow = arrow + 1
                
        if (position[0] >= 350 and position[0] <= 500) and (position[1] >= 190 and position[1] <= 240):
            if gold >= 20:
                gold = gold - 20
                sword = sword + 1
                
        if (position[0] >= 350 and position[0] <= 500) and (position[1] >= 260 and position[1] <= 310):
            if gold >= 5:
                gold = gold - 5
                bandage = bandage + 1
                
        if (position[0] >= 350 and position[0] <= 500) and (position[1] >= 330 and position[1] <= 380):
            if gold >= 6:
                gold = gold - 6
                mpot = mpot + 1
                
        #Selling
        if (position[0] >= 600 and position[0] <= 750) and (position[1] >= 50 and position[1] <= 100):
            if bow >= 1:
                bow = bow - 1
                gold = gold + 15
        
        if (position[0] >= 600 and position[0] <= 750) and (position[1] >= 120 and position[1] <= 170):
            if arrow >= 1:
                arrow = arrow - 1
                gold = gold + 2
                
        if (position[0] >= 600 and position[0] <= 750) and (position[1] >= 190 and position[1] <= 240):
            if sword >= 1:
                sword = sword - 1
                gold = gold + 20
                
        if (position[0] >= 600 and position[0] <= 750) and (position[1] >= 260 and position[1] <= 310):
            if bandage >= 1:
                bandage = bandage - 1
                gold = gold + 5
                
        if (position[0] >= 600 and position[0] <= 750) and (position[1] >= 330 and position[1] <= 380):
            if mpot >= 1:
                mpot = mpot - 1
                gold = gold + 6
                
        #continue button
        if (position[0] >= 310 and position[0] <= 495) and (position[1] >= 530 and position[1] <= 575):
            stage = 3
         
            
    elif stage == 3:### Combat
        ##Basic combat
        #Basic attack
        if (position[0] >= 35 and position[0] <= 140) and (position[1] >= 390 and position[1] <= 430):
            if sword2 >= 1:
                ehp = ehp - (stre*3 + random.randint((luck*2),(luck*3)))
                endturn()
            elif sword >= 1:
                ehp = ehp - (stre*2 + random.randint((luck*1),(luck*2)))
                endturn()
            else:
                ehp = ehp - (stre + random.randint(0,(luck)))
                endturn()
                
        #Shoot
        if (position[0] >= 35 and position[0] <= 140) and (position[1] >= 440 and position[1] <= 480):
            if bow2 >= 1 and arrow >= 1:
                ehp = ehp - (dext*3 + random.randint((luck*3),(luck*4)))
                arrow = arrow - 1
                if subturn >= 1:
                    endturn()
                    subturn = 0
                else:
                    subturn = 1
                    statreg()
            elif bow >= 1 and arrow >= 1:
                ehp = ehp - (dext*2 + random.randint((luck*1),(luck*3)))
                arrow = arrow - 1
                if subturn >= 1:
                    endturn()
                    subturn = 0
                else:
                    subturn = 1
                    statreg()
        ##Consumables
        #Bandage
        if (position[0] >= 35 and position[0] <= 140) and (position[1] >= 490 and position[1] <= 530):
            if bandage > 0:
                print "bandage"
                php = php + ((phpmax/3) + random.randint((luck),(luck*2)))
                bandage = bandage - 1
                if subturn >= 1:
                    endturn()
                    subturn = 0
                else:
                    subturn = 1
                    statreg()
        #MPot
        if (position[0] >= 35 and position[0] <= 140) and (position[1] >= 540 and position[1] <= 580):
            if mpot > 0:
                pmp = pmp + ((phpmax/2) + random.randint((luck*2),(luck*3)))
                mpot = mpot - 1
                print "mpot"
                if subturn >= 1:
                    endturn()
                    subturn = 0
                else:
                    subturn = 1
                    statreg()
                    
        ###Spells
        ##Column 1
        #S. Heal
        if (position[0] >= 150 and position[0] <= 255) and (position[1] >= 390 and position[1] <= 430):
            if inti >= 3:
                if pmp >= 4:
                    pmp = pmp - 4
                    php = php + ((phpmax/5) + random.randint(0,2))
                    endturn()
        #Amp Attack
        if (position[0] >= 150 and position[0] <= 255) and (position[1] >= 440 and position[1] <= 480):
            if inti >= 4:
                if pmp >= 6:
                    pmp = pmp - 6
                    amp = 1
                    endturn()
        #Ice bolt
        if (position[0] >= 150 and position[0] <= 255) and (position[1] >= 490 and position[1] <= 530):
            if inti >= 5:
                if pmp >= 5:
                    pmp = pmp - 5
                    ehp = ehp - (inti + random.randint(0,2))
                    endturn()
        #Heal
        if (position[0] >= 150 and position[0] <= 255) and (position[1] >= 540 and position[1] <= 580):
            print "heal"
            if inti >= 6:
                if pmp >= 6:
                    pmp = pmp - 6
                    php = php + ((phpmax/4) + random.randint(2,5))
                    endturn()

        ##Column 2
        #Deadly Strike
        if (position[0] >= 265 and position[0] <= 370) and (position[1] >= 390 and position[1] <= 430):
            if inti >= 7:
                if pmp >= 8:
                    pmp = pmp - 8
                    strike = 1
                    endturn()
        #Fireball
        if (position[0] >= 265 and position[0] <= 370) and (position[1] >= 440 and position[1] <= 480):
            if inti >= 9:
                if pmp >= 7:
                    pmp = pmp - 7
                    ehp = ehp - ((inti*2) + random.randint(0,2))
                    endturn()
        #L. Heal
        if (position[0] >= 38 and position[0] <= 370) and (position[1] >= 490 and position[1] <= 530):
            if inti >= 9:
                if pmp >= 8:
                    pmp = pmp - 8
                    php = php + ((phpmax/3) + random.randint(5,8))
                    endturn()
        #Freeze
        if (position[0] >= 265 and position[0] <= 370) and (position[1] >= 540 and position[1] <= 580):
            if inti >= 10:
                if pmp >= 8:
                    if ice == 0:
                        pmp = pmp - 8
                        ice = 1     
        ##Column 3
        #Battle focus
        if (position[0] >= 380 and position[0] <= 485) and (position[1] >= 390 and position[1] <= 430):
            if inti >= 12:
                if enemy >= 1:
                    pmp = pmp + ((pmpmax/5) + random.randint(5,8))
                    php = php + ((phpmax/5) + random.randint(5,8))
                    endturn()
        #G. Heal
        if (position[0] >= 380 and position[0] <= 485) and (position[1] >= 440 and position[1] <= 480):
            if inti >= 14:
                if pmp >= 10:
                    pmp = pmp - 10
                    php = php + ((phpmax/2) + random.randint(8,12))
                    endturn()
        #Electric Storm
        if (position[0] >= 380 and position[0] <= 485) and (position[1] >= 490 and position[1] <= 530):
            if inti >= 17:
                if pmp >= 14:
                    pmp = pmp - 14
                    ehp = ehp - ((inti*3) + random.randint(3,5))
                    statreg()
        #cataclysm
        if (position[0] >= 380 and position[0] <= 485) and (position[1] >= 540 and position[1] <= 580):
            if inti >= 19:
                if pmp >= 18:
                    pmp = pmp - 18
                    ehp = ehp - ((inti*5) + random.randint(12,15))
                    endturn()
        #Continue button for progression
        if (position[0] >= 625 and position[0] <= 800) and (position[1] >= 175 and position[1] <= 225):
            if enemy == 0:
                nextsubstage()
                subturn = 0
                collected = 0
    elif stage == 4 or stage == -1:
        if (position[0] >= 300 and position[0] <= 500) and (position[1] >= 450 and position[1] <= 500):
            dead = 0
            stage = 0; # 0 = start, 1 = character sheet, 2 = store, 3 = map, 4 = combat
            substage = 0; #0=near start 1=Eforest 2=Lforest 3=path 4=Edungeon 5=Ldungeon 6=Bdungeon -store- 7=Ekingdom 8=Lkingdom 9=Bkingdom 10=Castle 11=EndBoss
            progress = 0 #0-5, after 5 new substage
            gold = 75;
            unspec = 6;
            vita = 2;
            stre = 2;
            dext = 2;
            agil = 2;
            inti = 2;
            luck = 2;
            bandage = 0;
            mpot = 0;
            arrow = 0;
            sword = 0;
            sword2 = 0;
            bow = 0;
            bow2 = 0;
            enemy = 0;
            ehp = 0;
            ehpmax = 0;
            php = 6;
            phpmax = 6;
            pmp = 6;
            pmpmax = 6;
            pxp = 0;
            level = 1;
            pxpr = 12;
            pxpl = 0;
            edmg = 0;
            xpg = 0;
            gpg = 0;
            collected = 0;
            amp = 0;    # 1 = active, 0 = inactive
            strike = 0; # 1 = active, 0 = inactive
            ice = 0;    # 1 = active, 0 = inactive
            prot = 0;
            subturn = 0;
            shock = 0;
            

def draw(canvas):
    if stage == 0: # start screen ==================================================================================
        global dy, stbf, hid, action
        if stbf >= 6:
            if dy > -3:
                dy = dy - 0.03
                if hid < 49:
                    hid = hid + 1
        else:
            stbf = stbf + 1
        #background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 10, "#5555cc", "#5555cc")
        ##clouds
        #909090
        canvas.draw_circle([60,60 + 10/dy], 100, 25, "#909090", "#909090")
        canvas.draw_circle([220,60 + 10/dy], 100, 25, "#909090", "#909090")
        canvas.draw_circle([380,60 + 10/dy], 100, 25, "#909090", "#909090")
        canvas.draw_circle([540,60 + 10/dy], 100, 25, "#909090", "#909090")
        canvas.draw_circle([700,60 + 10/dy], 100, 25, "#909090", "#909090")
        canvas.draw_circle([760,40 + 10/dy], 40, 25, "#909090", "#909090")
        #a0a0a0
        canvas.draw_circle([500,80 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([550,70 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([685,75 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([430,75 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([620,70 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([50,106 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([70,56 + 10/dy], 50, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([180,111 + 10/dy], 100, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([140,111 + 10/dy], 80, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([230,126 + 10/dy], 75, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([275,96 + 10/dy], 70, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([360,106 + 10/dy], 85, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([415,106 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([735,86 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([645,116 + 10/dy], 80, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([715,141 + 10/dy], 40, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([595,96 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([520,126 + 10/dy], 60, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([458,170 + 10/dy], 5, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([434,170 + 10/dy], 15, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([300,170 + 10/dy], 15, 30, "#a0a0a0", "#a0a0a0")
        canvas.draw_circle([412,180 + 10/dy], 5, 30, "#a0a0a0", "#a0a0a0")

        #a8a8a8
        canvas.draw_circle([174,122 + 10/dy], 80, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([240,122 + 10/dy], 40, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([110,102 + 10/dy], 40, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([290,102 + 10/dy], 55, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([350,122 + 10/dy], 40, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([410,92 + 10/dy], 60, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([490,102 + 10/dy], 60, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([560,92 + 10/dy], 60, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([620,112 + 10/dy], 60, 25, "#a8a8a8", "#a8a8a8")
        canvas.draw_circle([680,102 + 10/dy], 60, 25, "#a8a8a8", "#a8a8a8")
        
        #b0b0b0
        canvas.draw_circle([169,124 + 10/dy], 55, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([229,114 + 10/dy], 40, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([288,105 + 10/dy], 40, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([350,117 + 10/dy], 30, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([410,90 + 10/dy], 45, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([490,105 + 10/dy], 45, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([565,95 + 10/dy], 45, 21, "#b0b0b0", "#b0b0b0")
        canvas.draw_circle([650,105 + 10/dy], 45, 21, "#b0b0b0", "#b0b0b0")
        
        #furtherst hill
        canvas.draw_circle([630,480 - 10/dy], 200, 30, "#00aa33")
        canvas.draw_circle([622,485 - 10/dy], 180, 30, "#00af33")
        canvas.draw_circle([614,490 - 10/dy], 160, 45, "#00b533")
        canvas.draw_circle([606,495 - 10/dy], 120, 55, "#00ba33")
        canvas.draw_circle([598,500 - 10/dy], 80, 50, "#00bf33")
        canvas.draw_circle([590,505 - 10/dy], 40, 50, "#00c533")
        canvas.draw_circle([582,510 - 10/dy], 15, 40, "#00ca33", "#00ca33")
        #middle hill
        canvas.draw_circle([380,510 - 10/dy], 200, 30, "#00aa33")
        canvas.draw_circle([372,515 - 10/dy], 180, 30, "#00af33")
        canvas.draw_circle([364,520 - 10/dy], 160, 45, "#00b533")
        canvas.draw_circle([356,525 - 10/dy], 120, 55, "#00ba33")
        canvas.draw_circle([348,530 - 10/dy], 80, 50, "#00bf33")
        canvas.draw_circle([340,535 - 10/dy], 40, 50, "#00c533")
        canvas.draw_circle([332,540 - 10/dy], 15, 40, "#00ca33", "#00ca33")
        #closest hill
        canvas.draw_circle([160,550 - 10/dy], 200, 30, "#00aa33")
        canvas.draw_circle([152,555 - 10/dy], 180, 30, "#00af33")
        canvas.draw_circle([144,560 - 10/dy], 160, 45, "#00b533")
        canvas.draw_circle([136,565 - 10/dy], 120, 55, "#00ba33")
        canvas.draw_circle([128,570 - 10/dy], 80, 50, "#00bf33")
        canvas.draw_circle([120,575 - 10/dy], 40, 50, "#00c533")
        canvas.draw_circle([112,580 - 10/dy], 15, 40, "#00ca33", "#00ca33")

        #draw ground
        canvas.draw_polygon([(0,580),(800,500),(800,600),(0,600)], 10, "#00aa33", "#00aa33")
        #Tower
        canvas.draw_polygon([(640,280 - 10/dy),(680,280 - 10/dy),(680,165 - 10/dy),(640,165 - 10/dy)], 2, "#666666", "#888888")
        canvas.draw_polygon([(635,165 - 10/dy),(660,105 - 10/dy),(685,165 - 10/dy)], 2, "#bd752f", "#cd853f")
        canvas.draw_polygon([(655,200 - 10/dy),(656,194 - 10/dy),(660,192 - 10/dy),(664,194 - 10/dy),(665,200 - 10/dy)], 2, "#333333", "#111111")
        canvas.draw_polygon([(653,203 - 10/dy),(667,203 - 10/dy),(667,204 - 10/dy),(653,204 - 10/dy),], 1, "#cd853f", "#cd853f")
        #start button + title
        canvas.draw_text('Title',[298,298] , 81, "#b0c525" + str(hid * 2))
        canvas.draw_text('Title',[300,300] , 80, "#b02525" + str(hid * 2))
        canvas.draw_polygon([(335,575),(470,575),(470,530),(335,530),], 5, "#daa520", "#800000")
        canvas.draw_text('Start',[355,569] , 48, "#b02525")
        
    elif stage == 1: # character sheet ================================================================================
        #background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 10, "#deb887", "#deb887")
        ### stats
        #stat text
        canvas.draw_text('Vitality:            ' + str(vita),[35,60] , 48, "#fec897")
        canvas.draw_text('Strength:          ' + str(stre),[38,110] , 48, "#f7cf89")
        canvas.draw_text('Dexterity:        ' + str(dext),[38,160] , 48, "#fec897")
        canvas.draw_text('Agility:            ' + str(agil),[36,210] , 48, "#f7cf89")
        canvas.draw_text('Intelligence:    ' + str(inti),[38,260] , 48, "#fec897")
        canvas.draw_text('Luck:               ' + str(luck),[38,310] , 48, "#f7cf89")
        canvas.draw_text('Points unspent:   ' + str(unspec),[38,410] , 48, "#f7dfa9")
        ##stat buttons
        #positive buttons
        canvas.draw_polygon([(380,25),(380,63),(418,63),(418,25)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,30),(385,58),(413,58),(413,30)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,42),(397,42),(397,30),(401,30),(401,42),(413,42),(413,46),(401,46),(401,58),(397,58),(397,46),(385,46)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(380,75),(380,113),(418,113),(418,75)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,80),(385,108),(413,108),(413,80)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,92),(397,92),(397,80),(401,80),(401,92),(413,92),(413,96),(401,96),(401,108),(397,108),(397,96),(385,96)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(380,125),(380,163),(418,163),(418,125)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,130),(385,158),(413,158),(413,130)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,142),(397,142),(397,130),(401,130),(401,142),(413,142),(413,146),(401,146),(401,158),(397,158),(397,146),(385,146)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(380,175),(380,213),(418,213),(418,175)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,180),(385,208),(413,208),(413,180)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,192),(397,192),(397,180),(401,180),(401,192),(413,192),(413,196),(401,196),(401,208),(397,208),(397,196),(385,196)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(380,225),(380,263),(418,263),(418,225)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,230),(385,258),(413,258),(413,230)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,242),(397,242),(397,230),(401,230),(401,242),(413,242),(413,246),(401,246),(401,258),(397,258),(397,246),(385,246)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(380,275),(380,313),(418,313),(418,275)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(385,280),(385,308),(413,308),(413,280)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(385,292),(397,292),(397,280),(401,280),(401,292),(413,292),(413,296),(401,296),(401,308),(397,308),(397,296),(385,296)], 1, "#daa520", "#fab530")
        
        #negetive buttons
        canvas.draw_polygon([(430,25),(430,63),(468,63),(468,25)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,30),(435,58),(463,58),(463,30)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,42),(463,42),(463,46),(435,46)], 1, "#daa520", "#fab530")

        canvas.draw_polygon([(430,75),(430,113),(468,113),(468,75)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,80),(435,108),(463,108),(463,80)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,92),(463,92),(463,96),(435,96)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(430,125),(430,163),(468,163),(468,125)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,130),(435,158),(463,158),(463,130)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,142),(463,142),(463,146),(435,146)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(430,175),(430,213),(468,213),(468,175)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,180),(435,208),(463,208),(463,180)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,192),(463,192),(463,196),(435,196)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(430,225),(430,263),(468,263),(468,225)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,230),(435,258),(463,258),(463,230)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,242),(463,242),(463,246),(435,246)], 1, "#daa520", "#fab530")
        
        canvas.draw_polygon([(430,275),(430,313),(468,313),(468,275)], 5, "#daa520", "#800000")
        canvas.draw_polygon([(435,280),(435,308),(463,308),(463,280)], 1, "#daa520", "#800000")
        canvas.draw_polygon([(435,292),(463,292),(463,296),(435,296)], 1, "#daa520", "#fab530")
        #Continue button
        if unspec == 0:
            canvas.draw_polygon([(310,575),(495,575),(495,530),(310,530),], 5, "#daa520", "#800000")
            canvas.draw_text('Continue',[313,569] , 48, "#b02525")
    elif stage == 2: # Store ========================================================================================
        # Background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 1, "#439423", "#439423")
        #continue
        canvas.draw_polygon([(310,575),(495,575),(495,530),(310,530),], 5, "#daa520", "#800000")
        canvas.draw_text('Continue',[313,569] , 48, "#b02525")
        #Items
        canvas.draw_polygon([(350,50),(350,100),(500,100),(500,50)], 3, "#aaba25", "#430423")
        canvas.draw_polygon([(353,53),(353,97),(497,97),(497,53)], 1, "#aaba25")
        canvas.draw_text('Bow',[355,88] , 40, "#b02525")
        canvas.draw_text('15g',[300,88] , 32, "#b02525")
        
        canvas.draw_polygon([(350,120),(350,170),(500,170),(500,120)], 3, "#aaba25", "#430423")
        canvas.draw_polygon([(353,123),(353,167),(497,167),(497,123)], 1, "#aaba25")
        canvas.draw_text('Arrow',[355,158] , 40, "#b02525")
        canvas.draw_text('2g',[300,158] , 32, "#b02525")
        
        canvas.draw_polygon([(350,190),(350,240),(500,240),(500,190)], 3, "#aaba25", "#430423")
        canvas.draw_polygon([(353,193),(353,237),(497,237),(497,193)], 1, "#aaba25")
        canvas.draw_text('Sword',[355,228] , 40, "#b02525")
        canvas.draw_text('20g',[300,228] , 32, "#b02525")
        
        canvas.draw_polygon([(350,260),(350,310),(500,310),(500,260)], 3, "#aaba25", "#430423")
        canvas.draw_polygon([(353,263),(353,307),(497,307),(497,263)], 1, "#aaba25")
        canvas.draw_text('Bandage',[355,298] , 40, "#b02525")
        canvas.draw_text('5g',[300,298] , 32, "#b02525")
                
        canvas.draw_polygon([(350,330),(350,380),(500,380),(500,330)], 3, "#aaba25", "#430423")
        canvas.draw_polygon([(353,333),(353,377),(497,377),(497,333)], 1, "#aaba25")
        canvas.draw_text('MPotion',[355,368] , 40, "#b02525")
        canvas.draw_text('6g',[300,368] , 32, "#b02525")
        #Inventory
        canvas.draw_text('Inventory',[612,25] , 32, "#fab530")
        canvas.draw_text(str(gold) + 'g',[525,25] , 32, "#fab530")
        
        if bow > 0:
            canvas.draw_polygon([(600,50),(600,100),(750,100),(750,50)], 3, "#aaba25", "#430423")
            canvas.draw_polygon([(603,53),(603,97),(747,97),(747,53)], 1, "#aaba25")
            if bow > 1 :
                canvas.draw_text(str(bow) + ' Bows',[605,88] , 28, "#b02525")
            else:
                canvas.draw_text(str(bow) + ' Bow',[605,88] , 28, "#b02525")
        
        if arrow > 0:
            canvas.draw_polygon([(600,120),(600,170),(750,170),(750,120)], 3, "#aaba25", "#430423")
            canvas.draw_polygon([(603,123),(603,167),(747,167),(747,123)], 1, "#aaba25")
            if arrow > 1 :
                canvas.draw_text(str(arrow) + ' Arrows',[605,158] , 28, "#b02525")
            else:
                canvas.draw_text(str(arrow) + ' Arrow',[605,158] , 28, "#b02525")
            
        if sword > 0:
            canvas.draw_polygon([(600,190),(600,240),(750,240),(750,190)], 3, "#aaba25", "#430423")
            canvas.draw_polygon([(603,193),(603,237),(747,237),(747,193)], 1, "#aaba25")
            if sword > 1 :
                canvas.draw_text(str(sword) + ' Swords',[605,228] , 28, "#b02525")
            else:
                canvas.draw_text(str(sword) + ' Sword',[605,228] , 28, "#b02525")
        
        if bandage > 0:
            canvas.draw_polygon([(600,260),(600,310),(750,310),(750,260)], 3, "#aaba25", "#430423")
            canvas.draw_polygon([(603,263),(603,307),(747,307),(747,263)], 1, "#aaba25")
            if bandage > 1 :
                canvas.draw_text(str(bandage) + ' Bandages',[605,298] , 28, "#b02525")
            else:
                canvas.draw_text(str(bandage) + ' Bandage',[605,298] , 28, "#b02525")
        
        if mpot > 0:
            canvas.draw_polygon([(600,330),(600,380),(750,380),(750,330)], 3, "#aaba25", "#430423")
            canvas.draw_polygon([(603,333),(603,377),(747,377),(747,333)], 1, "#aaba25")
            if bandage > 1 :
                canvas.draw_text(str(mpot) + ' MPotions',[605,368] , 28, "#b02525")
            else:
                canvas.draw_text(str(mpot) + ' MPotion',[605,368] , 28, "#b02525")
                
    elif stage == 3: # Combat ========================================================================================
        # Enemy Animation Clock
        global eani, eanibuf, ani, anibuf
        if enemy != 0: # 5 animation slides for each enemy... gl hf
            if eanibuf >= 8:
                eani = eani + 1
                eanibuf = 0
                if eani > 5:
                    eani = 0
            else:
                eani = eani + 1
        
        # Background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 10, "#dfdfdf", "#dfdfdf")
        #"map"
        if substage == 0:
            canvas.draw_text('Map: Just out of town',[20,30] , 24, "#b02525")
        if substage == 1:
            canvas.draw_text('Map: Early Forest',[20,30] , 24, "#b02525")
        if substage == 2:
            canvas.draw_text('Map: Late Forest',[20,30] , 24, "#b02525")
        if substage == 3:
            canvas.draw_text('Map: Dangerous Road',[20,30] , 24, "#b02525")
        if substage == 4:
            canvas.draw_text('Map: Early Dungeon',[20,30] , 24, "#b02525")
        if substage == 5:
            canvas.draw_text('Map: Late Dungeon',[20,30] , 24, "#b02525")    
        if substage == 6:
            canvas.draw_text('Map: Dungeon Boss',[20,30] , 24, "#b02525")
        if substage == 7:
            canvas.draw_text('Map: Early City',[20,30] , 24, "#b02525")
        if substage == 8:
            canvas.draw_text('Map: Late City',[20,30] , 24, "#b02525")    
        if substage == 9:
            canvas.draw_text('Map: City Boss',[20,30] , 24, "#b02525")    
        if substage == 10:
            canvas.draw_text('Map: Castle Grounds',[20,30] , 24, "#b02525")
        if substage == 11:
            canvas.draw_text('Map: Castle Boss',[20,30] , 24, "#b02525")    
        ## Status
        canvas.draw_polygon([(575,650),(850,650),(850,450),(575,450)], 10, "#bfbfbf", "#9f9f9f")
        #Experience
        canvas.draw_text('Level '+str(level),[585,420], 20, "#11ff66")
        canvas.draw_text('Experience  ' + str(pxp) + '/' + str(pxpr),[585,435] , 20, "#11ff66")
        canvas.draw_polygon([(585,440),(790,440),(790,450),(585,450)], 2, "#000000", "#333333")
        canvas.draw_polygon([(587,442),(587 + (((pxp-pxpl)*203)/(pxpr-pxpl)),442),(587 + (((pxp-pxpl)*203)/(pxpr-pxpl)),448),(587,448)], 2, "#11cc44", "#11cc44")
        #health
        canvas.draw_text('Health  ' + str(php) + '/' + str(phpmax),[600,475] , 24, "#b02525")
        canvas.draw_polygon([(600,480),(602 + (phpmax * 2),480),(602 + (phpmax * 2),490),(600,490)], 2, "#000000", "#333333")
        canvas.draw_polygon([(602,482),(600 + (php * 2),482),(600 + (php * 2),488),(602,488)], 2, "#dd3333", "#dd3333")
        #mana
        canvas.draw_text('Magic ' + str(pmp) + '/' + str(pmpmax),[600,520] , 24, "#b02525")
        canvas.draw_polygon([(600,525),(602 + (pmpmax * 2),525),(602 + (pmpmax * 2),535),(600,535)], 2, "#000000", "#333333")
        canvas.draw_polygon([(602,527),(600 + (pmp * 2),527),(600 + (pmp * 2),533),(602,533)], 2, "#3333dd", "#3333dd")
        ##Items
        #Consumables
        canvas.draw_text(str(bandage) + ' Bandages',[600,550] , 16, "#44ff66")
        canvas.draw_text(str(mpot) + ' Magic Potions',[600,565] , 16, "#44ff66")
        #Gold
        canvas.draw_text(str(gold) + ' Gold',[600,590] , 16, "#dddd44")
        
        ## Combat options
        # Standard Attacks bow + sword
        if sword == 0:
            canvas.draw_polygon([(35,390),(35,430),(140,430),(140,390)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Punch',[45,425] , 32, "#b02525")
        else:
            canvas.draw_polygon([(35,390),(35,430),(140,430),(140,390)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Attack',[45,425] , 32, "#b02525")
        
        if bow > 0 and arrow > 0:
            canvas.draw_polygon([(35,440),(35,480),(140,480),(140,440)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Shoot',[45,475] , 32, "#b02525")
            
        # Consumables
        if bandage > 0:
            canvas.draw_polygon([(35,490),(35,530),(140,530),(140,490)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Bandage',[45,525] , 32, "#b02525")
            
        if mpot > 0:
            canvas.draw_polygon([(35,540),(35,580),(140,580),(140,540)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Mpot',[45,575] , 32, "#b02525")
            
        ## Spells
        #Column 1
        if inti >= 3:
            canvas.draw_polygon([(150,390),(150,430),(255,430),(255,390)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Small Heal',[155,410] , 20, "#b02525")
            canvas.draw_text('4 MP',[155,425] , 20, "#b02525")
        if inti >= 4:
            canvas.draw_polygon([(150,440),(150,480),(255,480),(255,440)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Amplify',[155,460] , 20, "#b02525")
            canvas.draw_text('6 MP',[155,475] , 20, "#b02525")
        if inti >= 5:
            canvas.draw_polygon([(150,490),(150,530),(255,530),(255,490)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Ice Bolt',[155,510] , 20, "#b02525")
            canvas.draw_text('5 MP',[155,525] , 20, "#b02525")
        if inti >= 6:
            canvas.draw_polygon([(150,540),(150,580),(255,580),(255,540)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Heal',[155,560] , 20, "#b02525")
            canvas.draw_text('6 MP',[155,575] , 20, "#b02525")
        #Column 2
        if inti >= 7:
            canvas.draw_polygon([(265,390),(265,430),(370,430),(370,390)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Deadly Strike',[270,410] , 20, "#b02525")
            canvas.draw_text('8 MP',[270,425] , 20, "#b02525")
        if inti >= 9:
            canvas.draw_polygon([(265,440),(265,480),(370,480),(370,440)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Fireball',[270,460] , 20, "#b02525")
            canvas.draw_text('7 MP',[270,475] , 20, "#b02525")
        if inti >= 9:
            canvas.draw_polygon([(265,490),(265,530),(370,530),(370,490)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Large Heal',[270,510] , 20, "#b02525")
            canvas.draw_text('8 MP',[270,525] , 20, "#b02525")
        if inti >= 10:
            canvas.draw_polygon([(265,540),(265,580),(370,580),(370,540)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Freeze',[270,560] , 20, "#b02525")
            canvas.draw_text('8 MP',[270,575] , 20, "#b02525")
        #Column 3
        if inti >= 12:
            canvas.draw_polygon([(380,390),(380,430),(485,430),(485,390)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Battle Focus',[385,410] , 20, "#b02525")
            canvas.draw_text('0 MP',[385,425] , 20, "#b02525")
        if inti >= 14:
            canvas.draw_polygon([(380,440),(380,480),(485,480),(485,440)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Greater Heal',[385,460] , 20, "#b02525")
            canvas.draw_text('10 MP',[385,475] , 20, "#b02525")
        if inti >= 17:
            canvas.draw_polygon([(380,490),(380,530),(485,530),(485,490)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Electric Storm',[385,510] , 20, "#b02525")
            canvas.draw_text('14 MP',[385,525] , 20, "#b02525")
        if inti >= 19:
            canvas.draw_polygon([(380,540),(380,580),(485,580),(485,540)], 3, "#bfbfbf", "#9f9f9f")
            canvas.draw_text('Cataclysm',[385,560] , 20, "#b02525")
            canvas.draw_text('18 MP',[385,575] , 20, "#b02525")
        
        ###Enemies
        #Continue button
        if enemy == 0:
            canvas.draw_polygon([(850,175),(850,225),(625,225),(625,175)], 5, "#baba33", "#22aa44")
            canvas.draw_text('Continue',[632,215] , 44, "#aa2215")
            
        ##Enemy Status
        canvas.draw_polygon([(575,150),(850,150),(850,-50),(575,-50)], 10, "#bfbfbf", "#9f9f9f")    
        
        #Enemy health
        canvas.draw_text('Health  ' + str(ehp) + '/' + str(ehpmax),[600,30] , 24, "#b02525")
        canvas.draw_polygon([(600,35),(602 + (ehpmax * 2),35),(602 + (ehpmax * 2),45),(600,45)], 2, "#000000", "#333333")
        canvas.draw_polygon([(602,37),(600 + (ehp * 2),37),(600 + (ehp * 2),43),(602,43)], 2, "#dd3333", "#dd3333")
        
        #Enemy name
        if enemy == 1:
            canvas.draw_text('Enemy Slime',[585,15] , 16, "#b02525")
        if enemy == 2:
            canvas.draw_text('Enemy Boar',[585,15] , 16, "#b02525")
        if enemy == 3:
            canvas.draw_text('Enemy Wolf',[585,15] , 16, "#b02525")
        if enemy == 4:
            canvas.draw_text('Enemy Thief',[585,15] , 16, "#b02525")
        if enemy == 5:
            canvas.draw_text('Enemy Bandit',[585,15] , 16, "#b02525")
        if enemy == 6:
            canvas.draw_text('Enemy Skeleton',[585,15] , 16, "#b02525")
        if enemy == 7:
            canvas.draw_text('Enemy Zombie',[585,15] , 16, "#b02525")
        if enemy == 8:
            canvas.draw_text('Enemy Armored Skeleton',[585,15] , 16, "#b02525")
        if enemy == 9:
            canvas.draw_text('Enemy Armored Zombie',[585,15] , 16, "#b02525")
        if enemy == 10:
            canvas.draw_text('Enemy Minotaur',[585,15] , 16, "#b02525")
        if enemy == 11:
            canvas.draw_text('Enemy Mage',[585,15] , 16, "#b02525")
        if enemy == 12:
            canvas.draw_text('Enemy Cursed Soldier',[585,15] , 16, "#b02525")
        if enemy == 13:
            canvas.draw_text('Enemy Cursed Elite',[585,15] , 16, "#b02525")
        if enemy == 14:
            canvas.draw_text('Enemy Golem',[585,15] , 16, "#b02525")
        if enemy == 15:
            canvas.draw_text('Enemy Royal guard',[585,15] , 16, "#b02525")
        if enemy == 16:
            canvas.draw_text('Enemy Dark Wizard',[585,15] , 16, "#b02525")
    elif stage == 4: # You win==========================================================================================
        #background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 10, "#dfdfdf", "#dfdfdf")
        #text
        canvas.draw_text('Victory',[260,200] , 96, "#fec897")
        canvas.draw_text('You have defended the kingdom for now, but evil WILL return...',[150,280] , 32, "#f7cf89")
        #try again
        canvas.draw_polygon([(300,450),(300,500),(500,500),(500,450)], 5, "#bfbfbf", "#9f9f9f")
        canvas.draw_text('Try again',[320,488] , 40, "#b02525")
    elif stage == -1: # You lose========================================================================================
        #background color
        canvas.draw_polygon([(0,0),(800,0),(800,600),(0,600)], 10, "#666666", "#666666")
        canvas.draw_text('Defeat',[275,200] , 96, "#fe3827")
        canvas.draw_text('Evil has triumphed, but there is yet hope...',[150,280] , 32, "#f7cf89")
        #try again
        canvas.draw_polygon([(300,450),(300,500),(500,500),(500,450)], 5, "#bfbfbf", "#9f9f9f")
        canvas.draw_text('Try again',[320,488] , 40, "#b02525")
        
def nextsubstage():
    global enemy, progress, substage
    if substage == 0:#near start
        if progress >= 5:
            substage = 1
            progress = 0
        else:
            progress = progress + 1
            enemy = 1
            enemyspawn()
    if substage == 1:#Eforest
        if progress >= 5:
            substage = 2
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,2)
            if ren == 0:
                enemy = 1
            elif ren == 1 or ren == 2:
                enemy = 2
            enemyspawn()
    if substage == 2:#Lforest
        if progress >= 5:
            substage = 3
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,5)
            if ren == 0:
                enemy = 1
            elif ren == 1 or ren == 2:
                enemy = 2
            elif ren == 3 or ren == 4 or ren == 5:
                enemy = 3
            enemyspawn()
    if substage == 3:#Path
        if progress >= 5:
            substage = 4
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,5)
            if ren == 0:
                enemy = 3
            elif ren == 1 or ren == 2:
                enemy = 5
            elif ren == 3 or ren == 4 or ren == 5:
                enemy = 4
            enemyspawn()
    if substage == 4:#Edungeon
        
        if progress >= 5:
            substage = 5
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,5)
            if ren == 0:
                enemy = 5
            elif ren == 1 or ren == 2:
                enemy = 6
            elif ren == 3 or ren == 4 or ren == 5:
                enemy = 7
            enemyspawn()
    if substage == 5:#Ldungeon
        if progress >= 5:
            substage = 6
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,9)
            if ren == 0:
                enemy = 6
            elif ren == 1 or ren == 2:
                enemy = 7
            elif ren == 3 or ren == 4 or ren == 5:
                enemy = 8
            elif ren == 6 or ren == 7 or ren == 8 or ren == 9:
                enemy = 9
            enemyspawn()
    if substage == 6:#dungeon boss
        if progress >= 1:
            substage = 7
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,5)
            enemy = 10
            enemyspawn()
    if substage == 7:#Ekingdom
        if progress >= 5:
            substage = 8
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,2)
            if ren == 0:
                enemy = 11
            elif ren == 1 or ren == 2:
                enemy = 12
            enemyspawn()
    if substage == 8:#LKingdom
        if progress >= 5:
            substage = 9
            progress = 0
        else:
            progress = progress + 1
            ren = random.randint(0,5)
            if ren == 0:
                enemy = 12
            elif ren == 1 or ren == 2:
                enemy = 11
            elif ren == 3 or ren == 4 or ren == 5:
                enemy = 13
            enemyspawn()
    if substage == 9:#kingdom boss
        if progress >= 1:
            substage = 10
            progress = 0
        else:
            progress = progress + 1
            enemy = 14
            enemyspawn()
    if substage == 10:#castle
        if progress >= 3:
            substage = 11
            progress = 0
        else:
            progress = progress + 1
            enemy = 15
            enemyspawn()
    if substage == 11:#castle boss
        if progress >= 1:
            stage = 4 #win the game
            progress = 0
        else:
            progress = progress + 1
            enemy = 16
            enemyspawn()
    
def enemyspawn():
    global ehpmax, edmg, xpg, gpg, ehp
    if enemy == 0:#No enemy
        ehpmax = 0
        ehp = ehpmax
        edmg = 0
        xpg = 0
        gpg = 0
    elif enemy == 1:#Enemy Slime
        ehpmax = 8
        ehp = ehpmax
        edmg = 1
        xpg = 2
        gpg = 1
    elif enemy == 2:#Enemy Boar
        ehpmax = 12
        ehp = ehpmax
        edmg = 1
        xpg = 4
        gpg = 2
    elif enemy == 3:#Enemy Wolf
        ehpmax = 15
        ehp = ehpmax
        edmg = 3
        xpg = 10
        gpg = 3
    elif enemy == 4:#Enemy Thief
        ehpmax = 25
        ehp = ehpmax
        edmg = 2
        xpg = 12
        gpg = 6
    elif enemy == 5:#Enemy Bandit
        ehpmax = 30
        ehp = ehpmax
        edmg = 3
        xpg = 20
        gpg = 8
    elif enemy == 6:#Enemy Skeleton
        ehpmax = 40
        ehp = ehpmax
        edmg = 5
        xpg = 50
        gpg = 12
    elif enemy == 7:#Enemy Zombie
        ehpmax = 60
        ehp = ehpmax
        edmg = 3
        xpg = 40
        gpg = 15
    elif enemy == 8:#Enemy Armored Skeleton
        ehpmax = 60
        ehp = ehpmax
        edmg = 6
        xpg = 80
        gpg = 20
    elif enemy == 9:#Enemy Armored Zombie
        ehpmax = 90
        ehp = ehpmax
        edmg = 4
        xpg = 65
        gpg = 22
    elif enemy == 10:#Enemy Minotaur
        ehpmax = 150
        ehp = ehpmax
        edmg = 8
        xpg = 175
        gpg = 45
    elif enemy == 11:#Enemy Mage
        ehpmax = 75
        ehp = ehpmax
        edmg = 7
        xpg = 100
        gpg = 30
    elif enemy == 12:#Enemy Cursed Soldier
        ehpmax = 100
        ehp = ehpmax
        edmg = 6
        xpg = 80
        gpg = 25
    elif enemy == 13:#Enemy Cursed Elite
        ehpmax = 175
        ehp = ehpmax
        edmg = 8
        xpg = 150
        gpg = 35
    elif enemy == 14:#Enemy Golem
        ehpmax = 250
        ehp = ehpmax
        edmg = 10
        xpg = 275
        gpg = 50
    elif enemy == 15:#Enemy Royal guard
        ehpmax = 225
        ehp = ehpmax
        edmg = 9
        xpg = 225
        gpg = 40
    elif enemy == 16:#Enemy Dark Wizard
        ehpmax = 500
        ehp = ehpmax
        edmg = 12
        xpg = 500
        gpg = 100
    
def endturn():
    global php, enemy, ehp, pxp, gold, collected, subturn
    print "test1"
    if ehp <= 0:
        print "test1.5"
        if collected == 0:
            print "test2"
            gold = gold + gpg
            pxp = pxp + xpg
            xpcheck()
            enemy = 0
            enemyspawn()
            collected = 1
            print "test3"
    else:
        print "test4"
        php = php - edmg
        checkdeath()
    subturn = 0
    statreg()
    print "test5"
    
def statreg():
    global php, pmp, ehp
    if php > phpmax:
        php = phpmax
    if pmp > pmpmax:
        pmp = pmpmax
    if ehp < 0:
        ehp = 0
            
def checkdeath():
    global dead, stage
    if php <= 0:
        dead = 1
        stage = -1
    
def xpcheck():
    global level, unspec, pxpr, pxpl, stage
    if level == 1:
        pxpl = 0
        pxpr = 12
        if pxp >= 12:
            level = 2
            unspec = unspec + 2
            stage = 1
    if level == 2:
        pxpl = 12
        pxpr = 28
        if pxp >= 28:
            level = 3
            unspec = unspec + 2
            stage = 1
    if level == 3:
        pxpl = 28
        pxpr = 50
        if pxp >= 50:
            level = 4
            unspec = unspec + 2
            stage = 1
    if level == 4:
        pxpl = 50
        pxpr = 85
        if pxp >= 85:
            level = 5
            unspec = unspec + 2
            stage = 1
    if level == 5:
        pxpl = 85
        pxpr = 140
        if pxp >= 140:
            level = 6
            unspec = unspec + 2
            stage = 1
    if level == 6:
        pxpl = 140
        pxpr = 200
        if pxp >= 200:
            level = 7
            unspec = unspec + 2
            stage = 1
    if level == 7:
        pxpl = 200
        pxpr = 300
        if pxp >= 300:
            level = 8
            unspec = unspec + 2
            stage = 1
    if level == 8:
        pxpl = 300
        pxpr = 445
        if pxp >= 445:
            level = 9
            unspec = unspec + 2
            stage = 1
    if level == 9:
        pxpl = 445
        pxpr = 625
        if pxp >= 625:
            level = 10
            unspec = unspec + 2
            stage = 1
    if level == 10:
        pxpl = 625
        pxpr = 925
        if pxp >= 925:
            level = 11
            unspec = unspec + 2
            stage = 1
    if level == 11:
        pxpl = 925
        pxpr = 1250
        if pxp >= 1250:
            level = 12
            unspec = unspec + 2
            stage = 1
    if level == 12:
        pxpl = 1250
        pxpr = 1750
        if pxp >= 1750:
            level = 13
            unspec = unspec + 2
            stage = 1
    if level == 13:
        pxpl = 1750
        pxpr = 2500
        if pxp >= 2500:
            level = 14
            unspec = unspec + 2
            stage = 1
    if level == 14:
        pxpl = 2500
        pxpr = 3750
        if pxp >= 3750:
            level = 15
            unspec = unspec + 2
            stage = 1
   
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 800, 600)
frame.set_mouseclick_handler(button_click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
