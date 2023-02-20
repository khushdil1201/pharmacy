import logging
import telegram
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, MessageHandler, CommandHandler,CallbackQueryHandler, filters, ContextTypes, ConversationHandler, MessageHandler
from credentials import bot_token, bot_user_name,URL
#import openpyxl
#import json
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

lang='Тоҷикӣ'

data = {}

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("finish", finish))
    application.add_handler(CallbackQueryHandler(button))
   
    
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, find))
    
  

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

# set up the introductory statement for the bot when the /start command is invoked
async def start(update, context):
    """Starts the conversation and asks the user about their language."""
    reply_keyboard = [["Тоҷикӣ", "Русский", "English"]]
    await update.message.reply_text(
        "Привет! Выберите язык.\nСалом! Забонро интихоб кунед.\nHello! Select your language.",
    reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, input_field_placeholder="Язык|Забон|Language?"
    ),
    )


  
def build_keyboard(my_list) -> InlineKeyboardMarkup:
    """Helper function to build the next inline keyboard."""
  
    return InlineKeyboardMarkup.from_row(
      
      [InlineKeyboardButton(str(i+1), callback_data=str(i+1)) for i in range(Len)]
    )
choose_list=[]
if lang=='Русский':
   choose_list=["Продолжить","Завершить"]
elif lang=='Тоҷикӣ':
   choose_list=["Давом додан","Хотима додан"]
elif lang=='English':
   choose_list=["Continiue"," Finish"]
# def build_keyboard2(choose_list) -> InlineKeyboardMarkup:
#     """Helper function to build the next inline keyboard."""
  
#     return InlineKeyboardMarkup.from_row(
      
#       [InlineKeyboardButton(choose_list[i], callback_data=str(i+1)) for i in range(len(choose_list))]
#     )
def reply():
    if lang=='Тоҷикӣ':
        return "Лутфан интихоб кунед:"
    elif lang=='Русский':
        return "Пожалуйста выберите:"
    elif lang=='English':
        return "Please choose:"
def exit_func():
    if lang=='Русский':
        return "Для продолжения введите название другого препарата или нажмите кнопку завершения"
    elif lang=='Тоҷикӣ':
        return "Барои давом додан номи дигар доруро ворид кунед ё тугамачаи хотимаро пахш кунед"
    elif lang=='English':
        return "To continue enter name of another medication or press the button of finish"

# def example():
#     count=0
#     mylist=''
#     for j in example_list:
#         count=count+1

Digit=[]  
reply_keyboard1=[]  
# if lang=='Русский':
reply_keyboard1=[["Да","Нет"]] 
# elif lang=='Тоҷикӣ':
#    reply_keyboard1=[["Ҳа","Не"]]
# elif lang=='Русский':
#    reply_keyboard1=[["Yes","No"]]
async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    if (update.message.text).isdigit():
      global digit
      digit=(int)(update.message.text)
      if (int)(extra2)>=digit:
       Digit.append(digit)
       res=exit_func()
       add_list.append(digit*Price)

       await update.message.reply_text("Завершить покупок?",reply_markup=ReplyKeyboardMarkup(
          reply_keyboard1,  one_time_keyboard=True, input_field_placeholder="Выбор|Интихоб|Choise"
       ),)
       #await update.message.reply_text(res+":"+"\n                     /finish")
      elif (int)(extra2)<digit:
       Digit.append(digit)
       res=exit_func()
       add_list.append(digit*Price)

       await update.message.reply_text("Завершить покупок?",reply_markup=ReplyKeyboardMarkup(
          reply_keyboard1,  one_time_keyboard=True, input_field_placeholder="Выбор|Интихоб|Choise"
       ),)    
    else:
        if update.message.text not in ['Тоҷикӣ','English','Русский','Нет']: 
           temp=reply()
      
           found=search_by_name()
           if my_list==[]:
            await update.message.reply_text(found)
           else:
            await update.message.reply_text(found)
           await update.message.reply_text(temp, reply_markup=build_keyboard(my_list))
    #if update.message.text in [str(i) for i in range(data['Quantity'][extra2])]:
        
        else:
            global lang
            lang=update.message.text
            if update.message.text=='Русский':
             await update.message.reply_text(
            "Введите название препарата:",
           reply_markup=ReplyKeyboardRemove(),
           )
            elif update.message.text=='Тоҷикӣ':
                await update.message.reply_text(
                "Номи доруро ворид кунед:",
              reply_markup=ReplyKeyboardRemove(),
             )
            elif update.message.text=='Нет':
               await update.message.reply_text(
            "Введите название препарата:",
           reply_markup=ReplyKeyboardRemove(),
           )
            else:
             await update.message.reply_text(
            "Please type pill name:",
            reply_markup=ReplyKeyboardRemove(),
            )
