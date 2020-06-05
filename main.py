import telebot

import time

from telebot import types

#Bot token for gymfinder10 which is currently running on my home machine

#bot_token = 'removed'

#bot token for gymfinder 20 which i am currently testing with

bot_token = '1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI'

bot = telebot.TeleBot(bot_token)



@bot.message_handler(commands=['start'])

def send_welcome(message):

bot.reply_to(message, "welcome")



@bot.message_handler(commands=['location1'])

def send_welcome(message):

bot.reply_to(message, "location1 https://www.google.com/maps/search/?api=1&query=49.262628,-122.756295")



@bot.message_handler(commands=['a_man_and_his_horse'])

def send_welcome(message):

bot.reply_to(message, "a man and his horse https://www.google.com/maps/search/?api=1&query=49.262628,-122.756295")



@bot.message_handler(commands=['air_raid'])

def send_welcome(message):

bot.reply_to(message, "air raid https://www.google.com/maps/search/?api=1&query=49.276604,-122.85638")



@bot.message_handler(commands=['aspenwood_park'])

def send_welcome(message):

bot.reply_to(message, "aspenwood park https://www.google.com/maps/search/?api=1&query=49.301891,-122.829417")



@bot.message_handler(commands=['bigfoot'])

def send_welcome(message):

bot.reply_to(message, "bigfoot https://www.google.com/maps/search/?api=1&query=49.270679,-122.79089")



@bot.message_handler(commands=['blake_village_arch'])

def send_welcome(message):

bot.reply_to(message, "blake village arch https://www.google.com/maps/search/?api=1&query=49.291325,-122.748269")



@bot.message_handler(commands=['central_flower_box'])

def send_welcome(message):

bot.reply_to(message, "central flower box https://www.google.com/maps/search/?api=1&query=49.256024,-122.778776")



@bot.message_handler(commands=['central_park'])

def send_welcome(message):

bot.reply_to(message, "central park https://www.google.com/maps/search/?api=1&query=49.256274,-122.784292")



@bot.message_handler(commands=['chelsea_park'])

def send_welcome(message):

bot.reply_to(message, "chelsea park https://www.google.com/maps/search/?api=1&query=49.2823658,-122.750856")



@bot.message_handler(commands=['coquitlam_alliance_church'])

def send_welcome(message):

bot.reply_to(message, "coquitlam alliance church https://www.google.com/maps/search/?api=1&query=49.263306,-122.817135")



@bot.message_handler(commands=['coquitlam_central_station'])

def send_welcome(message):

bot.reply_to(message, "coquitlam central station https://www.google.com/maps/search/?api=1&query=49.273904,-122.799352")



@bot.message_handler(commands=['coq_christ_church_of_china'])

def send_welcome(message):

bot.reply_to(message, "coq christ church of china https://www.google.com/maps/search/?api=1&query=49.263479,-122.83928")



@bot.message_handler(commands=['coquitlam_christian_centre'])

def send_welcome(message):

bot.reply_to(message, "coquitlam christian centre https://www.google.com/maps/search/?api=1&query=49.279102,-122.813909")



@bot.message_handler(commands=['coquitlam_station_transit_map'])

def send_welcome(message):

bot.reply_to(message, "coquitlam station transit map https://www.google.com/maps/search/?api=1&query=49.275642,-122.798515")



@bot.message_handler(commands=['cpr_box'])

def send_welcome(message):

bot.reply_to(message, "cpr box https://www.google.com/maps/search/?api=1&query=49.277908,-122.858785")



@bot.message_handler(commands=['cunnings_field'])

def send_welcome(message):

bot.reply_to(message, "cunnings field https://www.google.com/maps/search/?api=1&query=49.291159,-122.788433")



@bot.message_handler(commands=['davison_park'])

def send_welcome(message):

bot.reply_to(message, "davison park https://www.google.com/maps/search/?api=1&query=49.283967,-122.752987")



@bot.message_handler(commands=['day_in_the_park_electrical_box'])

def send_welcome(message):

