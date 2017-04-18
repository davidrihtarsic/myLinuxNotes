# XANMOD KERNEL:
  XanMod is a mainline Linux kernel distribution with custom settings.
  Optimized to take full advantage of high-performance Desktops, PC Gamers,
  Workstations, Media Centers and others. Supports all recent 64-bit
  versions of Debian and Ubuntu-based systems. 

## Tested
based on [article](http://www.hecticgeek.com/2016/09/supercharge-ubuntu-16-04-lts-xanmod-kernel/)
tested on Ubuntu MATE (DELA SUPER!):
  * Firefox prej 10.5 s ... po tem 4.6 s
  * kopiranje dd (komanda) prej 9MB/s le pri bs=128K
  * po tem... 9MB/s pri 1K, 4K, 8K, 32K, 

## Installation	
1. https://xanmod.org/
2. First install the XanMod Repository Setup
3. manual...
	1. `echo 'deb http://deb.xanmod.org releases main' | sudo tee /etc/apt/  urces.list.d/xanmod-kernel.list && wget -qO - http://deb.xanmod.org/gpg.key   sudo apt-key add -`
	2. `sudo apt update && sudo apt install linux-xanmod-4.9`
	3. reboot
	4. `cat /proc/version` (preveri kernel verzijo:)
4. chane [cfg] disk scheduler:
	1. sudo cat /sys/block/sda/queue/scheduler (kateri so na razpolago)
	2. sudo subl /etc/#ault/grub (edit grub settings)
	3. spremeni vrstico:
		#GRUB_CMDLINE_LINUX_#AULT="quiet splash"
		GRUB_CMDLINE_LINUX_#AULT="quiet splash elevator=bfq"
	4. shrani
	5. sudo update-grub2
	6. reboot
	7. preveri disk scheduler:
		1. sudo cat /sys/block/sda/queue/scheduler
5. install Intel CPU support:
	1. ker sem prej dobil error:
		W: Possible missing firmware /lib/firmware/rtl_nic/rtl8107e-2.fw for dule   r8169
		sem namestil še firmware, a mislim, da ni šlo skoz...
	2. sudo apt install intel-microcode iucode-tool
	3. reboot
		
# EFI MODE:
  boot -> CSM enable
  security -> security boot control -> dissable

## installBUNSEN
  instaliral ...
  grub dal na sda1 (kjer sem našel efi... [sudo parted -l])
  kar nekaj sem probal... ni delalo - sedaj pišem kaj ne dela
  
  BIOS:
  new boot oprions:
  path:\efi\boot\bootx64.efi
  ne dela
  
  Test x-n
  probaj ta navodila:
  http://sarah.thesharps.us/2014/12/31/installing-debian-on-asus-ux301la/
  
  install
  grub -> /dev/sda1
  takoj ne dela... zažene se win10...
  path :\EFI\debian\grubx64.efi [ne dela]
  path :\efi\boot\bootx64.efi [ne dela]

# WIRELESS SETUP
  Wavemon...
  > `sudo apt-get install wavemon`

# XRANDR:
  te nastavitve so odvisne od monitorja... !
  
  1. najprej:
      `cvt 1280 1024 60`
      # 1280x1024 59.89 Hz (CVT 1.31M4) hsync: 63.67 kHz; pclk: 109.00 MHz
      # Modeline "1280x1024_60.00"  109.00  1280 1368 1496 1712  1024 1027 1034   1063   -hsync +vsync
      
  2. kopiras kar ti terminal vrže...:
    > `sudo xrandr --newmode "1280x1024"  109.00  1280 1368 1496 1712  1024 1027   1034   1063 -hsync +vsync`
  3. dodas v moznosti:
   	`sudo xrandr --addmode VGA1 1280x1024`
  4. potem nastavis resolucijo v 
    1. arandr ali
   	2. > `xrandr --output VGA1 --mode 1280x1024`

# KEYBOARD SETTINFS:
  Settings -> Reigon&Language -> Input Source
  for KeyBindings:

## ShortCuts():
  v settings>Keyboaard sem si nastavil nekaj bližnjic:
   > super+w > Firefox
   > super+e > Text Editor
   > super+f > File Manager
   > super+t > terminator

  v ~/.bashrc (file se zazene na zacetku)
   > bliznica ll namesto ...
   > alias ll='ls -alF'
   > tipki [đ] dodelimo znak [/]
   > xmodmap -e "keycode 35 = slash"
	
# FILEMANAGER:
  Všeč mi je filemanager THUNAR:
  > `sudo apt-get install thunar`

# TERMINAL:
  Terminal je najboljši terminator
  > `sudo apt-get install terminator`

## Preferences:
  [ ] Show title bar
  Profiles -> Colors = Green on Black
  Profiles -> Background -> Transparency = 50%

# LIBREOFFICE:
  Instal preko terminala:
  > `apt-get install libreoffice`

# TAB_CLICK:

  Da vklnjučiš Tab-CLICK greš v:
  1. settings
  2. mouse
  3. in nato : Tab-CLICK = ON
  Videl sem tudi, da problem reši tudi:
  > `synclient tapbutton1 = 1`

## Touchpad
  v [datoteki][/usr/share/X11/xorg.conf.d/50-synaptics.conf]
  dodas:
  >  Section "InputClass"
  >    Identifier      "Touchpad"                      # required
  >    MatchIsTouchpad "yes"                           # required
  >    Driver          "synaptics"                     # required
  >    Option          "MinSpeed"              "0.5"
  >    Option          "MaxSpeed"              "1.0"
  >    Option          "AccelFactor"           "0.075"
  >    Option          "TapButton1"            "1"
  >    Option          "TapButton2"            "3"     # multitouch
  >    Option          "TapButton3"            "2"     # multitouch
  >    Option          "VertTwoFingerScroll"   "1"     # multitouch
  >    Option          "HorizTwoFingerScroll"  "1"     # multitouch
  >    Option          "VertEdgeScroll"        "1"
  >    Option          "CoastingSpeed"         "8"
  >    Option          "CornerCoasting"        "1"
  >    Option          "CircularScrolling"     "1"
  >    Option          "CircScrollTrigger"     "7"
  >    Option          "EdgeMotionUseAlways"   "1"
  >    Option          "LBCornerButton"        "8"     # browser "back" btn
  >    Option          "RBCornerButton"        "9"     # browser "forward" btn
  >  EndSection

# SOUNDON:
==========
  Na začetku mi ni delal zvok... Rešitev je bila:
  1. lspci:
	  tako preveriš, če je Linux prepoznal zvočno...
	  na terminalu sem dobil:
	  '00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High #inition Audio Controller (rev 04)'
  2. apt-get install libasound2 alsa-utils alsa-oss 
  3. alsamixer:
	  in od "mutiraš" kanale, ki so zamutani

Druga rešitev (ali celo dopolnitev):
	- je, da v terminal napišeš:
		pulseaudio -D
	- secer napiše, da ni mišljeno, da bi bil zagnan kot root
		ampak Ok... po tem dela tudi:
		Settings>Soun

# THUNDERBIRD()
===============
  inštalacija je čisto reprosta:
  > `apt-get install thunderbird`

  ali če ni apt paketa:
  1. greš na njihovo stran in presnameš datoteko thunderbird.tar.db2
  2. extrahiraš v /opt/thunderbird
  3. preveriš če dela: ./thunderbird
  4. nastaviš privilegije (če je potrebno):
   > `sudo chown -R root:root /opt/hunderbird`
  5. in linkaš exe skript:
   > `sudo ln -fs /opt/thunderbird/thunderbird /usr/bin/hunderbird`

# SUBLIME TEXT 3
================

## Install:
  Greš na njihovo stran in snameš dol pravo verzijo (Ubuntu 64)
  nato pa v terminalu zaženeš:
  > cd Downloads
  > `dpkg -i Sublime...64.deb`

## Package Controll:
  Paket za koristne funkcionalnosti:

### install:
  1. goto [link][https://packagecontrol.io/installation]
  2. _copy_ code for Sublime 3:
    `import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)`
  3. View -> Show Console
  4. _paste_ 

### install GitHub:
  1. C+S+p -> Install Packages
  2. [Git()][https://github.com/kemayo/sublime-text-git/wiki]

####	nastavitve:
  The detail step:
   1. go to your local git project directory, [open][.git/config] file and
   2. edit: `https://{username}:{password}@github.com/{username}/{project}.git`
   3. input git push to check if it works.
    > jaz sem moral prej še spedenat v terminalu:
    > git commit -a -m "sublime pedenanje"
	  > git push (če je kak error prej še git pull... in popraviš razlike)

#### uporaba:
  1. popraviš file... & C+s (save)
  2. C+S+p -> quick commit (repo) -> `msg`
  3. C+S+p -> push

### MarkDown:
  1. Install Package: _Markdown extended_ (mogoče ni treba)
	2. Install Package: _Monokai extended_
	3. Preferences -> Color Scheme -> Monokail Extended -> Monokail Extended
	4. Install Package: _Markdown Editing_
	5. Set doc. syntax = Monokai Extended
	6. Preferences -> Package settings -> Markdown Editing -> Markdown Settings (standard) - User:
		{
			"color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
			"tab_size": 2,
			"line_numbers": true,
		    // Layout
			"draw_centered": false,
			"wrap_width": 0,
			"rulers": []
		}

### LaTeX:
  namestis paket preko:
   C+S+p -> Install Packages
   ~~~LaTeXTools~~~
   LaTeXing & LaTeX-cwg
   notes:
   * OK, prej moras namestiti dodatne pakete..:
   * sudo apt-get install texlive-full
   * sudo apt-get install latexmk
   * sudo apt-get install biber

### Spell Checker:
  download:
  	v direktorij: /home/david/.config/sublime-text-3/Packages/
  	wget https://github.com/titoBouzout/Dictionaries/archive/master.zip
  	unzip 
  ali ...
  	Download the language file from the appropiate OpenOffice extension
  	http://extensions.openoffice.org/en/project/  venian-dictionary-package-slovenski-paket-slovarjev
  	Rename the "some.oxt" file to "some.zip"
  	Unzip the file
  	Look for two files: "lang.aff" and "lang.dic". For example es_ES.aff and   ES.dic
  	Open the "lang.aff" to check the encoding used. Such the line: SET   -8859-1
  	Convert that file to UTF-8 from the used encoding
  	Convert "lang.dic" to UTF-8 from the used encoding.
  	Change SET ISO-8859-1 to SET UTF-8
  	In ST3, click on Preferences -> Browse Packages
  	Create a new folder, for example Language - Spanish
  	Move lang.dic and lang.aff to that folder
  	Activate the dictionary in ST3 (View -> Dictionary -> Language - Spanish   es_ES)
  	Press F6 to enable spell check
  View->Dictionaries
  oogle spell check:
  namestitev:
  	C+S+p -> Install Packages
  	Google Spell Check

# TEXMAKER
  1. Spell Checker:
  [download][http://extensions.services.openoffice.org/en/project/slovenian-dictionary-package-slovenski-paket-slovarjev]
	2. `unzip pac-sl.oxt`
	3. in prekopiraš datoteko sl-SI.dic v Sublime paketi direktorij (Preferences->Browse packages)
  4. nato nastaviš jezik : View->Dictionary->si-SL.dic

# TEAMVIEWER
  presnames teamviewer i386 (cetudi imas 64-bitni comp.)
  v terminalu> dpkg --add-architecture i386
  > apt-get update
  > `dpkg -i teamviewer_****_i386.deb`
  > sudo apt-get -f install

# QCAD
  1. presnameš inštalacijo iz njihove [strani][https://qcad.org/en/qcad-downloads-trial]
  2. nato spremeniš rivilegije datoteke:
	  > `sudo chmod 777 qcad*.run`
	3. in poženeš script:
	  > `./qcad*.run`

# FREECAD
	asdf
# GIMP
	asdf
# INKSCAPE
	asdf
# FRITZING
	asdf

# POPCORN-TIME
  1. Download [Popcorn-Time][https://www.popcorntime.ws/about]
  2. razpakiraš in daš dokumente v /opt/popcorn-time/
  3. polinkaš, da bo dosegljivo vsem:
		> `sudo ln -sf /opt/popcorn-time/Popcorn-Time /usr/bin/popcorn-time`
	4. Narediš še .desktop datoteko
		> `sudo nano /usr/share/applications/popcorntime.desktop`
	5. in vot vpišeš:
    [Desktop Entry]
    Version = 1.0
    Type = Application
    Terminal = false
    Name = Popcorn Time
    Exec = /usr/bin/popcorn-time
    Icon = /opt/popcorn-time/src/app/images/icon.png
    Categories = Application;

# ECLIPSE

## installation:
  ... nisem zapisal...
  ... presnameš, odpakiraš kopiraš v:
  /opt/eclipse/
  narediš link za vse uporabnike:
  	sudo ln -sf /opt/eclipse/cpp-neon/eclipse/eclipse /usr/bin/eclipse

## eclipse.desktop:
  sudo nano /usr/share/applications/eclipse.desktop
	[Desktop Entry]
	Version = Neon 2.0
	Type = Application
	Terminal = false
	Name = eclipse
	Exec = /usr/bin/eclipse
	Icon = /opt/eclipse/cpp-neon/eclipse/icon.xpm
	Categories = Development;

# ARDUINO
	pass

# GITHUB
## LITERATURA:
  1. [Link][https://www.youtube.com/watch?v=1h9_cB9mPT8]
	
## install:
Debian le:
 > `sudo apt-get install git`
	
## config:
> `git config --global user.name "xxxyyy"`
> `git config --global user.email "xxx.yyy@džimail.com"`
> `git config --global core.editor="subl"`
	
## general_use:
make new repository ... BlaBla_project (need to be on URL gitHub)
make dir on your computer for that project 
navigate to that dir
> `git init`

### editing:
na tem mestu spreminjaš FAJL...
> `git add .` #dodaj vse datoteke
> `git commit -m "comment"`
> `git commit -a -m "comment"` #naredi vse naenkrat
> `git status` # ni potreben a se vidi ce je potrebno kaj commitat
> `git diff` 	#ni potrebno a pokaže razlike...

### uploading:
kako da stvar na GitHub...
v spremenljivko "origin" spravimo URL projekta
> `git remote add origin https://github.com/davidrihtarsic/myZapiski.git`
> `git push ~~origin master~~` #daš na GitHub +username +passWd

### updating:
naprimer, da nekdo popravi kodo (recimo ti sam na GitHubu...
in nekdo tudi na compu ter naredi commit)
> `git commit -a -m "comment"`

hočeš naložit... novo verzijo in dobiš konflikt s tisto na GitHub-u
> `git push origin master` #in dobiš error:

	|hint: Updates were rejected because the remote contains work that you do
	|hint: not have locally. This is usually caused by another repository pushing
	|hint: to the same ref. You may want to first integrate the remote changes
	|hint: (e.g., 'git pull ...') before pushing again.
	|hint: See the 'Note about fast-forwards' in 'git push --help' for details.

potem naredis :
> `git pull` #ce je prvič lahko tudi: git pull origin master

in če je bil dokument spremenjen na ISTEM mestu (recimo v isti crstici)
potem je to v dokumentu označeno z:		

	|		<<<<<<< HEAD
	|				#to je novo na compu
	|		=======
	|				#to je novo na GitHubu
	|				#heh nisem si zapisoval
	|		>>>>>>> 14d185fbd48d55e9a37d7de3e4d9bde157aa8915

če pa je na različnih mestih pa dokument združi preko:
	
	| "recursive strategy"...
	
in je to - to :)
skratka popraviš in uploadaš še enkrat :) jeah!

# W3M:
## instalation:
> `apt-get install w3m`

## frendlyUse:
	v ~/bashrc vpišeš:
> `alias w3mm='w3m www.google.com'`

# DD_IBS_TEST.SH():
program za testiranje dd komnade...
kako hitro comp lahko kopira datoteke v odvisnosti ob bs= ? podatka...
Program je na [GitHubu][https://github.com/tdg5/blog/blob/master/_includes/scripts/dd_ibs_test.sh]

