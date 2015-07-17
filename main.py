#! /usr/bin/env python
from scramblr import scramblr
from pyg_latin import pyg_latin
from rain import rain
def init():
    menu()
    selection = raw_input('B===D:')
    if selection == '1':
        scramblr.loop()
    elif selection == '2':
        pyg_latin.loop()
    elif selection == '3':
        rows = int(raw_input('Number of rows:'))
        columns = int(raw_input('Number of columns:'))
        rain.rain(rows,columns)





def menu():
    welcome_msg = """
    =============================================
                    pRoG wElcoMEs yoU
                  {\       _____     ,
                 {* \     (*~*~*)   /}
                { ~ *\    ////^^\  /~}
                {*    \  (((/ 6 6 / *}
                {  * ~ \ )))c  = )*  }
                 {*   * ////'_/~` ~ }
                  {~ * (((( `.`\ *}' .:.
                   `{.~ )))`\ \))_.-:<*>:-
                      `{ (() `\_.-'` `:'
                        `)/ `. |
                         (    \'
                          \    \
                      _  __`\   |
                    |` `'   ``Y  ;
                    | /``-../  /
                    `'      | /
                            / `-._
                            `-----'
    Written by bbalingit and cloudyhls 4 the lulz
    ==============================================
    """
    menu="""
    =============================================
    Avalible applications:

    1. PyG Latin
    2. scramblr
    3. Asian Rains
    ==============================================
    """
    print welcome_msg
init()