# def choosing(parametr):
#    if lang=='Русский':
#       if parametr=='Нет':
         
         
add_list=[]
exit_list=[]
def kolich():
   mylist=''
   count=0
   i=0
   for j in example_list:
        count=count+1
        if lang=='Тоҷикӣ':
          mylist=mylist+str(i+1)+". "+j+str(Digit[i])+" д. "+"\n\n"
        elif lang=='Русский':
          mylist=mylist+str(i+1)+". "+j+str(Digit[i])+" шт. "+"\n\n"
        elif lang=='English':
          mylist=mylist+str(i+1)+". "+j+str(Digit[i])+" pc. "+"\n\n"
        i=i+1
   return mylist 
async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancels and ends the conversation."""    
    
    global add
    add=0
    global package
    for i in range(len(add_list)):
     add=add+add_list[i]
    
    kol=kolich()
    # for j in example_list:
    #     count=count+1
    #     if lang=='Тоҷикӣ':
    #       mylist=mylist+str(kol)+" дона "+j+"\n"
    #     elif lang=='Русский':
    #       mylist=mylist+str()+" штук "+j+"\n"
    #     elif lang=='English':
    #       mylist=mylist+str(Digit[k])+" pc. "+j+"\n"
    if lang=='Тоҷикӣ':
        package="Руйхати харид: \n\n"+kol+"\nҲисоби умумӣ: "+str(add)+" с."
        await update.message.reply_text(package, reply_markup=ReplyKeyboardRemove())
    elif lang=='Русский':
        package="Список покупок: \n\n"+kol+"\nОбщий счёт: "+str(add)+" с."
        await update.message.reply_text(package, reply_markup=ReplyKeyboardRemove())
    elif lang=='English':
        package="Shopping list: \n\n"+kol+"\nTotal score: "+str(add)+" TJS"
        await update.message.reply_text(package, reply_markup=ReplyKeyboardRemove()) 
    example_list.clear()
    add_list.clear()
    Digit.clear()
async def help_command(update, context):
    """Send a message when the command /help is issued."""
    if lang=='Тоҷикӣ':
        await update.message.reply_text("Ман ба Шумо барои ёфтани доруҳои лозимӣ кӯмак менамоям.\nШумо метавонед нархҳои доруро фаҳмед ва дар кадом дорухонаи мо ин дору вуҷуд дорад.")
    elif lang=='Русский':
        await update.message.reply_text("Я помогу Вам в поиске препаратов.\nЗдесь Вы можете узнать цену препаратов, а также в какой аптеке они находятся.")
    elif lang=='English':
        await update.message.reply_text("I will help you in searching pills.\nYou can explore prices here and also find out in which pharmacy you can find them.")

global action
action=False
onaction="Барои давом додан номи дигар доруро ворид кунед ё тугмачаи баромадро пахш кунед: /cancel"
onaction1="Для продолжения вводите другою название препарата или нажмите кнопку выхода: /cancel"
onaction2="For continiue enter any name of another medication or press the button of exit: /cancel" 
example_list=[]




count_list=[]
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Parses the CallbackQuery and updates the message text."""
    global extra2 
    query = update.callback_query
    extra2=str(data['Quantity'][int(query.data)-1])
    
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    b=len(my_list)-Len
    global extra,Price
    extra=str(new_list[b+int(query.data)-1])
    example_list.append(extra)
    Price=(data['Price'][int(query.data)-1])
   # add_list.append((data['Price'][int(query.data)-1]))
    choice=str(my_list[b+int(query.data)-1])
    
    if lang=='Русский':
    # await query.edit_message_text(text=f"Ваш выбор: "+"\n"+choice+"\n\n"+onaction1)
      await query.edit_message_text(text=f"Ваш выбор: "+"\n"+choice+"\n\n"+"Введите количество: ")
    elif lang=='Тоҷикӣ':
    # await query.edit_message_text(text=f"Интихоби шумо: "+"\n"+choice+"\n\n"+onaction)
      await query.edit_message_text(text=f"Интихоби шумо: "+"\n"+choice+"\n\n"+"Миқдори ин доруро ворид кунед: ")
    elif lang=='English':  
    # await query.edit_message_text(text=f"Your choise: "+"\n"+choice+"\n\n"+onaction2)
      await query.edit_message_text(text=f"Your choice: "+"\n"+choice+"\n\n"+"Enter the number of this medication: ")
