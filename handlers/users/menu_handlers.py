from aiogram import types
from loader import dp
from keyboards.inline.main_keyboards import macos_menu, m4, m4_pro, main_menu, m4_air, m3_menu, m3_pro_menu, m3_air_menu, m2_menu, m2_pro_menu, m2_air_menu, m1_menu, m1_pro_menu, m1_air_menu, iphone_menu, Iphone_16_Pro_menu, Iphone_14_Pro_menu, Iphone_13_Pro_menu, Iphone_11_menu, Iphone_11_Pro_menu, Iphone_15_Pro_menu, Iphone_XS_menu, Iphone_8_plus_menu, IWatch_mune, IWatch_Ultra_3_menu, IWatch_Series_11_menu, IWatch_SE_3_menu, IWatch_Series_10_menu, IWatch_Ultra_2_menu, IWatch_Series_9_menu, Access_menu, Airpods_menu, AirPods_Max, AirPods_Pro, AirPods_3, AirPods_2, mouse_menu, Magic_Mouse_3, Magic_Mouse_2, Magic_Mouse_1, Mighty_Mouse, Keyboard_menu, Magic_Keyboard, iPad_Keyboard, Wireless_Keyboard, Folio_Keyboard, Powerbank_menu, maggo_menu, minimag_menu, armorgo_menu, pack_menu


#=========================================MACBOOK M4===================================================================================================================
@dp.callback_query_handler(text="macos")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook Laptops",
                                    photo="https://avatars.mds.yandex.net/i?id=76648fc957a8389c8e185fdfd7d2196de9b24bb5-16447530-images-thumbs&n=13",
                                     reply_markup=macos_menu)


@dp.callback_query_handler(text="m4")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M4 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m4)
    

@dp.callback_query_handler(text="m4_pro")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M4  Laptops\n"
                                            f"– Chip: 14 yadroli CPU, 20 yadroli GPU, 16 yadroli Neural Engine, 273 GB/s xotira tezligi\n"
                                            f"– Xotira: 24 GB (48 GB gacha)\n"
                                            f"– Ekran: Liquid Retina XDR, ProMotion 120 Hz, 1000 nits SDR / 1600 nits HDR, nano-tekstura varianti\n"
                                            f"– Portlar: 3× Thunderbolt 5 (USB-C), HDMI, SDXC, MagSafe 3\n"
                                            f"– Batareya: ~22 soat (14), ~24 soat (16)\n"
                                            f"<b>Narxi</b>: $ 2 000",
                                    photo="https://avatars.mds.yandex.net/i?id=76648fc957a8389c8e185fdfd7d2196de9b24bb5-16447530-images-thumbs&n=13",
                                    reply_markup=m4_pro)
    

@dp.callback_query_handler(text="m4_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M4 Laptops\n",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m4)
    

@dp.callback_query_handler(text="macos_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook Laptops\n",
                                    photo="https://avatars.mds.yandex.net/i?id=76648fc957a8389c8e185fdfd7d2196de9b24bb5-16447530-images-thumbs&n=13",
                                    reply_markup=macos_menu)
    

@dp.callback_query_handler(text="main_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Apple Store",
                            photo="https://i.pinimg.com/originals/7e/0f/64/7e0f64e278cabce4752abac1d8432389.jpg",
                            reply_markup=main_menu)



@dp.callback_query_handler(text="m4_air")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M4 Laptops\n"
                                            f"MacBook Air (M4, 2025)\n"
                                            f"- Chip: Apple M4 (10-yadro CPU, 8/10-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 16GB (24GB/32GB opsiya)\n"
                                            f"- Saqlash: 256GB SSD (512GB–2TB opsiya)\n"
                                            f"- Displey: 13.6 yoki 15.3 Liquid Retina, 500 nit\n"
                                            f"- Batareya: 18 soat video, 15 soat internet\n"
                                            f"- Quvvat: MagSafe 3, fast-charge qo‘llab-quvvatlaydi\n"
                                            f"- Og‘irlik: ~1.24 kg (13), biroz og‘irroq (15)\n"
                                            f"<b>Narxi</b>: $ 1 700",
                                    photo="https://www.geeky-gadgets.com/wp-content/uploads/2024/07/M4-MacBook-Air.webp",
                                    reply_markup=m4_air)


@dp.callback_query_handler(text="m4")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M4",
                                    photo="https://avatars.mds.yandex.net/i?id=76648fc957a8389c8e185fdfd7d2196de9b24bb5-16447530-images-thumbs&n=13",
                                    reply_markup=m4)
    


#=========================================MACBOOK M3===================================================================================================================
@dp.callback_query_handler(text="m3")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M3 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m3_menu)
    

@dp.callback_query_handler(text="m3_pro")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M3 Pro Laptops\n"
                                            f"MacBook Pro (M3, 2023)\n"
                                            f"- Chip: Apple M3 (8-yadro CPU, 10-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 8GB (16GB/24GB opsiya)\n"
                                            f"- Saqlash: 512GB SSD (1TB–2TB opsiya)\n"
                                            f"- Displey: 14.2 Liquid Retina XDR, 3024×1964, 1000 nit (HDR’da 1600 nit)\n"
                                            f"- Batareya: 22 soat video, 15–18 soat internet\n"
                                            f"- Quvvat: MagSafe 3, 67W yoki 96W zaryadlovchi\n"
                                            f"- Og‘irlik: ~1.55 kg\n"
                                            f"- <b>Narxi</b>: $ 1 600",
                                    photo="https://i.ytimg.com/vi/JckONs4MsbI/maxresdefault.jpg",
                                    reply_markup=m3_pro_menu)
    


@dp.callback_query_handler(text="macos_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook Laptops",
                                    photo="https://avatars.mds.yandex.net/i?id=76648fc957a8389c8e185fdfd7d2196de9b24bb5-16447530-images-thumbs&n=13",
                                    reply_markup=macos_menu)


