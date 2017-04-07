def EFI_mode():
	boot -> CSM enable
	security -> security boot control -> dissable
def installBUNSEN():
	#instaliral ...
	#grub dal na sda1 (kjer sem našel efi... [sudo parted -l])
	# kar nekaj sem probal... ni delalo - sedaj pišem kaj ne dela
	# test x-1
	# BIOS:
	# new boot oprions:
	# - path:\efi\boot\bootx64.efi
	#ne dela
	# Test x-n
	# probaj ta navodila:
	# http://sarah.thesharps.us/2014/12/31/installing-debian-on-asus-ux301la/
	#-----
	#install
	# grub -> /dev/sda1
	# takoj ne dela... zažene se win10...
	# path :\EFI\debian\grubx64.efi [ne dela]
	# path :\efi\boot\bootx64.efi [ne dela]
def Wireless_Monitoring:
	Wavemon...
	sudo apt-get install wavemon
def KeyBoardSettings&Keybindings():
	Settings -> Reigon&Language -> Input Source
	for KeyBindings:
	def ShortCuts():
		v settings>Keyboaard sem si nastavil nekaj bližnjic:
			super+w > Firefox
			super+e > Text Editor
			super+f > File Manager
			super+t > terminator
			---
			v ~/.bashrc (file se zazene na zacetku)
			#bliznica ll namesto ...
			alias ll='ls -alF'
			#tipki [đ] dodelimo znak [/]
			xmodmap -e "keycode 35 = slash"
def FileManager():
	Všeč mi je filemanager THUNAR:
		- apt-get install thunar
def Terminal():
	Terminal je najboljši terminator
		-apt-get install terminator
	Preferences:
		[ ] Show title bar
		Profiles -> Colors = Green on Black
		Profiles -> Background -> Transparency = 50%
def LibreOffice():
	apt-get install libreoffice
def Tab_CLICK():
	Da vklnjučiš Tab-CLICK greš v:
		-settings
		-mouse
		-in nato : Tab-CLICK = ON
	Videl sem tudi, da problem reši tudi:
		synclient tapbutton1=1
def Touchpad()
	v dat /usr/share/X11/xorg.conf.d/50-synaptics.conf
	dodas:
	Section "InputClass"
		Identifier      "Touchpad"                      # required
		MatchIsTouchpad "yes"                           # required
		Driver          "synaptics"                     # required
		Option          "MinSpeed"              "0.5"
		Option          "MaxSpeed"              "1.0"
		Option          "AccelFactor"           "0.075"
		Option          "TapButton1"            "1"
		Option          "TapButton2"            "3"     # multitouch
		Option          "TapButton3"            "2"     # multitouch
		Option          "VertTwoFingerScroll"   "1"     # multitouch
		Option          "HorizTwoFingerScroll"  "1"     # multitouch
		Option          "VertEdgeScroll"        "1"
		Option          "CoastingSpeed"         "8"
		Option          "CornerCoasting"        "1"
		Option          "CircularScrolling"     "1"
		Option          "CircScrollTrigger"     "7"
		Option          "EdgeMotionUseAlways"   "1"
		Option          "LBCornerButton"        "8"     # browser "back" btn
		Option          "RBCornerButton"        "9"     # browser "forward" btn
	EndSection
def SoundON():
	Na začetku mi ni delal zvok... Rešitev je bila:
		- lspci:
			tako preveriš, če je Linux prepoznal zvočno...
			na terminalu sem dobil:
			'00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller (rev 04)'
		- apt-get install libasound2 alsa-utils alsa-oss 
		- alsamixer:
			in od "mutiraš" kanale, ki so zamutani
	Druga rešitev (ali celo dopolnitev):
		- je, da v terminal napišeš:
			pulseaudio -D
		- secer napiše, da ni mišljeno, da bi bil zagnan kot root
			ampak Ok... po tem dela tudi:
			Settings>Soun
def Thunderbird():
	inštalacija je čisto reprosta:
		- apt-get install thunderbird
	ali če ni povezave...
		- greš na njihovo stran in presnameš datoteko thunderbird.tar.db2
		- extrahiraš v /opt/thunderbird
		- preveriš če dela: ./thunderbird
		- nastaviš privilegije (če je potrebno): sudo chown -R root:root /opt/thunderbird
		- in linkaš exe skript: sudo ln -fs /opt/thunderbird/thunderbird /usr/bin/thunderbird
def Sublime text 3():
	greš na njihovo stran in snameš dol pravo verzijo (Ubuntu 64)
	nato pa v terminalu zaženeš:
	- cd Download1
	- dpkg -i Sublime...64.deb