bot.reply_to(message, "day in the park electrical box https://www.google.com/maps/search/?api=1&query=49.286922,-122.790836")



@bot.message_handler(commands=['eagle_ridge_hospital_fountain'])

def send_welcome(message):

bot.reply_to(message, "eagle ridge hospital fountain https://www.google.com/maps/search/?api=1&query=49.285489,-122.823027")



@bot.message_handler(commands=['eagle_ridge_united_church'])

def send_welcome(message):

bot.reply_to(message, "eagle ridge united church https://www.google.com/maps/search/?api=1&query=49.282924,-122.807609")



@bot.message_handler(commands=['elks_park'])

def send_welcome(message):

bot.reply_to(message, "elks park https://www.google.com/maps/search/?api=1&query=49.25827,-122.780644")



@bot.message_handler(commands=['experience_our_spirit'])

def send_welcome(message):

bot.reply_to(message, "experience our spirit https://www.google.com/maps/search/?api=1&query=49.266177,-122.777389")



@bot.message_handler(commands=['forest_wrap'])

def send_welcome(message):

bot.reply_to(message, "forest wrap https://www.google.com/maps/search/?api=1&query=49.293106,-122.756077")



@bot.message_handler(commands=['glass_art'])

def send_welcome(message):

bot.reply_to(message, "glass art https://www.google.com/maps/search/?api=1&query=49.279022,-122.799384")



@bot.message_handler(commands=['green_space_in_an_urban_env'])

def send_welcome(message):

bot.reply_to(message, "green space in an urban env https://www.google.com/maps/search/?api=1&query=49.285336,-122.815424")



@bot.message_handler(commands=['harrier_tot_lot_park'])

def send_welcome(message):

bot.reply_to(message, "harrier tot lot park https://www.google.com/maps/search/?api=1&query=49.280935,-122.816447")



@bot.message_handler(commands=['heritage_museum_and_archives'])

def send_welcome(message):

bot.reply_to(message, "heritage museum and archives https://www.google.com/maps/search/?api=1&query=49.26217,-122.779813")



@bot.message_handler(commands=['hidden_fountain_box'])

def send_welcome(message):

bot.reply_to(message, "hidden fountain box https://www.google.com/maps/search/?api=1&query=49.292382,-122.782246")



@bot.message_handler(commands=['hist_trail_marker_lions_park'])

def send_welcome(message):

bot.reply_to(message, "hist trail marker lions park https://www.google.com/maps/search/?api=1&query=49.266137,-122.780679")



@bot.message_handler(commands=['hoy_creek_trail_sign'])

def send_welcome(message):

bot.reply_to(message, "hoy creek trail sign https://www.google.com/maps/search/?api=1&query=49.28695,-122.794787")



@bot.message_handler(commands=['hyde_creek_education_center'])

def send_welcome(message):

bot.reply_to(message, "hyde creek education center https://www.google.com/maps/search/?api=1&query=49.276709,-122.75583")



@bot.message_handler(commands=['hyde_creek_nature_reserve'])

def send_welcome(message):

bot.reply_to(message, "hyde creek nature reserve https://www.google.com/maps/search/?api=1&query=49.282772,-122.738727")



@bot.message_handler(commands=['hyde_creek_recreation_centre'])

def send_welcome(message):

bot.reply_to(message, "hyde creek recreation centre https://www.google.com/maps/search/?api=1&query=49.275347,-122.751431")



@bot.message_handler(commands=['info_tiles'])

def send_welcome(message):

bot.reply_to(message, "info tiles https://www.google.com/maps/search/?api=1&query=49.278958,-122.850683")



@bot.message_handler(commands=['jaks_beer_wine_spirits'])

def send_welcome(message):

bot.reply_to(message, "jaks beer wine spirits https://www.google.com/maps/search/?api=1&query=49.276505,-122.792852")



@bot.message_handler(commands=['korean_frog'])

def send_welcome(message):

bot.reply_to(message, "korean frog https://www.google.com/maps/search/?api=1&query=49.299372,-122.760475")