# async def button2(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    query = update.callback_query
#    await query.answer()
#    await query.edit_message_text(text=f"___"+package)
    
my_list=[]
new_list=[]

   
            

def search_by_name():
    #read_xls()
    read_json()
    global Len
    Len=len(data['Product'])
    message=''
    if Len>0:
        for i in range(Len):   
            
            if lang=='Русский':
                str2=data['Product'][i]+"-\nЦена: "+str(data['Price'][i])+" с.\n"
                str1=str(i+1)+")\nНаименование: "+data['Product'][i] +  "\nЦена: "+str(data['Price'][i]) + " сомони" +"  \nСрок годности: "+data['DueTo'][i] +" \nАдрес аптеки: " +data['Address'][i]+" \nПроизводитель: "+str(data['Manufacturer'][i]+"\n\n")
            elif lang=='English':
                str2=data['Product'][i]+"-\nPrice: "+str(data['Price'][i])+" TJS\n"
                str1=str(i+1)+")\nName: "+data['Product'][i] + "  \nPrice: "+str(data['Price'][i]) + " сомони" + "  \nValid Till: "+data['DueTo'][i]+" \nAddress of pharmacy: " +data['Address'][i]+" \nManufacturer: "+str(data['Manufacturer'][i]+ " \n\n")
            else:
                str2=data['Product'][i]+"-\nНарх: "+str(data['Price'][i])+" с.\n"
                str1=str(i+1)+")\nНомгӯ: "+data['Product'][i] + "  \nНарх: "+str(data['Price'][i]) + " сомони" + "  \nМӯҳлат: "+data['DueTo'][i]+" \nСуроғаи дорухона: " +data['Address'][i] +" \nИстеҳсолкунанда: "+str(data['Manufacturer'][i]+ " \n\n")
            message=message+str1
            #new_list.append(str(data['Price'][i]))
            my_list.append(str1) 
            new_list.append(str2)
        return message
    else: #if i==len(data['Product'])-1:
      return not_found() 

def not_found():
   if lang=='Русский':
    return "Не нашёл запрашиваемый препарат, попробуйте другое наименование препарата"
   elif lang=='English':
    return "Could not find this product, try another product name"
   else:
    return "Ин дору ёфт нашуд, номи дигар доруро нависед"
# def read_xls():
#     xlsx_file = 'Product.xlsx'
#     wb_obj = openpyxl.load_workbook(xlsx_file) 

#     # Read the active sheet:
#     sheet = wb_obj.active

#     for i, row in enumerate(sheet.iter_rows(values_only=True)):
#         if i == 0:
#             data['Product'] = []
#             data['Quantity'] = []
#             data['Price'] = []
#             data['DueTo'] = []
#             data['Manufacturer'] = []
#         else:
#             data['Product'].append(row[0])
#             data['Quantity'].append(row[2])
#             data['Price'].append(row[3])
#             data['DueTo'].append(row[4])
#             data['Manufacturer'].append(row[5])

#     return data

