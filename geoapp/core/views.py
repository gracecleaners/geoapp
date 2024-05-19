from django.shortcuts import render, HttpResponse


# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# creating and object of the chatbot 
from chatterbot.trainers import ChatterBotCorpusTrainer

# Configure the chatbot with the correct model
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'default_response': 'Sorry, I don\'t know what that means.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    tagger_language='en_core_web_sm'  # Ensure this matches your spaCy model
)

# Custom training data
list_to_train = [
    "hi",
    "hi, there",
    "what's your name",
    "I'm just a chatbot",
    "what is your favorite food",
    "I don't eat"
]

# Train the bot with custom data
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

# Train the bot with the English corpus
# chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
# chatterBotCorpusTrainer.train('chatterbot.corpus.english')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

def index(request):
    return render(request, "index.html")


def chatbot(request):
    return render(request, 'chat.html')

def chat(request, chat_id):
    return HttpResponse(chat_id)

def map(request):
    return render(request, 'map.html')

