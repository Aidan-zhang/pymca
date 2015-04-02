#/*##########################################################################
# Copyright (C) 2004-2014 V.A. Sole, European Synchrotron Radiation Facility
#
# This file is part of the PyMca X-ray Fluorescence Toolkit developed at
# the ESRF by the Software group.
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This file is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Please contact the ESRF industrial unit (industry@esrf.fr) if this license
# is a problem for you.
#
#############################################################################*/
__author__ = "V.A. Sole - ESRF Data Analysis"
__contact__ = "sole@esrf.fr"
__license__ = "LGPL2+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
cursor_closedhand = [
"16 16 3 1",
"  c black",
". c gray100",
"X c None",
"XXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXX",
"XXXX  X  X  XXXX",
"XXX .. .. ..  XX",
"XXX ........ . X",
"XXXX ......... X",
"XXX  ......... X",
"XX ........... X",
"XX .......... XX",
"XXX ......... XX",
"XXXX ....... XXX",
"XXXXX ...... XXX",
"XXXXX ...... XXX",
"XXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXX"
]

cursor_normal = [
"16 16 4 1",
"  c #303030",
". c #dcdcdc",
"X c #ffffff",
"o c None",
"oooooooooooooooo",
"o   oooooooooooo",
"o      ooooooooo",
"o         oooooo",
"oX       ooooooo",
"oX      oooooooo",
"oX      oooooooo",
"oXX      ooooooo",
"ooX  XX   oooooo",
"ooX XooX   ooooo",
"ooXXooooX   oooo",
"oooooooooX   ooo",
"ooooooooooX  ooo",
"oooooooooooooooo",
"oooooooooooooooo",
"oooooooooooooooo"
]

cursor_openhand =[
"16 16 3 1",
"  c black",
". c gray100",
"X c None",
"XXXXXXX  XXXXXXX",
"XXX  X ..   XXXX",
"XX ..  .. .. XXX",
"XX ..  .. .. X X",
"XXX .. .. ..  . ",
"XXX .. .. .. .. ",
"X  . ....... .. ",
" ..  .......... ",
" ... ......... X",
"X ............ X",
"XX ........... X",
"XX .......... XX",
"XXX ......... XX",
"XXXX ....... XXX",
"XXXXX ...... XXX",
"XXXXXXXXXXXXXXXX"
]