@bot.message_handler(commands=['kyle_park'])

def send_welcome(message):

bot.reply_to(message, "kyle park https://www.google.com/maps/search/?api=1&query=49.275595,-122.856448")



@bot.message_handler(commands=['lafarge_lake'])

def send_welcome(message):

bot.reply_to(message, "lafarge lake https://www.google.com/maps/search/?api=1&query=49.286553,-122.789976")



@bot.message_handler(commands=['maple_creek_park'])

def send_welcome(message):

bot.reply_to(message, "maple creek park https://www.google.com/maps/search/?api=1&query=49.284293,-122.778188")



@bot.message_handler(commands=['metal_tree'])

def send_welcome(message):

bot.reply_to(message, "metal tree https://www.google.com/maps/search/?api=1&query=49.280479,-122.848558")



@bot.message_handler(commands=['millard_park'])

def send_welcome(message):

bot.reply_to(message, "millard park https://www.google.com/maps/search/?api=1&query=49.29628,-122.757598")



@bot.message_handler(commands=['mundy_park_east_entrance'])

def send_welcome(message):

bot.reply_to(message, "mundy park east entrance https://www.google.com/maps/search/?api=1&query=49.255736,-122.81671")



@bot.message_handler(commands=['mural_of_thrift'])

def send_welcome(message):

bot.reply_to(message, "mural of thrift https://www.google.com/maps/search/?api=1&query=49.277479,-122.805678")



@bot.message_handler(commands=['mysterious_saxophone_player'])

def send_welcome(message):

bot.reply_to(message, "mysterious saxophone player https://www.google.com/maps/search/?api=1&query=49.272501,-122.802818")



@bot.message_handler(commands=['nahanni_water_fountain'])

def send_welcome(message):

bot.reply_to(message, "nahanni water fountain https://www.google.com/maps/search/?api=1&query=49.27907,-122.832966")



@bot.message_handler(commands=['nestor_park'])

def send_welcome(message):

bot.reply_to(message, "nestor park https://www.google.com/maps/search/?api=1&query=49.290654,-122.778577")



@bot.message_handler(commands=['north_side_church_kingsway'])

def send_welcome(message):

bot.reply_to(message, "north side church kingsway https://www.google.com/maps/search/?api=1&query=49.265542,-122.787152")



@bot.message_handler(commands=['northside_church_david'])

def send_welcome(message):

bot.reply_to(message, "northside church david https://www.google.com/maps/search/?api=1&query=49.293989,-122.813814")



@bot.message_handler(commands=['old_mill_boathouse'])

def send_welcome(message):

bot.reply_to(message, "old mill boathouse https://www.google.com/maps/search/?api=1&query=49.279842,-122.850553")



@bot.message_handler(commands=['old_times'])

def send_welcome(message):

bot.reply_to(message, "old times https://www.google.com/maps/search/?api=1&query=49.276464,-122.834703")



@bot.message_handler(commands=['orchard_mason_bee_house'])

def send_welcome(message):

bot.reply_to(message, "orchard mason bee house https://www.google.com/maps/search/?api=1&query=49.286018,-122.784835")



@bot.message_handler(commands=['painted_electrical_box'])

def send_welcome(message):

bot.reply_to(message, "painted electrical box https://www.google.com/maps/search/?api=1&query=49.286755,-122.790351")



@bot.message_handler(commands=['panorama_park'])

def send_welcome(message):

bot.reply_to(message, "panorama park https://www.google.com/maps/search/?api=1&query=49.30074,-122.797998")



@bot.message_handler(commands=['poco_motion'])

def send_welcome(message):

bot.reply_to(message, "poco motion https://www.google.com/maps/search/?api=1&query=49.260584,-122.790882")



@bot.message_handler(commands=['port_coquitlam_cemetery'])

def send_welcome(message):

bot.reply_to(message, "port coquitlam cemetery https://www.google.com/maps/search/?api=1&query=49.28603,-122.767048")