@dp.callback_query_handler(text="m3_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M3 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m3_menu)


@dp.callback_query_handler(text="m3_air")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M3 Air Laptops\n"
                                            f"MacBook Air (M3, 2024)\n"
                                            f"- Chip: Apple M3 (8-yadro CPU, 8/10-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 8GB (16GB/24GB opsiya)\n"
                                            f"- Saqlash: 256GB SSD (512GB–2TB opsiya)\n"
                                            f"- Displey: 13.6 yoki 15.3 Liquid Retina, 500 nit\n"
                                            f"- Batareya: 18 soat video, 15 soat internet\n"
                                            f"- Quvvat: MagSafe 3, tez zaryadlash qo‘llab-quvvatlaydi\n"
                                            f"- Og‘irlik: ~1.24 kg (13), ~1.51 kg (15)\n"
                                            f"- <b>Narxi</b>: $ 1 300",
                                    photo="https://bilder.macwelt.de/4352514_original.jpg?quality=50&strip=all",
                                    reply_markup=m3_air_menu)


@dp.callback_query_handler(text="m3_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M3 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m3_menu)


@dp.callback_query_handler(text="main_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Apple Store",
                            photo="https://i.pinimg.com/originals/7e/0f/64/7e0f64e278cabce4752abac1d8432389.jpg",
                            reply_markup=main_menu)



#=========================================MACBOOK M2===================================================================================================================
@dp.callback_query_handler(text="m2")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M2 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m2_menu)
    

@dp.callback_query_handler(text="m2_pro")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M2 Pro Laptops\n"
                                            f"MacBook Pro (M2 Pro, 2023)\n"
                                            f"- Chip: Apple M2 Pro (10/12-yadro CPU, 16/19-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 16GB (32GB/64GB opsiya)\n"
                                            f"- Saqlash: 512GB SSD (1TB–8TB opsiya)\n"
                                            f"- Displey: 14.2 yoki 16.2 Liquid Retina XDR, 120 Hz ProMotion, 1000 nit SDR / 1600 nit HDR\n"
                                            f"- Portlar: 3× Thunderbolt 4 (USB-C), HDMI, SDXC, MagSafe 3\n"
                                            f"- Batareya: ~18 soat (14), ~22 soat (16)\n"
                                            f"- Og‘irlik: ~1.6 kg (14), ~2.15 kg (16)\n"
                                            f"- <b>Narxi</b>: $ 1 500",
                                            photo="https://tweakers.net/ext/i/2005575220.jpeg",
                                            reply_markup=m2_pro_menu)
    

@dp.callback_query_handler(text="m2_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M2 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m2_menu)
    

@dp.callback_query_handler(text="m2_air")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M2 Air Laptops\n"
                                            f"MacBook Air (M2, 2022)\n"
                                            f"- Chip: Apple M2 (8-yadro CPU, 8/10-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 8GB (16GB/24GB opsiya)\n"
                                            f"- Saqlash: 256GB SSD (512GB–2TB opsiya)\n"
                                            f"- Displey: 13.6 Liquid Retina, 500 nit\n"
                                            f"- Batareya: ~18 soat video, 15 soat internet\n"
                                            f"- Quvvat: MagSafe 3, tez zaryadlash qo‘llab-quvvatlaydi\n"
                                            f"- Og‘irlik: ~1.24 kg\n"
                                            f"- <b>Narxi</b>: $ 1 100",
                                            photo="https://i.ytimg.com/vi/g0J6qBEjLH0/maxresdefault.jpg?7857057827",
                                            reply_markup=m2_air_menu)


@dp.callback_query_handler(text="m2_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M2 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m2_menu)



#=========================================MACBOOK M1===================================================================================================================
@dp.callback_query_handler(text="m1")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M1 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m1_menu)


@dp.callback_query_handler(text="m1_pro")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M1 Pro Laptops\n"
                                            f"MacBook Pro (M1 Pro, 2021)\n"
                                            f"- Chip: Apple M1 Pro (8/10-yadro CPU, 14/16-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 16GB (32GB opsiya)\n"
                                            f"- Saqlash: 512GB SSD (1TB–8TB opsiya)\n"
                                            f"- Displey: 14.2 yoki 16.2 Liquid Retina XDR, 120 Hz ProMotion, 1000 nit SDR / 1600 nit HDR\n"
                                            f"- Portlar: 3× Thunderbolt 4 (USB-C), HDMI, SDXC, MagSafe 3\n"
                                            f"- Batareya: ~17 soat (14), ~21 soat (16)\n"
                                            f"- Og‘irlik: ~1.6 kg (14), ~2.1 kg (16)\n"
                                            f"- <b>Narxi</b>: $ 1 200",
                                            photo="https://i.ytimg.com/vi/aC6EcZMLWB0/maxresdefault.jpg",
                                            reply_markup=m1_pro_menu)


@dp.callback_query_handler(text="m1_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M1 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m1_menu)
    

@dp.callback_query_handler(text="m1_air")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"MacBook M1 Air Laptops\n"
                                            f"MacBook Air (M1, 2020)\n"
                                            f"- Chip: Apple M1 (8-yadro CPU, 7/8-yadro GPU, 16-yadro Neural Engine)\n"
                                            f"- Xotira: 8GB (16GB opsiya)\n"
                                            f"- Saqlash: 256GB SSD (512GB–2TB opsiya)\n"
                                            f"- Displey: 13.3 Retina (2560×1600), True Tone, 400 nit\n"
                                            f"- Batareya: ~15 soat internet, ~18 soat video\n"
                                            f"- Quvvat: USB-C / Thunderbolt 3 (2 ta port)\n"
                                            f"- Og‘irlik: ~1.29 kg\n"
                                            f"- <b>Narxi</b>: $ 900",
                                            photo="https://cdn.vox-cdn.com/uploads/chorus_asset/file/23759758/bfarsace_190101_5333_0005.jpg",
                                            reply_markup=m1_air_menu)


