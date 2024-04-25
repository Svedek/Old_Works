# Future note:
# This was intended to be a top down combat game
# that allowed for quick changing between melee,
# ranged (q), and magic (e) attacks. I did also start
# creating different weapons to switch to with 1-5.
# Original link: https://py2.codeskulptor.org/#user45_KeytuvofQTZSQwI.py

#Samuel Walsh

import random
import simplegui

screen = [0,0];

dir=[0,0]
player_position = [100,100]

player_mode = 0; #0 is mele, 1 is archery, 2 is magic
player_state = 0; #0 is not active, 1 is in ranged aim, 2 is after mele swing, 3 is rolling
mag_almt = [0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]; #[active[weak,strength]] #[0 fire, 1 ice, 2 electric, 3 earth, 4 air, 5 light, 6 dark]

rng_status = [[0,0,0],[0,0]]; #0 is dont have, 1 is have, 2 is active #[crossbow S. active, crossbow L. active, bolts] [longbow S. active, longbow L. active, arrows]
arrow1 =[0,[0,0],[0,0],8] #active,[pos],[going to],[spd]
arrow2 =[0,[0,0],[0,0],8]
arrow3 =[0,[0,0],[0,0],8]
#sec/dmg 2.666  3.75  4.666  5.625
mele_weps = [1,[1,8,3,2],[0,15,4,3],[0,28,6,4],[0,45,8,5]] #wep active,[owned, swingtime(low=good), dmg, range(low=bad), knockback] #[dagger, shortsword, longsword, claymore]
dmg_obj=[0,0,0,[0,0],[0,0]]#[time to stay, dmg, range, [pos of middle point closest to player],dir]
atkclk=0;

player_items = [0,0,0] #[hpot, mpot, spot]
q_items = [0,0,0] #quest items
player_hp = 3
player_hpmax = 3
player_mp = 3
player_mpmax = 3
player_stm = 3
player_stmmax = 3

stmclk=120;
stmclktime=120;

basespd=4;
spd=0;
crnrslow=1;

roll=0;
rolltime=15; #for easy change
rollspd=10;
rollcrnrslow=3;

dead=0;

#Exp/stats/levels
p_pow_exp = 0;
p_pow_expreq = 64;
p_pow_level = 0;

p_vit_exp = 0;
p_vit_expreq = 24;
p_vit_level = 0;

p_end_exp = 0;
p_end_expreq = 24;
p_end_level = 0;

p_mag_exp = 0;
p_mag_expreq = 32;
p_mag_level = 0;

p_str_exp = 0;
p_str_expreq = 32;
p_str_level = 0;

p_dex_exp = 0;
p_dex_expreq = 32;
p_dex_level = 0;
#Enemy stats [pos],hp,dmg,id,alive,kb-mod (default 10),kb-inflicted,[kb-dir],size,hexcolor border,hexcolor filling, range
e1sts=[[300,400],3,1,1,1,10,0,[0,0],12,'#55cc99','#33aa77',40];
e2sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e3sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e4sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e5sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e6sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e7sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e8sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
e9sts=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
#extra temp stats for enemies [e1,e2...][clock, spd, dir]
slimests=[[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]],[0,0,[0,0]]];
e2extra=[0];
e3extra=[0];
e4extra=[0];
e5extra=[0];
e6extra=[0];
e7extra=[0];
e8extra=[0];
e9extra=[0];

