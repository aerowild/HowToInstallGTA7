import datetime
import webbrowser
import time as tm
from tqdm import tqdm
import sys
import textwrap


ship=textwrap.dedent('''
                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \:.    / `.
                   / .-'':._.'`-. \
                   |/    /||\    \|
                 _..--"""````"""--.._
           _.-'``                    ``'-._
         -'                                '-
''')
shipLaunch=textwrap.dedent('''\
       !
       !
       ^
      / \
     /___\
    |=   =|
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
   /|##!##|\
  / |##!##| \
 /  |##!##|  \
|  / ^ | ^ \  |
| /  ( | )  \ |
|/   ( | )   \|
    ((   ))
   ((  :  ))
   ((  :  ))
    ((   ))
     (( ))
      ( )
       .
       .    

''')
shipInSpace=textwrap.dedent('''\
                                                   ,:
                                                 ,' |
                                                /   :
                                             --'   /
                                             \/ />/
                                             / /_\
                                          __/   /
                                          )'-. /
                                          ./  :\
                                           /.' '
                                         '/'
                                         +
                                        '
                                      `.
                                  .-"-
                                 (    |
                              . .-'  '.
                             ( (.   )8:
                         .'    / (_  )
                          _. :(.   )8P  `
                      .  (  `-' (  `.   .
                       .  :  (   .a8a)
                      /_`( "a `a. )"'
                  (  (/  .  ' )=='
                 (   (    )  .8"   +
                   (`'8a.( _(   (
                ..-. `8P    ) `  )  +
              -'   (      -ab:  )
            '    _  `    (8P"Ya
          _(    (    )b  -`.  ) +
         ( 8)  ( _.aP" _a   \( \   *
       +  )/    (8P   (88    )  )
          (a:f   "     `"       `   

''')

answer='https://www.google.co.kr/search?q=how+to+install+GTA+7'

now = datetime.datetime.now()
distance=(((2027-now.year)*12)-now.month)*2592000

print "\n\nDear noob 'GTA 7' seeker, welcome."
tm.sleep(1)

if distance > 0:
	print "Looks like we are not yet in your dream world. Let's make a journey into your dream world."
	tm.sleep(2)
	print "But we need a ship."
	print '.'
	tm.sleep(1)
	print '.'
	tm.sleep(1)
	print '.'
	print "I borrowed a ship from ShipMaster 'https://textart.io/art/tag/spaceship/1 '. Thank them."
	tm.sleep(1)
	print '.'
	tm.sleep(2)
	print "Personalizing your ship for you. In"
	r=5
	while(r>0):
		print r
		tm.sleep(1)
		r-=1
	print "\n\n"
	print ship
	tm.sleep(1)
	print "\n\nLike your ship? (what..its broken? don't worry about that.)"
	tm.sleep(2)
	print "\nLike it or not (ship or?), time to go...That's why\n\n"
	tm.sleep(2)
	print "Launching the ship in 10 seconds..."
	r=10
	while(r>0):
		print r
		tm.sleep(1)
		r-=1	
	print 'Go Go go\n\n'
	print shipLaunch
	tm.sleep(2)
	print '       .'
	tm.sleep(1)	
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)
	print '       .'
	tm.sleep(1)	
	print "\n\n\nNoob...wakeup, we are entering into the Space..."
	tm.sleep(2)
	print "Let me show you the beautiful view. Have a good look before we go beyond (your patience)\n\n"
	print shipInSpace
	tm.sleep(5)
	print '\n\n...'
	tm.sleep(1)	
	print '...'
	tm.sleep(1)
	print '...'
	tm.sleep(1)
	print '...'
	tm.sleep(1)
	print "\n\nhurrah!!! All set. \n\nNoob, nowlisten to me."
	print "\nIf you don't destroy the ship, I guarantee you to tell the answer of your question. Just, let us travel."
	print "\nEstimated time of flight: %d Seconds (Every Second counts)" % distance
	tm.sleep(5)
	print "\n\n\n\n\nTravelling at the speed of time. Hold on!\n"
else:
	print "Let's find out how to install GTA 7."
	tm.sleep(1)
	webbrowser.open(answer, new=2)
	sys.exit()
tq=tqdm(total=distance,unit='time',unit_scale=True)
while True:
	tq.update(1)
	tm.sleep(1)
	if distance<0:
		print "Wake up noob, we are here. Finally, Time to answer your question."
		tm.sleep(3)
		webbrowser.open(answer, new=2)
		print "Have fun...TA TA!"
		sys.exit()
	distance -= 1
tq.close()