@bot.message_handler(commands=['port_moody_orca'])

def send_welcome(message):

bot.reply_to(message, "port moody orca https://www.google.com/maps/search/?api=1&query=49.280357,-122.828342")



@bot.message_handler(commands=['port_moody_station_museum'])

def send_welcome(message):

bot.reply_to(message, "port moody station museum https://www.google.com/maps/search/?api=1&query=49.279292,-122.850667")



@bot.message_handler(commands=['port_moody_west_coast_station'])

def send_welcome(message):

bot.reply_to(message, "port moody west coast station https://www.google.com/maps/search/?api=1&query=49.277993,-122.846288")



@bot.message_handler(commands=['ranch_park_north_entrance_sign'])

def send_welcome(message):

bot.reply_to(message, "ranch park north entrance sign https://www.google.com/maps/search/?api=1&query=49.26579,-122.805887")



@bot.message_handler(commands=['riparian_areas_natures_highways'])

def send_welcome(message):

bot.reply_to(message, "riparian areas natures highways https://www.google.com/maps/search/?api=1&query=49.281864,-122.777951")



@bot.message_handler(commands=['riverbend_salmon_statue'])

def send_welcome(message):

bot.reply_to(message, "riverbend salmon statue https://www.google.com/maps/search/?api=1&query=49.263185,-122.790029")



@bot.message_handler(commands=['robot_attack'])

def send_welcome(message):

bot.reply_to(message, "robot attack https://www.google.com/maps/search/?api=1&query=49.279152,-122.847419")



@bot.message_handler(commands=['robson_park'])

def send_welcome(message):

bot.reply_to(message, "robson park https://www.google.com/maps/search/?api=1&query=49.298954,-122.787328")



@bot.message_handler(commands=['robson_park_tot_lot'])

def send_welcome(message):

bot.reply_to(message, "robson park tot lot https://www.google.com/maps/search/?api=1&query=49.299537,-122.786526")



@bot.message_handler(commands=['salmon_mural'])

def send_welcome(message):

bot.reply_to(message, "salmon mural https://www.google.com/maps/search/?api=1&query=49.26191,-122.781175")



@bot.message_handler(commands=['shaughnessy_bike_skills_park'])

def send_welcome(message):

bot.reply_to(message, "shaughnessy bike skills park https://www.google.com/maps/search/?api=1&query=49.275289,-122.774517")



@bot.message_handler(commands=['sheila_barrett_park'])

def send_welcome(message):

bot.reply_to(message, "sheila barrett park https://www.google.com/maps/search/?api=1&query=49.274981,-122.78988")



@bot.message_handler(commands=['site_of_st_clare_of_assisi'])

def send_welcome(message):

bot.reply_to(message, "site of st clare of assisi https://www.google.com/maps/search/?api=1&query=49.291724,-122.80087")



@bot.message_handler(commands=['south_side_church'])

def send_welcome(message):

bot.reply_to(message, "south side church https://www.google.com/maps/search/?api=1&query=49.254263,-122.778857")



@bot.message_handler(commands=['space_ship_mural'])

def send_welcome(message):

bot.reply_to(message, "space ship mural https://www.google.com/maps/search/?api=1&query=49.272326,-122.755513")



@bot.message_handler(commands=['sports'])

def send_welcome(message):

bot.reply_to(message, "sports https://www.google.com/maps/search/?api=1&query=49.271297,-122.767298")



@bot.message_handler(commands=['st_catherines_anglican_church'])

def send_welcome(message):

bot.reply_to(message, "st catherines anglican church https://www.google.com/maps/search/?api=1&query=49.271696,-122.775895")



@bot.message_handler(commands=['street_art'])

def send_welcome(message):

bot.reply_to(message, "street art https://www.google.com/maps/search/?api=1&query=49.259869,-122.757332")



@bot.message_handler(commands=['terry_fox_statue'])

def send_welcome(message):

bot.reply_to(message, "terry fox statue https://www.google.com/maps/search/?api=1&query=49.26075,-122.778331")



