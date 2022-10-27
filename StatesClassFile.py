from aiogram.dispatcher.filters.state import StatesGroup , State

class StatesClass(StatesGroup):
    Common = State()
    EnterName = State()
    EnterSurename = State()
    EnterPatronimyc = State()
    EnterPhone = State()
        
        
        