def keydown(key):
    global player_mode, player_position, dir, player_stm, p_end_exp, roll, rolltime, mag_almt, rng_status, mele_weps, atkclk
    if key == simplegui.KEY_MAP['w']:
        dir[1]=dir[1]-1
        if player_position[1] >18:
            player_position[1] = player_position[1] - 3
    if key == simplegui.KEY_MAP['a']:
        dir[0]=dir[0]-1
        if player_position[0] >15:
            player_position[0] = player_position[0] - 3
    if key == simplegui.KEY_MAP['s']:
        dir[1]=dir[1]+1
        if player_position[1] <680:
            player_position[1] = player_position[1] + 3
    if key == simplegui.KEY_MAP['d']:
        dir[0]=dir[0]+1
        if player_position[0] <985:
            player_position[0] = player_position[0] + 3
    if atkclk <=0:
        if key == simplegui.KEY_MAP['q']:
            if player_mode == 1:
                player_mode = 0
            else:
                player_mode = 1
        if key == simplegui.KEY_MAP['e']:
            if player_mode == 2:
                player_mode = 0
            else:
                player_mode = 2
        if key == simplegui.KEY_MAP['r']:
            if dir != [0,0] and player_stm > 0 and roll <= 0:
                roll = rolltime
                player_stm = player_stm - 1
                p_end_exp = p_end_exp + 1
            #do exp check
    ###Change active weapon/spell alignment
    if key == simplegui.KEY_MAP['1']:
        if player_mode == 0: #mele
            mele_weps[0] = 0 #dagger
        elif player_mode == 1: #archery
            rng_status[0] = 0 #crossbow
        elif player_mode == 2: #magic
            mag_almt[0]=0 #fire            
    if key == simplegui.KEY_MAP['2']:
        if player_mode == 0: #mele
            mele_weps[0] = 1 #shortsword
        elif player_mode == 1: #archery
            rng_status[0] = 1 #longbow
        elif player_mode == 2: #magic
            mag_almt[0]=1 #ice
    if key == simplegui.KEY_MAP['3']:
        if player_mode == 0: #mele
            mele_weps[0] = 2 #longsword
        elif player_mode == 2: #magic
            mag_almt[0]=2 #electric
    if key == simplegui.KEY_MAP['4']:
        if player_mode == 0: #mele
            mele_weps[0] = 3 #claymore
        elif player_mode == 2: #magic
            mag_almt[0]=3 #earth
    if key == simplegui.KEY_MAP['5']:
        if player_mode == 2: #magic
            mag_almt[0]=4 #air
    if key == simplegui.KEY_MAP['6']:
        if player_mode == 2: #magic
            mag_almt[0]=5 #light
    if key == simplegui.KEY_MAP['7']:
        if player_mode == 2: #magic
            mag_almt[0]=6 #dark

def keyup(key):
    global dir
    if key == simplegui.KEY_MAP['w']:
        dir[1]=dir[1]+1
    if key == simplegui.KEY_MAP['a']:
        dir[0]=dir[0]+1
    if key == simplegui.KEY_MAP['s']:
        dir[1]=dir[1]-1
    if key == simplegui.KEY_MAP['d']:
        dir[0]=dir[0]-1
        
#player_mode = 0; #0 is mele, 1 is archery, 2 is magic
#player_state = 0; #0 is not active, 1 is in ranged aim, 2 is after mele swing, 3 is rolling
#mag_almt = [0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]; #[active[weak,strength]] #[0 fire, 1 ice, 2 electric, 3 earth, 4 air, 5 light, 6 dark]
#rng_status = [[0,0,0],[0,0]]; #0 is dont have, 1 is have, 2 is active #[crossbow S. active, crossbow L. active, bolts] [longbow S. active, longbow L. active, arrows]
#mele_weps = [1,[1,6,5,3],[0,12,9,4],[0,22,13,6],[0,34,16,9]] #wep active,[owned, swingtime(low=good), dmg, range(low=bad)] #[dagger, shortsword, longsword, claymore]
#dmg_obj=[0,0,0,[0,0],[0,0]]#[time to stay, dmg, range, [pos of middle point closest to player],[dir]]

def mouseclick(pos):
    global player_mode, player_state, mag_almt, rng_status, mele_weps, dmg_obj, player_position, atkclk, roll
    if roll <= 0:
        if player_mode == 0:#mele
            if atkclk <= 0:
                p1 = pos[0] - player_position[0]
                p2 = pos[1] - player_position[1]
                if abs(p1) >= abs(p2):
                    d = p1 + 0.00
                    d = abs(d)
                elif abs(p1) <= abs(p2):
                    d = p2 + 0.00
                    d = abs(d)
                else:
                    print('check mouseclick function')
                if d != 0:
                    pos1 = [p1/d, p2/d]
                    pos2 = [(round(pos1[0])),(round(pos1[1]))]
                    print(pos1)
                    print(pos2)
                else:
                    print('div 0')
                atkclk = mele_weps[mele_weps[0]][1]*2
                dmg_obj = [mele_weps[mele_weps[0]][1], mele_weps[mele_weps[0]][2],mele_weps[mele_weps[0]][3],player_position,pos2]
        elif player_mode == 1:#archery
            print(mele_weps[1][2])
        elif player_mode == 2:#magic
            print('ma')
    