def TeamViewer
	- presnames teamviewer i386 (cetudi imas 64-bitni comp.)
	- v terminalu> dpkg --add-architecture i386
	- apt-get update
	- dpkg -i teamviewer_****_i386.deb
	- sudo apt-get -f install

# RISANJE
def qCad():
	- presnameš inštalacijo iz njihove strani:
	https://qcad.org/en/qcad-downloads-trial
	- nato spremeniš rivilegije datoteke:
	sudo chmod 777 qcad*.run
	- in poženeš script:
	./qcad*.run
def FreeCAD():
	asdf
def Gimp():
	asdf
def Inkscape():
	asdf
def Fritzing():
	asdf
def Popcorn-Time
	Download1 Popcorn-Time : https://www.popcorntime.ws/about
	razpakiraš in daš dokumente v /opt/popcorn-time/
	polinkaš, da bo dosegljivo vsem:
		sudo ln -sf /opt/popcorn-time/Popcorn-Time /usr/bin/popcorn-time
	Narediš še .desktop datoteko
		sudo nano /usr/share/applications/popcorntime.desktop
	in vot vpišeš:
		[Desktop Entry]
		Version = 1.0
		Type = Application
		Terminal = false
		Name = Popcorn Time
		Exec = /usr/bin/popcorn-time
		Icon = /opt/popcorn-time/src/app/images/icon.png
		Categories = Application;

# PROGRAMIRANJE
def eclipse
	for installation:
		... nisem zapisal...
		... presnameš, odpakiraš kopiraš v:
		/opt/eclipse/
		narediš link za vse uporabnike:
			sudo ln -sf /opt/eclipse/cpp-neon/eclipse/eclipse /usr/bin/eclipse
	for eclipse.desktop:
		sudo nano /usr/share/applications/eclipse.desktop
		[Desktop Entry]
		Version = Neon 2.0
		Type = Application
		Terminal = false
		Name = eclipse
		Exec = /usr/bin/eclipse
		Icon = /opt/eclipse/cpp-neon/eclipse/icon.xpm
		Categories = Development;
def Arduino():
	pass
def GitHub():
	for literatura:
		# https://www.youtube.com/watch?v=1h9_cB9mPT8
	for install:
		# za Debian le:
		sudo apt-get install git
	for config:
		git config --global user.name "xxxyyy"
		git config --global user.email "xxx.yyy@džimail.com"
		git config --global core.editor="subl"
	for general_use:
		make new repository ... BlaBla_project (need to be on URL gitHub)
		make dir on your computer for that project 
		navigate to that dir
		:git init
		for editing:
			## na tem mestu spreminjaš FAJL...
			#:git add . #dodaj vse datoteke
			#:git commit -m "comment"
			:git commit -a -m "comment" #naredi vse naenkrat
			:git status # ni potreben a se vidi ce je potrebno kaj commitat
			:git diff 	#ni potrebno a pokaže razlike...
		for uploading:
			## kako da stvar na GitHub...
			# v spremenljivko "origin" spravimo URL projekta
			:git remote add origin https://github.com/davidrihtarsic/myZapiski.git
			:git push ~~origin master~~ #daš na GitHub +username +passWd
		for updating:
			## naprimer, da nekdo popravi kodo (recimo ti sam na GitHubu...
			## in nekdo tudi na compu ter naredi commit)
			:git commit -a -m "comment"
			## hočeš naložit... novo verzijo in dobiš konflikt s tisto na GitHub-u
			:git push origin master #in dobiš error
				#hint: Updates were rejected because the remote contains work that you do
				#hint: not have locally. This is usually caused by another repository pushing
				#hint: to the same ref. You may want to first integrate the remote changes
				#hint: (e.g., 'git pull ...') before pushing again.
				#hint: See the 'Note about fast-forwards' in 'git push --help' for details.
			## potem naredis
			:git pull #ce je prvič lahko tudi: git pull origin master
			# in če je bil dokument spremenjen na ISTEM mestu (recimo v isti crstici)
			# potem je to v dokumentu označeno z:
				#<<<<<<< HEAD
				#			#to je novo na compu
				#=======
				#			#to je novo na GitHubu
				#		#heh nisem si zapisoval
				#>>>>>>> 14d185fbd48d55e9a37d7de3e4d9bde157aa8915
			# če pa je na različnih mestih pa dokument združi preko "recursive strategy"...
			# in je to - to :)
			# skratka popraviš in uploadaš še enkrat :) jeah!
def w3m():
	for instalation :
		apt-get install w3m
	for frendlyUse:
		v ~/bashrc vpišeš:
		alias w3mm='w3m www.google.com'
def dd_ibs_test.sh():
	program za testiranje dd komnade...
	kako hitro comp lahko kopira datoteke v odvisnosti ob bs= ? podatka...
	Program je na GitHubu