cursor_pointinghand = [
"25 25 3 1",
"  c black",
". c gray100",
"X c None",
"XXXXXXXXX..XXXXXXXXXXXXXX",
"XXXXXXXX.  .XXXXXXXXXXXXX",
"XXXXXXXX .. XXXXXXXXXXXXX",
"XXXXXXXX .. XXXXXXXXXXXXX",
"XXXXXXXX .. XXXXXXXXXXXXX",
"XXXXXXXX .. XXXXXXXXXXXXX",
"XXXXXXXX .. XXXXXXXXXXXXX",
"XXXXXXXX ..   XXXXXXXXXXX",
"XXXXXXXX .. ..   XXXXXXXX",
"XXXXXXXX .. .. ..  XXXXXX",
"XXXXX  X .. .. .. . XXXXX",
"XXXX ..  .. .. .. . XXXXX",
"XXXX ... .......... XXXXX",
"XXXXX ............. XXXXX",
"XXXXXX ............ XXXXX",
"XXXXXX ............ XXXXX",
"XXXXXXX .......... XXXXXX",
"XXXXXXX .......... XXXXXX",
"XXXXXXXX ........ XXXXXXX",
"XXXXXXXX ........ XXXXXXX",
"XXXXXXXX          XXXXXXX",
"XXXXXXXX          XXXXXXX",
"XXXXXXXX          XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

cursor_sizeall = [
"25 25 3 1",
"  c black",
". c white",
"X c None",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXX....XXXXXXXXXXX",
"XXXXXXXXX..  ..XXXXXXXXXX",
"XXXXXXXX..    ..XXXXXXXXX",
"XXXXXXX..      ..XXXXXXXX",
"XXXXXXX.        .XXXXXXXX",
"XXXXX..XXXX  XXXX..XXXXXX",
"XXXX.. XXXX  XXXX ..XXXXX",
"XXX..  XXXX  XXXX  ..XXXX",
"XX..   XXXX  XXXX   ..XXX",
"XX.                  .XXX",
"XX.                  .XXX",
"XX..   XXXX  XXXX   ..XXX",
"XXX..  XXXX  XXXX  ..XXXX",
"XXXX.. XXXX  XXXX ..XXXXX",
"XXXXX..XXXX  XXXX..XXXXXX",
"XXXXXXX.        .XXXXXXXX",
"XXXXXXX..      ..XXXXXXXX",
"XXXXXXXX..    ..XXXXXXXXX",
"XXXXXXXXX..  ..XXXXXXXXXX",
"XXXXXXXXXX....XXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

cursor_what = [
"16 16 3 1",
" 	c None",
"o	c #000000",
"a	c #000080",
"o        aaaaa  ",
"oo      aaa aaa ",
"ooo    aaa   aaa",
"oooo   aa     aa",
"ooooo  aa     aa",
"oooooo  a    aaa",
"ooooooo     aaa ",
"oooooooo   aaa  ",
"ooooooooo aaa   ",
"ooooo     aaa   ",
"oo ooo          ",
"o  ooo    aaa   ",
"    ooo   aaa   ",
"    ooo         ",
"     ooo        ",
"     ooo        "
]




image_cubeBo_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###a..............####.",
"........###aa.............#####.",
".......###.aa............###.##.",
"......###..aa...........###..##.",
".....###...aa..........###...##.",
"....###....aa.........###....##.",
"...###.....aa........###.....##.",
"..#####################......##.",
".#####################.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aa.......##.......##.",
".##........aaaaaaaaa##aaaaaa###.",
".##.......aaaaaaaaaa##aaaaa###..",
".##......aaabbbbbbbb##bbbb###...",
".##.....aaabbbbbbbbb##bbb###....",
".##....aaabbbbbbbbbb##bb###.....",
".##...aaabbbbbbbbbbb##b###......",
".##..aaabbbbbbbbbbbb#####.......",
".##.aaabbbbbbbbbbbbb####........",
".##aaabbbbbbbbbbbbbb###.........",
".#####################..........",
".####################...........",
"................................"
]
image_cubeR_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###a..............####.",
"........###aa.............#####.",
".......###.aa............###b##.",
"......###..aa...........###bb##.",
".....###...aa..........###bbb##.",
"....###....aa.........###bbbb##.",
"...###.....aa........###bbbbb##.",
"..#####################bbbbbb##.",
".#####################bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aa.......##bbbbbbb##.",
".##........aaaaaaaaa##bbbbbb###.",
".##.......aaaaaaaaaa##bbbbb###..",
".##......aaa........##bbbb###...",
".##.....aaa.........##bbb###....",
".##....aaa..........##bb###.....",
".##...aaa...........##b###......",
".##..aaa............#####.......",
".##.aaa.............####........",
".##aaa..............###.........",
".#####################..........",
".####################...........",
"................................"
]
image_cubeT_data = [
"32 32 4 1",
". c None",
"# c #000000",
"a c #0080ff",
"b c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###aaaaaaaaaaaaaaa####.",
"........###aaaaaaaaaaaaaaa#####.",
".......###aaaaaaaaaaaaaaa###.##.",
"......###aaaaaaaaaaaaaaa###..##.",
".....###aaaaaaaaaaaaaaa###...##.",
"....###aaaaaaaaaaaaaaa###....##.",
"...###aaaaaaaaaaaaaaa###.....##.",
"..#####################......##.",
".#####################.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bb.......##.......##.",
".##........bbbbbbbbb##bbbbbb###.",
".##.......bbbbbbbbbb##bbbbb###..",
".##......bbb........##....###...",
".##.....bbb.........##...###....",
".##....bbb..........##..###.....",
".##...bbb...........##.###......",
".##..bbb............#####.......",
".##.bbb.............####........",
".##bbb..............###.........",
".#####################..........",
".####################...........",
"................................"
]
image_cubeL_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###a..............####.",
"........###aa.............#####.",
".......###baa............###.##.",
"......###bbaa...........###..##.",
".....###bbbaa..........###...##.",
"....###bbbbaa.........###....##.",
"...###bbbbbaa........###.....##.",
"..#####################......##.",
".#####################.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaa.......##.......##.",
".##bbbbbbbbaaaaaaaaa##aaaaaa###.",
".##bbbbbbbaaaaaaaaaa##aaaaa###..",
".##bbbbbbaaa........##....###...",
".##bbbbbaaa.........##...###....",
".##bbbbaaa..........##..###.....",
".##bbbaaa...........##.###......",
".##bbaaa............#####.......",
".##baaa.............####........",
".##aaa..............###.........",
".#####################..........",
".####################...........",
"................................"
]
image_cubeBa_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###abbbbbbbbbbbbbb####.",
"........###aabbbbbbbbbbbbb#####.",
".......###.aabbbbbbbbbbbb###b##.",
"......###..aabbbbbbbbbbb###bb##.",
".....###...aabbbbbbbbbb###bbb##.",
"....###....aabbbbbbbbb###bbbb##.",
"...###.....aabbbbbbbb###bbbbb##.",
"..#####################bbbbbb##.",
".#####################bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aabbbbbbb##bbbbbbb##.",
".##........aaaaaaaaa##aaaaaa###.",
".##.......aaaaaaaaaa##aaaaa###..",
".##......aaa........##....###...",
".##.....aaa.........##...###....",
".##....aaa..........##..###.....",
".##...aaa...........##.###......",
".##..aaa............#####.......",
".##.aaa.............####........",
".##aaa..............###.........",
".#####################..........",
".####################...........",
"................................"
]
image_cubeF_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###a..............####.",
"........###aa.............#####.",
".......###.aa............###.##.",
"......###..aa...........###..##.",
".....###...aa..........###...##.",
"....###....aa.........###....##.",
"...###.....aa........###.....##.",
"..#####################......##.",
".#####################.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##.......##.",
".##bbbbbbbbbbbbbbbbb##aaaaaa###.",
".##bbbbbbbbbbbbbbbbb##aaaaa###..",
".##bbbbbbbbbbbbbbbbb##....###...",
".##bbbbbbbbbbbbbbbbb##...###....",
".##bbbbbbbbbbbbbbbbb##..###.....",
".##bbbbbbbbbbbbbbbbb##.###......",
".##bbbbbbbbbbbbbbbbb#####.......",
".##bbbbbbbbbbbbbbbbb####........",
".##bbbbbbbbbbbbbbbbb###.........",
".#####################..........",
".####################...........",
"................................"
]