@dp.callback_query_handler(text="m1_menu")
async def show_macos_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="MacBook M1 Laptops",
                                    photo="https://i.ytimg.com/vi/KCk50jiKi_s/maxresdefault.jpg",
                                    reply_markup=m1_menu)


#=========================================Iphone 16 Pro===================================================================================================================
@dp.callback_query_handler(text="phone")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="IPHONE",
                                    photo="https://i.pinimg.com/originals/80/fd/d6/80fdd643f5c00c155a0e5d74753e8341.jpg",
                                    reply_markup=iphone_menu)


@dp.callback_query_handler(text="Iphone 16 Pro")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 16 Pro\n"
                                            f"iPhone 16 Pro (2024)\n"
                                            f"- Chip: A18 Pro\n"
                                            f"- Xotira: 8GB RAM\n"
                                            f"- Saqlash: 128GB–1TB\n"
                                            f"- Displey: 6.3 Super Retina XDR OLED, 120Hz\n"
                                            f"- Kamera: 48MP asosiy, 48MP ultra-wide, 12MP telephoto (5x zoom), 12MP old\n"
                                            f"- Material: Titaniy ramka, IP68\n"
                                            f"- Port: USB-C, 5G, Wi-Fi 7\n"
                                            f"- Batareya: ~27 soat video\n"
                                            f"- Og‘irlik: ~199 g\n"
                                            f"- <b>Narxi</b>: $ 1 500",                                    
                                            photo="https://i.ytimg.com/vi/q0yv7g_fwK0/oardefault.jpg?sqp=-oaymwEYCNAFENAFSFqQAgHyq4qpAwcIARUAAIhC&rs=AOn4CLCbHXVjHKrMUK0V-bvYjNcUrpMX9g",
                                            reply_markup=Iphone_16_Pro_menu)


@dp.callback_query_handler(text="iphone_menu")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="IPHONE",
                                    photo="https://i.pinimg.com/originals/80/fd/d6/80fdd643f5c00c155a0e5d74753e8341.jpg",
                                    reply_markup=iphone_menu)
    

@dp.callback_query_handler(text="main_menu")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Apple Store",
                            photo="https://i.pinimg.com/originals/7e/0f/64/7e0f64e278cabce4752abac1d8432389.jpg",
                            reply_markup=main_menu)

#=========================================Iphone 14 Pro===================================================================================================================
@dp.callback_query_handler(text="Iphone 14 Pro")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 14 Pro\n"
                                            f"iPhone 14 Pro (2022)\n"
                                            f"- Chip: A16 Bionic\n"
                                            f"- Xotira: 6GB RAM\n"
                                            f"- Saqlash: 128GB–1TB\n"
                                            f"- Displey: 6.1 Super Retina XDR OLED, 120Hz, Always-On\n"
                                            f"- Kamera: 48MP asosiy, 12MP ultra-wide, 12MP telephoto (3x zoom), 12MP old\n"
                                            f"- Material: Zanglamaydigan po‘lat, IP68\n"
                                            f"- Port: Lightning, 5G, Wi-Fi 6\n"
                                            f"- Batareya: ~23 soat video\n"
                                            f"- Og‘irlik: ~206 g\n"
                                            f"- <b>Narxi</b>: $ 1 150",                               
                                            photo="https://cdn1.ozone.ru/s3/multimedia-f/6607097331.jpg",
                                            reply_markup=Iphone_14_Pro_menu)


#=========================================Iphone 13 Pro===================================================================================================================
@dp.callback_query_handler(text="Iphone 13 Pro")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 13 Pro\n"
                                            f"iPhone 13 Pro (2021)\n"
                                            f"- Chip: A15 Bionic (5-yadroli GPU)\n"
                                            f"- Xotira: 6GB RAM\n"
                                            f"- Saqlash: 128GB–1TB\n"
                                            f"- Displey: 6.1 Super Retina XDR OLED, 120Hz ProMotion\n"
                                            f"- Kamera: 12MP asosiy, 12MP ultra-wide, 12MP telephoto (3x zoom), 12MP old\n"
                                            f"- Material: Zanglamaydigan po‘lat, IP68\n"
                                            f"- Port: Lightning, 5G, Wi-Fi 6\n"
                                            f"- Batareya: ~22 soat video\n"
                                            f"- Og‘irlik: ~204 g\n"
                                            f"- <b>Narxi</b>: $ 1 669",                        
                                            photo="https://micro-line.ru/images/thumbnails/3030/3030/detailed/1333/orig_rrtk-wo.jpg",
                                            reply_markup=Iphone_13_Pro_menu)



#=========================================Iphone 11===================================================================================================================
@dp.callback_query_handler(text="Iphone 11")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 11\n"
                                            f"iPhone 11 (2019)\n"
                                            f"- Chip: A13 Bionic\n"
                                            f"- Xotira: 4GB RAM\n"
                                            f"- Saqlash: 64GB–256GB\n"
                                            f"- Displey: 6.1 Liquid Retina HD (LCD)\n"
                                            f"- Kamera: 12MP asosiy, 12MP ultra-wide, 12MP old\n"
                                            f"- Material: Alyuminiy va shisha, IP68\n"
                                            f"- Port: Lightning, 4G LTE, Wi-Fi 6\n"
                                            f"- Batareya: ~17 soat video\n"
                                            f"- Og‘irlik: ~194 g\n"
                                            f"- <b>Narxi</b>: $ 660",                   
                                            photo="https://cdn1.ozone.ru/s3/multimedia-u/6370347042.jpg",
                                            reply_markup=Iphone_11_menu)



