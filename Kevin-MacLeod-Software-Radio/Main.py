#!/usr/bin/python3
# Kevin MacLeod software radio client
# SPDX-License: GPL3
# Import section
import os
import random
""" NOTE
This radio is for use within video games that have a radio present (such as Grand Theft Auto)
It is a radio of royalty-free music. So long as you do not remove Kevin Macleods name, it is
completely fine to use.
"""
''' NEW FEATURES TODO
CHOOSE A RANDOM STATION
CHOOSE A RANDOM SONG
SONG LISTING
VLC SUPPORT
NATIVE OGG RENDERING
NATIVE MP3 RENDERING
NATIVE PNG RENDERING OF ALBUM ART
ALBUM PLAYERS
RADIO INTERFACE (CLI)
RADIO INTERFACE (GUI)
PORT TO OTHER LANGUAGES (AppleScript, C, C#, Vala, D, HTML5, Rust, Google Go, Julia, Red, Racket, Perl, Scheme, etc.)
'''
# Misc Variables
languageCurrent = str("English (USA)")
''' Supported languages
Arabic
Armenian
Amharic
Afrikaans
Belarusian
Bulgarian
Chinese (Traditional)
Chinese (Simplified)
Czech
Catalan
Danish
Dutch
English (USA)
English (UK)
Esperanto
French
Finnish
German
Greek
Hebrew
Icelandic
Japanese
Korean (South)
Korean (North)
Lithuanian
Macedonian
Norwegian
Odia
Persian
Polish
Punjabi
Russian
Swedish
Slovak
Slovenian
Spanish (Mexico)
Spanish (Spain)
Turkish
Thai
Telugu
Ukrainian
Uzbek
Vietnamese
Welsh
Walloon
Xhosa
Yiddish
Zulu
'''
audioPrefFormat = str("MP3")
albumDiscographyEnUSA-array = ["Action Cuts", "Anamalie", "Aspiring", "Atlantean Twilight", "Bitter Suite", "Calming", "Carpe Diem", "Cephalopod", "Christmas!", "Comedy Scoring", "Danse Macabre", "Dark Continent", "Darkness", "Dark World", "Destruction Device", "Disco Ultralounge", "Dream Catcher", "Elona MP3 Pack", "Ethereal", "Ever Mindful", "Exhilarate", "Experimental", "Falcon Banner", "Famous Classics", "Ferret", "Film Noire", "Final Battle", "Funkorama", "Garden Music", "Ghostpocalypse", "Groovy", "Happyrock", "Hard Electronic", "Healing", "Horror Soundscapes", "Impact", "Laserpack", "Latinesque", "Light Electronic", "Maccary Bay", "Madness and Paranoia", "Mad Pianist", "Magic Scout- A Calm Experience", "Medium Electronic", "Mesmerize", "Miami Nights", "Mystery", "Mystic Force", "Netherworld Shanty", "Oddities", "Organic Meditations", "Ossuary", "Pixelland", "Polka! Polka! Polka!", "Primal Drive", "PsychoKiller", "Rains Will Fall", "Reggae & Ska", "Reunited", "Rollin’ at 5", "Romance", "Royalty Free", "Sadness", "Shadowlands", "Sheep Reliability", "Silent Film- Dark Collection", "Silent Film- Light Collection", "Somewhere Sunny", "Spirit", "Spring Chicken", "Supernatural Haunting", "Take the Lead", "Teh Jazzes", "Tenebrous Brothers Carnival", "Thatched Villagers", "The Ambient", "The Descent", "Touching Moments", "Tranquility 5", "Traveller", "Utility", "Vadodara", "Vicious", "video Classica", "Virtutes Instrumenti", "Wonders", "]
station1-Songs-MP3 = [""]
station1-Songs-OGG = [""]
station1-Songs-ALL = [""]
station2-Songs-MP3 = [""]
station2-Songs-OGG = [""]
station2-Songs-ALL = [""]
station3-Songs-MP3 = [""]
station3-Songs-OGG = [""]
station3-Songs-ALL = [""]
station4-Songs-MP3 = [""]
station4-Songs-OGG = [""]
station4-Songs-ALL = [""]
station5-Songs-MP3 = [""]
station5-Songs-OGG = [""]
station5-Songs-ALL = [""]
station6-Songs-MP3 = [""]
station6-Songs-OGG = [""]
station6-Songs-ALL = [""]
station7-Songs-MP3 = [""]
station7-Songs-OGG = [""]
station7-Songs-ALL = [""]
station8-Songs-MP3 = [""]
station8-Songs-OGG = [""]
station8-Songs-ALL = [""]
station9-Songs-MP3 = [""]
station9-Songs-OGG = [""]
station9-Songs-ALL = [""]
station10-Songs-MP3 = [""]
station10-Songs-OGG = [""]
station10-Songs-ALL = [""]
station11-Songs-MP3 = [""]
station11-Songs-OGG = [""]
station11-Songs-ALL = [""]
station12-Songs-MP3 = [""]
station12-Songs-OGG = [""]
station12-Songs-ALL = [""]
station13-Songs-MP3 = [""]
station13-Songs-OGG = [""]
station13-Songs-ALL = [""]
station14-Songs-MP3 = [""]
station14-Songs-OGG = [""]
station14-Songs-ALL = [""]
station15-Songs-MP3 = [""]
station15-Songs-OGG = [""]
station15-Songs-ALL = [""]
station16-Songs-MP3 = [""]
station16-Songs-OGG = [""]
station16-Songs-ALL = [""]
station17-Songs-MP3 = [""]
station17-Songs-OGG = [""]
station17-Songs-ALL = [""]
station18-Songs-MP3 = [""]
station18-Songs-OGG = [""]
station18-Songs-ALL = [""]
station19-Songs-MP3 = [""]
station19-Songs-OGG = [""]
station19-Songs-ALL = [""]
station20-Songs-MP3 = [""]
station20-Songs-OGG = [""]
station20-Songs-ALL = [""]
station21-Songs-MP3 = [""]
station21-Songs-OGG = [""]
station21-Songs-ALL = [""]
station22-Songs-MP3 = [""]
station22-Songs-OGG = [""]
station22-Songs-ALL = [""]
station23-Songs-MP3 = [""]
station23-Songs-OGG = [""]
station23-Songs-ALL = [""]
station24-Songs-MP3 = [""]
station24-Songs-OGG = [""]
station24-Songs-ALL = [""]
station25-Songs-MP3 = [""]
station25-Songs-OGG = [""]
station25-Songs-ALL = [""]
station26-Songs-MP3 = [""]
station26-Songs-OGG = [""]
station26-Songs-ALL = [""]
station27-Songs-MP3 = [""]
station27-Songs-OGG = [""]
station27-Songs-ALL = [""]
station28-Songs-MP3 = [""]
station28-Songs-OGG = [""]
station28-Songs-ALL = [""]
station29-Songs-MP3 = [""]
station29-Songs-OGG = [""]
station29-Songs-ALL = [""]
station30-Songs-MP3 = [""]
station30-Songs-OGG = [""]
station30-Songs-ALL = [""]
station31-Songs-MP3 = [""]
station31-Songs-OGG = [""]
station31-Songs-ALL = [""]
station32-Songs-MP3 = [""]
station32-Songs-OGG = [""]
station32-Songs-ALL = [""]
station33-Songs-MP3 = [""]
station33-Songs-OGG = [""]
station33-Songs-ALL = [""]
station34-Songs-MP3 = [""]
station34-Songs-OGG = [""]
station34-Songs-ALL = [""]
station35-Songs-MP3 = [""]
station35-Songs-OGG = [""]
station35-Songs-ALL = [""]
station36-Songs-MP3 = [""]
station36-Songs-OGG = [""]
station36-Songs-ALL = [""]
station37-Songs-MP3 = [""]
station37-Songs-OGG = [""]
station37-Songs-ALL = [""]
station38-Songs-MP3 = [""]
station38-Songs-OGG = [""]
station38-Songs-ALL = [""]
station39-Songs-MP3 = [""]
station39-Songs-OGG = [""]
station39-Songs-ALL = [""]
station40-Songs-MP3 = [""]
station40-Songs-OGG = [""]
station40-Songs-ALL = [""]
station41-Songs-MP3 = [""]
station41-Songs-OGG = [""]
station41-Songs-ALL = [""]
station42-Songs-MP3 = [""]
station42-Songs-OGG = [""]
station42-Songs-ALL = [""]
station43-Songs-MP3 = [""]
station43-Songs-OGG = [""]
station43-Songs-ALL = [""]
station44-Songs-MP3 = [""]
station44-Songs-OGG = [""]
station44-Songs-ALL = [""]
station45-Songs-MP3 = [""]
station45-Songs-OGG = [""]
station45-Songs-ALL = [""]
station46-Songs-MP3 = [""]
station46-Songs-OGG = [""]
station46-Songs-ALL = [""]
station47-Songs-MP3 = [""]
station47-Songs-OGG = [""]
station47-Songs-ALL = [""]
station48-Songs-MP3 = [""]
station48-Songs-OGG = [""]
station48-Songs-ALL = [""]
station49-Songs-MP3 = [""]
station49-Songs-OGG = [""]
station49-Songs-ALL = [""]
station50-Songs-MP3 = [""]
station50-Songs-OGG = [""]
station50-Songs-ALL = [""]
station51-Songs-MP3 = [""]
station51-Songs-OGG = [""]
station51-Songs-ALL = [""]
station52-Songs-MP3 = [""]
station52-Songs-OGG = [""]
station52-Songs-ALL = [""]
station53-Songs-MP3 = [""]
station53-Songs-OGG = [""]
station53-Songs-ALL = [""]
station54-Songs-MP3 = [""]
station54-Songs-OGG = [""]
station54-Songs-ALL = [""]
station55-Songs-MP3 = [""]
station55-Songs-OGG = [""]
station55-Songs-ALL = [""]
station56-Songs-MP3 = [""]
station56-Songs-OGG = [""]
station56-Songs-ALL = [""]
station57-Songs-MP3 = [""]
station57-Songs-OGG = [""]
station57-Songs-ALL = [""]
station58-Songs-MP3 = [""]
station58-Songs-OGG = [""]
station58-Songs-ALL = [""]
station59-Songs-MP3 = [""]
station59-Songs-OGG = [""]
station59-Songs-ALL = [""]
station60-Songs-MP3 = [""]
station60-Songs-OGG = [""]
station60-Songs-ALL = [""]
station61-Songs-MP3 = [""]
station61-Songs-OGG = [""]
station61-Songs-ALL = [""]
station62-Songs-MP3 = [""]
station62-Songs-OGG = [""]
station62-Songs-ALL = [""]
station63-Songs-MP3 = [""]
station63-Songs-OGG = [""]
station63-Songs-ALL = [""]
station64-Songs-MP3 = [""]
station64-Songs-OGG = [""]
station64-Songs-ALL = [""]
station65-Songs-MP3 = [""]
station65-Songs-OGG = [""]
station65-Songs-ALL = [""]
station66-Songs-MP3 = [""]
station66-Songs-OGG = [""]
station66-Songs-ALL = [""]
station67-Songs-MP3 = [""]
station67-Songs-OGG = [""]
station67-Songs-ALL = [""]
station68-Songs-MP3 = [""]
station68-Songs-OGG = [""]
station68-Songs-ALL = [""]
station69-Songs-MP3 = [""]
station69-Songs-OGG = [""]
station69-Songs-ALL = [""]
station70-Songs-MP3 = [""]
station70-Songs-OGG = [""]
station70-Songs-ALL = [""]
station71-Songs-MP3 = [""]
station71-Songs-OGG = [""]
station71-Songs-ALL = [""]
station72-Songs-MP3 = [""]
station72-Songs-OGG = [""]
station72-Songs-ALL = [""]
station73-Songs-MP3 = [""]
station73-Songs-OGG = [""]
station73-Songs-ALL = [""]
station74-Songs-MP3 = [""]
station74-Songs-OGG = [""]
station74-Songs-ALL = [""]
station75-Songs-MP3 = [""]
station75-Songs-OGG = [""]
station75-Songs-ALL = [""]
station76-Songs-MP3 = [""]
station76-Songs-OGG = [""]
station76-Songs-ALL = [""]
station77-Songs-MP3 = [""]
station77-Songs-OGG = [""]
station77-Songs-ALL = [""]
station78-Songs-MP3 = [""]
station78-Songs-OGG = [""]
station78-Songs-ALL = [""]
station79-Songs-MP3 = [""]
station79-Songs-OGG = [""]
station79-Songs-ALL = [""]
station80-Songs-MP3 = [""]
station80-Songs-OGG = [""]
station80-Songs-ALL = [""]
station81-Songs-MP3 = [""]
station81-Songs-OGG = [""]
station81-Songs-ALL = [""]
station82-Songs-MP3 = [""]
station82-Songs-OGG = [""]
station82-Songs-ALL = [""]
station83-Songs-MP3 = [""]
station83-Songs-OGG = [""]
station83-Songs-ALL = [""]
station84-Songs-MP3 = [""]
station84-Songs-OGG = [""]
station84-Songs-ALL = [""]
station85-Songs-MP3 = [""]
station85-Songs-OGG = [""]
station85-Songs-ALL = [""]
station86-Songs-MP3 = [""]
station86-Songs-OGG = [""]
station86-Songs-ALL = [""]
""" TODO
List all songs in the arrays
"""
# Functions
def client():
    print(str(titleText) + "\n")
    print(str(leadTxt) + "\n")
    optionConsole = str(input(":"))
    optionConsole.upper()
    if (optionConsole == "O" or "SETTINGS"):
        return settings()
        break
    elif (optionConsole == "S" or "STATIONS"):
        return stationSelect()
        break
    elif (optionConsole == "Q" or "QUIT" or "EXIT" or "END"):
        return quit1()
        break
    else:
        print(str(invalidLeadOptionTxt))
        return clientRestart()
        break 
    # break
def clientRestart():
    return client()
    break
def englishSetup1():
    '''
    Each string is initialized this way, so that injection scripts can easily change the language
    to the preferred language of the listener. The default language is English (USA)
    '''
    titleText = "Kevin MacLeod software radio"
    leadTxt = "Choose an option:\nSettings (O) Stations (S) Quit (Q)"
    audioPrefTxt1 = "Audio preference:"
    audioPrefTxt2 = "MP3 (M) | OGG (O) | Any (A)"
    enterCodeTxt = "Enter a letter to continue: "
    codeInvalidAudioTxt = "Invalid code. Please enter a letter M, O, or A"
    radioStationSelectTxt = "Select a radio station: \n"
    exitTxt = "Press [ENTER] key to quit"
    stationListingTxt = "Action Cuts\nAnamalie\nAspiring\nAtlantean Twilight\nBitter Suite\nCalming\nCarpe Diem\nCephalopod\nChristmas!\nComedy Scoring\nDanse Macabre\nDark Continent\nDarkness\nDark World\nDestruction Device\nDisco Ultralounge\nDream Catcher\nElona MP3 Pack\nEthereal\nEver Mindful\nExhilarate\nExperimental\nFalcon Banner\nFamous Classics\nFerret\nFilm Noire\nFinal Battle\nFunkorama\nGarden Music\nGhostpocalypse\nGroovy\nHappyrock\nHard Electronic\nHealing\nHorror Soundscapes\nImpact\nLaserpack\nLatinesque\nLight Electronic\nMaccary Bay\nMadness and Paranoia\nMad Pianist\nMagic Scout- A Calm Experience\nMedium Electronic\nMesmerize\nMiami Nights\nMystery\nMystic Force\nNetherworld Shanty\nOddities\nOrganic Meditations\nOssuary\nPixelland\nPolka! Polka! Polka!\nPrimal Drive\nPsychoKiller\nRains Will Fall\nReggae & Ska\nReunited\nRollin’ at 5\nRomance\nRoyalty Free\nSadness\nShadowlands\nSheep Reliability\nSilent Film- Dark Collection\nSilent Film- Light Collection\nSomewhere Sunny\nSpirit\nSpring Chicken\nSupernatural Haunting\nTake the Lead\nTeh Jazzes\nTenebrous Brothers Carnival\nThatched Villagers\nThe Ambient\nThe Descent\nTouching Moments\nTranquility 5\nTraveller\nUtility\nVadodara\nVicious\nvideo Classica\nVirtutes Instrumenti\nWonders\n"
    station1Txt = "Action Cuts"
    station2Txt = "Anamalie"
    station3Txt = "Aspiring"
    station4Txt = "Atlantean Twilight"
    station5Txt = "Bitter Suite"
    station6Txt = "Calming"
    station7Txt = "Carpe Diem"
    station8Txt = "Cephalopod"
    station9Txt = "Christmas!"
    station10Txt = "Comedy Scoring"
    station11Txt = "Danse Macabre"
    station12Txt = "Dark Continent"
    station13Txt = "Darkness"
    station14Txt = "Dark World"
    station15Txt = "Destruction Device"
    station16Txt = "Disco Ultralounge"
    station17Txt = "Dream Catcher"
    station18Txt = "Elona MP3 Pack"
    station19Txt = "Ethereal"
    station20Txt = "Ever Mindful"
    station21Txt = "Exhilarate"
    station22Txt = "Experimental"
    station23Txt = "Falcon Banner"
    station24Txt = "Famous Classics"
    station25Txt = "Ferret"
    station26Txt = "Film Noire"
    station27Txt = "Final Battle"
    station28Txt = "Funkorama"
    station29Txt = "Garden Music"
    station30Txt = "Ghostpocalypse"
    station31Txt = "Groovy"
    station32Txt = "Happyrock"
    station33Txt = "Hard Electronic"
    station34Txt = "Healing"
    station35Txt = "Horror Soundscapes"
    station36Txt = "Impact"
    station37Txt = "Laserpack"
    station38Txt = "Latinesque"
    station39Txt = "Light Electronic"
    station40Txt = "Maccary Bay"
    station41Txt = "Madness and Paranoia"
    station42Txt = "Mad Pianist"
    station43Txt = "Magic Scout- A Calm Experience"
    station44Txt = "Medium Electronic"
    station45Txt = "Mesmerize"
    station46Txt = "Miami Nights"
    station47Txt = "Mystery"
    station48Txt = "Mystic Force"
    station49Txt = "Netherworld Shanty"
    station50Txt = "Oddities"
    station51Txt = "Organic Meditations"
    station52Txt = "Ossuary"
    station53Txt = "Pixelland"
    station54Txt = "Polka! Polka! Polka!"
    station55Txt = "Primal Drive"
    station56Txt = "PsychoKiller"
    station57Txt = "Rains Will Fall"
    station58Txt = "Reggae & Ska"
    station59Txt = "Reunited"
    station60Txt = "Rollin’ at 5"
    station61Txt = "Romance"
    station62Txt = "Royalty Free"
    station63Txt = "Sadness"
    station64Txt = "Shadowlands
    station65Txt = "Sheep Reliability"
    station66Txt = "Silent Film- Dark Collection"
    station67Txt = "Silent Film- Light Collection"
    station68Txt = "Somewhere Sunny"
    station69Txt = "Spirit"
    station70Txt = "Spring Chicken"
    station71Txt = "Supernatural Haunting"
    station72Txt = "Take the Lead"
    station73Txt = "Teh Jazzes"
    station74Txt = "Tenebrous Brothers Carnival"
    station75Txt = "Thatched Villagers"
    station76Txt = "The Ambient"
    station77Txt = "The Descent"
    station78Txt = "Touching Moments"
    station79Txt = "Tranquility 5"
    station80Txt = "Traveller"
    station81Txt = "Utility"
    station82Txt = "Vadodara"
    station83Txt = "Vicious"
    station84Txt = "video Classica"
    station85Txt = "Virtutes Instrumenti"
    station86Txt = "Wonders"
    break
def languageSetup():
    if (languageCurrent == "English (USA)"):
        return englishSetup1()
        break
    elif (languageCurrent == "English (UK)"):
        return englishSetup2()
        break
    else (languageCurrent != "English (USA)" or "English (UK)"):
        languageCurrent == "English (USA)"
        return clientRestart()
        break
def main():
    return languageSetup()
    break
def quit1():
    noMore = input(str(exitTxt))
    break
def stationSelect():
    print(str(stationListingTxt) + "\n")
    optionConsole2 = str(input(":"))
    optionConsole2.upper()
    
    if (optionConsole2 == 1
    
    
    break
def settings():
    print(str(audioPrefTxt1) + "\n" + str(audioPrefTxt2) + "\n")
    getAudioPrefIn = str(input(str(enterCodeTxt)))
    getAudioPrefIn.upper()
    if (getAudioPrefIn == "M" or "MP3"):
        audioPrefFormat == "MP3"
        break
    elif (getAudioPrefIn == "O" or "OGG"):
        audioPrefFormat == "OGG"
        break
    elif (getAudioPrefIn == "A" or "ANY"):
        audioPrefFormat == "ANY"
        break
    else
        print(str(codeInvalidAudioTxt))
        return settings()
        break
# Program
return main()
break
# End
""" File info
File version: 1 (2023, Friday, October 20th at 11:39 am PST)
File type: Python source file (*.py)
Line count (including blank lines and compiler line): 516
"""