@bot.message_handler(commands=['the_coquitlam_crunch_07_k_mark'])

def send_welcome(message):

bot.reply_to(message, "the coquitlam crunch 07 k mark https://www.google.com/maps/search/?api=1&query=49.297616,-122.815484")



@bot.message_handler(commands=['the_kingdom_hall'])

def send_welcome(message):

bot.reply_to(message, "the kingdom hall https://www.google.com/maps/search/?api=1&query=49.294888,-122.780716")



@bot.message_handler(commands=['tidal_train'])

def send_welcome(message):

bot.reply_to(message, "tidal train https://www.google.com/maps/search/?api=1&query=49.282231,-122.829341")



@bot.message_handler(commands=['tot_lot'])

def send_welcome(message):

bot.reply_to(message, "tot lot https://www.google.com/maps/search/?api=1&query=49.300533,-122.810478")



@bot.message_handler(commands=['town_centre_park'])

def send_welcome(message):

bot.reply_to(message, "town centre park https://www.google.com/maps/search/?api=1&query=49.292459,-122.789879")



@bot.message_handler(commands=['traboulay_poco_trail'])

def send_welcome(message):

bot.reply_to(message, "traboulay poco trail https://www.google.com/maps/search/?api=1&query=49.285418,-122.733626")



@bot.message_handler(commands=['tricks_bench'])

def send_welcome(message):

bot.reply_to(message, "tricks bench https://www.google.com/maps/search/?api=1&query=49.284985,-122.789088")



@bot.message_handler(commands=['twisted_human_body'])

def send_welcome(message):

bot.reply_to(message, "twisted human body https://www.google.com/maps/search/?api=1&query=49.297899,-122.840572")



@bot.message_handler(commands=['veterans_park'])

def send_welcome(message):

bot.reply_to(message, "veterans park https://www.google.com/maps/search/?api=1&query=49.262461,-122.78126")



@bot.message_handler(commands=['victoria_park_board'])

def send_welcome(message):

bot.reply_to(message, "victoria park board https://www.google.com/maps/search/?api=1&query=49.285845,-122.749007")



@bot.message_handler(commands=['victory_baptist_church'])

def send_welcome(message):

bot.reply_to(message, "victory baptist church https://www.google.com/maps/search/?api=1&query=49.271461,-122.774952")



@bot.message_handler(commands=['water_refuge_at_m1'])

def send_welcome(message):

bot.reply_to(message, "water refuge at m1 https://www.google.com/maps/search/?api=1&query=49.281994,-122.795351")



@bot.message_handler(commands=['westcoast_express_poco_station'])

def send_welcome(message):

bot.reply_to(message, "westcoast express poco station https://www.google.com/maps/search/?api=1&query=49.261459,-122.774186")



@bot.message_handler(commands=['whale_mural'])

def send_welcome(message):

bot.reply_to(message, "whale mural https://www.google.com/maps/search/?api=1&query=49.268357,-122.774998")



@bot.message_handler(commands=['windsor_gate_flower_box'])

def send_welcome(message):

bot.reply_to(message, "windsor gate flower box https://www.google.com/maps/search/?api=1&query=49.279064,-122.784648")



@bot.message_handler(commands=['windsor_gate_waterfall'])

def send_welcome(message):

bot.reply_to(message, "windsor gate waterfall https://www.google.com/maps/search/?api=1&query=49.278754,-122.787903")



@bot.message_handler(commands=['wooden_pyramid_sculpture'])

def send_welcome(message):

bot.reply_to(message, "wooden pyramid sculpture https://www.google.com/maps/search/?api=1&query=49.273893,-122.816279")



@bot.message_handler(commands=['workers_memorial'])

def send_welcome(message):

bot.reply_to(message, "workers memorial https://www.google.com/maps/search/?api=1&query=49.283295,-122.828881")



@bot.message_handler(commands=['ursa_madre'])

def send_welcome(message):

bot.reply_to(message, "ursa madre https://goo.gl/maps/5b5nXFeTfKn")