#=========================================Iphone 11 Pro===================================================================================================================================================================================
@dp.callback_query_handler(text="Iphone 11 Pro")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 11 Pro\n"
                                            f"iPhone 11 Pro (2019)"
                                            f"- Chip: A13 Bionic\n"
                                            f"- Xotira: 4GB RAM\n"
                                            f"- Saqlash: 64GB–512GB\n"
                                            f"- Displey: 5.8 Super Retina XDR OLED, HDR10, Dolby Vision\n"
                                            f"- Kamera: 12MP asosiy, 12MP ultra-wide, 12MP telephoto (2x zoom), 12MP old\n"
                                            f"- Material: Zanglamaydigan po‘lat va mat shisha, IP68\n"
                                            f"- Port: Lightning, 4G LTE, Wi-Fi 6\n"
                                            f"- Batareya: ~18 soat video\n"
                                            f"- Og‘irlik: ~188 g\n"
                                            f"- <b>Narxi</b>: $ 749",        
                                            photo="https://m.media-amazon.com/images/I/81mxun+6pEL.jpg",
                                            reply_markup=Iphone_11_Pro_menu)
    

#=========================================Iphone 15===================================================================================================================================================================================
@dp.callback_query_handler(text="Iphone 15 Pro")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 15 Pro\n"
                                            f"iPhone 15 Pro (2023)\n"
                                            f"- Chip: A17 Pro (3 nm)\n"
                                            f"- Xotira: 8GB RAM\n"
                                            f"- Saqlash: 128GB–1TB\n"
                                            f"- Displey: 6.1 Super Retina XDR OLED, 120Hz, Always-On\n"
                                            f"- Kamera: 48MP asosiy, 12MP ultra-wide, 12MP telephoto (3x zoom), 12MP old\n"
                                            f"- Port: USB-C (10Gbps), 5G, Wi-Fi 6E\n"
                                            f"- Batareya: ~23 soat video\n"
                                            f"- Og‘irlik: ~187 g\n"
                                            f"- <b>Narxi</b>: $ 2 000",
                                            photo="https://cdn1.ozone.ru/s3/multimedia-1-i/7344369342.jpg",
                                            reply_markup=Iphone_15_Pro_menu)


#=========================================Iphone XS===================================================================================================================================================================================
@dp.callback_query_handler(text="Iphone XS")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone XS\n"
                                            f"iPhone XS (2018)\n"
                                            f"- Chip: Apple A12 Bionic\n"
                                            f"- Xotira: 4GB RAM\n"
                                            f"- Saqlash: 64GB, 256GB, 512GB\n"
                                            f"- Displey: 5.8 Super Retina OLED, HDR10, Dolby Vision, 1125×2436\n"
                                            f"- Kamera: 12MP (asosiy, telephoto 2x) + 7MP old kamera\n"
                                            f"- Batareya: ~20 soat gaplashuv, ~12 soat internet\n"
                                            f"- Port: Lightning, Face ID\n"
                                            f"- Material: Zanglamaydigan po‘lat ramka, IP68\n"
                                            f"- Og‘irlik: ~177 g\n"
                                            f"- <b>Narxi</b>: $ 260",
                                            photo="https://i.ebayimg.com/images/g/-sAAAOSwoTlgSm~K/s-l500.jpg",
                                            reply_markup=Iphone_XS_menu)


#=========================================Iphone 8+===================================================================================================================================================================================
@dp.callback_query_handler(text="Iphone 8+")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Iphone 8+\n"
                                            f"iPhone 8 Plus (2017)"
                                            f"- Chip: Apple A11 Bionic\n"
                                            f"- Xotira: 3GB RAM\n"
                                            f"- Saqlash: 64GB, 128GB, 256GB\n"
                                            f"- Displey: 5.5 Retina IPS LCD, 1080×1920, True Tone\n"
                                            f"- Kamera: 12MP (asosiy, telephoto 2x) + 7MP old kamera\n"
                                            f"- Batareya: ~21 soat gaplashuv, ~13 soat internet\n"
                                            f"- Port: Lightning, Touch ID (Home tugmasida)\n"
                                            f"- Material: Alyuminiy + shisha, IP67\n"
                                            f"- Og‘irlik: ~202 g\n"
                                            f"- <b>Narxi</b>: $ 89",
                                            photo="https://static.tildacdn.com/tild3037-3833-4639-a433-356337626464/iphone-8-plus.jpg",
                                            reply_markup=Iphone_8_plus_menu)
    

#=========================================IWatch Ultra 3===================================================================================================================================================================================
@dp.callback_query_handler(text="watch")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="IWatch\n",
                                    photo="https://staticg.sportskeeda.com/editor/2022/09/b75d6-16625727337695-1920.jpg",
                                    reply_markup=IWatch_mune)
    

@dp.callback_query_handler(text="Iwatch ultra 3")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Apple IWatch Ultra 3</b>\n"
                                            f"Apple IWatch Ultra 3 (2025)\n"
                                            f"- Chip: Apple S10\n"
                                            f"- Xotira: 64 GB\n"
                                            f"- Ekran: 1.98 LTPO3 OLED, 3000 nit\n"
                                            f"- Batareya: 42 soat (72 soat Low Power)\n"
                                            f"- Chidamlilik: WR100 (100 m), IP6X changdan himoya\n"
                                            f"- GPS: Dual-frequency (L1+L5)\n"
                                            f"- Sensorlar: Yurak urishi, SpO2, ECG, harorat, chuqurlik o‘lchagich\n"
                                            f"- Material: Titanium, sapphire kristalli ekran\n"
                                            f"- <b>Narxi</b>: $ 789",                                   
                                            photo="https://i.ytimg.com/vi/qiNTVerJSTM/maxresdefault.jpg",
                                            reply_markup=IWatch_Ultra_3_menu)



@dp.callback_query_handler(text="IWatch_mune")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption="IWatch\n",
                                    photo="https://staticg.sportskeeda.com/editor/2022/09/b75d6-16625727337695-1920.jpg",
                                    reply_markup=IWatch_mune)
    