def mousedrag(position):
    print('yes')
        
def draw(canvas):
    global player_stm, player_stmmax, player_mp, player_mpmax, player_hp, player_hpmax, player_position, player_mode, dir, spd, roll, rollspd, crnrslow, rollcrnrslow, stmclk, stmclktime, mag_almt, dmg_obj, mele_weps, e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts, atkclk
    ###Player Movement
    ##Base
    if dir[1]==-1:
        if player_position[1] >18:
            player_position[1] = player_position[1] - spd
    if dir[0]==-1:
        if player_position[0] >15:
            player_position[0] = player_position[0] - spd
    if dir[1]==1:
        if player_position[1] <680:
            player_position[1] = player_position[1] + spd
    if dir[0]==1:
        if player_position[0] <985:
            player_position[0] = player_position[0] + spd
    ##Shaping movement at angles
    if dir[0]==0 or dir[1]==0:
        if roll>0:
            spd = rollspd
            roll = roll-1
        else:
            spd = basespd
    else:
        if roll>0:
            spd = rollspd - rollcrnrslow
            roll = roll-1
        else:
            spd = basespd - crnrslow
    ###stats
    canvas.draw_polygon([(0,700),(1000,700),(1000,800),(0,800)],8,'#555555','#777777')
    ##health
    if player_hp > player_hpmax:
        player_hp = player_hpmax
    canvas.draw_polygon([(100,715),(100 + player_hpmax * 40,715),(100 + player_hpmax * 40,730),(100,730)],5,'#222222','#111111')
    canvas.draw_polygon([(100,715),(100 + player_hp * 40,715),(100 + player_hp * 40,730),(100,730)],5,'#b54535','#c04c3c')
    ##magic
    if player_mp > player_mpmax:
        player_mp = player_mpmax
    canvas.draw_polygon([(100,745),(100 + player_mpmax * 40,745),(100 + player_mpmax * 40,760),(100,760)],5,'#222222','#111111')
    canvas.draw_polygon([(100,745),(100 + player_mp * 40,745),(100 + player_mp * 40,760),(100,760)],5,'#3355b0','#3a5cb8')
    ##stamina
    if player_stm > player_stmmax:
        player_stm = player_stmmax
    canvas.draw_polygon([(100,775),(100 + player_stmmax * 40,775),(100 + player_stmmax * 40,790),(100,790)],5,'#222222','#111111')
    canvas.draw_polygon([(100,775),(100 + player_stm * 40,775),(100 + player_stm * 40,790),(100,790)],5,'#35b535','#3cc53c')
    #stamina regen
    if player_stm < player_stmmax:
        if stmclk <= 0:
            player_stm = player_stm + 1
            stmclk = stmclktime
        elif stmclk > 0:
            stmclk = stmclk - 1

    ###entities
    ##Enemies
    if (e1sts[4]==1):
        canvas.draw_circle([e1sts[0][0],e1sts[0][1]], e1sts[8], 3, e1sts[9],e1sts[10])
    if (e2sts[4]==1):
        canvas.draw_circle([e2sts[0][0],e2sts[0][1]], e2sts[8], 3, e2sts[9],e2sts[10])
    if (e3sts[4]==1):
        canvas.draw_circle([e3sts[0][0],e3sts[0][1]], e3sts[8], 3, e3sts[9],e3sts[10])
    if (e4sts[4]==1):
        canvas.draw_circle([e4sts[0][0],e4sts[0][1]], e4sts[8], 3, e4sts[9],e4sts[10])
    if (e5sts[4]==1):
        canvas.draw_circle([e5sts[0][0],e5sts[0][1]], e5sts[8], 3, e5sts[9],e5sts[10])
    if (e6sts[4]==1):
        canvas.draw_circle([e6sts[0][0],e6sts[0][1]], e6sts[8], 3, e6sts[9],e6sts[10])
    if (e7sts[4]==1):
        canvas.draw_circle([e7sts[0][0],e7sts[0][1]], e7sts[8], 3, e7sts[9],e7sts[10])
    if (e8sts[4]==1):
        canvas.draw_circle([e8sts[0][0],e8sts[0][1]], e8sts[8], 3, e8sts[9],e8sts[10])
    if (e9sts[4]==1):
        canvas.draw_circle([e9sts[0][0],e9sts[0][1]], e9sts[8], 3, e9sts[9],e9sts[10])
    eai()
    ##Player
    #Model
    if player_mode == 0:
        canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#cccccc','#aaaaaa')
    elif player_mode == 1:
        canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#bb7777','#77bb77')
    elif player_mode == 2:
        if mag_almt[0] == 0: #fire
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#cc5555','#aa3333')
        elif mag_almt[0] == 1:#ice
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#7777dd','#5555bb')
        elif mag_almt[0] == 2:#electric
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#7777d6','#aaaa66')
        elif mag_almt[0] == 3:#earth
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#997766','#776644')
        elif mag_almt[0] == 4:#air
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#cccc99','#aaaa77')
        elif mag_almt[0] == 5:#light
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#f0f0f0','#ddddaa')
        elif mag_almt[0] == 6:#dark
            canvas.draw_circle([player_position[0], player_position[1]], 12, 3, '#0f0f0f','#330633')
    else:
        print('Player mode not 0, 1, or 2')
    
    ##dammage object
    if atkclk > 0:
        atkclk = atkclk-1
    #mele_weps = [1,[1,6,5,3],[0,12,9,4],[0,22,13,6],[0,34,16,9]] #wep active,[owned, swingtime(low=good), dmg, range(low=bad), knockback] #[dagger, shortsword, longsword, claymore]
    #dmg_obj=[0,0,0,[0,0],[0,0]]#[time to stay, dmg, range, [pos of middle point closest to player],[dir]]
    if dmg_obj[0] > 0:
        if dmg_obj[4] == [0.0,-1.0]:
            temp = [0.0,-1.0]
            dircheck([0.0,-1.0])
            print('uu')
        elif dmg_obj[4] == [1.0,-1.0]:
            temp = [1.0,-1.0]
            dircheck([1.0,-1.0])
            print('uurr')
        elif dmg_obj[4] == [1.0,0.0]:
            temp = [1.0,0.0]
            dircheck([1.0,0.0])
            print('rr')
        elif dmg_obj[4] == [1.0,1.0]:
            temp = [1.0,1.0]
            dircheck([1.0,1.0])
            print('ddrr')
        elif dmg_obj[4] == [0.0,1.0]:
            temp = [0.0,1.0]
            dircheck([0.0,1.0])
            print('dd')
        elif dmg_obj[4] == [-1.0,1.0]:
            temp = [-1.0,1.0]
            dircheck([-1.0,1.0])
            print('ddll')
        elif dmg_obj[4] == [-1.0,0.0]:
            temp = [-1.0,0.0]
            dircheck([-1.0,0.0])
            print('ll')
        elif dmg_obj[4] == [-1.0,-1.0]:
            temp = [-1.0,-1.0]
            dircheck([-1.0,-1.0])
            print('uull')
        if temp[0] == 0.00:
            canvas.draw_polygon([(player_position[0]+dmg_obj[2]*3,player_position[1]+6*temp[1]),(player_position[0]-dmg_obj[2]*3,player_position[1]+6*temp[1]),(player_position[0]-dmg_obj[2]*3,player_position[1]+12*dmg_obj[2]*temp[1]),(player_position[0]+dmg_obj[2]*3,player_position[1]+12*dmg_obj[2]*temp[1])],5,'#ff3333','#999933')
        elif temp[1] == 0.00:
            canvas.draw_polygon([(player_position[0]+6*temp[0],player_position[1]+dmg_obj[2]*3),(player_position[0]+6*temp[0],player_position[1]-dmg_obj[2]*3),(player_position[0]+12*dmg_obj[2]*temp[0],player_position[1]-dmg_obj[2]*3),(player_position[0]+12*dmg_obj[2]*temp[0],player_position[1]+dmg_obj[2]*3)],5,'#ff3333','#999933')
        else:
            canvas.draw_polygon([(player_position[0]+temp[0]*4*dmg_obj[2]-temp[0]*dmg_obj[2],player_position[1]-temp[1]*dmg_obj[2]),(player_position[0]-temp[0]*dmg_obj[2],player_position[1]+temp[1]*4*dmg_obj[2]-temp[1]*dmg_obj[2]),(player_position[0]+temp[0]*6*dmg_obj[2],player_position[1]+temp[1]*4*dmg_obj[2]+temp[1]*6*dmg_obj[2]),(player_position[0]+temp[0]*4*dmg_obj[2]+temp[0]*6*dmg_obj[2],player_position[1]+temp[1]*6*dmg_obj[2])],5,'#ff3333','#999933')
        dmg_obj[0] = dmg_obj[0] -1