@bot.message_handler(commands=['silver_springs'])

def send_welcome(message):

bot.reply_to(message, "silver springs https://goo.gl/maps/SXy41agWBf12")



@bot.message_handler(commands=['marguerite_park'])

def send_welcome(message):

bot.reply_to(message, "marguerite park https://goo.gl/maps/xL3gzS391f82")



@bot.message_handler(commands=['coquitlam_west_coast_express'])

def send_welcome(message):

bot.reply_to(message, "coquitlam west coast express https://www.google.com/maps/search/?api=1&query=49.273904,-122.799352")



@bot.message_handler(commands=['cccc'])

def send_welcome(message):

bot.reply_to(message, "cccc https://www.google.com/maps/search/?api=1&query=49.263479,-122.83928")



@bot.message_handler(commands=['ccc'])

def send_welcome(message):

bot.reply_to(message, "ccc https://www.google.com/maps/search/?api=1&query=49.279102,-122.813909")



@bot.message_handler(commands=['coquitlam_bus_loop'])

def send_welcome(message):

bot.reply_to(message, "coquitlam bus loop https://www.google.com/maps/search/?api=1&query=49.275642,-122.798515")



@bot.message_handler(commands=['earls'])

def send_welcome(message):

bot.reply_to(message, "earls https://www.google.com/maps/search/?api=1&query=49.266177,-122.777389")



@bot.message_handler(commands=['coquitlam_centre'])

def send_welcome(message):

bot.reply_to(message, "coquitlam centre https://www.google.com/maps/search/?api=1&query=49.279022,-122.799384")



@bot.message_handler(commands=['lions_park'])

def send_welcome(message):

bot.reply_to(message, "lions park https://www.google.com/maps/search/?api=1&query=49.266137,-122.780679")



@bot.message_handler(commands=['frog_gym'])

def send_welcome(message):

bot.reply_to(message, "frog gym https://www.google.com/maps/search/?api=1&query=49.299372,-122.760475")



@bot.message_handler(commands=['bee_house'])

def send_welcome(message):

bot.reply_to(message, "bee house https://www.google.com/maps/search/?api=1&query=49.286018,-122.784835")



@bot.message_handler(commands=['gates_park'])

def send_welcome(message):

bot.reply_to(message, "gates park https://www.google.com/maps/search/?api=1&query=49.260584,-122.790882")



@bot.message_handler(commands=['orca'])

def send_welcome(message):

bot.reply_to(message, "orca https://www.google.com/maps/search/?api=1&query=49.280357,-122.828342")



@bot.message_handler(commands=['salmon_statue'])

def send_welcome(message):

bot.reply_to(message, "salmon statue https://www.google.com/maps/search/?api=1&query=49.263185,-122.790029")



@bot.message_handler(commands=['kingdom_hall'])

def send_welcome(message):

bot.reply_to(message, "kingdom hall https://www.google.com/maps/search/?api=1&query=49.294888,-122.780716")



@bot.message_handler(commands=['m1'])

def send_welcome(message):

bot.reply_to(message, "m1 https://www.google.com/maps/search/?api=1&query=49.281994,-122.795351")



@bot.message_handler(commands=['poco_west_coast_express'])

def send_welcome(message):

bot.reply_to(message, "poco west coast express https://www.google.com/maps/search/?api=1&query=49.261459,-122.774186")



@bot.message_handler(commands=['aggie_park'])

def send_welcome(message):

bot.reply_to(message, "aggie park https://www.google.com/maps/search/?api=1&query=49.268357,-122.774998")



@bot.message_handler(commands=['ursa'])

def send_welcome(message):

bot.reply_to(message, "ursa https://goo.gl/maps/5b5nXFeTfKn")



@bot.message_handler(commands=['hockaday_park_tot_lot'])

def send_welcome(message):

bot.reply_to(message, "hockaday park tot lot https://goo.gl/maps/isxP5t2iZpk")





while True:

try:

bot.polling()

except Exception:

time.sleep(15)