@dp.callback_query_handler(text="main_menu")
async def show_iphone_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"Apple Store",
                            photo="https://i.pinimg.com/originals/7e/0f/64/7e0f64e278cabce4752abac1d8432389.jpg",
                            reply_markup=main_menu)
    

#=========================================IWatch Series 11===================================================================================================================================================================================
@dp.callback_query_handler(text="Iwatch series 11")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Iwatch series 11</b>\n"
                                            f"Apple IWatch Series 11 (2025)\n"
                                            f"- Chip: Apple S10 SiP\n"
                                            f"- Saqlash: 64 GB\n"
                                            f"- Displey: 42/46 mm LTPO OLED, 2000 nit\n"
                                            f"- Batareya: ~24 soat (Low Power’da uzoqroq)\n"
                                            f"- Funksiyalar: ECG, SpO2, uyqu kuzatuvchi, yurak urishi\n"
                                            f"- Chidamlilik: 50 m suv, kuchliroq Ion-X shisha\n"
                                            f"- Material: Alyuminiy va titaniy variantlar\n"
                                            f"- <b>Narxi</b>: $ 399",                         
                                            photo="https://citymagazine.b-cdn.net/wp-content/uploads/2025/06/hero-apple-watch-11-blue-color-2025-0-jpg.webp",
                                            reply_markup=IWatch_Series_11_menu)
    

#=========================================IWatch SE 3===================================================================================================================================================================================
@dp.callback_query_handler(text="Iwatch se 3")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>IWatch SE 3</b>\n"
                                            f"Apple IWatch SE 3 (2025)\n"
                                            f"- Chip: Apple S10 SiP\n"
                                            f"- O‘lcham: 40mm / 44mm\n"
                                            f"- Displey: Retina OLED\n"
                                            f"- Batareya: ~18 soat\n"
                                            f"- Funksiyalar: Yurak urishi, uyqu kuzatuvchi, asosiy sog‘liq sensorlari\n"
                                            f"- Material: Alyuminiy\n"
                                            f"- <b>Narxi</b>: $ 249",
                                            photo="https://www.apple.com/v/apple-watch-se-3/a/images/overview/product-viewer/product_landing__fn9ldzg4foey_large_2x.jpg",
                                            reply_markup=IWatch_SE_3_menu)



#=========================================IWatch Series 10===================================================================================================================================================================================
@dp.callback_query_handler(text="Iwatch series 10")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>IWatch Series 10</b>\n"
                                            f"<b>Apple IWatch Series 10</b>\n"
                                            f"- Chip: S10 SiP\n"
                                            f"- Xotira: 64 GB\n"
                                            f"- Displey: LTPO OLED, 2000 nit\n"
                                            f"- O‘lcham: 42 mm / 46 mm\n"
                                            f"- Chidamlilik: 50 m suv, IP6X\n"
                                            f"- Sensorlar: Yurak urishi, ECG, SpO₂, harorat\n"
                                            f"- Batareya: 18 soat (36 soat Low Power Mode)\n"
                                            f"- <b>Narxi</b>: $ 399",
                                            photo="https://microless.com/cdn/products/072a62ae7e42049bb20667bfd57b400c-md.jpg",
                                            reply_markup=IWatch_Series_10_menu)


#=========================================IWatch Ultra 2===================================================================================================================================================================================
@dp.callback_query_handler(text="Iwatch ultra 2")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>IWatch Ultra 2</b>\n"
                                            f"Apple IWatch Ultra 2\n"  
                                            f"- Chip: S9, 64 GB\n"  
                                            f"- Ekran: 1.92″ Retina OLED, 3000 nit\n"  
                                            f"- O‘lcham: 49 mm, titan korpus\n"  
                                            f"- Himoya: IP6X, WR100, MIL-STD-810\n"  
                                            f"- Sensorlar: Yurak, ECG, SpO₂, harorat, chuqurlik\n" 
                                            f"- Batareya: 36 soat (72 soat Low Power)\n"  
                                            f"- Qo‘shimcha: Action Button, siren, double-tap gesture\n" 
                                            f"- <b>Narxi</b>: $ 799", 
                                            photo="https://cdn.mgig.fr/2024/09/mg-2b59a347-w2600.jpg",
                                            reply_markup=IWatch_Ultra_2_menu)
    

#=========================================IWatch Series 9===================================================================================================================================================================================
@dp.callback_query_handler(text="Iwatch series 9")
async def show_Iwatch_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Iwatch Series 9</b>\n"
                                            f"Apple IWatch Series 9\n"  
                                            f"- Chip: S9 SiP\n"  
                                            f"- Saqlash: 64 GB\n"  
                                            f"- Displey: 1.9, Retina LTPO OLED, 2000 nit\n" 
                                            f"- O‘lchamlar: 41 mm / 45 mm\n" 
                                            f"- Himoya: 50 m suvga chidamlilik, IP6X chang himoyasi\n" 
                                            f"- Sensorlar: yurak urishi, ECG, SpO₂, harorat, kompas, always-on altimetr \n"
                                            f"- Batareya: ~18 soat oddiy ishlash, ~36 soat Low Power rejimida\n" 
                                            f"- <b>Narxi</b>: $ 399",
                                            photo="https://cdn1.ozone.ru/s3/multimedia-p/c600/6762621517.jpg",
                                            reply_markup=IWatch_Series_9_menu)


#=========================================Accessories===================================================================================================================================================================================
@dp.callback_query_handler(text="access")
async def show_Access_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Accessories</b>\n",
                                    photo="https://cdn.dsmcdn.com/seller-store/uploads/105150/e45cf2a1-60fa-45bd-941d-7e8b196622ef.jpg",
                                    reply_markup=Access_menu)


