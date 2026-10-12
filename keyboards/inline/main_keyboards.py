from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📱 IPhone", callback_data='phone'),
        InlineKeyboardButton(text="💻 MacBook", callback_data='macos')
    ],
    [
        InlineKeyboardButton(text="⌚ IWatch", callback_data='watch'),
        InlineKeyboardButton(text="🛍 Accessories", callback_data='access')
    ],
])


macos_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 M1", callback_data='m1'),
        InlineKeyboardButton(text="💻 M2", callback_data='m2')
    ],
    [ 
        InlineKeyboardButton(text="💻 M3", callback_data='m3'),
        InlineKeyboardButton(text="💻 M4", callback_data='m4')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='main_menu')
    ],
])

#=========================================MACBOOK M4===================================================================================================================
m4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Air", callback_data='m4_air'),
        InlineKeyboardButton(text="💻 Pro", callback_data='m4_pro')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='macos_menu')
    ],
])


m4_pro = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m4_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])


m4_air = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m4_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================MACBOOK M3===================================================================================================================

m3_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Air", callback_data='m3_air'),
        InlineKeyboardButton(text="💻 Pro", callback_data='m3_pro')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='macos_menu')
    ],
])


m3_pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m3_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])


m3_air_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m3_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================MACBOOK M2===================================================================================================================

m2_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Air", callback_data='m2_air'),
        InlineKeyboardButton(text="💻 Pro", callback_data='m2_pro')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='macos_menu')
    ],
])


m2_pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m2_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])


m2_air_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m2_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================MACBOOK M1===================================================================================================================
m1_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Air", callback_data='m1_air'),
        InlineKeyboardButton(text="💻 Pro", callback_data='m1_pro')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='macos_menu')
    ],
])


m1_pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m1_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])


m1_air_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='m1_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IPHONE===================================================================================================================

iphone_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📱 Iphone 16 Pro", callback_data='Iphone 16 Pro'),
        InlineKeyboardButton(text="📱 Iphone 14 Pro", callback_data='Iphone 14 Pro')
    ],
    [ 
        InlineKeyboardButton(text="📱 Iphone 13 Pro", callback_data='Iphone 13 Pro'),
        InlineKeyboardButton(text="📱 Iphone 11", callback_data='Iphone 11')
    ],
    [
        InlineKeyboardButton(text="📱 Iphone 11 Pro", callback_data='Iphone 11 Pro'),
        InlineKeyboardButton(text="📱 Iphone 15 Pro", callback_data='Iphone 15 Pro')
    ],
    [
        InlineKeyboardButton(text="📱 Iphone XS", callback_data='Iphone XS'),
        InlineKeyboardButton(text="📱 Iphone 8+", callback_data='Iphone 8+')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='main_menu')
    ],
])
#=========================================IPHONE 16 PRO===================================================================================================================

Iphone_16_Pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IPHONE 14 PRO===================================================================================================================

Iphone_14_Pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IPHONE 13 PRO===================================================================================================================

Iphone_13_Pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Iphone 11===================================================================================================================
Iphone_11_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Iphone 11 Pro======================================================================================================================================================================================================================================

Iphone_11_Pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Iphone 15======================================================================================================================================================================================================================================

Iphone_15_Pro_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Iphone XS======================================================================================================================================================================================================================================================================================================================================

Iphone_XS_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Iphone 8+======================================================================================================================================================================================================================================================================================================================================================================================================================================

Iphone_8_plus_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='iphone_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IWatch======================================================================================================================================================================================================================================================================================================================================================================================================================================

IWatch_mune = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⌚ IWatch Ultra 3", callback_data='Iwatch ultra 3'),
        InlineKeyboardButton(text="⌚ IWatch Series 11", callback_data='Iwatch series 11')
    ],
    [ 
        InlineKeyboardButton(text="⌚ IWatch SE 3", callback_data='Iwatch se 3'),
        InlineKeyboardButton(text="⌚ IWatch Series 10", callback_data='Iwatch series 10')
    ],
    [
        InlineKeyboardButton(text="⌚ IWatch Ultra 2", callback_data='Iwatch ultra 2'),
        InlineKeyboardButton(text="⌚ IWatch Series 9", callback_data='Iwatch series 9')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='main_menu')
    ],
])
#=========================================IWatch Ultra 3======================================================================================================================================================================================================================================================================================================================================================================================================================================

IWatch_Ultra_3_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Watch Series 11======================================================================================================================================================================================================================================================================================================================================================================================================================================

IWatch_Series_11_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IWatch SE 3===================================================================================================================================================================================

IWatch_SE_3_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IWatch Series 10===================================================================================================================================================================================

IWatch_Series_10_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IWatch Ultra 2===================================================================================================================================================================================

