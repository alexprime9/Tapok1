from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_kb_top = InlineKeyboardMarkup(row_width=2)
inline_kb_top.insert(InlineKeyboardButton('Курс', url='https://yandex.ru/search/?text'
                                                      '=курс+рубля+к+юаню+на+сегодня&clid=2270455&banerid=6301000000'
                                                      '%3A65900c74ce1e2f1784a08086&win=626&lr=123817'))