#! /usr/bin/env python
from scramblr import scramblr
from pyg_latin import pyg_latin
def init():
    menu()
    selection = raw_input('B===D:')
    if selection == '1':
        scramblr.loop()
    elif selection == '2':
        pyg_latin.loop()



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
                         (   \'
                          \   \
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
    ==============================================
    """
    print welcome_msg
init()