json_list =[
    {
        "Id": 0,
        "ProductName": "Новокаин 0,1 г №10 суппоз рект.",
        "Barcode": "4820013360061",
        "Quantity": 8,
        "Price": 2.0000,
        "ExpireDate": "01-01-2026",
        "ManufactName": "Украина",
        "Address": "Санта Русь Караболо"
    },
    {
        "Id": 0,
        "ProductName": "Новокаин 0,1 г №10 суппоз рект.",
        "Barcode": "4820013360061",
        "Quantity": 3,
        "Price": 5.0000,
        "ExpireDate": "01-03-2023",
        "ManufactName": "Украина",
        "Address": "Аптека Шифо"
        
    },
    {
        "Id": 0,
        "ProductName": "Новокаин 0,1 г №10 суппоз рект.",
        "Barcode": "4820013360061",
        "Quantity": 28,
        "Price": 14.0000,
        "ExpireDate": "01-01-2026",
        "ManufactName": "Украина",
        "Address": "Аптека Мадад"
    },
    {
        "Id": 0,
        "ProductName": "Новокаин 0,5 % №10 амп по 5 мл.",
        "Barcode": "4607005933836",
        "Quantity": 10,
        "Price": 12.0000,
        "ExpireDate": "01-01-2025",
        "ManufactName": "Россия",
        "Address": "Аптека Саховат"
    },
    {
        "Id": 0,
        "ProductName": "Новокаин 0.5 % №10 амп по 5 мл",
        "Barcode": "4680013245009",
        "Quantity": 3,
        "Price": 6.0000,
        "ExpireDate": "01-06-2022",
        "ManufactName": "Россия",
        "Address": "Аптека Авис Сити"
    }
]
def read_json():
    # url = "https://rightgreyphone20.conveyor.cloud/api/assortments?keyword="+productname
   
    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"
    # headers["Content-Type"] = "application/json"
    # try:
    #     resp = requests.get(url, headers=headers)
    #     json_list = resp.json()
    #     print(resp.raise_for_status())
    # except requests.exceptions.RequestException as err:
    #     print ("OOps: Something Else",err)
    # except requests.exceptions.HTTPError as errh:
    #     print ("Http Error:",errh)
    # except requests.exceptions.ConnectionError as errc:
    #     print ("Error Connecting:",errc)
    # except requests.exceptions.Timeout as errt:
    #     print ("Timeout Error:",errt) 
   
    



    data['Product'] = []
    data['Price'] = []
    data['DueTo'] = []
    data['Manufacturer'] = []
    data['Quantity'] = []
    data['Address'] = []
    for i in json_list:
        for key, value in i.items():
            if key=="ProductName":
                data['Product'].append(i['ProductName'])
            if key=="Price":
                data['Price'].append(i['Price'])
            if key=="ExpireDate":
                data['DueTo'].append(i['ExpireDate'])  
            if key=="ManufactName":
                data['Manufacturer'].append(i['ManufactName'])
            if key=="Quantity":
                data['Quantity'].append(i['Quantity'])  
            if key=="Address":
                data['Address'].append(i['Address'])  
    #print(data)
    
    return data


#  [
#     {
#         "Id": 0,
#         "ProductName": "Парацетамол 200 мг №10 тб (детск)",
#         "Barcode": "4810201004068",
#         "Quantity": 55,
#         "Price": 1.5000,
#         "ExpireDate": "01-09-2023",
#         "ManufactName": "Россия"
#     },
#     {
#         "Id": 0,
#         "ProductName": "Парацетамол 250 мг  мг сироп 100 мл",
#         "Barcode": "4640018642067",
#         "Quantity": 2,
#         "Price": 11.0000,
#         "ExpireDate": "01-07-2023",
#         "ManufactName": "Индия"
#     },
#     {
#         "Id": 0,
#         "ProductName": "Парацетамол 500 мг №10 тб.",
#         "Barcode": "8908009796011",
#         "Quantity": 23,
#         "Price": 1.5000,
#         "ExpireDate": "01-01-2022",
#         "ManufactName": "Индия"
#     },
#     {
#         "Id": 0,
#         "ProductName": "Парацетамол детс суспен 120мг/5 мл ",
#         "Barcode": "4602565030025",
#         "Quantity": 1,
#         "Price": 14.7000,
#         "ExpireDate": "01-03-2023",
#         "ManufactName": "Россия"
#     },
#     {
#         "Id": 0,
#         "ProductName": "Парацетамол детс суспен 120мг/5 мл ",
#         "Barcode": "4602565030025",
#         "Quantity": 1,
#         "Price": 15.0000,
#         "ExpireDate": "01-05-2023",
#         "ManufactName": "Россия"
#     }
#  ]


if __name__ == '__main__':   
    main()
