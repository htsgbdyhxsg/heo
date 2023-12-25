import requests
import telebot,time,random
from telebot import types
from gatet import Tele
import os
token = '6469189252:AAGQtZguj-aJGYQxXxl2sp015TLP10uPukE'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber ='5718023113'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان يغالي")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @MNOW4 ''', reply_markup=mes)
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Insufficient Funds
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 1$
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S7
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "Insufficient Funds" in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'success' in last:
					msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 1$
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S7
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
				else:
					dd += 1
				random_number = random.randint(1, 25)

				time.sleep(random_number)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
@bot.message_handler(commands=["chk"])
def start(message):
	name='𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 𝙲𝚅𝚅 1$'
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
	try:
		cc=message.text.replace('/chk ', '')
	except:
		bot.reply_to(message, "Wrong format ❌")
		return
	try:
		data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
	except:
		pass
	try:
		bank=(data['bank']['name'])
	except:
				bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		emj=(data['country']['emoji'])
	except:
				emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		cn=(data['country']['name'])
	except:
				cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		dicr=(data['scheme'])
	except:
				dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		typ=(data['type'])
	except:
				typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		url=(data['bank']['url'])
	except:
		url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		last = str(Tele(cc))
	except Exception as e:
		print(e)
		last='ERROR'
		
	if "live" in last or 'Funds' in last:
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code> 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {name} 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	elif 'successfully' in last:
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {name} 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	else:
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code> 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝐷𝐸𝐶𝐿𝐼𝑁𝐸𝐷 ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆ 𝒅𝒆𝒗 : 𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪 [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
print("تم تشغيل البوت")
bot.polling()