image_cube45_data = [
"32 32 4 1",
". c None",
"# c #000000",
"b c #0080ff",
"a c #585858",
"................................",
"...........####################.",
"..........#####################.",
".........###abbbbbbbbbbbbbb####.",
"........###aabbbbbbbbbbbbb#####.",
".......###baabbbbbbbbbbbb###b##.",
"......###bbaabbbbbbbbbbb###bb##.",
".....###bbbaabbbbbbbbbb###bbb##.",
"....###bbbbaabbbbbbbbb###bbbb##.",
"...###bbbbbaabbbbbbbb###bbbbb##.",
"..#####################bbbbbb##.",
".#####################bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaabbbbbbb##bbbbbbb##.",
".##bbbbbbbbaaaaaaaaa##aaaaaa###.",
".##bbbbbbbaaaaaaaaaa##aaaaa###..",
".##bbbbbbaaabbbbbbbb##bbbb###...",
".##bbbbbaaabbbbbbbbb##bbb###....",
".##bbbbaaabbbbbbbbbb##bb###.....",
".##bbbaaabbbbbbbbbbb##b###......",
".##bbaaabbbbbbbbbbbb#####.......",
".##baaabbbbbbbbbbbbb####........",
".##aaabbbbbbbbbbbbbb###.........",
".#####################..........",
".####################...........",
"................................"
]

image_scene_data = [
"22 22 5 1",
". c None",
"b c #0000ff",
"v c #00ff00",
"j c #00ffff",
"g c #ffffff",
"......................",
"......................",
".........gggg.........",
".......gggggggg.......",
".....bbbggbbbgggb.....",
"....bbbbbbbbbvbbbb....",
"...bbvvvbbbbbvvbbbb...",
"..bbbbvvvbbbvvvbbbbb..",
"..bbbbbbbbbbvvvvbbbb..",
".bbbbbbbbbbbbvvvbbbbb.",
".bbbvvvvbbbbbvvbbbbbb.",
".bbbvvvvvbbbbvvvbbbbb.",
".bbbbbvvvbbbbvbbbbbbb.",
"..bbbbbvbvbbvvbbbbbb..",
"..bbbbbbvbbbvvvvvvbb..",
"...bbbbbbbbvvvvvbvb...",
"....bbbbbbbbvvvvvv....",
".....ggggggbbbbgg.....",
".......gggggggg.......",
".........gggg.........",
"......................",
"......................"
]

image_object_data = [
"22 22 7 1",
". c None",
"# c #000000",
"b c #2e2e2e",
"c c #5c5c5c",
"d c #878787",
"e c #c2c2c2",
"a c #ffffff",
"......................",
"....##########........",
"....#aaaaaaa#b#.......",
"....#aaaaaaa#cb#......",
"....#aaaaaaa#dcb#.....",
"....#aaaaaaa#edcb#....",
"....#aaaaaaa#aedcb#...",
"....#aaaaaaa#######...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....#aaaaaaaaaaaaa#...",
"....###############...",
"......................",
"......................"
]