#mele_weps = [1,[1,6,5,3],[0,12,9,4],[0,22,13,6],[0,34,16,9]] #wep active,[owned, swingtime(low=good), range(low=bad), dmg] #[dagger, shortsword, longsword, claymore]        
#[(player_position[0]+dmg_obj[2]*3,player_position[1]+6*temp[1]),(player_position[0]-dmg_obj[2]*3,player_position[1]+6*temp[1]),(player_position[0]-dmg_obj[2]*3,player_position[1]+12*dmg_obj[2]*temp[1]),(player_position[0]+dmg_obj[2]*3,player_position[1]+12*dmg_obj[2]*temp[1])]
#[(player_position[0]+6*temp[0],player_position[1]+dmg_obj[2]*3),(player_position[0]+6*temp[0],player_position[1]-dmg_obj[2]*3),(player_position[0]+12*dmg_obj[2]*temp[0],player_position[1]-dmg_obj[2]*3),(player_position[0]+12*dmg_obj[2]*temp[0],player_position[1]+dmg_obj[2]*3)]

#Enemy stats [pos],hp,dmg,id,alive,kb-mod (default 10),kb-inflicted,[kb-dir],size,hexcolor border,hexcolor filling,range
#mele_weps = [1,[1,6,5,3],[0,12,9,4],[0,22,13,6],[0,34,16,9]] #wep active,[owned, swingtime(low=good), dmg, range(low=bad), knockback] #[dagger, shortsword, longsword, claymore]

