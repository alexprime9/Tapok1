from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('Ужасы', callback_data='123')
#inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Камедия', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('Фантастика', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('Семейный', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('Мелодрама', callback_data='btn5')

inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)