image_zoomin_data = [
"22 22 164 2",
"Qt c None",
"#0 c #000000",
".a c #1f1f1f",
".b c #212121",
".e c #232323",
".k c #252626",
"aF c #292929",
"#6 c #2b2d2d",
"am c #2d2d2e",
"aa c #323333",
"as c #343434",
".E c #373737",
"ax c #3a3a3b",
".l c #3c3d3d",
".t c #3c3e3d",
"aC c #454546",
"aG c #464646",
"#I c #46a7b1",
"#N c #474747",
"aB c #484848",
"ac c #485050",
".u c #494949",
"#T c #4bacb5",
"#w c #4cb6bf",
"#H c #4cb9c4",
".P c #4d4f4f",
"ab c #4d5859",
"#Y c #515453",
"a# c #515555",
"#x c #52b0ba",
"#l c #52b3bd",
".F c #555555",
"ap c #575757",
"#S c #57b3be",
"#c c #585858",
".2 c #595959",
"#U c #5bb5bf",
"ai c #5c5c5c",
"aD c #5c5c5d",
"#k c #5cc1ce",
"ah c #5f5f60",
"#B c #5f605f",
"## c #5fbbc6",
"#v c #5fc9d4",
"#J c #62bbc5",
"ad c #636363",
"aw c #646464",
".f c #646666",
"au c #656565",
"af c #666666",
"an c #666667",
"#G c #66c5d2",
"aE c #696969",
".c c #6a6a6a",
"#R c #6cc4ce",
"at c #6d6d6e",
"#o c #6e6e6e",
".Q c #6f6f6f",
"#. c #70cad7",
".j c #717675",
"#3 c #72c3cc",
".Z c #72c6d0",
"ay c #767677",
"#2 c #76c4cc",
"az c #787878",
"#F c #79ced9",
"#j c #79d2de",
"ar c #7c7c7c",
".R c #7c7f7e",
"#u c #7ed4e0",
".# c #7f7f7f",
"#L c #7f7f80",
"ao c #828282",
".Y c #82d0db",
"#p c #848888",
"#E c #86d1dc",
"a. c #879698",
"#7 c #8a8a8a",
"#Q c #8ad0da",
".1 c #8c9697",
".M c #8cd1da",
"#1 c #8cd2da",
".9 c #8dd9e3",
".v c #8f9493",
".3 c #909594",
"#m c #90d5de",
"#z c #91a1a3",
"#y c #91d6df",
".N c #92d4dd",
"#i c #92dbe5",
"al c #939393",
"#t c #93dbe5",
"#V c #94d6de",
"ae c #959595",
"#d c #95999a",
"#a c #97d9e1",
"#X c #9c9c9c",
"#O c #9cabac",
"#n c #9cbbbf",
"#D c #9cd9e2",
"#b c #9db8bb",
"#s c #9ddee7",
".X c #9ddfe8",
"#4 c #9fdae1",
".0 c #a0dee6",
"#9 c #a1cbd1",
".m c #a2a9a8",
".D c #a2acad",
".B c #a3dce5",
"#A c #a4a4a4",
"#r c #a5dbe3",
".L c #a5e0e8",
"ag c #a8cfcf",
".8 c #a8e2ea",
"#h c #a9e3eb",
"#8 c #aad9de",
".g c #adb5b6",
".s c #adbabb",
".i c #aeb7b9",
".A c #aee3eb",
"#Z c #b0c2c3",
"#M c #b4b4b4",
"#K c #b6e4ea",
"#g c #b6e8ee",
"#5 c #b7d0d2",
"#W c #b8cbcd",
"#P c #b8e5eb",
".W c #b9e8ee",
".h c #bbc6c8",
"#f c #bce6ea",
"#C c #c1dce1",
".C c #c2e8ed",
".7 c #c2eaf0",
".K c #c2ebf0",
".z c #c6edf2",
"aA c #c8c8c8",
".O c #c8eaef",
"aj c #cacaca",
".5 c #caeef1",
"aH c #cbcbcb",
".G c #cbd6d6",
".q c #cbedf2",
"#q c #cde8eb",
".r c #cdecf1",
".6 c #cdeff2",
"aq c #d1d1d1",
".V c #d5f1f4",
".y c #d5f3f5",
".p c #d7f1f5",
"av c #d8d8d8",
".n c #d8e6e7",
"ak c #d9d9d9",
"#e c #daeef1",
".S c #dbe9eb",
".o c #dbf0f3",
".J c #ddf4f6",
".w c #dfecec",
".T c #dff5f7",
".4 c #e0f1f4",
".U c #e3f6f7",
".x c #e8f7f9",
".H c #e9f8f9",
".I c #ebfafa",
".d c #ececec",
"QtQtQtQtQt.#.a.b.a.c.dQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.e.f.g.h.i.j.kQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQt.l.m.n.o.p.q.r.s.tQtQtQtQtQtQtQtQtQtQt",
"QtQt.u.v.w.x.y.z.A.B.C.D.EQtQtQtQtQtQtQtQtQt",
"QtQt.F.G.H.I.J.K.L.M.N.O.PQtQtQtQtQtQtQtQtQt",
"Qt.Q.R.S.T.U.V.W.X.Y.Z.0.1.2QtQtQtQtQtQtQtQt",
"Qt.Q.3.4.5.6.7.8.9#.###a#b#cQtQtQtQtQtQtQtQt",
"Qt.Q#d#e#f#g#h#i#j#k#l#m#n#cQtQtQtQtQtQtQtQt",
"Qt#o#p#q#r#s#t#u#v#w#x#y#z#cQtQtQtQtQtQtQtQt",
"Qt#A#B#C#D#E#F#G#H#I#J#K#L#MQtQtQtQtQtQtQtQt",
"QtQt#N#O#P#Q#R#S#T#U#V#W#L#LQtQtQtQtQtQtQtQt",
"QtQt#X#Y#Z#0#1#2#3#4#5.f#6#LQtQtQtQtQtQtQtQt",
"QtQtQt#7#0#0#0#8#9a.a#aa#L#L#MQtQtQtQtQtQtQt",
"QtQtQtQt#0#0#0abacadae#6#L#Laf#MQtQtQtQtQtQt",
"QtQtQtQt#0#0#0QtQtQtQtag#6ah.#aiajQtQtQtQtQt",
"Qt#0#0#0#0#0#0#0#0#0QtakalamanaoapakQtQtQtQt",
"#0#0#0#0#0#0#0#0#0#0#0QtaqarasataoauavQtQtQt",
"Qt#0#0#0#0#0#0#0#0#0QtQtQtQtawaxayazarQtQtQt",
"QtQtQtQt#0#0#0QtQtQtQtQtQtQtaAaBaCaDaEQtQtQt",
"QtQtQtQt#0#0#0QtQtQtQtQtQtQtQtaAaFaGaHQtQtQt",
"QtQtQtQt#0#0#0QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt#0QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]

image_zoomout_data = [
"22 22 169 2",
"Qt c None",
"ao c #000000",
".a c #1f1f1f",
".b c #212121",
".d c #232323",
".j c #252626",
"aK c #292929",
"#5 c #2b2d2d",
"ar c #2d2d2e",
"ac c #323333",
"ax c #343434",
".D c #373737",
"aC c #3a3a3b",
".k c #3c3d3d",
".s c #3c3e3d",
"aH c #454546",
"aL c #464646",
"#H c #46a7b1",
"#M c #474747",
"#7 c #474a4b",
"ae c #474e4f",
"aG c #484848",
"ag c #485050",
".t c #494949",
"#S c #4bacb5",
"#v c #4cb6bf",
"#G c #4cb9c4",
".O c #4d4f4f",
"af c #4d5859",
"#X c #515453",
"ab c #515555",
"#w c #52b0ba",
"#k c #52b3bd",
".E c #555555",
"au c #575757",
"#R c #57b3be",
"#b c #585858",
".1 c #595959",
"#T c #5bb5bf",
"am c #5c5c5c",
"aI c #5c5c5d",
"#j c #5cc1ce",
"al c #5f5f60",
"#A c #5f605f",
"#. c #5fbbc6",
"#u c #5fc9d4",
"#I c #62bbc5",
"ah c #636363",
"aB c #646464",
".e c #646666",
"az c #656565",
"aj c #666666",
"as c #666667",
"#F c #66c5d2",
"aJ c #696969",
".c c #6a6a6a",
"#Q c #6cc4ce",
"ad c #6d6d6d",
"ay c #6d6d6e",
"#n c #6e6e6e",
".P c #6f6f6f",
".9 c #70cad7",
".i c #717675",
"#2 c #72c3cc",
".Y c #72c6d0",
"aD c #767677",
"#1 c #76c4cc",
"aE c #787878",
"#E c #79ced9",
"#i c #79d2de",
"aw c #7c7c7c",
".Q c #7c7f7e",
"#t c #7ed4e0",
".# c #7f7f7f",
"#K c #7f7f80",
"#8 c #808e90",
"at c #828282",
".X c #82d0db",
"#o c #848888",
"#D c #86d1dc",
"aa c #879698",
"#6 c #8a8a8a",
"#P c #8ad0da",
".0 c #8c9697",
".L c #8cd1da",
"#0 c #8cd2da",
".8 c #8dd9e3",
".u c #8f9493",
".2 c #909594",
"#l c #90d5de",
"#y c #91a1a3",
"#x c #91d6df",
".M c #92d4dd",
"#h c #92dbe5",
"aq c #939393",
"#s c #93dbe5",
"#U c #94d6de",
"ai c #959595",
"#c c #95999a",
"## c #97d9e1",
"#W c #9c9c9c",
"#N c #9cabac",
"#m c #9cbbbf",
"#C c #9cd9e2",
"#a c #9db8bb",
"#r c #9ddee7",
".W c #9ddfe8",
"#3 c #9fdae1",
".Z c #a0dee6",
"a# c #a1cbd1",
".l c #a2a9a8",
".C c #a2acad",
".A c #a3dce5",
"#z c #a4a4a4",
"#q c #a5dbe3",
".K c #a5e0e8",
"#9 c #a8cacf",
"ak c #a8cfcf",
".7 c #a8e2ea",
"#g c #a9e3eb",
"a. c #aad9de",
".f c #adb5b6",
".r c #adbabb",
".h c #aeb7b9",
".z c #aee3eb",
"#Y c #b0c2c3",
"#Z c #b0e0e7",
"#L c #b4b4b4",
"#J c #b6e4ea",
"#f c #b6e8ee",
"#4 c #b7d0d2",
"#V c #b8cbcd",
"#O c #b8e5eb",
".V c #b9e8ee",
".g c #bbc6c8",
"#e c #bce6ea",
"#B c #c1dce1",
".B c #c2e8ed",
".6 c #c2eaf0",
".J c #c2ebf0",
".y c #c6edf2",
"aF c #c8c8c8",
".N c #c8eaef",
"an c #cacaca",
".4 c #caeef1",
"aM c #cbcbcb",
".F c #cbd6d6",
".p c #cbedf2",
"#p c #cde8eb",
".q c #cdecf1",
".5 c #cdeff2",
"av c #d1d1d1",
".U c #d5f1f4",
".x c #d5f3f5",
".o c #d7f1f5",
"aA c #d8d8d8",
".m c #d8e6e7",
"ap c #d9d9d9",
"#d c #daeef1",
".R c #dbe9eb",
".n c #dbf0f3",
".I c #ddf4f6",
".v c #dfecec",
".S c #dff5f7",
".3 c #e0f1f4",
".T c #e3f6f7",
".w c #e8f7f9",
".G c #e9f8f9",
".H c #ebfafa",
"QtQtQtQtQt.#.a.b.a.cQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQt.d.e.f.g.h.i.jQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQt.k.l.m.n.o.p.q.r.sQtQtQtQtQtQtQtQtQtQt",
"QtQt.t.u.v.w.x.y.z.A.B.C.DQtQtQtQtQtQtQtQtQt",
"QtQt.E.F.G.H.I.J.K.L.M.N.OQtQtQtQtQtQtQtQtQt",
"Qt.P.Q.R.S.T.U.V.W.X.Y.Z.0.1QtQtQtQtQtQtQtQt",
"Qt.P.2.3.4.5.6.7.8.9#.###a#bQtQtQtQtQtQtQtQt",
"Qt.P#c#d#e#f#g#h#i#j#k#l#m#bQtQtQtQtQtQtQtQt",
"Qt#n#o#p#q#r#s#t#u#v#w#x#y#bQtQtQtQtQtQtQtQt",
"Qt#z#A#B#C#D#E#F#G#H#I#J#K#LQtQtQtQtQtQtQtQt",
"QtQt#M#N#O#P#Q#R#S#T#U#V#K#KQtQtQtQtQtQtQtQt",
"QtQt#W#X#Y#Z#0#1#2#3#4.e#5#KQtQtQtQtQtQtQtQt",
"QtQtQt#6#7#8#9a.a#aaabac#K#K#LQtQtQtQtQtQtQt",
"QtQtQtQtQtadaeafagahai#5#K#Kaj#LQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtak#5al.#amanQtQtQtQtQt",
"QtaoaoaoaoaoaoaoaoaoQtapaqarasatauapQtQtQtQt",
"aoaoaoaoaoaoaoaoaoaoaoQtavawaxayatazaAQtQtQt",
"QtaoaoaoaoaoaoaoaoaoQtQtQtQtaBaCaDaEawQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtaFaGaHaIaJQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtaFaKaLaMQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]


image_print_data = [
"22 22 88 2",
"Qt c None",
".2 c #000000",
".S c #08ff08",
"#v c #100810",
".U c #101010",
"#c c #101018",
".M c #181018",
"#e c #181818",
".A c #181821",
".L c #211821",
"#l c #212121",
".z c #212129",
"#m c #292129",
"#u c #292929",
"#n c #292931",
".R c #29ff29",
"#o c #312931",
".T c #313131",
"#p c #313139",
".Z c #31ff31",
"#q c #393139",
"#t c #393939",
".y c #393942",
"#s c #423942",
".o c #424242",
"#h c #4a4a52",
".n c #5a525a",
"#r c #5a5a63",
".I c #5ace5a",
"#b c #6b636b",
".p c #6b6b6b",
".x c #6b6b73",
".Y c #6bff63",
".l c #736b73",
".t c #7b737b",
".s c #7b7384",
".0 c #7bff7b",
".r c #847b84",
".u c #847b8c",
"#g c #84848c",
".v c #8c7b94",
"#i c #8c848c",
".w c #8c8494",
"#j c #8c8c8c",
".8 c #8c8c94",
".m c #948c94",
"#k c #948c9c",
"#f c #949494",
".q c #94949c",
".J c #94c694",
"#d c #9c949c",
"#a c #9c94a5",
".k c #9c9c9c",
".N c #9c9ca5",
".H c #9ccea5",
".K c #a59ca5",
"#. c #a59cad",
".i c #a5a5a5",
".3 c #a5a5ad",
"## c #ad9cad",
".V c #ada5ad",
".d c #adadad",
".j c #adadb5",
".9 c #b5adb5",
".# c #b5b5b5",
".a c #bdbdbd",
".7 c #bdd6bd",
".c c #c6c6c6",
".5 c #cec6ce",
".b c #cecece",
".4 c #ceced6",
".F c #d6ced6",
".G c #d6cede",
".h c #d6d6d6",
".E c #d6d6de",
".Q c #d6ffd6",
".B c #ded6de",
".1 c #ded6e7",
".g c #dedede",
".D c #dedee7",
".6 c #e7dee7",
".f c #e7e7e7",
".C c #e7e7ef",
".X c #e7ffe7",
".O c #efe7ef",
".e c #efefef",
".W c #f7f7f7",
".P c #ffffff",
"QtQtQtQtQtQt.#.a.b.b.b.b.c.c.a.a.d.aQtQtQtQt",
"QtQtQtQtQtQt.a.e.f.f.f.f.f.e.e.e.g.aQtQtQtQt",
"QtQtQtQtQtQt.a.c.c.c.b.b.c.c.c.c.a.cQtQtQtQt",
"QtQtQtQtQtQt.#.a.a.a.a.#.a.a.#.#.d.aQtQtQtQt",
"QtQtQtQtQt.c.d.c.a.c.c.c.a.a.a.c.#QtQtQtQtQt",
"QtQtQtQtQt.a.a.#.a.a.a.a.a.a.c.c.#QtQtQtQtQt",
"QtQtQtQtQt.a.#.c.a.a.a.a.a.c.a.c.dQtQtQtQtQt",
"QtQtQtQtQt.c.a.a.a.a.a.a.a.a.a.a.#QtQtQtQtQt",
"QtQtQtQtQt.d.b.f.g.g.g.g.g.g.h.g.i.i.jQtQtQt",
"QtQtQt.a.k.l.#.h.b.h.b.h.b.h.g.g.m.n.o.p.#Qt",
"QtQt.a.q.r.s.t.t.t.t.t.t.t.u.v.w.x.y.z.A.o.i",
"Qt.a.k.B.C.D.B.E.E.E.E.F.G.H.I.J.K.o.L.L.M.y",
".a.N.O.P.P.P.P.P.P.P.P.P.Q.R.S.R.b.v.T.A.U.L",
".V.W.P.P.P.P.P.P.P.P.P.P.X.Y.Z.0.P.1.t.A.2.L",
".3.E.4.5.4.h.E.E.g.6.D.B.D.E.7.F.4.5.8.M.2.A",
".m.9.j.V.3#..3.K#.#..i#..K#.###a.q.8#b#c.2.L",
".m.j.j#..3.K.K.K.N.K.N.N.N.N#a#d#d.w#b#c.2#e",
"#f#.#..K.N.K.N.N.N#a.k#a#d#d#d#a.m#g#b.M.2#h",
".m.3.K.K#a.k#a#d#a.k#a#d#a#d.q.m.8#i.x#c#e.d",
"#f#g#i.w#j.w#i.8.w#i.8.8.m.8.m#k.8.w#b#e#fQt",
".#.l.z.A#l.z#m#m#m#n#o#o#p#p#q#q#p#o#p#fQtQt",
"QtQt.d#r#s#s#t#p.T.T.T#u#u.z#e#e#v.o.kQtQtQt"
]

image_cut_data = [
"22 22 3 1",
". c None",
"# c #000000",
"a c #000082",
"......................",
".......#.....#........",
".......#.....#........",
".......#.....#........",
".......#....##........",
".......##...#.........",
"........#...#.........",
"........##.##.........",
".........###..........",
".........###..........",
"..........#...........",
".........a#a..........",
"........aa.aaa........",
".......a.a.a..a.......",
"......a..a.a...a......",
".....a...a.a....a.....",
"....a....a.a....a.....",
"....a....a..a...a.....",
"....a....a..a..a......",
"....a...a....aa.......",
".....aaa..............",
"......................"
]

image_copy_data = [
"22 22 6 1",
". c None",
"# c #000000",
"b c #000082",
"c c #3c3cfd",
"d c #8b8bfd",
"a c #ffffff",
"......................",
"......................",
"########..............",
"#aaaaaa##.............",
"#a####a#a#............",
"#aaaaaa#aa#...........",
"#a####a#bbbbbbbb......",
"#aaaaaa#baaaaaabb.....",
"#a#####aba####abcb....",
"#aaaaaaabaaaaaabdcb...",
"#a#####aba####abadcb..",
"#aaaaaaabaaaaaabbbbbb.",
"#a#####aba####aaaaaab.",
"#aaaaaaabaaaaaaaaaaab.",
"#a#####aba#########ab.",
"#aaaaaaabaaaaaaaaaaab.",
"########ba#########ab.",
"........baaaaaaaaaaab.",
"........ba#########ab.",
"........baaaaaaaaaaab.",
"........bbbbbbbbbbbbb.",
"......................"
]

image_delete_data = [
"22 22 2 1",
". c None",
"# c #ff0000",
"......................",
"......................",
".................###..",
"...............####...",
".###..........###.....",
"..####.......###......",
"....####....###.......",
"......####.###........",
".......######.........",
"........######........",
"........#######.......",
".......#########......",
".......###..#####.....",
"......####...#####....",
".....####.....#####...",
"....#####.....#####...",
"...#####.......###....",
"...#####.......##.....",
"...####...............",
"....##................",
"......................",
"......................"
]


image_paste_data = [
"22 22 8 1",
". c None",
"# c #000000",
"e c #000084",
"c c #848200",
"b c #848284",
"d c #c6c3c6",
"a c #ffff00",
"f c #ffffff",
"......................",
".......#####..........",
"..######aaa######.....",
".######aaaaa######....",
"##bcb##a###a##bcb##...",
"#bcb#ddddddddd#bcb#...",
"#cbc#ddddddddd#cbc#...",
"#bcb###########bcb#...",
"#cbcbcbcbcbcbcbcbc#...",
"#bcbcbcbcbcbcbcbcb#...",
"#cbcbcbceeeeeeeeee#...",
"#bcbcbcbefffffffefe...",
"#cbcbcbcefeeeeefeffe..",
"#bcbcbcbefffffffefffe.",
"#cbcbcbcefeeeeefeffffe",
"#bcbcbcbefffffffeeeeee",
"#cbcbcbcefeeeeeffffffe",
"#bcbcbcbeffffffffffffe",
"#cbcbcbcefeeeeeeeeeefe",
".#######effffffffffffe",
"........eeeeeeeeeeeeee",
"......................"
]

file_open = ["22 22 5 1",
". c None",
"# c #000000",
"c c #848200",
"a c #ffff00",
"b c #ffffff",
"......................",
"......................",
"......................",
"............####....#.",
"...........#....##.##.",
"..................###.",
".................####.",
".####...........#####.",
"#abab##########.......",
"#babababababab#.......",
"#ababababababa#.......",
"#babababababab#.......",
"#ababab###############",
"#babab##cccccccccccc##",
"#abab##cccccccccccc##.",
"#bab##cccccccccccc##..",
"#ab##cccccccccccc##...",
"#b##cccccccccccc##....",
"###cccccccccccc##.....",
"##cccccccccccc##......",
"###############.......",
"......................"]

file_save = ["22 22 5 1",
". c None",
"# c #000000",
"a c #848200",
"b c #c1c1c1",
"c c #cab5d1",
"......................",
".####################.",
".#aa#bbbbbbbbbbbb#bb#.",
".#aa#bbbbbbbbbbbb#bb#.",
".#aa#bbbbbbbbbcbb####.",
".#aa#bbbccbbbbbbb#aa#.",
".#aa#bbbccbbbbbbb#aa#.",
".#aa#bbbbbbbbbbbb#aa#.",
".#aa#bbbbbbbbbbbb#aa#.",
".#aa#bbbbbbbbbbbb#aa#.",
".#aa#bbbbbbbbbbbb#aa#.",
".#aaa############aaa#.",
".#aaaaaaaaaaaaaaaaaa#.",
".#aaaaaaaaaaaaaaaaaa#.",
".#aaa#############aa#.",
".#aaa#########bbb#aa#.",
".#aaa#########bbb#aa#.",
".#aaa#########bbb#aa#.",
".#aaa#########bbb#aa#.",
".#aaa#########bbb#aa#.",
"..##################..",
"......................"]

icon_playr = ["22 22 2 1",
". c None",
"# c #000000",
"......................",
"......................",
"...................##.",
".................####.",
"...............######.",
".............########.",
"...........##########.",
".........############.",
".......##############.",
".....################.",
"...##################.",
"...##################.",
".....################.",
".......##############.",
".........############.",
"...........##########.",
".............########.",
"...............######.",
".................####.",
"...................##.",
"......................",
"......................"]

icon_play = ["22 22 2 1",
". c None",
"# c #000000",
"......................",
"......................",
".##...................",
".####.................",
".######...............",
".########.............",
".##########...........",
".############.........",
".##############.......",
".################.....",
".##################...",
".##################...",
".################.....",
".##############.......",
".############.........",
".##########...........",
".########.............",
".######...............",
".####.................",
".##...................",
"......................",
"......................"]

icon_stop = ["22 22 2 1",
". c None",
"# c #000000",
"......................",
"......................",
"......................",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"...################...",
"......................",
"......................",
"......................"]

icon_pause = ["22 22 2 1",
". c None",
"# c #000000",
"......................",
"......................",
"......................",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"...#####......#####...",
"......................",
"......................",
"......................"]

icon_record = ["22 22 2 1",
". c None",
"# c #ff0000",
"......................",
"......................",
"......................",
"......................",
"........######........",
"......##########......",
"....##############....",
"...################...",
"...################...",
"..##################..",
"..##################..",
"..##################..",
"..##################..",
"...################...",
"...################...",
"....##############....",
"......##########......",
"........######........",
"......................",
"......................",
"......................",
"......................"]

IconDict= {'cube_bottom':image_cubeBo_data,
           'cube_right':image_cubeR_data,
           'cube_top' :image_cubeT_data,
           'cube_left' :image_cubeL_data,
           'cube_front' :image_cubeF_data,
           'cube_back' :image_cubeBa_data,
           'cube_45' :image_cube45_data,
           'cursor_closedhand': cursor_closedhand,
           'cursor_normal': cursor_normal,
           'cursor_openhand': cursor_openhand,
           'cursor_pointinghand': cursor_pointinghand,
           'cursor_sizeall':cursor_sizeall,
           'cursor_what': cursor_what,
           'cut': image_cut_data,
           'copy': image_copy_data,
           'delete': image_delete_data,
           'paste': image_paste_data,
           'print': image_print_data,
           'play': icon_play,
           'playr': icon_playr,
           'stop': icon_stop,
           'pause': icon_pause,
           'file_open': file_open,
           'file_save': file_save,
}


def showIcons():
    import sys
    from . import Object3DQt as qt

    a = qt.QApplication(sys.argv)
    a.lastWindowClosed.connect(a.quit)
    w = qt.QWidget()
    g = qt.QGridLayout(w)

    idx = 0
    for name,icon in IconDict.items():
        #print "name",name
        lab = qt.QLabel(w)
        lab.setText(str(name))
        g.addWidget(lab, idx, 0)
        lab = qt.QLabel(w)
        lab.setPixmap(qt.QPixmap(icon))
        g.addWidget(lab, idx, 1)
        idx += 1

    w.show()
    a.exec_()

if __name__=='__main__':
    showIcons()