#=========================================Airpods===================================================================================================================================================================================  
@dp.callback_query_handler(text="airpods")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods</b>\n",
                                    photo="https://9to5mac.com/wp-content/uploads/sites/6/2021/10/Screen-Shot-2021-10-18-at-1.14.27-PM.jpg",
                                    reply_markup=Airpods_menu)
    

#=========================================Airpods Max===================================================================================================================================================================================  
@dp.callback_query_handler(text="max")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods Max</b>\n"
                                            f"Model: AirPods Max\n"
                                            f"-Chip: Apple H1 (har bir quloqchinda)\n"
                                            f"-ANC: Active Noise Cancellation\n"
                                            f"-Transparency: Transparency mode\n"
                                            f"-Audio: Spatial Audio + Dynamic Head Tracking\n"
                                            f"-Design: Memory foam ear cushions, mesh headband\n"
                                            f"-Battery: ~20 soat (ANC/Spatial Audio bilan)\n"
                                            f"-Charge: Lightning port + Smart Case\n"
                                            f"-Features: Siri qo‘llab-quvvatlash\n"
                                            f"-<b>Narxi</b>: $ 549",
                                            photo="https://s3files.core77.com/blog/images/1115225_81_103579_bNgFP3rac.jpg",
                                            reply_markup=AirPods_Max)
    

#=========================================Airpods Pro===================================================================================================================================================================================  
@dp.callback_query_handler(text="pro")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods Pro 2</b>\n"
                                            f"Model: AirPods Pro 2 (USB-C)\n"
                                            f"-Chip: Apple H2\n"
                                            f"-ANC: Active Noise Cancellation\n"
                                            f"-Transparency: Adaptive Transparency\n"
                                            f"-Audio: Personalized Spatial Audio\n"
                                            f"-Case: MagSafe + USB-C charging\n"
                                            f"-Battery: ~6 soat (quloqchin), 30 soat (quti bilan)\n"
                                            f"-Features: IP54 (suv va changdan himoya), Siri qo‘llab-quvvatlash\n"
                                            f"-<b>Narxi</b>: $ 249",
                                            photo="https://avatars.mds.yandex.net/get-mpic/4034173/img_id1971319845272491560.png/orig",
                                            reply_markup=AirPods_Pro)



@dp.callback_query_handler(text="Airpods_menu")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods</b>\n",
                                    photo="https://9to5mac.com/wp-content/uploads/sites/6/2021/10/Screen-Shot-2021-10-18-at-1.14.27-PM.jpg",
                                    reply_markup=Airpods_menu)
    

@dp.callback_query_handler(text="Access_menu")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Accessories</b>\n",
                                    photo="https://cdn.dsmcdn.com/seller-store/uploads/105150/e45cf2a1-60fa-45bd-941d-7e8b196622ef.jpg",
                                    reply_markup=Access_menu)
    

#=========================================Airpods 3===================================================================================================================================================================================  
@dp.callback_query_handler(text="air")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods 3</b>\n"
                                            f"Model: AirPods 3 (3rd Gen)\n"
                                            f"-Chip: Apple H1\n"
                                            f"-ANC: Yo‘q\n"
                                            f"-Transparency: Yo‘q\n"
                                            f"-Audio: Spatial Audio + Dynamic Head Tracking\n"
                                            f"-Battery: ~6 soat (quloqchin), 30 soat (quti bilan)\n"
                                            f"-Case: MagSafe/Wireless charging\n"
                                            f"-Design: In-ear, qisqaroq sopka\n"
                                            f"-Features: Siri qo‘llab-quvvatlash, terga chidamli (IPX4)\n"
                                            f"-<b>Narxi</b>: $ 179",
                                            photo="https://www.apple.com/newsroom/images/product/airpods/standard/Apple_AirPods-3rd-gen_iPhone-13-pairing_10182021_inline.jpg.large.jpg",
                                            reply_markup=AirPods_3)
    

#=========================================Airpods 2===================================================================================================================================================================================  
@dp.callback_query_handler(text="ikki")
async def show_Airpods_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Airpods 2</b>\n"
                                            f"Model: AirPods 2 (2nd Gen)\n"
                                            f"-Chip: Apple H1\n"
                                            f"-ANC: Yo‘q\n"
                                            f"-Transparency: Yo‘q\n"
                                            f"-Audio: Oddiy stereo audio\n"
                                            f"-Battery: ~5 soat (quloqchin), 24 soat (quti bilan)\n"
                                            f"-Case: Lightning charging case (Wireless opsiya ham bor)\n"
                                            f"-Design: Classic uzun sopkali\n"
                                            f"-Features: Siri qo‘llab-quvvatlash, tezkor ulanish\n"
                                            f"-<b>Narxi</b>: $ 129",
                                            photo="https://i.ytimg.com/vi/jkUMblxVV5c/maxresdefault.jpg",
                                            reply_markup=AirPods_2)
    

#=========================================Mouse=================================================================================================================================================================================== 
@dp.callback_query_handler(text="mouse")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Mouse</b>\n",
                                            photo="https://sc01.alicdn.com/kf/Hc205b56885cc4c39adc103f45d218ec5E/223470067/Hc205b56885cc4c39adc103f45d218ec5E.jpg",
                                            reply_markup=mouse_menu)


#=========================================Magic Mouse 3=================================================================================================================================================================================== 
@dp.callback_query_handler(text="mouse3")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Magic Mouse 3</b>\n"
                                            f"Model: Magic Mouse 3 (USB-C, 2024)\n"
                                            f"-Ulanish: Bluetooth + USB-C\n"
                                            f"-Sirt: Multi-Touch\n"
                                            f"-Og'irlik: ≈ 99 g\n"
                                            f"-O'lcham: 2.16 × 5.71 × 11.35 cm\n"
                                            f"-Quvvat: Ichki zaryadlanadigan batareya\n"
                                            f"-<b>Narx</b>: $99",
                                            photo="https://cdn1.ozone.ru/s3/multimedia-1-k/c600/7280423192.jpg",
                                            reply_markup=Magic_Mouse_3)



