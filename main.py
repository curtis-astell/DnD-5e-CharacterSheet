import sys,math
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QLineEdit,QTabWidget,\
                            QDialog,QComboBox,QSpinBox,QMainWindow,QCheckBox,\
                            QPlainTextEdit,QTableWidget,QPushButton,QGroupBox,\
                            QListWidget
from PyQt5.QtGui import QIcon

#Initialize GUI window
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('5e Character Creator')
        self.setGeometry(100,80,490,630)
        self.setWindowIcon(QIcon('icons/d20icon'))
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(10,10,470,610)
        self.tabWidget.addTab(statsTab(),'Stats')
        self.tabWidget.addTab(itemTab(),'Inventory')
        self.tabWidget.addTab(magicTab(), 'Spells') 
        charNameLabel=QLabel('Character Name:')

#Class holds "stats" tab, contains basic character information                
class statsTab(QWidget):
    def __init__(self):
        super().__init__()
        #Line edit to enter character name
        charNameLabel = QLabel('Character Name:', self)
        charNameLabel.move(10,10)         
        charNameEdit = QLineEdit(self)
        charNameEdit.move(10,25)
        
        #Drop down list to select character class
        classLabel = QLabel('Class:',self)
        classLabel.move(155,10)
        classSelect = QComboBox(self)
        #Classes available in vanilla D&D 5e PHB
        classList = [' ','Barbarian','Bard','Cleric','Druid','Fighter','Monk',\
                     'Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
        classSelect.addItems(classList)
        classSelect.move(185,8)
        classSelect.setFixedWidth(83)
        
        #Drop down list to select character race
        raceLabel = QLabel('Race:',self)
        raceLabel.move(155,35)
        raceSelect = QComboBox(self)
        #Races available in vanilla D&D 5e PHB
        raceList = [' ','Dwarf','Elf','Halfling','Human','Dragonborn','Gnome',\
                     'Half-Elf','Half-Orc','Tiefling']
        raceSelect.addItems(raceList)
        raceSelect.move(185,30)
        
        #Drop down list to select character background
        bgLabel = QLabel('Background:',self)
        bgLabel.move(275,10)
        bgSelect = QComboBox(self)
        #Backgrounds available in vanilla D&D 5e PHB
        #Backgrounds available in vanilla D&D 5e PHB
        bgList = [' ','Acolyte','Charlatan','Criminal','Entertainer','Folk Hero',\
                  'Guild Artisan','Hermit','Noble','Outlander','Sage','Sailor',\
                  'Soldier','Urchin']
        bgSelect.addItems(bgList)
        bgSelect.move(336,8)
        bgSelect.setFixedWidth(99)
        
        #Drop down list to select character alignment
        alignLabel = QLabel('Alignment:',self)
        alignLabel.move(275,35)
        alignSelect = QComboBox(self)
        #List of all alignments
        alignList = [' ','Lawful Good','Lawful Neutral','Lawful Evil',\
                     'Neutral Good','True Neutral','Neutral Evil',\
                     'Chaotic Good','Chaotic Neutral','Chaotic Evil']
        alignSelect.addItems(alignList)
        alignSelect.move(336,30)
        alignSelect.setFixedWidth(99)
        
        #Following spinboxes for adjusting character attributes
        #Numbers range from 1 to 18
        #Following line edits automatically calculate modifiers for user
        attrLabel = QLabel('Attributes',self)
        attrLabel.move(10,60)
        
        self.strLabel = QLabel('STR',self)
        self.strLabel.move(10,80)
        self.strStat = QSpinBox(self)
        self.strStat.setFixedWidth(35)
        self.strStat.move(35,78)
        self.strStat.setRange(1,18)
        self.strStat.setValue(10)
        self.strStat.valueChanged.connect(self.modCalc)
        self.strMod = QLineEdit(self)
        self.strMod.setReadOnly(True)
        self.strMod.setFixedWidth(25)
        self.strMod.move(70,78)
        
        self.dexLabel = QLabel('DEX',self)
        self.dexLabel.move(10,100)
        self.dexStat = QSpinBox(self)
        self.dexStat.setFixedWidth(35)
        self.dexStat.move(35,98)
        self.dexStat.setRange(1,18)
        self.dexStat.setValue(10)
        self.dexStat.valueChanged.connect(self.modCalc)
        self.dexMod = QLineEdit(self)
        self.dexMod.setReadOnly(True)
        self.dexMod.setFixedWidth(25)
        self.dexMod.move(70,98)
        
        self.conLabel = QLabel('CON',self)
        self.conLabel.move(10,120)
        self.conStat = QSpinBox(self)
        self.conStat.setFixedWidth(35)
        self.conStat.move(35,118)
        self.conStat.setRange(1,18)
        self.conStat.setValue(10)
        self.conStat.valueChanged.connect(self.modCalc)
        self.conMod = QLineEdit(self)
        self.conMod.setReadOnly(True)
        self.conMod.setFixedWidth(25)
        self.conMod.move(70,118)
        
        self.intLabel = QLabel('INT',self)
        self.intLabel.move(10,140)
        self.intStat = QSpinBox(self)
        self.intStat.setFixedWidth(35)
        self.intStat.move(35,138)
        self.intStat.setRange(1,18)
        self.intStat.setValue(10)
        self.intStat.valueChanged.connect(self.modCalc)
        self.intMod = QLineEdit(self)
        self.intMod.setReadOnly(True)
        self.intMod.setFixedWidth(25)
        self.intMod.move(70,138)
        
        self.wisLabel = QLabel('WIS',self)
        self.wisLabel.move(10,160)
        self.wisStat = QSpinBox(self)
        self.wisStat.setFixedWidth(35)
        self.wisStat.move(35,158)
        self.wisStat.setRange(1,18)
        self.wisStat.setValue(10)
        self.wisStat.valueChanged.connect(self.modCalc)
        self.wisMod = QLineEdit(self)
        self.wisMod.setReadOnly(True)
        self.wisMod.setFixedWidth(25)
        self.wisMod.move(70,158)
        
        self.chaLabel = QLabel('CHA',self)
        self.chaLabel.move(10,180)
        self.chaStat = QSpinBox(self)
        self.chaStat.setFixedWidth(35)
        self.chaStat.move(35,178)
        self.chaStat.setRange(1,18)
        self.chaStat.setValue(10)    
        self.chaStat.valueChanged.connect(self.modCalc)
        self.chaMod = QLineEdit(self)
        self.chaMod.setReadOnly(True)
        self.chaMod.setFixedWidth(25)
        self.chaMod.move(70,178)
        
        #Check boxes for attribute saving throws
        #Boxes automatically add proficiency bonus to modifier for final result
        savThrowLabel = QLabel('Saving Throws',self)
        savThrowLabel.move(105,60)        
        
        self.savThroStr = QCheckBox('Strength',self)
        self.savThroStr.move(105,80)
        self.savThroStr.toggled.connect(self.modCalc)
        self.savThroStrMod = QLineEdit(self)
        self.savThroStrMod.setReadOnly(True)
        self.savThroStrMod.setFixedWidth(25)
        self.savThroStrMod.move(181,78)
        
        self.savThroDex = QCheckBox('Dexterity',self)
        self.savThroDex.move(105,100)
        self.savThroDex.toggled.connect(self.modCalc)
        self.savThroDexMod = QLineEdit(self)
        self.savThroDexMod.setReadOnly(True)
        self.savThroDexMod.setFixedWidth(25)
        self.savThroDexMod.move(181,98)
        
        self.savThroCon = QCheckBox('Constitution',self)
        self.savThroCon.move(105,120)
        self.savThroCon.toggled.connect(self.modCalc)
        self.savThroConMod = QLineEdit(self)
        self.savThroConMod.setReadOnly(True)
        self.savThroConMod.setFixedWidth(25)
        self.savThroConMod.move(181,118)
        
        self.savThroInt = QCheckBox('Intelligence',self)
        self.savThroInt.move(105,140)
        self.savThroInt.toggled.connect(self.modCalc)
        self.savThroIntMod = QLineEdit(self)
        self.savThroIntMod.setReadOnly(True)
        self.savThroIntMod.setFixedWidth(25)
        self.savThroIntMod.move(181,138)
        
        self.savThroWis = QCheckBox('Wisdom',self)
        self.savThroWis.move(105,160)
        self.savThroWis.toggled.connect(self.modCalc)
        self.savThroWisMod = QLineEdit(self)
        self.savThroWisMod.setReadOnly(True)
        self.savThroWisMod.setFixedWidth(25)
        self.savThroWisMod.move(181,158)
        
        self.savThroCha = QCheckBox('Charisma',self)
        self.savThroCha.move(105,180)
        self.savThroCha.toggled.connect(self.modCalc)
        self.savThroChaMod = QLineEdit(self)
        self.savThroChaMod.setReadOnly(True)
        self.savThroChaMod.setFixedWidth(25)
        self.savThroChaMod.move(181,178)
        
        #Check boxes for character skills
        #Again, boxes will add modifier with proficiency bonus
        self.skillLabel = QLabel('Skills',self)
        self.skillLabel.move(10,205)
        
        self.acroSkillCheckBox = QCheckBox(self)
        self.acroSkillCheckBox.move(10,220)
        self.acroSkillCheckBox.toggled.connect(self.modCalc)
        self.acroSkillMod = QLineEdit(self)
        self.acroSkillMod.setReadOnly(True)
        self.acroSkillMod.setFixedWidth(25)
        self.acroSkillMod.move(24,218)
        self.acroSkillLabel = QLabel('Acrobatics',self)
        self.acroSkillLabel.move(51,220)
        
        self.anihandSkillCheckBox = QCheckBox(self)
        self.anihandSkillCheckBox.move(10,240)
        self.anihandSkillCheckBox.toggled.connect(self.modCalc)
        self.anihandSkillMod = QLineEdit(self)
        self.anihandSkillMod.setReadOnly(True)
        self.anihandSkillMod.setFixedWidth(25)
        self.anihandSkillMod.move(24,238)
        self.anihandSkillLabel = QLabel('Animal Handling',self)
        self.anihandSkillLabel.move(51,240)
        
        self.arcanaSkillCheckBox = QCheckBox(self)
        self.arcanaSkillCheckBox.move(10,260)
        self.arcanaSkillCheckBox.toggled.connect(self.modCalc)
        self.arcanaSkillMod = QLineEdit(self)
        self.arcanaSkillMod.setReadOnly(True)
        self.arcanaSkillMod.setFixedWidth(25)
        self.arcanaSkillMod.move(24,258)
        self.arcanaSkillLabel = QLabel('Arcana',self)
        self.arcanaSkillLabel.move(51,260)
        
        self.athlSkillCheckBox = QCheckBox(self)
        self.athlSkillCheckBox.move(10,280)
        self.athlSkillCheckBox.toggled.connect(self.modCalc)
        self.athlSkillMod = QLineEdit(self)
        self.athlSkillMod.setReadOnly(True)
        self.athlSkillMod.setFixedWidth(25)
        self.athlSkillMod.move(24,278)
        self.athlSkillLabel = QLabel('Athletics',self)
        self.athlSkillLabel.move(51,280)
        
        self.decepSkillCheckBox = QCheckBox(self)
        self.decepSkillCheckBox.move(10,300)
        self.decepSkillCheckBox.toggled.connect(self.modCalc)
        self.decepSkillMod = QLineEdit(self)
        self.decepSkillMod.setReadOnly(True)
        self.decepSkillMod.setFixedWidth(25)
        self.decepSkillMod.move(24,298)
        self.decepSkillLabel = QLabel('Deception',self)
        self.decepSkillLabel.move(51,300)  
        
        self.histSkillCheckBox = QCheckBox(self)
        self.histSkillCheckBox.move(10,320)
        self.histSkillCheckBox.toggled.connect(self.modCalc)
        self.histSkillMod = QLineEdit(self)
        self.histSkillMod.setReadOnly(True)
        self.histSkillMod.setFixedWidth(25)
        self.histSkillMod.move(24,318)
        self.histSkillLabel = QLabel('History',self)
        self.histSkillLabel.move(51,320)
        
        self.insiSkillCheckBox = QCheckBox(self)
        self.insiSkillCheckBox.move(10,340)
        self.insiSkillCheckBox.toggled.connect(self.modCalc)
        self.insiSkillMod = QLineEdit(self)
        self.insiSkillMod.setReadOnly(True)
        self.insiSkillMod.setFixedWidth(25)
        self.insiSkillMod.move(24,338)
        self.insiSkillLabel = QLabel('Insight',self)
        self.insiSkillLabel.move(51,340)
        
        self.intimSkillCheckBox = QCheckBox(self)
        self.intimSkillCheckBox.move(10,360)
        self.intimSkillCheckBox.toggled.connect(self.modCalc)
        self.intimSkillMod = QLineEdit(self)
        self.intimSkillMod.setReadOnly(True)
        self.intimSkillMod.setFixedWidth(25)
        self.intimSkillMod.move(24,358)
        self.intimSkillLabel = QLabel('Intimidation',self)
        self.intimSkillLabel.move(51,360)
        
        self.invesSkillCheckBox = QCheckBox(self)
        self.invesSkillCheckBox.move(10,380)
        self.invesSkillCheckBox.toggled.connect(self.modCalc)
        self.invesSkillMod = QLineEdit(self)
        self.invesSkillMod.setReadOnly(True)
        self.invesSkillMod.setFixedWidth(25)
        self.invesSkillMod.move(24,378)
        self.invesSkillLabel = QLabel('Investigation',self)
        self.invesSkillLabel.move(51,380)   
        
        self.medSkillCheckBox = QCheckBox(self)
        self.medSkillCheckBox.move(10,400)
        self.medSkillCheckBox.toggled.connect(self.modCalc)
        self.medSkillMod = QLineEdit(self)
        self.medSkillMod.setReadOnly(True)
        self.medSkillMod.setFixedWidth(25)
        self.medSkillMod.move(24,398)
        self.medSkillLabel = QLabel('Medicine',self)
        self.medSkillLabel.move(51,400)
        
        self.natrSkillCheckBox = QCheckBox(self)
        self.natrSkillCheckBox.move(10,420)
        self.natrSkillCheckBox.toggled.connect(self.modCalc)
        self.natrSkillMod = QLineEdit(self)
        self.natrSkillMod.setReadOnly(True)
        self.natrSkillMod.setFixedWidth(25)
        self.natrSkillMod.move(24,418)
        self.natrSkillLabel = QLabel('Nature',self)
        self.natrSkillLabel.move(51,420)     
        
        self.percpSkillCheckBox = QCheckBox(self)
        self.percpSkillCheckBox.move(10,440)
        self.percpSkillCheckBox.toggled.connect(self.modCalc)
        self.percpSkillMod = QLineEdit(self)
        self.percpSkillMod.setReadOnly(True)
        self.percpSkillMod.setFixedWidth(25)
        self.percpSkillMod.move(24,438)
        self.percpSkillLabel = QLabel('Perception',self)
        self.percpSkillLabel.move(51,440)
        
        self.perfSkillCheckBox = QCheckBox(self)
        self.perfSkillCheckBox.move(10,460)
        self.perfSkillCheckBox.toggled.connect(self.modCalc)
        self.perfSkillMod = QLineEdit(self)
        self.perfSkillMod.setReadOnly(True)
        self.perfSkillMod.setFixedWidth(25)
        self.perfSkillMod.move(24,458)
        self.perfSkillLabel = QLabel('Performance',self)
        self.perfSkillLabel.move(51,460)
        
        self.persSkillCheckBox = QCheckBox(self)
        self.persSkillCheckBox.move(10,480)
        self.persSkillCheckBox.toggled.connect(self.modCalc)
        self.persSkillMod = QLineEdit(self)
        self.persSkillMod.setReadOnly(True)
        self.persSkillMod.setFixedWidth(25)
        self.persSkillMod.move(24,478)
        self.persSkillLabel = QLabel('Persuasion',self)
        self.persSkillLabel.move(51,480)   
        
        self.reliSkillCheckBox = QCheckBox(self)
        self.reliSkillCheckBox.move(10,500)
        self.reliSkillCheckBox.toggled.connect(self.modCalc)
        self.reliSkillMod = QLineEdit(self)
        self.reliSkillMod.setReadOnly(True)
        self.reliSkillMod.setFixedWidth(25)
        self.reliSkillMod.move(24,498)
        self.reliSkillLabel = QLabel('Religion',self)
        self.reliSkillLabel.move(51,500)
        
        self.sleightSkillCheckBox = QCheckBox(self)
        self.sleightSkillCheckBox.move(10,520)
        self.sleightSkillCheckBox.toggled.connect(self.modCalc)
        self.sleightSkillMod = QLineEdit(self)
        self.sleightSkillMod.setReadOnly(True)
        self.sleightSkillMod.setFixedWidth(25)
        self.sleightSkillMod.move(24,518)
        self.sleightSkillLabel = QLabel('Sleight of Hand',self)
        self.sleightSkillLabel.move(51,520)
        
        self.stealthSkillCheckBox = QCheckBox(self)
        self.stealthSkillCheckBox.move(10,540)
        self.stealthSkillCheckBox.toggled.connect(self.modCalc)
        self.stealthSkillMod = QLineEdit(self)
        self.stealthSkillMod.setReadOnly(True)
        self.stealthSkillMod.setFixedWidth(25)
        self.stealthSkillMod.move(24,538)
        self.stealthSkillLabel = QLabel('Stealth',self)
        self.stealthSkillLabel.move(51,540)     
        
        self.survSkillCheckBox = QCheckBox(self)
        self.survSkillCheckBox.move(10,560)
        self.survSkillCheckBox.toggled.connect(self.modCalc)
        self.survSkillMod = QLineEdit(self)
        self.survSkillMod.setReadOnly(True)
        self.survSkillMod.setFixedWidth(25)
        self.survSkillMod.move(24,558)
        self.survSkillLabel = QLabel('Survival',self)
        self.survSkillLabel.move(51,560)
        
        #Line edits for adding AC, initiative, speed, HP & hit dice
        acLabel = QLabel('AC:',self)
        acLabel.move(230,65)
        acBox = QLineEdit(self)
        acBox.setFixedWidth(25)
        acBox.move(250,63)
        
        initLabel = QLabel('Initiative:',self)
        initLabel.move(280,65)
        initBox = QLineEdit(self)
        initBox.setFixedWidth(25)
        initBox.move(328,63)
        
        speedLabel = QLabel('Speed:',self)
        speedLabel.move(360,65)
        speedBox = QLineEdit(self)
        speedBox.setFixedWidth(25)
        speedBox.move(395,63)
        
        hpMaxLabel = QLabel('Hit Point Maximum:',self)
        hpMaxLabel.move(230,90)
        hpMaxBox = QLineEdit(self)
        hpMaxBox.setFixedWidth(25)
        hpMaxBox.move(325,88)
        
        hitDiceLabel = QLabel('Hit Dice:',self)
        hitDiceLabel.move(355,90)
        hitDiceBox = QLineEdit(self)
        hitDiceBox.setFixedWidth(30)
        hitDiceBox.move(395,88)
        
        #Text edit to add player bio, no character limit
        characterBioLabel = QLabel('Character Bio',self)
        characterBioLabel.move(225,115)
        characterBio = QPlainTextEdit(self)
        characterBio.move(225,130)
        characterBio.setFixedHeight(75)
        characterBio.setFixedWidth(200)
        
        #Chart for adding attacks/damaging spells
        #Room for attack name, bonus & damage/type
        attacksLabel = QLabel('Attacks & Spellcasting',self)
        attacksLabel.move(148,220)
        attacksChart = QTableWidget(self)
        attacksChart.setColumnCount(3)
        attacksChart.setRowCount(5)
        attacksChart.setFixedWidth(330)
        attacksChart.move(130,240)
        attacksChart.setHorizontalHeaderLabels(['Name','Attack Bonus',\
                                               'Damage/Type'])
        attacksChart.horizontalHeader().setDefaultSectionSize(103)
        
        #Misc section, as is found on vanilla printed 5e sheets
        otherLabel = QLabel('Other Proficiencies, Languages & Traits',self)
        otherLabel.move(148,440)
        otherBox = QPlainTextEdit(self)
        otherBox.move(130,460)
        otherBox.setFixedHeight(120)
        otherBox.setFixedWidth(320)
        
        self.modCalc()
        
    #"modCalc" function automatically adjusts modifiers for character stats
    #Formula for modifiers is always (Stat - 10) / 2, rounded down
    #Zero division error will return 0
    def modCalc(self):
        strStatVal = self.strStat.value()
        try:
            strModVal = math.floor((strStatVal - 10) / 2)
        except ZeroDivisionError:
            strModVal = 0
        self.strMod.setText('%d' % (strModVal))
    
        dexStatVal = self.dexStat.value()
        try:
            dexModVal = math.floor((dexStatVal - 10) / 2)
        except ZeroDivisionError:
            dexModVal = 0
        self.dexMod.setText('%d' % (dexModVal))
        
        conStatVal = self.conStat.value()
        try:
            conModVal = math.floor((conStatVal - 10) / 2)
        except ZeroDivisionError:
            conModVal = 0
        self.conMod.setText('%d' % (conModVal))
        
        intStatVal = self.intStat.value()
        try:
            intModVal = math.floor((intStatVal - 10) / 2)
        except ZeroDivisionError:
            intModVal = 0
        self.intMod.setText('%d' % (intModVal))
        
        wisStatVal = self.wisStat.value()
        try:
            wisModVal = math.floor((wisStatVal - 10) / 2)
        except ZeroDivisionError:
            wisModVal = 0
        self.wisMod.setText('%d' % (wisModVal))
        
        chaStatVal = self.chaStat.value()
        try:
            chaModVal = math.floor((chaStatVal - 10) / 2)
        except ZeroDivisionError:
            chaModVal = 0
        self.chaMod.setText('%d' % (chaModVal))
        
        #Saving throw formula is always modifier plus 2
        savThroStrVal = strModVal + 2
        if self.savThroStr.isChecked():
            self.savThroStrMod.setText('%d' % (savThroStrVal))
        else:
            self.savThroStrMod.setText('')
            
        savThroDexVal = dexModVal + 2
        if self.savThroDex.isChecked():
            self.savThroDexMod.setText('%d' % (savThroDexVal))
        else:
            self.savThroDexMod.setText('')
            
        savThroConVal = conModVal + 2
        if self.savThroCon.isChecked():
            self.savThroConMod.setText('%d' % (savThroConVal))
        else:
            self.savThroConMod.setText('')
            
        savThroIntVal = intModVal + 2
        if self.savThroInt.isChecked():
            self.savThroIntMod.setText('%d' % (savThroIntVal))
        else:
            self.savThroIntMod.setText('')
            
        savThroWisVal = wisModVal + 2
        if self.savThroWis.isChecked():
            self.savThroWisMod.setText('%d' % (savThroWisVal))
        else:
            self.savThroWisMod.setText('')
            
        savThroChaVal = chaModVal + 2
        if self.savThroCha.isChecked():
            self.savThroChaMod.setText('%d' % (savThroChaVal))
        else: 
            self.savThroChaMod.setText('')
        
        #Skill formula is always modifier plus 2    
        acroSkillVal = dexModVal + 2
        if self.acroSkillCheckBox.isChecked():
            self.acroSkillMod.setText('%d' % (acroSkillVal))
        else:
            self.acroSkillMod.setText('')
            
        anihandSkillVal = wisModVal + 2
        if self.anihandSkillCheckBox.isChecked():
            self.anihandSkillMod.setText('%d' % (anihandSkillVal))
        else:
            self.anihandSkillMod.setText('')
            
        arcanaSkillVal = intModVal + 2
        if self.arcanaSkillCheckBox.isChecked():
            self.arcanaSkillMod.setText('%d' % (arcanaSkillVal))
        else:
            self.arcanaSkillMod.setText('')
            
        athlSkillVal = strModVal + 2
        if self.athlSkillCheckBox.isChecked():
            self.athlSkillMod.setText('%d' % (athlSkillVal))
        else:
            self.athlSkillMod.setText('')
            
        decepSkillVal = chaModVal + 2
        if self.decepSkillCheckBox.isChecked():
            self.decepSkillMod.setText('%d' % (decepSkillVal))
        else:
            self.decepSkillMod.setText('')
            
        histSkillVal = intModVal + 2
        if self.histSkillCheckBox.isChecked():
            self.histSkillMod.setText('%d' % (histSkillVal))
        else:
            self.histSkillMod.setText('')
            
        insiSkillVal = wisModVal + 2
        if self.insiSkillCheckBox.isChecked():
            self.insiSkillMod.setText('%d' % (insiSkillVal))
        else:
            self.insiSkillMod.setText('')
            
        intimSkillVal = chaModVal + 2
        if self.intimSkillCheckBox.isChecked():
            self.intimSkillMod.setText('%d' % (intimSkillVal))
        else:
            self.intimSkillMod.setText('')
            
        invesSkillVal = intModVal + 2
        if self.invesSkillCheckBox.isChecked():
            self.invesSkillMod.setText('%d' % (invesSkillVal))
        else:
            self.invesSkillMod.setText('')
            
        medSkillVal = wisModVal + 2
        if self.medSkillCheckBox.isChecked():
            self.medSkillMod.setText('%d' % (medSkillVal))
        else: 
            self.medSkillMod.setText('')
            
        natrSkillVal = intModVal + 2
        if self.natrSkillCheckBox.isChecked():
            self.natrSkillMod.setText('%d' % (natrSkillVal))
        else:
            self.natrSkillMod.setText('')
            
        percpSkillVal = wisModVal + 2
        if self.percpSkillCheckBox.isChecked():
            self.percpSkillMod.setText('%d' % (percpSkillVal))
        else:
            self.percpSkillMod.setText('')
            
        perfSkillVal = chaModVal + 2
        if self.perfSkillCheckBox.isChecked():
            self.perfSkillMod.setText('%d' % (perfSkillVal))
        else:
            self.perfSkillMod.setText('')
            
        persSkillVal = chaModVal + 2
        if self.persSkillCheckBox.isChecked():
            self.persSkillMod.setText('%d' % (persSkillVal))
        else:
            self.persSkillMod.setText('')
            
        reliSkillVal = intModVal + 2
        if self.reliSkillCheckBox.isChecked():
            self.reliSkillMod.setText('%d' % (reliSkillVal))
        else:
            self.reliSkillMod.setText('')
            
        sleightSkillVal = dexModVal + 2
        if self.sleightSkillCheckBox.isChecked():
            self.sleightSkillMod.setText('%d' % (sleightSkillVal))
        else:
            self.sleightSkillMod.setText('')
            
        stealthSkillVal = dexModVal + 2
        if self.stealthSkillCheckBox.isChecked():
            self.stealthSkillMod.setText('%d' % (stealthSkillVal))
        else:
            self.stealthSkillMod.setText('')
          
        survSkillVal = wisModVal + 2
        if self.survSkillCheckBox.isChecked():
            self.survSkillMod.setText('%d' % (survSkillVal))
        else:
            self.survSkillMod.setText('')

#Inventory tab for keeping track of starting money and items purchased                       
class itemTab(QWidget):
    def __init__(self):
        super().__init__()
        #General inventory for miscellaneous items
        self.miscInventoryEntry = QTableWidget(self)
        self.miscInventoryEntry.setRowCount(8)
        self.miscInventoryEntry.setColumnCount(1)
        self.miscInventoryEntry.move(10,10)
        self.miscInventoryEntry.setHorizontalHeaderLabels(['Misc.'])
        self.miscInventoryEntry.setFixedWidth(152)
        self.miscInventoryEntry.setFixedHeight(280)
        self.miscInventoryEntry.horizontalHeader().setDefaultSectionSize(123)
        self.miscAddRowButton = QPushButton(self)
        self.miscAddRowButton.setIcon(QIcon('icons/addRow.png'))
        self.miscAddRowButton.move(160,9)
        self.miscAddRowButton.setToolTip('Add Row')
        self.miscAddRowButton.clicked.connect(self.miscAddRow)
        self.miscRemoveRowButton = QPushButton(self)
        self.miscRemoveRowButton.setIcon(QIcon('icons/removeRow.png'))
        self.miscRemoveRowButton.move(160,31)
        self.miscRemoveRowButton.setToolTip('Remove Row')
        self.miscRemoveRowButton.clicked.connect(self.miscRemoveRow)
        
        #Weapon inventory
        self.weapInventoryEntry = QTableWidget(self)
        self.weapInventoryEntry.setRowCount(5)
        self.weapInventoryEntry.setColumnCount(3)
        self.weapInventoryEntry.setHorizontalHeaderLabels(['Weapon','Damage',\
                                                           'Properties'])
        self.weapInventoryEntry.horizontalHeader().setDefaultSectionSize(79)
        self.weapInventoryEntry.move(200,100)
        self.weapAddRowButton = QPushButton(self)
        self.weapAddRowButton.setIcon(QIcon('icons/addRow.png'))
        self.weapAddRowButton.move(174,247)
        self.weapAddRowButton.setToolTip('Add Row')
        self.weapAddRowButton.clicked.connect(self.weapAddRow)
        self.weapRemoveRowButton = QPushButton(self)
        self.weapRemoveRowButton.setIcon(QIcon('icons/removeRow.png'))
        self.weapRemoveRowButton.move(174,269)
        self.weapRemoveRowButton.setToolTip('Remove Row')
        self.weapRemoveRowButton.clicked.connect(self.weapRemoveRow)
        
        #Armour inventory with section for AC
        self.armoInventoryEntry = QTableWidget(self)
        self.armoInventoryEntry.setRowCount(5)
        self.armoInventoryEntry.setColumnCount(2)
        self.armoInventoryEntry.setHorizontalHeaderLabels(['Armour','AC'])
        self.armoInventoryEntry.move(10,300)
        self.armoInventoryEntry.setFixedWidth(220)
        self.armoAddRowButton = QPushButton(self)
        self.armoAddRowButton.setIcon(QIcon('icons/addRow.png'))
        self.armoAddRowButton.move(228,447)
        self.armoAddRowButton.setToolTip('Add Row')
        self.armoAddRowButton.clicked.connect(self.armoAddRow)
        self.armoRemoveRowButton = QPushButton(self)
        self.armoRemoveRowButton.setIcon(QIcon('icons/removeRow.png'))
        self.armoRemoveRowButton.move(228,469)
        self.armoRemoveRowButton.clicked.connect(self.armoRemoveRow)
        
        #Special inventory listing for money and other essentials
        mneGroup = QGroupBox('Money/Essentials',self)
        mneGroup.move(200,5)
        mneGroup.setFixedWidth(256)
        mneGroup.setFixedHeight(90)
        
        #Copper coins
        self.cpBox = QLineEdit(self)
        self.cpBox.move(240,20)
        self.cpBox.setFixedWidth(25)
        self.cpWal = self.cpBox.text
        cpLabel = QLabel('Copper',self)
        cpLabel.move(270,22)
        
        #Silver coins 
        self.spBox = QLineEdit(self)
        self.spBox.move(240,44)
        self.spBox.setFixedWidth(25)
        spLabel = QLabel('Silver',self)
        spLabel.move(270,46)
        
        #Gold coins
        self.gpBox = QLineEdit(self)
        self.gpBox.move(240,68)
        self.gpBox.setFixedWidth(25)
        gpLabel = QLabel('Gold',self)
        gpLabel.move(270,70)
        
        #Carried torches
        torchesLabel = QLabel('Torches',self)
        torchesLabel.move(365,22)
        self.torchCount = QLineEdit(self)
        self.torchCount.move(335,20)
        self.torchCount.setFixedWidth(25)
        
        #Held rations
        rationsLabel = QLabel('Days of Rations',self)
        rationsLabel.move(365,46)
        self.rationsCount = QLineEdit(self)
        self.rationsCount.move(335,44)
        self.rationsCount.setFixedWidth(25)
        
        #Feet of rope
        ropeLabel = QLabel('Feet of Rope',self)
        ropeLabel.move(365,68)
        self.ropeCount = QLineEdit(self)
        self.ropeCount.move(335,66)
        self.ropeCount.setFixedWidth(25)
        
        #Not currently functioning, opens blank window
        self.sw = None
        self.buyButton = QPushButton(self)
        self.buyButton.move(300,300)
        self.buyButton.setIcon(QIcon('icons/coinpurse'))
        self.buyButton.clicked.connect(self.openStoreWindow)
    
    #Following buttons allow users to expand and shrink size of inventory    
    def miscAddRow(self):
        self.miscInventoryEntry.insertRow(1)
        
    def miscRemoveRow(self):
        self.miscInventoryEntry.removeRow(1)
        
    def weapAddRow(self):
        self.weapInventoryEntry.insertRow(1)
        
    def weapRemoveRow(self):
        self.weapInventoryEntry.removeRow(1)
        
    def armoAddRow(self):
        self.armoInventoryEntry.insertRow(1)
    
    def armoRemoveRow(self):
        self.armoInventoryEntry.removeRow(1)
        
    def openStoreWindow(self):
        if self.sw is None:
            self.sw = storeWindow()
        self.sw.show()
        
class storeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Store')
        self.setGeometry(600,80,490,630)
        self.miscStore = QListWidget(self)
        self.miscStore.move(10,10)
            
class magicTab(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
dnd5eSheet = mainWindow()
dnd5eSheet.show()
app.exec()