IWatch_Ultra_2_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================IWatch Series 9===================================================================================================================================================================================

IWatch_Series_9_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='IWatch_mune'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Accessories==================================================================================================================================================================================


Access_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎧 AirPods", callback_data='airpods'),
        InlineKeyboardButton(text="⌨️ Keyboard", callback_data='keyboard')
    ],
    [ 
        InlineKeyboardButton(text="🖱 Mouse", callback_data='mouse'),
        InlineKeyboardButton(text="🔋 PowerBank", callback_data='power')
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='main_menu')
    ],
])
#==========================================AirPods==================================================================================================================================================================================

Airpods_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎧 AirPods Max", callback_data='max'),
        InlineKeyboardButton(text="🎧 AirPods Pro 2", callback_data='pro')
    ],
    [ 
        InlineKeyboardButton(text="🎧 AirPods 3", callback_data='air'),
        InlineKeyboardButton(text="🎧 AirPods 2", callback_data='ikki')
    ],    
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Access_menu')
    ],
])
#==========================================AirPods Max==================================================================================================================================================================================

AirPods_Max = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Airpods_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================AirPods Pro 2==================================================================================================================================================================================

AirPods_Pro = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Airpods_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================AirPods 3==================================================================================================================================================================================================================

AirPods_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Airpods_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================AirPods 2==================================================================================================================================================================================================================

AirPods_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Airpods_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Mouse==================================================================================================================================================================================================================

mouse_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🖱 Mighty Mouse", callback_data='mighty_mouse'),
        InlineKeyboardButton(text="🖱 Magic Mouse 1", callback_data='mouse1')
    ],
    [
        InlineKeyboardButton(text="🖱 Magic Mouse 2", callback_data='mouse2'),
        InlineKeyboardButton(text="🖱 Magic Mouse 3", callback_data='mouse3')
    ],
    [
        InlineKeyboardButton(text="⬅️ Ortga", callback_data='Access_menu'),
    ],
])          
#==========================================Magic Mouse 3==================================================================================================================================================================================================================

Magic_Mouse_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='mouse_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Magic Mouse 2=================================================================================================================================================================================================================

Magic_Mouse_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='mouse_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Magic Mouse 1=================================================================================================================================================================================================================================================================================

Magic_Mouse_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='mouse_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Mighty Mouse=================================================================================================================================================================================================================================================================================================================================================

Mighty_Mouse = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='mouse_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Keyboard=================================================================================================================================================================================================================================================================================================================================================

Keyboard_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⌨️ Magic Keyboard", callback_data='magic keyboard'),
        InlineKeyboardButton(text="⌨️ iPad uchun klaviaturalar", callback_data='ipad keyboard')
    ],
    [
        InlineKeyboardButton(text="⌨️ Apple Wireless Keyboard", callback_data='wireless keyboard'),
        InlineKeyboardButton(text="⌨️ Magic Keyboard Folio", callback_data='folio keyboard')
    ],
    [
        InlineKeyboardButton(text="⬅️ Ortga", callback_data='Access_menu'),
    ],
]) 
#==========================================Magic Keyboard=================================================================================================================================================================================================================================================================================================================================================

Magic_Keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Keyboard_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================iPad keyboard=================================================================================================================================================================================================================================================================================================================================================

iPad_Keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Keyboard_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Apple Wireless Keyboard=================================================================================================================================================================================================================================================================================================================================================

Wireless_Keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Keyboard_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#==========================================Magic Keyboard Folio=================================================================================================================================================================================================================================================================================================================================================

Folio_Keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Keyboard_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Powerbank===================================================================================================================================================================================

Powerbank_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔋 Anker MagGo 5K", callback_data='maggo'),
        InlineKeyboardButton(text="🔋 Apple MagSafe Battery Pack", callback_data='pack')
    ],
    [
        InlineKeyboardButton(text="🔋 Torras MiniMag", callback_data='minimag'),
        InlineKeyboardButton(text="🔋 Benks ArmorGo", callback_data='armorgo')
    ],
    [
        InlineKeyboardButton(text="⬅️ Ortga", callback_data='Access_menu'),
    ],
])
#=========================================Anker MagGo 5K===================================================================================================================================================================================

maggo_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Powerbank_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Apple MagSafe Battery Pack===================================================================================================================================================================================

pack_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Powerbank_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Torras MiniMag===================================================================================================================================================================================

minimag_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Powerbank_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])
#=========================================Benks ArmorGo===================================================================================================================================================================================

armorgo_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data='Powerbank_menu'),
        InlineKeyboardButton(text="💵 Buy", url="https://t.me/muhammadjonnmominov")
    ],
])