@dp.callback_query_handler(text="mouse_menu")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Mouse</b>\n",
                                    photo="https://sc01.alicdn.com/kf/Hc205b56885cc4c39adc103f45d218ec5E/223470067/Hc205b56885cc4c39adc103f45d218ec5E.jpg",
                                    reply_markup=mouse_menu)
    

#=========================================Magic Mouse 2=================================================================================================================================================================================== 
@dp.callback_query_handler(text="mouse2")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Magic Mouse 2</b>\n"
                                            f"Magic Mouse 2\n"  
                                            f"- Multi-Touch sirt, gesture qo‘llab-quvvatlaydi\n"  
                                            f"- O‘rnatilgan qayta zaryadlanadigan batareya\n"  
                                            f"- Bluetooth, Lightning port orqali zaryad\n"  
                                            f"- O‘lchami: 11.35 × 5.71 × 2.16 sm\n"  
                                            f"- Og‘irligi: ~99 g\n" 
                                            f"- <b>Narxi</b>: $ 79",
                                            photo="https://i.ytimg.com/vi/qn6fz_6_fcw/maxresdefault.jpg",
                                            reply_markup=Magic_Mouse_2)
    

#=========================================Magic Mouse 1=================================================================================================================================================================================== 
@dp.callback_query_handler(text="mouse1")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Magic Mouse 1</b>\n"
                                            f"Magic Mouse 1\n"  
                                            f"- Ishlab chiqarilgan: 2009 yil\n"  
                                            f"- Batareya: 2× AA batareyada ishlaydi\n"  
                                            f"- Bog‘lanish: Bluetooth 2.1 + EDR\n"  
                                            f"- Surface: Multi-Touch, sahifalar va hujjatlar orasida siljitish\n" 
                                            f"- O‘lchami: 11.35 × 5.71 × 2.16 sm\n"  
                                            f"- Og‘irligi: ~105 g (batareya bilan)\n"  
                                            f"- <b>Narxi</b>: $ 40",
                                            photo="https://5x86.ru/pic/big/1606566.jpg",
                                            reply_markup=Magic_Mouse_1)
    

#=========================================Mighty Mouse=================================================================================================================================================================================== 
@dp.callback_query_handler(text="mighty_mouse")
async def show_Mouse_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Mighty Mouse</b>\n"
                                            f"Mighty Mouse\n" 
                                            f"- Chiqarilgan: 2005 yil\n"  
                                            f"- Bog‘lanish: USB (simli) va keyinchalik Bluetooth (simli/simsiz versiyalari)\n"  
                                            f"- Scroll: 360° to‘liq aylanish imkoniyatiga ega kichik scroll ball\n"  
                                            f"- Tugmalar: Chap, o‘ng, yon tugmalar (bosim sezuvchi sensorlar)\n"  
                                            f"- Dizayn: Oq rangli, simmetrik (chap/o‘ng qo‘l uchun)\n"  
                                            f"- Og‘irligi: ~105 g\n"  
                                            f"- <b>Narxi</b>: $ 20",
                                            photo="https://i.ebayimg.com/images/g/7t0AAOSwzIxnvz~-/s-l1600.jpg",
                                            reply_markup=Mighty_Mouse)
    

#=========================================keyboard=================================================================================================================================================================================== 
@dp.callback_query_handler(text="keyboard")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Keyboard</b>\n",
                                    photo="https://cdn.pixabay.com/photo/2016/01/27/19/41/mac-1165191_1280.jpg",
                                    reply_markup=Keyboard_menu)
    
#=========================================magic keyboard=================================================================================================================================================================================== 
@dp.callback_query_handler(text="magic keyboard")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Magic Keyboard</b>\n"
                                            f"⌨️ Magic Keyboard\n"  
                                            f"- Ulanish: Bluetooth, USB-C\n"  
                                            f"- Bateriya: Ichki, uzoq muddat\n"  
                                            f"- Variantlari: Oddiy, Numeric Keypad, Touch ID\n"  
                                            f"- Tugmalar: Past profil, jim bosiladi\n"  
                                            f"- Moslik: Mac, iPad, iPhone\n"  
                                            f"- Dizayn: Ingichka, alyuminiy, oq/space gray\n"  
                                            f"- <b>Narxi</b>: $ 199",
                                            photo="https://40.img.avito.st/image/1/1.LD19mba5gNRLMELRKYVmcq46ht7JuogWzDqC0MEwitY.oBWglsbrXwlCcOSbnGlW2tUuYpIx9TriPGE0YkGtjgs",
                                            reply_markup=Magic_Keyboard)
    

@dp.callback_query_handler(text="Keyboard_menu")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Keyboard</b>\n",
                                    photo="https://cdn.pixabay.com/photo/2016/01/27/19/41/mac-1165191_1280.jpg",
                                    reply_markup=Keyboard_menu)
    

#=========================================ipad keyboard=================================================================================================================================================================================== 
@dp.callback_query_handler(text="ipad keyboard")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>iPad Keyboard</b>\n"
                                            f"📱 Magic Keyboard for iPad\n"  
                                            f"- Moslik: iPad Pro va iPad Air (yangi modellari)\n"  
                                            f"- Ulanish: Smart Connector (Bluetooth kerak emas)\n"  
                                            f"- Dizayn: Himoya qopqoq + klaviatura, trackpad bilan\n"  
                                            f"- Tugmalar: Orqa yoritilgan, past profil, qulay yozish\n"  
                                            f"- Burchak: 130° gacha sozlanadigan magnitli holat\n"  
                                            f"- Zaryad: iPad orqali ishlaydi, USB-C porti mavjud\n"  
                                            f"- Afzallik: iPadni to‘liq “noutbuk”ga aylantiradi\n"
                                            f"- <b>Narxi</b>: $ 229",  
                                            photo="https://www.iphones.ru/wp-content/plugins/wonderm00ns-simple-facebook-open-graph-tags/fbimg.php?img=https%3A%2F%2Fwww.iphones.ru%2Fwp-content%2Fuploads%2F2021%2F05%2FC45E1007-A475-42AF-B8B2-5A9C619145B2.jpeg",
                                            reply_markup=iPad_Keyboard)
    

