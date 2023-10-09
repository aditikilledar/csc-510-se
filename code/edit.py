import helper
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

# === Documentation of edit.py ===

def run(m, bot):
    """
    run(message, bot): This is the main function used to implement the delete feature.
    It takes 2 arguments for processing - message which is the message from the user, and
    bot which is the telegram bot object from the main code.py function. It gets the details
    for the expense to be edited from here and passes control onto edit2(m, bot): for further processing.
    """
    chat_id = m.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getUserHistory(chat_id):
        expense_data = c.split(",")
        str_date = "Date=" + expense_data[0]
        str_category = ",\t\tCategory=" + expense_data[1]
        str_amount = ",\t\tAmount=$" + expense_data[2]
        markup.add(str_date + str_category + str_amount)
    info = bot.reply_to(m, "Select expense to be edited:", reply_markup=markup)
    bot.register_next_step_handler(info, select_category_to_be_updated, bot)

def select_category_to_be_updated(m, bot):
    info = m.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_data = [] if info is None else info.split(",")

    # Prompt the user for all three fields in one message
    bot.send_message(
        m.chat.id,
        "Enter the updated information in the format: Date=NewDate, Category=NewCategory, Amount=NewAmount",
        reply_markup=markup
    )
    
    bot.register_next_step_handler(m, process_updated_data, bot, selected_data)

def process_updated_data(m, bot, selected_data):
    updated_info = m.text
    updated_fields = updated_info.split(",")
    updated_values = {}
    
    # Parse and store the updated fields and values
    for field in updated_fields:
        key, value = field.strip().split("=")
        updated_values[key] = value
    
    # Check if all three fields are provided
    if "Date" in updated_values and "Category" in updated_values and "Amount" in updated_values:
        new_date = updated_values["Date"]
        new_category = updated_values["Category"]
        new_amount = updated_values["Amount"]
        
        # Update the data
        edit_data(bot, selected_data, new_date, new_category, new_amount, m.chat.id)
        bot.reply_to(m, "Expense details are updated.")
    else:
        bot.reply_to(m, "Please provide all three fields: Date, Category, and Amount in the correct format.")

def edit_data(bot, selected_data, new_date, new_category, new_amount, chat_id):
    """
    Update the expense data here using the new values (new_date, new_category, new_amount).
    Implement this function according to your data storage and update logic.
    """
    user_list = helper.read_json()
    chat_id = chat_id
    data_edit = helper.getUserHistory(chat_id)

    for i in range(len(data_edit)):
        user_data = data_edit[i].split(",")
        selected_date = selected_data[0].split("=")[1]
        selected_category = selected_data[1].split("=")[1]
        selected_amount = selected_data[2].split("=")[1]
        if (
            user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]
        ):
            data_edit[i] = (
                new_date + "," + new_category + "," + new_amount
            )
            break

    user_list[str(chat_id)]["data"] = data_edit
    helper.write_json(user_list)

if __name__ == "__main__":
    # You might have some code here to initialize and start your bot.
    # Make sure to include your bot's initialization and start-up logic here.
    pass