def dircheck(di):
    global e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts, player_position, dmg_obj
    if (di[0]==0):
        if (e1sts[0][1]-player_position[1])/(abs(e1sts[0][1]-player_position[1])) == di[1]:
            if e1sts[4] == 1:
                if ((e1sts[0][0]-player_position[0]-e1sts[8] <= dmg_obj[2]*3 and e1sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e1sts[8]) and (abs(e1sts[0][1]-player_position[1]) >= abs(6*di[1])-e1sts[8] and abs(e1sts[0][1]-player_position[1])-e1sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e1 = 1
                    print 'hit'
            if e2sts[4] == 1:
                if ((e2sts[0][0]-player_position[0]-e2sts[8] <= dmg_obj[2]*3 and e2sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e2sts[8]) and (abs(e2sts[0][1]-player_position[1]) >= abs(6*di[1])-e2sts[8] and abs(e2sts[0][1]-player_position[1])-e2sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e2 = 1
            if e3sts[4] == 1:
                if ((e3sts[0][0]-player_position[0]-e3sts[8] <= dmg_obj[2]*3 and e3sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e3sts[8]) and (abs(e3sts[0][1]-player_position[1]) >= abs(6*di[1])-e3sts[8] and abs(e3sts[0][1]-player_position[1])-e3sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e3 = 1
            if e4sts[4] == 1:
                if ((e4sts[0][0]-player_position[0]-e4sts[8] <= dmg_obj[2]*3 and e4sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e4sts[8]) and (abs(e4sts[0][1]-player_position[1]) >= abs(6*di[1])-e4sts[8] and abs(e4sts[0][1]-player_position[1])-e4sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e4 = 1
            if e5sts[4] == 1:
                if ((e5sts[0][0]-player_position[0]-e5sts[8] <= dmg_obj[2]*3 and e5sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e5sts[8]) and (abs(e5sts[0][1]-player_position[1]) >= abs(6*di[1])-e5sts[8] and abs(e5sts[0][1]-player_position[1])-e5sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e5 = 1
            if e6sts[4] == 1:
                if ((e6sts[0][0]-player_position[0]-e6sts[8] <= dmg_obj[2]*3 and e6sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e6sts[8]) and (abs(e6sts[0][1]-player_position[1]) >= abs(6*di[1])-e6sts[8] and abs(e6sts[0][1]-player_position[1])-e6sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e6 = 1
            if e7sts[4] == 1:
                if ((e7sts[0][0]-player_position[0]-e7sts[8] <= dmg_obj[2]*3 and e7sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e7sts[8]) and (abs(e7sts[0][1]-player_position[1]) >= abs(6*di[1])-e7sts[8] and abs(e7sts[0][1]-player_position[1])-e7sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e7 = 1
            if e8sts[4] == 1:
                if ((e8sts[0][0]-player_position[0]-e8sts[8] <= dmg_obj[2]*3 and e8sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e8sts[8]) and (abs(e8sts[0][1]-player_position[1]) >= abs(6*di[1])-e8sts[8] and abs(e8sts[0][1]-player_position[1])-e8sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e8 = 1
            if e9sts[4] == 1:
                if ((e9sts[0][0]-player_position[0]-e9sts[8] <= dmg_obj[2]*3 and e9sts[0][0]-player_position[0] >= -dmg_obj[2]*3-e9sts[8]) and (abs(e9sts[0][1]-player_position[1]) >= abs(6*di[1])-e9sts[8] and abs(e9sts[0][1]-player_position[1])-e9sts[8] <= abs(12*dmg_obj[2]*di[1]))):
                    e9 = 1
    elif (di[1]==0):
        if (e1sts[0][0]-player_position[0])/(abs(e1sts[0][0]-player_position[0])) == di[0]:
            if e1sts[4] == 1:
                if ((e1sts[0][1]-player_position[1]-e1sts[8] <= dmg_obj[2]*3 and e1sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e1sts[8]) and (abs(e1sts[0][0]-player_position[0]) >= abs(6*di[0])-e1sts[8] and abs(e1sts[0][0]-player_position[0])-e1sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e1 = 1
                    print 'hit'
            if e2sts[4] == 1:
                if ((e2sts[0][1]-player_position[1]-e2sts[8] <= dmg_obj[2]*3 and e2sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e2sts[8]) and (abs(e2sts[0][0]-player_position[0]) >= abs(6*di[0])-e2sts[8] and abs(e2sts[0][0]-player_position[0])-e2sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e2 = 1
            if e3sts[4] == 1:
                if ((e3sts[0][1]-player_position[1]-e3sts[8] <= dmg_obj[2]*3 and e3sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e3sts[8]) and (abs(e3sts[0][0]-player_position[0]) >= abs(6*di[0])-e3sts[8] and abs(e3sts[0][0]-player_position[0])-e3sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e3 = 1
            if e4sts[4] == 1:
                if ((e4sts[0][1]-player_position[1]-e4sts[8] <= dmg_obj[2]*3 and e4sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e4sts[8]) and (abs(e4sts[0][0]-player_position[0]) >= abs(6*di[0])-e4sts[8] and abs(e4sts[0][0]-player_position[0])-e4sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e4 = 1
            if e5sts[4] == 1:
                if ((e5sts[0][1]-player_position[1]-e5sts[8] <= dmg_obj[2]*3 and e5sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e5sts[8]) and (abs(e5sts[0][0]-player_position[0]) >= abs(6*di[0])-e5sts[8] and abs(e5sts[0][0]-player_position[0])-e5sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e5 = 1
            if e6sts[4] == 1:
                if ((e6sts[0][1]-player_position[1]-e6sts[8] <= dmg_obj[2]*3 and e6sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e6sts[8]) and (abs(e6sts[0][0]-player_position[0]) >= abs(6*di[0])-e6sts[8] and abs(e6sts[0][0]-player_position[0])-e6sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e6 = 1
            if e7sts[4] == 1:
                if ((e7sts[0][1]-player_position[1]-e7sts[8] <= dmg_obj[2]*3 and e7sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e7sts[8]) and (abs(e7sts[0][0]-player_position[0]) >= abs(6*di[0])-e7sts[8] and abs(e7sts[0][0]-player_position[0])-e7sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e7 = 1
            if e8sts[4] == 1:
                if ((e8sts[0][1]-player_position[1]-e8sts[8] <= dmg_obj[2]*3 and e8sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e8sts[8]) and (abs(e8sts[0][0]-player_position[0]) >= abs(6*di[0])-e8sts[8] and abs(e8sts[0][0]-player_position[0])-e8sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e8 = 1
            if e9sts[4] == 1:
                if ((e9sts[0][1]-player_position[1]-e9sts[8] <= dmg_obj[2]*3 and e9sts[0][1]-player_position[1] >= -dmg_obj[2]*3-e9sts[8]) and (abs(e9sts[0][0]-player_position[0]) >= abs(6*di[0])-e9sts[8] and abs(e9sts[0][0]-player_position[0])-e9sts[8] <= abs(12*dmg_obj[2]*di[0]))):
                    e9 = 1
                
    else:
        print()
    
def inrange(rng,pos):
    global player_position
    #Checking if in range of entity
    if (abs(player_position[0] - pos[0]) > rng) and abs(player_position[1] - pos[1]) > rng:
        loc = [player_position[0] - pos[0],player_position[1] - pos[1]]
        if abs(loc[0]) >= abs(loc[1]):
            d = loc[0] + 0.00
            d = abs(d)
        elif abs(loc[0]) <= abs(loc[1]):
            d = loc[1] + 0.00
            d = abs(d)
        if d != 0:
            pos1 = [loc[0]/d, loc[1]/d]
            pos2 = [(round(pos1[0])),(round(pos1[1]))]
        return(pos2);
    else:
        return('o');
#Enemy stats [pos],hp,dmg,id,alive,kb-mod (default 10),kb-inflicted,[kb-dir],size,hexcolor border,hexcolor filling, range
#ids and presets
#slime=[[0,0],3,1,1,1,10,0,[0,0],12,'#55cc99','#33aa77',40];
def einitiate(pos,id,enum):
    global e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts
    enull=[[1,1],0,0,0,0,0,0,[0,0],12,'#ffffff','#ffffff',0];
    elist = [e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts]
    for e in elist:
        e=enull


def eai():
    global e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts, e1extra, e2extra, e3extra, e4extra, e5extra, e6extra, e7extra, e8extra, e9extra
    f=-1;
    elist = [e1sts, e2sts, e3sts, e4sts, e5sts, e6sts, e7sts, e8sts, e9sts]
    for e in elist:
        f=f+1
        if e[4]==1:
            if e[3]==0:#null
                print('null enemy');
            if e[3]==1:#slime
                e[0]=slimeai(inrange(e[11],e[0]),e[0],f)
        
#extra temp stats for enemies [e1,e2...][clock, spd, dir]

def slimeai(ran,epos,num):
    global slimests
    if (slimests[num][0] <= 0):
        if (ran == 'o'):
            slimests[num][2]=[random.randint(-1, 1),random.randint(-1, 1)]
        else:
            slimests[num][2]=ran
        slimests[num] = [random.randrange(90, 151, 5),random.randrange(50, 71, 5),slimests[num][2]]
    slimests[num] = [slimests[num][0]-1,round(slimests[num][1]/1.2, 2),slimests[num][2]]
    pos = [epos[0]+(slimests[num][2][0]*slimests[num][1]/10),epos[1]+(slimests[num][2][1]*slimests[num][1]/10)]
    print spd
    print 'o'
    print slimests[num][1]
    return(pos)
    
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 1000, 800)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouseclick)
frame.set_mousedrag_handler(mousedrag)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