#=========================================Apple Wireless Keyboard=================================================================================================================================================================================== 
@dp.callback_query_handler(text="wireless keyboard")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Wireless Keyboard</b>\n"
                                            f"⌨️ Apple Wireless Keyboard\n"
                                            f"- Ulanish: Bluetooth (sim-siz)\n"
                                            f"- Quvvat: 2 dona AA batareya bilan ishlaydi\n"
                                            f"- Moslik: Mac, iPad, iPhone\n"
                                            f"- Dizayn: Alyuminiy korpus, oq tugmalar\n"
                                            f"- Tugmalar: Past profil, jim bosiladi\n"
                                            f"- Afzalliklari: Ixcham, yengil, portativ\n"
                                            f"- Kamchilik: Yangi Magic Keyboard’ga qaraganda eskirgan\n"
                                            f"- <b>Narxi</b>: $ 129",  
                                            photo="https://m.media-amazon.com/images/I/71TYTXwcniL.jpg",
                                            reply_markup=Wireless_Keyboard)
    

#=========================================Magic Keyboard Folio=================================================================================================================================================================================== 
@dp.callback_query_handler(text="folio keyboard")
async def show_keyboard_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Magic Keyboard Folio</b>\n"
                                            f"📱 Magic Keyboard Folio\n"  
                                            f"- Ulanish: Bluetooth (sim-siz)\n"  
                                            f"-Mosligi: iPad 10th Gen\n"                     
                                            f"-Dizayn: 2 qismli, magnitli\n"  
                                            f"-Tugmalar: Scissor, 1mm travel\n"  
                                            f"-Trackpad: Katta, Multi-Touch\n"  
                                            f"-Qo‘shimcha: Shortcut qatori\n"  
                                            f"-<b>Narxi</b>: $ 229", 
                                            photo="https://www.bhphotovideo.com/images/fb/apple_mqdp3ll_a_magic_keyboard_folio_for_1731167.jpg",
                                            reply_markup=Folio_Keyboard) 
    

#=========================================Powerbank===================================================================================================================================================================================
@dp.callback_query_handler(text="power")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Powerbank</b>\n",
                                    photo="https://cdn1.ozone.ru/s3/multimedia-6/c600/6329215290.jpg",
                                    reply_markup=Powerbank_menu)
    

#=========================================Anker MagGo 5K===================================================================================================================================================================================
@dp.callback_query_handler(text="maggo")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Anker MagGo 5K</b>\n"
                                            f"🔋 Anker MagGo 5K\n"  
                                            f"-Sig‘imi: 5000 mAh\n"  
                                            f"-Simsiz zaryad: 15W (Qi2)\n"  
                                            f"-USB-C: 20W chiqish\n"  
                                            f"-Og‘irligi: 122 g\n"  
                                            f"-<b>Narxi</b>: $ 49",
                                            photo="https://ffrefills.com/wp-content/uploads/2022/02/powercoremaggo5k.jpg",
                                            reply_markup=maggo_menu)
    

@dp.callback_query_handler(text="Powerbank_menu")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Powerbank</b>\n",
                                    photo="https://static.4u.am/origin/product/1024/3HIiPXIHw335czqs.jpg",
                                    reply_markup=Powerbank_menu)
    

#=========================================Apple MagSafe Battery Pack===================================================================================================================================================================================
@dp.callback_query_handler(text="pack")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Apple MagSafe Battery Pack</b>\n"
                                            f"🔋 Apple MagSafe Battery Pack\n"  
                                            f"-Sig‘im: 1,460 mAh (~11 Wh)\n"  
                                            f"-Simsiz zaryad: 7.5W (15W adapter bilan)\n"  
                                            f"-Og‘irligi: 114 g, qalinligi 11 mm\n"    
                                            f"-Mosligi: iPhone 12, 13, 14, 15 seriyalari\n"  
                                            f"-<b>Narxi</b>: $ 99",
                                            photo="https://i.ebayimg.com/images/g/R3QAAOSw00BlO9y~/s-l1200.png",
                                            reply_markup=pack_menu)
    

#=========================================Torras MiniMag===================================================================================================================================================================================
@dp.callback_query_handler(text="minimag")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Torras MiniMag</b>\n"
                                            f"🔋 Torras MiniMag\n"  
                                            f"-5,000 mAh\n"  
                                            f"-Simsiz zaryad Qi-mos (MagSafe)\n"  
                                            f"-USB-C ~18W chiqish\n"  
                                            f"-Og‘irligi ~115 g\n"  
                                            f"-<b>Narxi</b>: $ 39", 
                                            photo="https://images-na.ssl-images-amazon.com/images/I/61HrSosTbzL._AC_UL600_SR600,400_.jpg",
                                            reply_markup=minimag_menu)


#=========================================Benks ArmorGo===================================================================================================================================================================================
@dp.callback_query_handler(text="armorgo")
async def show_power_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption=f"<b>Benks ArmorGo</b>\n"
                                            f"🔋 Benks ArmorGo\n"  
                                            f"-Sig‘im: 5000/10000 mAh\n"  
                                            f"-Simsiz: MagSafe 15W\n"  
                                            f"-USB-C: 22.5W\n"  
                                            f"-Material: Aramid fiber\n"  
                                            f"-<b>Narxi</b>: $ 50", 
                                            photo="https://m.media-amazon.com/images/I/71hr-NIFwKL._UF894%2C1000_QL80_.jpg",
                                            reply_markup=armorgo_menu)
