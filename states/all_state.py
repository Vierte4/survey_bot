from aiogram.dispatcher.filters.state import StatesGroup, State

class Answer(StatesGroup):
    openanswer = State()

class GetSolve(StatesGroup):
    solve = State()


